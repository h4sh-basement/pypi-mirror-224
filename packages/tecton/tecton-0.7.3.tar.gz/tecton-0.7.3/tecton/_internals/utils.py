import collections
from datetime import datetime
from datetime import timezone
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Union

import numpy as np
import pandas as pd
import pendulum
from pyspark.sql import DataFrame as pysparkDF
from pyspark.sql.types import TimestampType

from tecton._internals import errors
from tecton._internals import metadata_service
from tecton._internals.display import Displayable
from tecton_core import specs
from tecton_core.errors import INGEST_COLUMN_TYPE_MISMATCH
from tecton_core.errors import TectonValidationError
from tecton_core.fco_container import FcoContainer
from tecton_core.id_helper import IdHelper
from tecton_core.query.node_interface import DataframeWrapper
from tecton_core.query_consts import UDF_INTERNAL
from tecton_core.schema import Schema
from tecton_proto.args.pipeline_pb2 import PipelineNode
from tecton_proto.consumption.consumption_pb2 import ConsumptionInfo
from tecton_proto.data.freshness_status_pb2 import FreshnessStatus
from tecton_proto.data.materialization_status_pb2 import DataSourceType
from tecton_proto.data.materialization_status_pb2 import MaterializationAttemptStatus
from tecton_proto.data.materialization_status_pb2 import MaterializationStatusState
from tecton_proto.metadataservice.metadata_service_pb2 import GetFeatureFreshnessRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetWorkspaceRequest
from tecton_proto.metadataservice.metadata_service_pb2 import QueryFeatureViewsRequest
from tecton_spark.schema_spark_utils import schema_from_spark


_TIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z"
KEY_DELETION_MAX = 500000


def validate_join_keys(join_keys: List[str]):
    """
    Validates that `join_keys` is not empty and has non-empty distinct values.

    :raises TectonValidationError: if `join_keys` is invalid.
    """
    if not join_keys:
        msg = "join_keys"
        raise errors.EMPTY_ARGUMENT(msg)

    if "" in join_keys:
        msg = "join_keys"
        raise errors.EMPTY_ELEMENT_IN_ARGUMENT(msg)

    if len(join_keys) > len(set(join_keys)):
        msg = "join_keys"
        raise errors.DUPLICATED_ELEMENTS_IN_ARGUMENT(msg)


def validate_spine_dataframe(
    spine: DataframeWrapper, timestamp_key: Optional[str], request_context_keys: List[str] = None
):
    spine_df = spine._dataframe
    if timestamp_key:
        if timestamp_key not in spine_df.columns:
            msg = "timestamp_key"
            raise errors.MISSING_SPINE_COLUMN(msg, timestamp_key, spine_df.columns)
        if isinstance(spine_df, pysparkDF):
            data_type = spine_df.schema[timestamp_key].dataType
            if not isinstance(data_type, TimestampType):
                raise errors.INVALID_SPINE_TIME_KEY_TYPE_SPARK(data_type)
        elif isinstance(spine_df, pd.DataFrame):
            dtypes = dict(spine_df.dtypes)
            data_type = dtypes[timestamp_key]
            if not pd.api.types.is_datetime64_any_dtype(dtypes[timestamp_key]):
                raise errors.INVALID_SPINE_TIME_KEY_TYPE_PANDAS(data_type)
    if request_context_keys:
        for key in request_context_keys:
            if key not in spine_df.columns:
                raise errors.MISSING_REQUEST_DATA_IN_SPINE(key, spine_df.columns)


def format_seconds_into_highest_unit(total_seconds):
    intervals = [("wk", 60 * 60 * 24 * 7), ("d", 60 * 60 * 24), ("h", 60 * 60), ("m", 60), ("s", 1)]

    units = []
    for abbreviation, size in intervals:
        count = total_seconds // size
        total_seconds %= size
        if count != 0:
            units.append(f"{count}{abbreviation}")

    return " ".join(units[:2] if len(units) > 2 else units)


def snake_to_capitalized(snake_str):
    return "".join(x.title() for x in snake_str.split("_"))


def format_materialization_attempts(
    materialization_attempts, verbose=False, limit=1000, sort_columns=None, errors_only=False
) -> Tuple[List, List[List]]:
    """
    Formats a list of materialization attempts for use in Displayable.from_table
    Returns (column_names, materialization_status_rows).
    """
    column_names = ["TYPE", "WINDOW_START_TIME", "WINDOW_END_TIME", "STATUS", "ATTEMPT"]
    if verbose:
        column_names.extend(
            [
                "MATERIALIZATION_TASK",
                "ENV_VERSION",
                "TERMINATION_REASON",
                "STATE_MESSAGE",
                "TASK_SCHEDULED_AT",
                "ONLINE_WRITE_ROWS",
                "ONLINE_WRITE_BYTES",
                "OFFLINE_WRITE_ROWS",
            ]
        )
    column_names.extend(["JOB_CREATED_AT", "JOB_LOGS"])

    materialization_attempts = materialization_attempts[:limit]
    if errors_only:
        materialization_attempts = [
            attempt
            for attempt in materialization_attempts
            if _materialization_status_state_name(attempt.materialization_state) == "ERROR"
        ]

    materialization_status_rows = []
    for attempt_status in materialization_attempts:
        data = _get_materialization_status_row_data(attempt_status)
        materialization_status_rows.append([data[c] for c in column_names])

    if sort_columns:
        keys = [k.upper() for k in sort_columns.split(",")]
        indices = []
        for key in keys:
            try:
                indices.append(column_names.index(key))
            except ValueError:
                msg = f"Unknown sort key {key}, should be one of: {','.join(column_names)}"
                raise ValueError(msg)
        materialization_status_rows.sort(key=lambda r: [r[i] for i in indices])

    return column_names, materialization_status_rows


def _materialization_status_state_name(state: MaterializationStatusState) -> str:
    state_name = MaterializationStatusState.Name(state)
    return state_name.replace("MATERIALIZATION_STATUS_STATE_", "")


def _get_materialization_status_row_data(attempt_status: MaterializationAttemptStatus) -> Dict[str, str]:
    status_dict = {}
    status_dict["TYPE"] = (
        "STREAM"
        if attempt_status.data_source_type == DataSourceType.DATA_SOURCE_TYPE_STREAM
        else "BATCH"
        if attempt_status.data_source_type == DataSourceType.DATA_SOURCE_TYPE_BATCH
        else "INGEST"
        if attempt_status.data_source_type == DataSourceType.DATA_SOURCE_TYPE_INGEST
        else "DELETION"
        if attempt_status.data_source_type == DataSourceType.DATA_SOURCE_TYPE_DELETION
        else "UNKNOWN"
    )
    status_dict["WINDOW_START_TIME"] = (
        "N/A"
        if not attempt_status.HasField("window_start_time")
        else attempt_status.window_start_time.ToDatetime().replace(tzinfo=timezone.utc).strftime(_TIME_FORMAT)
    )
    status_dict["WINDOW_END_TIME"] = (
        "N/A"
        if not attempt_status.HasField("window_end_time")
        else attempt_status.window_end_time.ToDatetime().replace(tzinfo=timezone.utc).strftime(_TIME_FORMAT)
    )
    status_dict["STATUS"] = _materialization_status_state_name(attempt_status.materialization_state)
    status_dict["ATTEMPT"] = "N/A" if not attempt_status.HasField("attempt_number") else attempt_status.attempt_number
    status_dict["MATERIALIZATION_TASK"] = IdHelper.to_string(attempt_status.materialization_task_id)
    status_dict["ENV_VERSION"] = attempt_status.spark_cluster_environment_version
    status_dict["TERMINATION_REASON"] = (
        "N/A"
        if not attempt_status.HasField("termination_reason")
        or len(attempt_status.termination_reason) == 0
        or attempt_status.termination_reason == "UNKNOWN_TERMINATION_REASON"
        else attempt_status.termination_reason
    )
    status_dict["STATE_MESSAGE"] = (
        "N/A"
        if not attempt_status.HasField("state_message") or len(attempt_status.state_message) == 0
        else attempt_status.state_message
    )
    status_dict["TASK_SCHEDULED_AT"] = (
        "N/A"
        if not attempt_status.HasField("materialization_task_created_at")
        else attempt_status.materialization_task_created_at.ToDatetime()
        .replace(tzinfo=timezone.utc)
        .strftime(_TIME_FORMAT)
    )
    status_dict["JOB_CREATED_AT"] = (
        "N/A"
        if not attempt_status.HasField("attempt_created_at")
        else attempt_status.attempt_created_at.ToDatetime().replace(tzinfo=timezone.utc).strftime(_TIME_FORMAT)
    )
    status_dict["JOB_LOGS"] = "N/A" if not attempt_status.HasField("run_page_url") else attempt_status.run_page_url

    consumption_metrics = ["ONLINE_WRITE_ROWS", "ONLINE_WRITE_BYTES", "OFFLINE_WRITE_ROWS"]
    for m in consumption_metrics:
        status_dict[m] = 0
    for info in attempt_status.consumption_info:
        if info.metric in consumption_metrics:
            status_dict[info.metric] += info.units_consumed
    for m in consumption_metrics:
        status_dict[m] = str(status_dict[m])

    return status_dict


def get_num_dependent_fv(node: PipelineNode, visited_inputs: Dict[str, bool]) -> int:
    if node.HasField("feature_view_node"):
        if node.feature_view_node.input_name in visited_inputs:
            return 0
        visited_inputs[node.feature_view_node.input_name] = True
        return 1
    elif node.HasField("transformation_node"):
        ret = 0
        for child in node.transformation_node.inputs:
            ret = ret + get_num_dependent_fv(child.node, visited_inputs)
        return ret
    return 0


def infer_timestamp(spine: Union[pd.DataFrame, pysparkDF, DataframeWrapper]) -> Optional[str]:
    if isinstance(spine, DataframeWrapper):
        spine = spine._dataframe
    dtypes = dict(spine.dtypes)

    if isinstance(spine, pd.DataFrame):
        timestamp_cols = [(k, v) for (k, v) in dtypes.items() if pd.api.types.is_datetime64_any_dtype(v)]
    elif isinstance(spine, pysparkDF):
        timestamp_cols = [(k, v) for (k, v) in dtypes.items() if v == "timestamp"]
    else:
        msg = f"Unexpected data type for spine: {type(spine)}"
        raise TectonValidationError(msg)

    if len(timestamp_cols) > 1 or len(timestamp_cols) == 0:
        msg = f"Could not infer timestamp keys from {dtypes}; please specify explicitly"
        raise TectonValidationError(msg)
    return timestamp_cols[0][0]


def can_be_stale(ff_proto: FreshnessStatus) -> bool:
    return (
        ff_proto.expected_freshness.seconds > 0 and ff_proto.freshness.seconds > 0 and ff_proto.materialization_enabled
    )


def format_freshness_table(freshness_statuses: List[FreshnessStatus]) -> Displayable:
    timestamp_format = "%x %H:%M"
    headers = [
        "Feature View",
        "Materialized?",
        "Stale?",
        "Freshness",
        "Expected Freshness",
        "Created",
        "Stream?",
    ]

    freshness_data = [
        [
            ff_proto.feature_view_name,
            str(ff_proto.materialization_enabled),
            str(ff_proto.is_stale) if can_be_stale(ff_proto) else "-",
            format_seconds_into_highest_unit(ff_proto.freshness.seconds) if can_be_stale(ff_proto) else "-",
            format_seconds_into_highest_unit(ff_proto.expected_freshness.seconds) if can_be_stale(ff_proto) else "-",
            datetime.fromtimestamp(ff_proto.created_at.seconds).strftime(timestamp_format),
            str(ff_proto.is_stream),
        ]
        for ff_proto in freshness_statuses
    ]

    sort_order = {"True": 0, "False": 1, "-": 2}
    freshness_data = sorted(freshness_data, key=lambda row: sort_order[row[2]])
    table = Displayable.from_table(headings=headers, rows=freshness_data, max_width=0)
    table._text_table.set_cols_align(["c" for _ in range(len(headers))])
    return table


def get_all_freshness(workspace: str):
    request = QueryFeatureViewsRequest()
    request.workspace = workspace
    response = metadata_service.instance().QueryFeatureViews(request)
    fco_container = FcoContainer.from_proto(response.fco_container)
    fv_ids = []
    for spec in fco_container.get_root_fcos():
        if isinstance(spec, specs.MaterializedFeatureViewSpec):
            fv_ids.append(IdHelper.from_string(spec.id))

    freshness_statuses = []

    for fv_id in fv_ids:
        fresh_request = GetFeatureFreshnessRequest()
        fresh_request.fco_locator.id.CopyFrom(fv_id)
        fresh_request.fco_locator.workspace = workspace
        fresh_response = metadata_service.instance().GetFeatureFreshness(fresh_request)
        freshness_statuses.append(fresh_response.freshness_status)

    return freshness_statuses


def is_live_workspace(workspace_name: str) -> bool:
    request = GetWorkspaceRequest()
    request.workspace_name = workspace_name
    response = metadata_service.instance().GetWorkspace(request)
    return response.workspace.capabilities.materializable


def filter_internal_columns(df: pysparkDF) -> pysparkDF:
    output_columns = [f"`{c.name}`" for c in df.schema if UDF_INTERNAL not in c.name]
    return df.select(*output_columns)


def validate_request_data(
    request_data: Optional[dict],
    required_request_context_keys: List[str],
    is_read_api_v3=True,
):
    missing_keys = set(required_request_context_keys) - set(request_data.keys()) if request_data else None
    if missing_keys:
        # TODO:(read-api) remove this check and old error message once get_feature_vector is deleted
        if is_read_api_v3:
            raise errors.GET_ONLINE_FEATURES_MISSING_REQUEST_KEY(missing_keys)
        raise errors.GET_FEATURE_VECTOR_MISSING_REQUEST_KEY(missing_keys)


def validate_join_key_types(join_keys: Mapping[str, Union[int, np.int_, str, bytes]]):
    if not isinstance(join_keys, dict):
        raise errors.INVALID_JOIN_KEYS_TYPE(type(join_keys))
    for key in join_keys:
        if type(join_keys[key]) not in [int, np.int_, str, bytes]:
            raise errors.INVALID_INDIVIDUAL_JOIN_KEY_TYPE(key, type(join_keys[key]))


def validate_entity_deletion_keys_dataframe(df: pysparkDF, join_keys: List[str], view_schema: Schema):
    if len(set(df.columns)) != len(df.columns):
        raise errors.DUPLICATED_COLS_IN_KEYS(", ".join(list(df.columns)))
    row_count = df.count()
    if row_count > KEY_DELETION_MAX:
        raise errors.TOO_MANY_KEYS
    if row_count == 0:
        msg = "join_keys"
        raise errors.EMPTY_ARGUMENT(msg)
    if set(df.columns) != set(join_keys):
        raise errors.INCORRECT_KEYS(", ".join(list(df.columns)), ", ".join(join_keys))
    df_columns = schema_from_spark(df.schema).column_name_and_data_types()
    fv_columns = view_schema.column_name_and_data_types()
    for df_column in df_columns:
        if df_column not in fv_columns:
            raise INGEST_COLUMN_TYPE_MISMATCH(
                df_column[0], [x for x in fv_columns if x[0] == df_column[0]][0][1], df_column[1]
            )


def get_time_limits_of_pandas_dataframe(df: pd.DataFrame, time_key: str) -> pendulum.Period:
    time_start = df[time_key].min()
    time_end = df[time_key].max()
    # Need to add 1 microsecond to the end time, since the range is exclusive at the end, and we need
    # to make sure to include the very last feature value (in terms of the event timestamp).
    return pendulum.instance(time_end).add(microseconds=1) - pendulum.instance(time_start)


def make_consumption_map(consumption_infos: List[ConsumptionInfo]) -> Dict[str, ConsumptionInfo]:
    m = collections.defaultdict(int)
    for info in consumption_infos:
        m[info.metric] += info.units_consumed
    return m


def plural(x: int, singular: str, plural: str):
    """
    Returns the `singular` string if `x` is equal to 1 and `plural` if not.
    """
    if x == 1:
        return singular
    else:
        return plural
