import json
import logging
import time
import urllib
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Union

import attrs
import numpy as np
import pandas
import pendulum
import requests
from google.protobuf import json_format
from pyspark.sql import dataframe as pyspark_dataframe
from typeguard import typechecked

from tecton._internals import athena_api
from tecton._internals import display
from tecton._internals import errors
from tecton._internals import metadata_service
from tecton._internals import query_helper
from tecton._internals import sdk_decorators
from tecton._internals import snowflake_api
from tecton._internals import spark_api
from tecton._internals import utils as internal_utils
from tecton._internals import validations_api
from tecton.framework import base_tecton_object
from tecton.framework import compute_mode
from tecton.framework import configs
from tecton.framework import data_frame as tecton_dataframe
from tecton.framework import feature_view as framework_feature_view
from tecton_core import conf
from tecton_core import fco_container
from tecton_core import feature_definition_wrapper
from tecton_core import feature_set_config
from tecton_core import id_helper
from tecton_core import query_consts
from tecton_core import request_context
from tecton_core import specs
from tecton_proto.api.featureservice import feature_service_pb2 as feature_service__api_pb2
from tecton_proto.args import basic_info_pb2
from tecton_proto.args import fco_args_pb2
from tecton_proto.args import feature_service_pb2 as feature_service__args_pb2
from tecton_proto.metadataservice import metadata_service_pb2
from tecton_proto.validation import validator_pb2


logger = logging.getLogger(__name__)


@attrs.define(eq=False)
class FeatureService(base_tecton_object.BaseTectonObject):
    """A Tecton Feature Service.

    In Tecton, a Feature Service exposes an API for accessing a set of FeatureViews.

    Once deployed in production, each model has one associated Feature Service that serves the model its features. A
    Feature Service contains a list of the Feature Views associated with a model. It also includes user-provided
    metadata such as name, description, and owner that Tecton uses to organize feature data.

    An example of Feature Service declaration

    .. code-block:: python

        from tecton import FeatureService, LoggingConfig
        # Import your feature views declared in your feature repo directory
        from feature_repo.features.feature_views import last_transaction_amount_sql, transaction_amount_is_high
        ...

        # Declare Feature Service
        fraud_detection_feature_service = FeatureService(
            name='fraud_detection_feature_service',
            description='A FeatureService providing features for a model that predicts if a transaction is fraudulent.',
            features=[
                last_transaction_amount_sql,
                transaction_amount_is_high,
                ...
            ]
            logging=LoggingConfig(
                sample_rate=0.5,
                log_effective_times=False,
            )
            tags={'release': 'staging'},
        )

    Attributes:
        info: A dataclass containing basic info about this Tecton Object.
    """

    # A Feature Service spec, i.e. a dataclass representation of the Tecton object that is used in most functional use
    # cases, e.g. constructing queries. Set only after the object has been validated. Remote objects, i.e. applied
    # objects fetched from the backend, are assumed valid.
    _spec: Optional[specs.FeatureServiceSpec] = attrs.field(repr=False)

    # A Tecton "args" proto. Only set if this object was defined locally, i.e. this object was not applied
    # and fetched from the Tecton backend.
    _args: Optional[feature_service__args_pb2.FeatureServiceArgs] = attrs.field(
        repr=False, on_setattr=attrs.setters.frozen
    )

    # The feature references that make up this Feature Service.
    _feature_references: Tuple[framework_feature_view.FeatureReference, ...] = attrs.field(
        on_setattr=attrs.setters.frozen
    )

    # The feature set config for this Feature Service. The feature set config is used for query construction and
    # represents a super set of the feature references in _feature_references because of indirect feature definition
    # dependencies. For example, _feature_references may contain a single ODFV, but _feature_set_config may represent
    # that ODFV plus a batch feature view input to that ODFV. The _feature_set_config is set only after the
    # FeatureService object has been validated.
    _feature_set_config: Optional[feature_set_config.FeatureSetConfig] = attrs.field(repr=False)

    def __init__(
        self,
        *,
        name: str,
        description: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        owner: Optional[str] = None,
        prevent_destroy: bool = False,
        online_serving_enabled: bool = True,
        features: List[Union[framework_feature_view.FeatureReference, framework_feature_view.FeatureView]] = None,
        logging: Optional[configs.LoggingConfig] = None,
        on_demand_environment: Optional[str] = None,
    ):
        """
        Instantiates a new FeatureService.

        :param name: A unique name for the Feature Service.
        :param description: A human-readable description.
        :param tags: Tags associated with this Tecton Object (key-value pairs of arbitrary metadata).
        :param owner: Owner name (typically the email of the primary maintainer).
        :param prevent_destroy: If True, this Tecton object will be blocked from being deleted or re-created (i.e. a
            destructive update) during tecton plan/apply. To remove or update this object, `prevent_destroy` must be set to False
            via the same tecton apply or a separate tecton apply. `prevent_destroy` can be used to prevent accidental changes
            such as inadvertantly deleting a Feature Service used in production or recreating a Feature View that
            triggers expensive rematerialization jobs. `prevent_destroy` also blocks changes to dependent Tecton objects
            that would trigger a recreate of the tagged object, e.g. if `prevent_destroy` is set on a Feature Service,
            that will also prevent deletions or re-creates of Feature Views used in that service. `prevent_destroy` is
            only enforced in live (i.e. non-dev) workspaces.
        :param online_serving_enabled: (Optional, default True) If True, users can send realtime requests
            to this FeatureService, and only FeatureViews with online materialization enabled can be added
            to this FeatureService.
        :param features: The list of FeatureView or FeatureReference that this FeatureService will serve.
        :param logging: A configuration for logging feature requests sent to this Feature Service.
        :param on_demand_environment: Configuration for where on demand features should be computed online.
        """
        from tecton.cli import common as cli_common

        feature_references = []
        for feature in features:
            if isinstance(feature, framework_feature_view.FeatureReference):
                feature_references.append(feature)
            elif isinstance(feature, framework_feature_view.FeatureView):
                feature_references.append(framework_feature_view.FeatureReference(feature_definition=feature))
            else:
                msg = f"Object in FeatureService.features with an invalid type: {type(feature)}. Should be of type FeatureReference or Feature View."
                raise TypeError(msg)

        feature_packages = [_feature_reference_to_feature_service_feature_package(ref) for ref in feature_references]

        args = feature_service__args_pb2.FeatureServiceArgs(
            feature_service_id=id_helper.IdHelper.generate_id(),
            info=basic_info_pb2.BasicInfo(name=name, description=description, tags=tags, owner=owner),
            prevent_destroy=prevent_destroy,
            online_serving_enabled=online_serving_enabled,
            feature_packages=feature_packages,
            version=feature_definition_wrapper.FrameworkVersion.FWV5.value,
            logging=logging._to_proto() if logging else None,
            on_demand_environment=on_demand_environment,
        )
        info = base_tecton_object.TectonObjectInfo.from_args_proto(args.info, args.feature_service_id)
        source_info = cli_common.construct_fco_source_info(args.feature_service_id)
        self.__attrs_init__(
            info=info,
            spec=None,
            args=args,
            source_info=source_info,
            feature_references=feature_references,
            feature_set_config=None,
        )
        base_tecton_object._register_local_object(self)

    @classmethod
    @typechecked
    def _from_spec(cls, spec: specs.FeatureServiceSpec, fco_container: fco_container.FcoContainer) -> "FeatureService":
        """Create a Feature Service from directly from a spec. Specs are assumed valid and will not be re-validated."""
        feature_set_config_ = feature_set_config.FeatureSetConfig.from_feature_service_spec(spec, fco_container)
        info = base_tecton_object.TectonObjectInfo.from_spec(spec)

        feature_references = []
        for feature_set_item in spec.feature_set_items:
            fv_spec = fco_container.get_by_id(feature_set_item.feature_view_id)
            fv = framework_feature_view.feature_view_from_spec(fv_spec, fco_container)
            join_key_mapping = {
                jkm.feature_view_column_name: jkm.spine_column_name for jkm in feature_set_item.join_key_mappings
            }
            ref = framework_feature_view.FeatureReference(
                feature_definition=fv,
                namespace=feature_set_item.namespace,
                features=feature_set_item.feature_columns,
                override_join_keys=join_key_mapping,
            )
            feature_references.append(ref)

        obj = cls.__new__(cls)  # Instantiate the object. Does not call init.
        obj.__attrs_init__(
            info=info,
            spec=spec,
            args=None,
            source_info=None,
            feature_references=tuple(feature_references),
            feature_set_config=feature_set_config_,
        )

        return obj

    @sdk_decorators.assert_local_object
    def _build_args(self) -> fco_args_pb2.FcoArgs:
        return fco_args_pb2.FcoArgs(feature_service=self._args)

    def _build_fco_validation_args(self) -> validator_pb2.FcoValidationArgs:
        if self.info._is_local_object:
            return validator_pb2.FcoValidationArgs(
                feature_service=validator_pb2.FeatureServiceValidationArgs(
                    args=self._args,
                )
            )
        else:
            return self._spec.validation_args

    def _get_dependent_objects(self, include_indirect_dependencies: bool) -> List[base_tecton_object.BaseTectonObject]:
        dependent_objects = []
        for fv in self._feature_definitions:
            if include_indirect_dependencies:
                dependent_objects.extend(fv._get_dependent_objects(include_indirect_dependencies=True) + [fv])
            else:
                dependent_objects.append(fv)

        # Dedupe by ID.
        return list({fco_obj.id: fco_obj for fco_obj in dependent_objects}.values())

    @property
    def _is_valid(self) -> bool:
        return self._spec is not None

    def _validate(self, indentation_level: int = 0) -> None:
        if self._is_valid:
            return

        validations_api.print_validating_dependencies(self, self._feature_definitions, indentation_level)
        dependent_specs = []
        for feature_definition in self._feature_definitions:
            feature_definition._validate(indentation_level + 1)
            dependent_specs.extend(feature_definition._get_dependent_specs() + [feature_definition._spec])

        validations_api.run_backend_validation_and_assert_valid(
            self,
            validator_pb2.ValidationRequest(
                validation_args=[
                    dependent_obj._build_fco_validation_args()
                    for dependent_obj in self._get_dependent_objects(include_indirect_dependencies=True)
                ]
                + [self._build_fco_validation_args()],
            ),
            indentation_level,
        )

        supplement = specs.FeatureServiceSpecArgsSupplement(
            ids_to_feature_views={spec.id: spec for spec in dependent_specs if isinstance(spec, specs.FeatureViewSpec)}
        )
        fs_spec = specs.FeatureServiceSpec.from_args_proto(self._args, supplement)

        fco_container_specs = [fs_spec] + dependent_specs
        fco_container_ = fco_container.FcoContainer.from_specs(specs=fco_container_specs, root_ids=[fs_spec.id])
        self._feature_set_config = feature_set_config.FeatureSetConfig.from_feature_service_spec(
            fs_spec, fco_container_
        )
        self._spec = fs_spec

    @sdk_decorators.sdk_public_method
    @sdk_decorators.assert_remote_object
    def summary(self) -> display.Displayable:
        """Displays a human readable summary of this Feature View."""
        request = metadata_service_pb2.GetFeatureServiceSummaryRequest(
            feature_service_id=self._spec.id_proto, workspace=self._spec.workspace
        )
        response = metadata_service.instance().GetFeatureServiceSummary(request)

        items_map = {}
        summary_items = []
        for item in response.general_items:
            items_map[item.key] = item
            if item.display_name:
                summary_items.append((item.display_name, item.multi_values if item.multi_values else item.value))

        if not internal_utils.is_live_workspace(self.workspace):
            return display.Displayable.from_properties(items=summary_items)

        api_service = conf.get_or_raise("API_SERVICE")
        if "localhost" in api_service and "ingress" in api_service:
            return display.Displayable.from_properties(items=summary_items)

        if "curlEndpoint" in items_map and "curlParamsJson" in items_map:
            service_url = urllib.parse.urljoin(api_service, items_map["curlEndpoint"].value)
            curl_params_json = json.dumps(json.loads(items_map["curlParamsJson"].value), indent=2)
            curl_header = items_map["curlHeader"].value
            curl_str = "curl -X POST " + service_url + '\\\n-H "' + curl_header + "\"-d\\\n'" + curl_params_json + "'"
            summary_items.append(("Example cURL", curl_str))
        return display.Displayable.from_properties(items=summary_items)

    @property
    @sdk_decorators.sdk_public_method
    def features(self) -> List[framework_feature_view.FeatureReference]:
        """Returns the list of feature references included in this Feature Service.

        FeatureReferences are references to Feature Views/Tables that may select a subset of features, override the
        Feature View/Table namespace, or re-map join-keys.
        """
        return list(self._feature_references)

    @property
    @sdk_decorators.sdk_public_method
    def feature_views(self) -> Set[framework_feature_view.FeatureView]:
        """Returns the set of Feature Views directly depended on by this Feature Service.

        A single Feature View may be included multiple times in a Feature Service under different namespaces. See the
        FeatureReference documentation. This method dedupes those Feature Views.
        """

        # Dedupe by ids.
        # TODO(jake): Tecton objects should probably be hashable based on their id.
        return set({ref.feature_definition.id: ref.feature_definition for ref in self._feature_references}.values())

    @sdk_decorators.sdk_public_method(requires_validation=True)
    def get_feature_columns(self) -> List[str]:
        """Returns the list of all feature columns included in this feature service."""
        all_features = self._feature_set_config.features
        return [feature for feature in all_features if not feature.startswith(query_consts.UDF_INTERNAL)]

    # TODO(follow-up PR): Clean up this method. (Holding off to minimize backport.)
    @property
    def _feature_definitions(self) -> Set[framework_feature_view.FeatureView]:
        """Returns the set of unique Feature Definitions directly depended on by this Feature Service.

        A single Feature Definition may be included multiple times in a Feature Service under different namespaces.
        This method dedupes those.
        """
        return set(ref.feature_definition for ref in self._feature_references)

    @sdk_decorators.assert_valid
    def _check_can_query_from_source(self, from_source: Optional[bool]) -> framework_feature_view.QuerySources:
        all_query_sources = framework_feature_view.QuerySources()

        for fv in self._feature_definitions:
            sources = fv._check_can_query_from_source(from_source)
            all_query_sources += sources

        return all_query_sources

    @sdk_decorators.sdk_public_method(requires_validation=True)
    def get_historical_features(
        self,
        spine: Union[pyspark_dataframe.DataFrame, pandas.DataFrame, tecton_dataframe.TectonDataFrame, str],
        timestamp_key: Optional[str] = None,
        include_feature_view_timestamp_columns: bool = False,
        from_source: Optional[bool] = None,
        save: bool = False,
        save_as: Optional[str] = None,
    ) -> tecton_dataframe.TectonDataFrame:
        """Fetch a :class:`TectonDataFrame` of feature values from this FeatureService.

        This method will return feature values for each row provided in the spine DataFrame. The feature values
        returned by this method will respect the timestamp provided in the timestamp column of the spine DataFrame.

        By default (i.e. ``from_source=None``), this method fetches feature values from the Offline Store for Feature
        Views that have offline materialization enabled and otherwise computes feature values on the fly from raw data.

        :param spine: A dataframe of possible join keys, request data keys, and timestamps that specify which feature values to fetch.To distinguish
            between spine columns and feature columns, feature columns are labeled as `feature_view_name__feature_name`
            in the returned DataFrame.
        :type spine: Union[pyspark.sql.DataFrame, pandas.DataFrame, TectonDataFrame]
        :param timestamp_key: Name of the time column in the spine DataFrame.
            This method will fetch the latest features computed before the specified timestamps in this column.
            Not applicable if the FeatureService stricly contains OnDemandFeatureViews with no feature view dependencies.
        :type timestamp_key: str
        :param include_feature_view_timestamp_columns: Whether to include timestamp columns for each FeatureView in the FeatureService. Default is False.
        :type include_feature_view_timestamp_columns: bool
        :param from_source: Whether feature values should be recomputed from the original data source. If ``None``,
            feature values will be fetched from the Offline Store for Feature Views that have offline materialization
            enabled and otherwise computes feature values on the fly from raw data. Use ``from_source=True`` to force
            computing from raw data and ``from_source=False`` to error if any Feature Views are not materialized.
            Defaults to None.
        :type from_source: bool
        :param save: Whether to persist the DataFrame as a Dataset object. Default is False. This parameter is not supported in Tecton on Snowflake.
        :type save: bool
        :param save_as: Name to save the DataFrame as.
            If unspecified and save=True, a name will be generated. This parameter is not supported in Tecton on Snowflake.
        :type save_as: str

        Examples:
            A FeatureService :py:mod:`fs` that contains a BatchFeatureView and StreamFeatureView with join keys :py:mod:`user_id` and :py:mod:`ad_id`.

            1) :py:mod:`fs.get_historical_features(spine)` where :py:mod:`spine=pandas.Dataframe({'user_id': [1,2,3], 'ad_id': ['a234', 'b256', 'c9102'], 'date': [datetime(...), datetime(...), datetime(...)]})`
            Fetch historical features from the offline store for users 1, 2, and 3 for the specified timestamps and ad ids in the spine.

            2) :py:mod:`fs.get_historical_features(spine, save_as='my_dataset)` where :py:mod:`spine=pandas.Dataframe({'user_id': [1,2,3], 'ad_id': ['a234', 'b256', 'c9102'], 'date': [datetime(...), datetime(...), datetime(...)]})`
            Fetch historical features from the offline store for users 1, 2, and 3 for the specified timestamps and ad ids in the spine. Save the DataFrame as dataset with the name :py:mod:`my_dataset`.

            3) :py:mod:`fv.get_historical_features(spine, timestamp_key='date_1')` where :py:mod:`spine=pandas.Dataframe({'user_id': [1,2,3], 'ad_id': ['a234', 'b256', 'c9102'],
            'date_1': [datetime(...), ...], 'date_2': [datetime(...), ...]})`
            Fetch historical features from the offline store for users 1, 2, and 3 for the ad ids and specified timestamps in the :py:mod:`date_1` column in the spine.

            A FeatureService :py:mod:`fs_on_demand` that contains only OnDemandFeatureViews and expects request time data for the key :py:mod:`amount`.

            | The request time data is defined in the feature definition as such:
            | `request_schema = StructType()`
            | `request_schema.add(StructField('amount', DoubleType()))`
            | `transaction_request = RequestDataSource(request_schema=request_schema)`

            1) :py:mod:`fs_on_demand.get_historical_features(spine)` where :py:mod:`spine=pandas.Dataframe({'amount': [30, 50, 10000]})`
            Fetch historical features from the offline store with request data inputs 30, 50, and 10000.

            A FeatureService :py:mod:`fs_all` that contains feature views of all types with join key 'user_id' and expects request time data for the key :py:mod:`amount`.

            1) :py:mod:`fs_all.get_historical_features(spine)` where :py:mod:`spine=pandas.Dataframe({'user_id': [1,2,3], 'amount': [30, 50, 10000], 'date': [datetime(...), datetime(...), datetime(...)]})`
            Fetch historical features from the offline store for users 1, 2, and 3 for the specified timestamps and request data inputs in the spine.

         :return: A Tecton :class:`TectonDataFrame`.
        """

        feature_view_text = internal_utils.plural(len(self._feature_definitions), "Feature View", "Feature Views")
        logger.info(f"Computing historical feature values for {len(self._feature_definitions)} {feature_view_text}.")
        sources = self._check_can_query_from_source(from_source)
        sources.display()

        if compute_mode.get_compute_mode() == compute_mode.ComputeMode.SNOWFLAKE:
            return snowflake_api.get_historical_features(
                spine=spine,
                timestamp_key=timestamp_key,
                include_feature_view_timestamp_columns=include_feature_view_timestamp_columns,
                from_source=from_source,
                save=save,
                save_as=save_as,
                feature_set_config=self._feature_set_config,
            )

        if compute_mode.get_compute_mode() == compute_mode.ComputeMode.ATHENA:
            if not internal_utils.is_live_workspace(self.workspace):
                raise errors.ATHENA_COMPUTE_ONLY_SUPPORTED_IN_LIVE_WORKSPACE
            return athena_api.get_historical_features(
                spine=spine,
                timestamp_key=timestamp_key,
                include_feature_view_timestamp_columns=include_feature_view_timestamp_columns,
                from_source=from_source,
                save=save,
                save_as=save_as,
                feature_set_config=self._feature_set_config,
            )

        if isinstance(spine, str):
            msg = "When using spark compute, `spine` must be one of (pyspark.sql.dataframe.DataFrame, pandas.core.frame.DataFrame, tecton.framework.data_frame.TectonDataFrame); got str instead."
            raise TypeError(msg)

        return spark_api.get_historical_features_for_feature_service(
            feature_service_spec=self._spec,
            feature_set_config=self._feature_set_config,
            spine=spine,
            timestamp_key=timestamp_key,
            from_source=from_source,
            save=save,
            save_as=save_as,
        )

    @sdk_decorators.sdk_public_method
    @sdk_decorators.assert_remote_object
    @typechecked
    def get_online_features(
        self,
        join_keys: Optional[Mapping[str, Union[int, np.int_, str, bytes]]] = None,
        include_join_keys_in_response: bool = False,
        request_data: Optional[Mapping[str, Union[int, np.int_, str, bytes, float]]] = None,
    ) -> tecton_dataframe.FeatureVector:
        """
        Returns a single Tecton :class:`tecton.FeatureVector` from the Online Store.
        At least one of join_keys or request_data is required.

        :param join_keys: Join keys of the enclosed FeatureViews.
        :param include_join_keys_in_response: Whether to include join keys as part of the response FeatureVector.
        :param request_data: Dictionary of request context values. Only applicable when the FeatureService contains OnDemandFeatureViews.

        Examples:
            A FeatureService :py:mod:`fs` that contains a BatchFeatureView and StreamFeatureView with join keys :py:mod:`user_id` and :py:mod:`ad_id`.

            1) :py:mod:`fs.get_online_features(join_keys={'user_id': 1, 'ad_id': 'c234'})`
            Fetch the latest features from the online store for user 1 and ad 'c234'.

            2) :py:mod:`fv.get_online_features(join_keys={'user_id': 1, 'ad_id': 'c234'}, include_join_keys_in_respone=True)`
            Fetch the latest features from the online store for user 1 and ad id 'c234'. Include the join key information (user_id=1, ad_id='c234') in the returned FeatureVector.

            A FeatureService :py:mod:`fs_on_demand` that contains only OnDemandFeatureViews and expects request time data for key :py:mod:`amount`.

            | The request time data is defined in the feature definition as such:
            | `request_schema = StructType()`
            | `request_schema.add(StructField('amount', DoubleType()))`
            | `transaction_request = RequestDataSource(request_schema=request_schema)`

            1) :py:mod:`fs_on_demand.get_online_features(request_data={'amount': 30})`
            Fetch the latest features from the online store with amount = 30.

            A FeatureService :py:mod:`fs_all` that contains feature views of all types with join key :py:mod:`user_id` and expects request time data for key :py:mod:`amount`.

            1) :py:mod:`fs_all.get_online_features(join_keys={'user_id': 1}, request_data={'amount': 30})`
            Fetch the latest features from the online store for user 1 with amount = 30.

        :return: A :class:`tecton.FeatureVector` of the results.
        """
        # Default to empty dicts.
        join_keys = join_keys or {}
        request_data = request_data or {}

        if not internal_utils.is_live_workspace(self.workspace):
            msg = "get_online_features"
            raise errors.UNSUPPORTED_OPERATION_IN_DEVELOPMENT_WORKSPACE(msg)

        if not self._spec.online_serving_enabled:
            msg = "get_online_features"
            raise errors.UNSUPPORTED_OPERATION(msg, "online_serving_enabled was not defined for this Feature Service.")
        if not join_keys and not request_data:
            raise errors.FS_GET_ONLINE_FEATURES_REQUIRED_ARGS

        fs_contains_non_odfvs = not all(fd.is_on_demand for fd in self._feature_set_config.feature_definitions)
        if fs_contains_non_odfvs and not join_keys:
            raise errors.GET_ONLINE_FEATURES_FS_JOIN_KEYS

        request_context = self._request_context
        required_request_context_keys = list(request_context.schema.keys())
        if required_request_context_keys and not request_data:
            raise errors.GET_ONLINE_FEATURES_FS_NO_REQUEST_DATA(required_request_context_keys)
        internal_utils.validate_request_data(request_data, required_request_context_keys)

        return query_helper._QueryHelper(self.workspace, feature_service_name=self.name).get_feature_vector(
            join_keys,
            include_join_keys_in_response,
            request_data,
            request_context,
        )

    @sdk_decorators.sdk_public_method
    @sdk_decorators.assert_remote_object
    @typechecked
    def query_features(
        self, join_keys: Mapping[str, Union[np.int_, int, str, bytes]]
    ) -> tecton_dataframe.TectonDataFrame:
        """
        [Advanced Feature] Queries the FeatureService with a partial set of join_keys defined in the ``online_serving_index``
        of the included FeatureViews. Returns a Tecton :class:`TectonDataFrame` of all matched records.

        :param join_keys: Query join keys, i.e., a union of join keys in the ``online_serving_index`` of all
            enclosed FeatureViews.
        :return: A Tecton :class:`TectonDataFrame`
        """
        if not internal_utils.is_live_workspace(self.workspace):
            msg = "query_features"
            raise errors.UNSUPPORTED_OPERATION_IN_DEVELOPMENT_WORKSPACE(msg)

        if not self._spec.online_serving_enabled:
            msg = "query_features"
            raise errors.UNSUPPORTED_OPERATION(msg, "online_serving_enabled was not defined for this Feature Service.")

        return query_helper._QueryHelper(self.workspace, feature_service_name=self.name).query_features(join_keys)

    @property
    def _request_context(self) -> request_context.RequestContext:
        merged_context = request_context.RequestContext({})
        for fv in self._feature_definitions:
            if isinstance(fv, framework_feature_view.OnDemandFeatureView):
                merged_context.merge(fv._request_context)
        return merged_context

    @sdk_decorators.assert_remote_object
    def _wait_until_ready(
        self, timeout: Optional[pendulum.Duration] = None, wait_for_materialization=True, verbose=False
    ):
        """Blocks until the service is ready to serve real-time requests.

        The FeatureService is considered ready once every FeatureView that has been added to it
        has had at least once successful materialization run.

        :param timeout: The timeout to wait. Defaults to 15 minutes.
        :param wait_for_materialization: If False, does not wait for batch materialization to complete.
        """
        if not internal_utils.is_live_workspace(self.workspace):
            msg = "_wait_until_ready"
            raise errors.UNSUPPORTED_OPERATION_IN_DEVELOPMENT_WORKSPACE(msg)

        if timeout is None:
            timeout = pendulum.Duration(minutes=15)

        deadline = pendulum.now() + timeout

        has_been_not_ready = False
        while True:
            request = feature_service__api_pb2.GetFeatureServiceStateRequest()
            request.feature_service_locator.feature_service_name = self.name
            request.feature_service_locator.workspace_name = self.workspace
            http_response = requests.post(
                urllib.parse.urljoin(
                    conf.get_or_raise("FEATURE_SERVICE") + "/", "v1/feature-service/get-feature-service-state"
                ),
                data=json_format.MessageToJson(request),
                headers=query_helper._QueryHelper(self.workspace, feature_service_name=self.name)._prepare_headers(),
            )
            details = http_response.json()
            if http_response.status_code == 404:
                # FeatureService is not ready to serve
                if verbose:
                    logger.info(f" Waiting for FeatureService to be ready to serve ({details['message']})")
                else:
                    logger.info(" Waiting for FeatureService to be ready to serve")
            elif http_response.status_code == 200:
                # FeatureService is ready
                if verbose:
                    logger.info(f"wait_until_ready: Ready! Response={http_response.text}")
                else:
                    logger.info("wait_until_ready: Ready!")
                # Extra wait time due to different FS hosts being potentially out-of-sync in picking up the latest state
                if has_been_not_ready:
                    time.sleep(20)
                return
            else:
                http_response.raise_for_status()
                return
            if pendulum.now() > deadline:
                logger.info(f"wait_until_ready: Response={http_response.text}")
                raise TimeoutError()
            has_been_not_ready = True
            time.sleep(10)
            continue


def _feature_reference_to_feature_service_feature_package(
    feature_reference: framework_feature_view.FeatureReference,
) -> feature_service__args_pb2.FeatureServiceFeaturePackage:
    if feature_reference.override_join_keys:
        override_join_keys = [
            feature_service__args_pb2.ColumnPair(feature_column=fv_key, spine_column=spine_key)
            for fv_key, spine_key in sorted(feature_reference.override_join_keys.items())
        ]
    else:
        override_join_keys = None

    return feature_service__args_pb2.FeatureServiceFeaturePackage(
        feature_package_id=feature_reference.feature_definition._id_proto,
        namespace=feature_reference.namespace,
        override_join_keys=override_join_keys,
        features=feature_reference.features if feature_reference.features else None,
    )
