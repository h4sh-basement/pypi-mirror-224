import json
import typing
from typing import Dict
from typing import List
from typing import Optional

import pendulum

from tecton_core import errors
from tecton_core import feature_definition_wrapper
from tecton_core import id_helper
from tecton_core import materialization_context
from tecton_core import schema_derivation_utils as core_schema_derivation_utils
from tecton_core import specs
from tecton_proto.args import data_source_pb2
from tecton_proto.args import feature_view_pb2
from tecton_proto.args import pipeline_pb2
from tecton_proto.args import virtual_data_source_pb2
from tecton_proto.common import schema_pb2
from tecton_proto.common import spark_schema_pb2
from tecton_snowflake import pipeline_helper
from tecton_snowflake import snowflake_type_utils
from tecton_snowflake.utils import format_sql


if typing.TYPE_CHECKING:
    import snowflake.connector
    import snowflake.snowpark


def _get_mock_sql_for_data_source(data_source_spec: specs.DataSourceSpec) -> str:
    """Adds LIMIT 0 to data sources during fv schema derivation to improve performance.

    Similar to get_data_source_schema_sql expect this method runs on specs."""
    snowflake_source = data_source_spec.batch_source
    if type(snowflake_source) != specs.SnowflakeSourceSpec:
        msg = f"The batch source for Data Source {data_source_spec.name} must be a Snowflake source."
        raise ValueError(msg)

    if snowflake_source.table:
        sql_str = (
            f"SELECT * FROM ({snowflake_source.database}.{snowflake_source.schema}.{snowflake_source.table}) LIMIT 0"
        )
    elif snowflake_source.query:
        sql_str = f"SELECT * FROM ({snowflake_source.query}) LIMIT 0"
    else:
        msg = "A Snowflake source must have one of 'query' or 'table' set"
        raise ValueError(msg)
    return format_sql(sql_str)


def get_data_source_schema_sql(ds_args: data_source_pb2.SnowflakeDataSourceArgs) -> str:
    """Return the SQL used to query the data source provided during schema derivation.

    Similar to _get_mock_sql_for_data_source expect this method runs on data source args."""
    if ds_args.HasField("table"):
        if not ds_args.database and not ds_args.schema:
            msg = "A Snowflake source must set 'database', 'schema', and 'table' to read from a Snowflake table."
            raise ValueError(msg)
        full_table_name = f"{ds_args.database}.{ds_args.schema}.{ds_args.table}"
        sql_str = f"SELECT * FROM {full_table_name} LIMIT 0"
    elif ds_args.HasField("query"):
        sql_str = f"SELECT * FROM ({ds_args.query}) LIMIT 0"
    else:
        msg = "A Snowflake source must have one of 'query' or 'table' set"
        raise ValueError(msg)
    return format_sql(sql_str)


def get_snowflake_schema(
    ds_args: virtual_data_source_pb2.VirtualDataSourceArgs, connection: "snowflake.connector.Connection"
) -> spark_schema_pb2.SparkSchema:
    """Derive schema for snowflake data source on snowflake compute.

    This method is used for notebook driven development.
    The logic should mirror logic in resolveBatch() in SnowflakeDDL.kt.
    """
    cur = connection.cursor()

    sql_str = get_data_source_schema_sql(ds_args.snowflake_ds_config)
    try:
        cur.execute(sql_str)
    except Exception:
        msg = f"Running the following SQL failed: {sql_str}"
        raise errors.TectonInternalError(msg)

    # Get the schema from the previously ran query
    query_id = cur.sfqid
    cur.execute(f"DESCRIBE RESULT '{query_id}';")
    schema_list = cur.fetchall()  # TODO: use fetch_pandas_all() once it supports describe statements

    proto = spark_schema_pb2.SparkSchema()
    for row in schema_list:
        # schema returned is in the form (name, type,...)
        name = row[0]
        proto_field = proto.fields.add()
        proto_field.name = name
        proto_field.structfield_json = json.dumps({"name": name, "type": row[1], "nullable": True, "metadata": {}})
    return proto


def _get_mock_sql_inputs_for_schema_derivation(
    pipeline: pipeline_pb2.Pipeline, data_source_specs: List[specs.DataSourceSpec]
) -> Dict[str, str]:
    data_source_nodes = feature_definition_wrapper.pipeline_to_ds_inputs(pipeline).values()
    id_to_spec = {spec.id: spec for spec in data_source_specs}
    mock_sql_inputs = {}
    for node in data_source_nodes:
        data_source_id = id_helper.IdHelper.to_string(node.virtual_data_source_id)
        spec = id_to_spec[data_source_id]
        # Map the data source input name to the SQL to run. The input name and data source name are not always the same.
        mock_sql_inputs[node.input_name] = _get_mock_sql_for_data_source(spec)
    return mock_sql_inputs


def get_feature_view_schema_sql(
    pipeline: pipeline_pb2.Pipeline,
    transformation_specs: List[specs.TransformationSpec],
    data_source_specs: List[specs.DataSourceSpec],
    materialization_context: materialization_context.BaseMaterializationContext,
    session: Optional["snowflake.snowpark.Session"] = None,
) -> str:
    """Return the SQL used to run fv schema derivation."""
    # Create mock sql inputs for data sources to improve performance.
    mock_sql_inputs = _get_mock_sql_inputs_for_schema_derivation(pipeline, data_source_specs)

    return pipeline_helper.pipeline_to_sql_string(
        pipeline,
        data_source_specs,
        transformation_specs,
        mock_sql_inputs=mock_sql_inputs,
        materialization_context=materialization_context,
        session=session,
    )


def get_feature_view_view_schema(
    feature_view_args: feature_view_pb2.FeatureViewArgs,
    transformation_specs: List[specs.TransformationSpec],
    data_source_specs: List[specs.DataSourceSpec],
    connection: "snowflake.connector.Connection",
    session: Optional["snowflake.snowpark.Session"] = None,
) -> schema_pb2.Schema:
    """Compute the Feature View view schema.

    This method is used for notebook driven development.
    The logic should mirror logic in resolve() in SnowflakeDDL.kt.
    """
    cur = connection.cursor()

    # Create a default materialization context for the feature view.
    _tecton_materialization_context = materialization_context.BoundMaterializationContext._create_internal(
        pendulum.from_timestamp(0, pendulum.tz.UTC),
        pendulum.datetime(2100, 1, 1),
        pendulum.Duration(),
    )

    sql_str = get_feature_view_schema_sql(
        feature_view_args.pipeline, transformation_specs, data_source_specs, _tecton_materialization_context, session
    )
    try:
        cur.execute(sql_str)
    except Exception:
        msg = f"Running the following SQL failed: {sql_str}"
        raise errors.TectonInternalError(msg)

    # Get the schema from the previously ran query
    query_id = cur.sfqid
    cur.execute(f"DESCRIBE RESULT '{query_id}';")
    schema_list = cur.fetchall()  # TODO: use fetch_pandas_all() once it supports describe statements

    columns = []
    for row in schema_list:
        # schema returned is in the form (name, type,...)
        name = row[0]
        tecton_type = snowflake_type_utils.snowflake_type_to_tecton_type(row[1], name)
        column_proto = schema_pb2.Column()
        column_proto.CopyFrom(core_schema_derivation_utils.column_from_tecton_data_type(tecton_type))
        column_proto.name = name
        columns.append(column_proto)

    return schema_pb2.Schema(columns=columns)
