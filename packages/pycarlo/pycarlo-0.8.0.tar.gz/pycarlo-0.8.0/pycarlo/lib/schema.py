import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo


__docformat__ = 'markdown'


########################################################################
# Scalars and Enumerations
########################################################################
class AccessKeyIndexEnum(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `account`None
    * `user`None
    '''
    __schema__ = schema
    __choices__ = ('account', 'user')


class AccountNotificationDigestSettingsModelDigestType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ANOMALIES_DIGEST`: anomalies based digest
    * `INACTIVE_DIGEST`: inactive monitors digest
    * `MISCONF_DIGEST`: misconfigured monitors digest
    '''
    __schema__ = schema
    __choices__ = ('ANOMALIES_DIGEST', 'INACTIVE_DIGEST', 'MISCONF_DIGEST')


class AccountNotificationRoutingRulesModelMonitorLabelsMatchType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `AND`: AND
    * `OR`: OR
    '''
    __schema__ = schema
    __choices__ = ('AND', 'OR')


class AccountNotificationSettingsModelNotificationScheduleType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `BACKUP_OR_FAILURE`: Backup Or Failure
    * `DIGEST`: Digest
    * `REALTIME`: Realtime
    '''
    __schema__ = schema
    __choices__ = ('BACKUP_OR_FAILURE', 'DIGEST', 'REALTIME')


class AccountNotificationSettingsModelType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ALATION`: Alation
    * `EMAIL`: Email
    * `MATTERMOST`: Mattermost
    * `MSTEAMS`: Msteams
    * `OPSGENIE`: Opsgenie
    * `PAGERDUTY`: Pagerduty
    * `SLACK`: Slack
    * `SLACK_V2`: Slack V2
    * `WEBHOOK`: Webhook
    '''
    __schema__ = schema
    __choices__ = ('ALATION', 'EMAIL', 'MATTERMOST', 'MSTEAMS', 'OPSGENIE', 'PAGERDUTY', 'SLACK', 'SLACK_V2', 'WEBHOOK')


class AggregationFunction(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `AVG`None
    * `MAX`None
    * `MIN`None
    '''
    __schema__ = schema
    __choices__ = ('AVG', 'MAX', 'MIN')


class BiContainerModelType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `LOOKER`: Looker
    * `POWER_BI`: Power BI
    * `TABLEAU`: Tableau
    '''
    __schema__ = schema
    __choices__ = ('LOOKER', 'POWER_BI', 'TABLEAU')


Boolean = sgqlc.types.Boolean

class ComparisonType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ABSOLUTE_VOLUME`None
    * `CHANGE`None
    * `DYNAMIC_THRESHOLD`None
    * `FRESHNESS`None
    * `GROWTH_VOLUME`None
    * `THRESHOLD`None
    '''
    __schema__ = schema
    __choices__ = ('ABSOLUTE_VOLUME', 'CHANGE', 'DYNAMIC_THRESHOLD', 'FRESHNESS', 'GROWTH_VOLUME', 'THRESHOLD')


class ConnectionModelType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ATHENA`: Athena
    * `BIGQUERY`: BigQuery
    * `DATABRICKS_DELTA`: Databricks Delta
    * `DATABRICKS_METASTORE`: Databricks metastore
    * `DATABRICKS_SQL_WAREHOUSE`: Databricks Sql Warehouse
    * `DBT_CLOUD`: dbt Cloud
    * `DBT_CLOUD_V2`: dbt Cloud v2
    * `DBT_CLOUD_WEBHOOK`: dbt Cloud Webhook
    * `DBT_CORE`: dbt Core
    * `FIVETRAN`: Fivetran
    * `GLUE`: Glue
    * `HIVE`: Hive
    * `HIVE_MYSQL`: Hive (MySQL)
    * `HIVE_S3`: Hive (S3 Location)
    * `LOOKER`: Looker
    * `LOOKER_GIT`: Looker Git
    * `LOOKER_GIT_CLONE`: Looker Git Clone either ssh or https
    * `LOOKER_GIT_SSH`: Looker Git SSH
    * `POWER_BI`: Power BI
    * `PRESTO`: Presto
    * `PRESTO_S3`: Presto (S3 Location)
    * `REDSHIFT`: Amazon Redshift
    * `S3`: S3
    * `S3_AIRFLOW_LOG_EVENTS`: S3 Airflow Log Events
    * `S3_METADATA_EVENTS`: S3 Metadata Events
    * `S3_QL_EVENTS`: S3 Query Log Events
    * `SNOWFLAKE`: Snowflake
    * `SPARK`: Spark
    * `TABLEAU`: Tableau
    * `TRANSACTIONAL_DB`: transactional-db
    '''
    __schema__ = schema
    __choices__ = ('ATHENA', 'BIGQUERY', 'DATABRICKS_DELTA', 'DATABRICKS_METASTORE', 'DATABRICKS_SQL_WAREHOUSE', 'DBT_CLOUD', 'DBT_CLOUD_V2', 'DBT_CLOUD_WEBHOOK', 'DBT_CORE', 'FIVETRAN', 'GLUE', 'HIVE', 'HIVE_MYSQL', 'HIVE_S3', 'LOOKER', 'LOOKER_GIT', 'LOOKER_GIT_CLONE', 'LOOKER_GIT_SSH', 'POWER_BI', 'PRESTO', 'PRESTO_S3', 'REDSHIFT', 'S3', 'S3_AIRFLOW_LOG_EVENTS', 'S3_METADATA_EVENTS', 'S3_QL_EVENTS', 'SNOWFLAKE', 'SPARK', 'TABLEAU', 'TRANSACTIONAL_DB')


class CustomRuleComparisonOperator(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EQ`None
    * `GT`None
    * `GTE`None
    * `LT`None
    * `LTE`None
    * `NEQ`None
    '''
    __schema__ = schema
    __choices__ = ('EQ', 'GT', 'GTE', 'LT', 'LTE', 'NEQ')


class CustomRuleModelQueryResultType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `SINGLE_NUMERIC`: SINGLE_NUMERIC
    '''
    __schema__ = schema
    __choices__ = ('SINGLE_NUMERIC',)


class CustomRuleModelRuleType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CUSTOM_SQL`: Custom SQL Metric Rule
    * `FIELD_QUALITY`: Field Quality Rule
    * `FRESHNESS`: Freshness Rule
    * `TABLE_METRIC`: Table Metric Rule
    * `VOLUME`: Volume Rule
    '''
    __schema__ = schema
    __choices__ = ('CUSTOM_SQL', 'FIELD_QUALITY', 'FRESHNESS', 'TABLE_METRIC', 'VOLUME')


class DataAssetTypeEnum(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ASSET_TYPE_EXTERNAL`None
    * `ASSET_TYPE_SNOWFLAKE_STREAM`None
    * `ASSET_TYPE_TABLE`None
    * `ASSET_TYPE_VIEW`None
    * `ASSET_TYPE_WILDCARD_TABLE`None
    '''
    __schema__ = schema
    __choices__ = ('ASSET_TYPE_EXTERNAL', 'ASSET_TYPE_SNOWFLAKE_STREAM', 'ASSET_TYPE_TABLE', 'ASSET_TYPE_VIEW', 'ASSET_TYPE_WILDCARD_TABLE')


class DataCollectorEventTypes(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `s3_airflow_log_events`None
    * `s3_metadata_events`None
    * `s3_ql_events`None
    '''
    __schema__ = schema
    __choices__ = ('s3_airflow_log_events', 's3_metadata_events', 's3_ql_events')


class DataCollectorScheduleModelDeleteReason(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `NONE`: Empty reason
    * `NO_COLLECTOR`: No Collector
    '''
    __schema__ = schema
    __choices__ = ('NONE', 'NO_COLLECTOR')


class DataCollectorScheduleModelScheduleType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `DYNAMIC`: Dynamic
    * `FIXED`: Fixed
    * `LOOSE`: Loose
    * `MANUAL`: Manual
    '''
    __schema__ = schema
    __choices__ = ('DYNAMIC', 'FIXED', 'LOOSE', 'MANUAL')


class DataCollectorScheduleModelSkipReason(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CONNECTION_DISABLED`: Connection disabled
    * `MANUALLY_SKIPPED`: Manually skipped
    * `NONE`: Empty reason
    '''
    __schema__ = schema
    __choices__ = ('CONNECTION_DISABLED', 'MANUALLY_SKIPPED', 'NONE')


class DataColumnTypes(sgqlc.types.Enum):
    '''Available types for column values.

    Enumeration Choices:

    * `CHART`None
    * `DATE_TIME`None
    * `HOURS`None
    * `NUMERIC`None
    * `PERCENTAGE`None
    * `TEXT`None
    '''
    __schema__ = schema
    __choices__ = ('CHART', 'DATE_TIME', 'HOURS', 'NUMERIC', 'PERCENTAGE', 'TEXT')


class DataMaintenanceMetric(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ALL`None
    * `DT_METRICS`None
    * `FH_METRICS`None
    * `FRESHNESS`None
    * `VOLUME`None
    '''
    __schema__ = schema
    __choices__ = ('ALL', 'DT_METRICS', 'FH_METRICS', 'FRESHNESS', 'VOLUME')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DbtProjectModelSource(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CLI`: CLI
    * `DBT_CLOUD`: dbt Cloud
    * `DBT_CORE`: dbt Core
    '''
    __schema__ = schema
    __choices__ = ('CLI', 'DBT_CLOUD', 'DBT_CORE')


class DetectorStatus(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ACTIVE`None
    * `INACTIVE`None
    * `TRAINING`None
    '''
    __schema__ = schema
    __choices__ = ('ACTIVE', 'INACTIVE', 'TRAINING')


class EtlType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `FIVETRAN`None
    '''
    __schema__ = schema
    __choices__ = ('FIVETRAN',)


class EventModelEventState(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `FALSE_POSITIVE`: FALSE POSITIVE
    * `MUTED`: MUTED
    * `NOTIFIED`: NOTIFIED
    * `NO_ACTION_REQUIRED`: NO ACTION REQUIRED
    * `OPEN`: OPEN
    * `RESOLVED`: RESOLVED
    * `STALE`: STALE
    * `SYSTEM_RESOLVED`: RESOLVED
    * `TIMELINE`: Timeline event status
    * `USER_RESOLVED`: RESOLVED
    '''
    __schema__ = schema
    __choices__ = ('FALSE_POSITIVE', 'MUTED', 'NOTIFIED', 'NO_ACTION_REQUIRED', 'OPEN', 'RESOLVED', 'STALE', 'SYSTEM_RESOLVED', 'TIMELINE', 'USER_RESOLVED')


class EventModelEventType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `COMMENT`: Timeline Comment
    * `CUSTOM_RULE_ANOM`: Custom Rule Anomaly
    * `DBT_MODEL_ERROR`: dbt Model Error
    * `DBT_TEST_FAILURE`: dbt Test Failure
    * `DELETE_TABLE`: Delete Table
    * `DIST_ANOM`: Distribution Anomaly
    * `FRESH_ANOM`: Freshness Anomaly
    * `INACTIVE_MONITOR`: Inactive Monitor
    * `INCIDENT_OWNER_UPDATE`: Incident Owner Update
    * `INCIDENT_SEVERITY_UPDATE`: Incident Severity Update
    * `INCIDENT_SLACK_THREAD`: Incident Slack Thread
    * `INCIDENT_SPLIT`: Incident Split
    * `INCIDENT_STATUS_UPDATE`: Incident Status Update
    * `JSON_SCHEMA_CHANGE`: JSON Schema Change
    * `METRIC_ANOM`: Metric Anomaly
    * `QUERY_RUNTIME_ANOM`: Query Runtime Anomaly
    * `SCHEMA_CHANGE`: Schema Change
    * `SIZE_ANOM`: Size Anomaly
    * `SIZE_DIFF`: Row count anomaly
    * `UNCHANGED_SIZE_ANOM`: Unchanged Size Anomaly
    '''
    __schema__ = schema
    __choices__ = ('COMMENT', 'CUSTOM_RULE_ANOM', 'DBT_MODEL_ERROR', 'DBT_TEST_FAILURE', 'DELETE_TABLE', 'DIST_ANOM', 'FRESH_ANOM', 'INACTIVE_MONITOR', 'INCIDENT_OWNER_UPDATE', 'INCIDENT_SEVERITY_UPDATE', 'INCIDENT_SLACK_THREAD', 'INCIDENT_SPLIT', 'INCIDENT_STATUS_UPDATE', 'JSON_SCHEMA_CHANGE', 'METRIC_ANOM', 'QUERY_RUNTIME_ANOM', 'SCHEMA_CHANGE', 'SIZE_ANOM', 'SIZE_DIFF', 'UNCHANGED_SIZE_ANOM')


class EventMutingRuleModelRuleType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `EXACT_MATCH_RULE`: Exact match Rule
    * `REGEX_RULE`: Regex Rule
    '''
    __schema__ = schema
    __choices__ = ('EXACT_MATCH_RULE', 'REGEX_RULE')


class EventRcaStatusModelReason(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `BASELINE_SAMPLE_INSUFFICIENT`: Baseline sample too small to run
      analysis.
    * `BREACHES_SAMPLE_INSUFFICIENT`: Breaches sample too small to run
      analysis.
    * `DATA_SAMPLING_DISABLED`: Data Sampling disabled for warehouse
    * `DOES_NOT_MEET_CRITERIA`: Does not meet criteria
    * `EVENT_MISSING_INCIDENT`: Event missing incident
    * `EVENT_MISSING_TABLE`: Event missing associated table
    * `MISSING_EVENT_WAREHOUSE`: Missing event warehouse connection.
    * `NO_EXPLANATORY_FIELDS`: Unable to identify explanatory fields
    * `NO_HISTORY_ACCESS_METHOD_SELECTED`: No relevant history access
      method could be selected
    * `NO_TIME_FIELDS`: Unable to identify time fields
    * `PERMISSION_FAILURE`: Failure due to insufficient permissions
    * `QUERY_TIMEOUT`: RCA query timeout
    * `RCA_QUOTA_EXCEEDED`: RCA quota exceeded. Not running.
    * `RESOURCES_EXCEEDED`: Resources exceeded when running query.
    * `S3_OBJECT_WRITER_NOT_SUPPORTED`: S3 object writer not supported
    * `SQL_COMPILATION_ERROR`: Error in SQL RCA query.
    * `TABLE_TYPE_NOT_SUPPORTED`: Table type not supported
    * `UNKNOWN`: RCA failure needs further investigation to determine
      failure cause.
    * `WAREHOUSE_DISABLED`: Warehouse disabled for RCA
    '''
    __schema__ = schema
    __choices__ = ('BASELINE_SAMPLE_INSUFFICIENT', 'BREACHES_SAMPLE_INSUFFICIENT', 'DATA_SAMPLING_DISABLED', 'DOES_NOT_MEET_CRITERIA', 'EVENT_MISSING_INCIDENT', 'EVENT_MISSING_TABLE', 'MISSING_EVENT_WAREHOUSE', 'NO_EXPLANATORY_FIELDS', 'NO_HISTORY_ACCESS_METHOD_SELECTED', 'NO_TIME_FIELDS', 'PERMISSION_FAILURE', 'QUERY_TIMEOUT', 'RCA_QUOTA_EXCEEDED', 'RESOURCES_EXCEEDED', 'S3_OBJECT_WRITER_NOT_SUPPORTED', 'SQL_COMPILATION_ERROR', 'TABLE_TYPE_NOT_SUPPORTED', 'UNKNOWN', 'WAREHOUSE_DISABLED')


class ExecDashboardMetrics(sgqlc.types.Enum):
    '''Available executive dashboard metrics.      For series, we
    use the plural. Ex: INCIDENTS_COUNTS, vs. singular for single. Ex:
    TABLES_COUNT

    Enumeration Choices:

    * `DAILY_TABLES_COUNTS`None
    * `FIELD_MONITOR_UPTIME_PCT`None
    * `FRESHNESS_UPTIME_PCT`None
    * `INCIDENTS_CLASSIFIED_COUNTS`None
    * `INCIDENTS_COUNTS`None
    * `INCIDENTS_COUNTS_BY_TABLE`None
    * `INCIDENTS_MEAN_TIME_TO_FIRST_RESPONSE`None
    * `INCIDENTS_MEAN_TIME_TO_RESOLUTION`None
    * `INCIDENTS_MEDIAN_TIME_TO_FIRST_RESPONSE`None
    * `INCIDENTS_MEDIAN_TIME_TO_RESOLUTION`None
    * `INCIDENTS_STATUS_UPDATE_RATE`None
    * `MONITORS_COUNTS`None
    * `MONITORS_CREATED_COUNT`None
    * `MONITORS_INCIDENTS_COUNTS`None
    * `OOTB_FRESHNESS_UPTIME_PCT`None
    * `OOTB_VOLUME_UPTIME_PCT`None
    * `SQL_RULES_UPTIME_PCT`None
    * `STACK_SUMMARY`None
    * `USER_APP_VIEWS_COUNTS`None
    * `USER_PAGE_VIEWS_COUNTS`None
    * `USER_VISITS_COUNTS`None
    * `VOLUME_UPTIME_PCT`None
    '''
    __schema__ = schema
    __choices__ = ('DAILY_TABLES_COUNTS', 'FIELD_MONITOR_UPTIME_PCT', 'FRESHNESS_UPTIME_PCT', 'INCIDENTS_CLASSIFIED_COUNTS', 'INCIDENTS_COUNTS', 'INCIDENTS_COUNTS_BY_TABLE', 'INCIDENTS_MEAN_TIME_TO_FIRST_RESPONSE', 'INCIDENTS_MEAN_TIME_TO_RESOLUTION', 'INCIDENTS_MEDIAN_TIME_TO_FIRST_RESPONSE', 'INCIDENTS_MEDIAN_TIME_TO_RESOLUTION', 'INCIDENTS_STATUS_UPDATE_RATE', 'MONITORS_COUNTS', 'MONITORS_CREATED_COUNT', 'MONITORS_INCIDENTS_COUNTS', 'OOTB_FRESHNESS_UPTIME_PCT', 'OOTB_VOLUME_UPTIME_PCT', 'SQL_RULES_UPTIME_PCT', 'STACK_SUMMARY', 'USER_APP_VIEWS_COUNTS', 'USER_PAGE_VIEWS_COUNTS', 'USER_VISITS_COUNTS', 'VOLUME_UPTIME_PCT')


class ExecDashboardTables(sgqlc.types.Enum):
    '''Available executive dashboard tables.

    Enumeration Choices:

    * `DOMAINS_TABLE`None
    * `MONITORS_TABLE`None
    * `OBJECT_TYPES_TABLE`None
    * `USERS_TABLE`None
    '''
    __schema__ = schema
    __choices__ = ('DOMAINS_TABLE', 'MONITORS_TABLE', 'OBJECT_TYPES_TABLE', 'USERS_TABLE')


class FacetType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `TAGS`None
    * `TAG_NAMES`None
    * `TAG_VALUES`None
    '''
    __schema__ = schema
    __choices__ = ('TAGS', 'TAG_NAMES', 'TAG_VALUES')


class FieldMetricType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `APPROX_DISTINCTNESS`None
    * `MAX_LENGTH`None
    * `MEAN_LENGTH`None
    * `MIN_LENGTH`None
    * `NEGATIVE_RATE`None
    * `NULL_RATE`None
    * `NUMERIC_MAX`None
    * `NUMERIC_MEAN`None
    * `NUMERIC_MIN`None
    * `ZERO_RATE`None
    '''
    __schema__ = schema
    __choices__ = ('APPROX_DISTINCTNESS', 'MAX_LENGTH', 'MEAN_LENGTH', 'MIN_LENGTH', 'NEGATIVE_RATE', 'NULL_RATE', 'NUMERIC_MAX', 'NUMERIC_MEAN', 'NUMERIC_MIN', 'ZERO_RATE')


class FieldQueryType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `APPROX_DISTINCTNESS`None
    * `DISTINCT_VALUES`None
    * `MAX_LENGTH`None
    * `MEAN_LENGTH`None
    * `MIN_LENGTH`None
    * `MISSING_VALUES`None
    * `NEGATIVE_RATE`None
    * `NOT_IN_VALUES`None
    * `NULL_RATE`None
    * `NUMERIC_MAX`None
    * `NUMERIC_MEAN`None
    * `NUMERIC_MIN`None
    * `ZERO_RATE`None
    '''
    __schema__ = schema
    __choices__ = ('APPROX_DISTINCTNESS', 'DISTINCT_VALUES', 'MAX_LENGTH', 'MEAN_LENGTH', 'MIN_LENGTH', 'MISSING_VALUES', 'NEGATIVE_RATE', 'NOT_IN_VALUES', 'NULL_RATE', 'NUMERIC_MAX', 'NUMERIC_MEAN', 'NUMERIC_MIN', 'ZERO_RATE')


class FieldType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `BOOLEAN`None
    * `DATE`None
    * `NUMERIC`None
    * `TEXT`None
    * `TIME`None
    * `UNKNOWN`None
    '''
    __schema__ = schema
    __choices__ = ('BOOLEAN', 'DATE', 'NUMERIC', 'TEXT', 'TIME', 'UNKNOWN')


class FivetranConnectorSetupStates(sgqlc.types.Enum):
    '''Defines the current setup state of a Fivetran Connector

    Enumeration Choices:

    * `BROKEN`None
    * `CONNECTED`None
    * `INCOMPLETE`None
    '''
    __schema__ = schema
    __choices__ = ('BROKEN', 'CONNECTED', 'INCOMPLETE')


class FivetranConnectorStatuses(sgqlc.types.Enum):
    '''Defines the user facing statues of Fivetran connectors.
    See: https://fivetran.com/docs/getting-started/fivetran-
    dashboard/connectors#connectorstatus

    Enumeration Choices:

    * `Active`None
    * `Broken`None
    * `Delayed`None
    * `Incomplete`None
    * `Paused`None
    '''
    __schema__ = schema
    __choices__ = ('Active', 'Broken', 'Delayed', 'Incomplete', 'Paused')


class FivetranConnectorSyncStates(sgqlc.types.Enum):
    '''Defines the current sync state of a Fivetran Connector

    Enumeration Choices:

    * `PAUSED`None
    * `RESCHEDULED`None
    * `SCHEDULED`None
    * `SYNCING`None
    '''
    __schema__ = schema
    __choices__ = ('PAUSED', 'RESCHEDULED', 'SCHEDULED', 'SYNCING')


class FivetranConnectorUpdateStates(sgqlc.types.Enum):
    '''Defines the current data update state of a Fivetran connector

    Enumeration Choices:

    * `DELAYED`None
    * `ON_SCHEDULE`None
    '''
    __schema__ = schema
    __choices__ = ('DELAYED', 'ON_SCHEDULE')


Float = sgqlc.types.Float

class GenericScalar(sgqlc.types.Scalar):
    '''The `GenericScalar` scalar type represents a generic GraphQL
    scalar value that could be: String, Boolean, Int, Float, List or
    Object.
    '''
    __schema__ = schema


ID = sgqlc.types.ID

class IdempotentStatus(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `COMPLETED`None
    * `ERROR`None
    * `IN_PROGRESS`None
    '''
    __schema__ = schema
    __choices__ = ('COMPLETED', 'ERROR', 'IN_PROGRESS')


class ImportanceScoreOperator(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EQ`None
    * `GT`None
    * `GTE`None
    * `LT`None
    * `LTE`None
    * `RANGE`None
    '''
    __schema__ = schema
    __choices__ = ('EQ', 'GT', 'GTE', 'LT', 'LTE', 'RANGE')


class IncidentCategory(sgqlc.types.Enum):
    '''Categories to classify incidents

    Enumeration Choices:

    * `dbt_errors`None
    * `dimension`None
    * `field_health`None
    * `field_quality_rule`None
    * `freshness`None
    * `schema`None
    * `sql_rule`None
    * `volume`None
    '''
    __schema__ = schema
    __choices__ = ('dbt_errors', 'dimension', 'field_health', 'field_quality_rule', 'freshness', 'schema', 'sql_rule', 'volume')


class IncidentGroupBy(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `STATUS`None
    * `TYPE`None
    '''
    __schema__ = schema
    __choices__ = ('STATUS', 'TYPE')


class IncidentModelFeedback(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ANOMALY_NORMALIZED`: Anomaly Normalized
    * `EXPECTED`: Expected
    * `FALSE_POSITIVE`: False Positive
    * `FALSE_POSITIVE_6`: False Positive
    * `FIXED`: Fixed
    * `HELPFUL`: Helpful
    * `INVESTIGATING`: Investigating
    * `NOT_HELPFUL`: Not Helpful
    * `NO_ACTION_NEEDED`: No Action Needed
    '''
    __schema__ = schema
    __choices__ = ('ANOMALY_NORMALIZED', 'EXPECTED', 'FALSE_POSITIVE', 'FALSE_POSITIVE_6', 'FIXED', 'HELPFUL', 'INVESTIGATING', 'NOT_HELPFUL', 'NO_ACTION_NEEDED')


class IncidentModelIncidentType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ANOMALIES`: Anomalies
    * `CUSTOM_RULE_ANOMALIES`: Custom Rule Anomalies
    * `DBT_ERRORS`: dbt Errors
    * `DELETED_TABLES`: Deleted Tables
    * `JSON_SCHEMA_CHANGES`: JSON Schema Changes
    * `METRIC_ANOMALIES`: Metric Anomalies
    * `PERFORMANCE_ANOMALIES`: Performance Anomalies
    * `PSEUDO_INTEGRATION_TEST`: Pseudo Anomalies
    * `SCHEMA_CHANGES`: Schema Changes
    '''
    __schema__ = schema
    __choices__ = ('ANOMALIES', 'CUSTOM_RULE_ANOMALIES', 'DBT_ERRORS', 'DELETED_TABLES', 'JSON_SCHEMA_CHANGES', 'METRIC_ANOMALIES', 'PERFORMANCE_ANOMALIES', 'PSEUDO_INTEGRATION_TEST', 'SCHEMA_CHANGES')


class IncidentReactionReason(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DetectorTooSensitive`None
    * `DontCareAboutThisTable`None
    * `SeenThisTooManyTimes`None
    '''
    __schema__ = schema
    __choices__ = ('DetectorTooSensitive', 'DontCareAboutThisTable', 'SeenThisTooManyTimes')


class IncidentReactionType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `Helpful`None
    * `NotHelpful`None
    '''
    __schema__ = schema
    __choices__ = ('Helpful', 'NotHelpful')


class IncidentSubType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `abnormal_size_change`None
    * `data_added`None
    * `data_removed`None
    * `dbt_model_error`None
    * `dbt_test_failure`None
    * `dimension_anomaly`None
    * `field_metrics_anomaly`None
    * `field_quality_rule_breach`None
    * `fields_added`None
    * `fields_changed`None
    * `fields_removed`None
    * `freshness_anomaly`None
    * `freshness_sli_rule_breach`None
    * `json_fields_added`None
    * `json_fields_removed`None
    * `sql_rule_breach`None
    * `unchanged_size`None
    * `volume_anomaly`None
    * `volume_sli_rule_breach`None
    '''
    __schema__ = schema
    __choices__ = ('abnormal_size_change', 'data_added', 'data_removed', 'dbt_model_error', 'dbt_test_failure', 'dimension_anomaly', 'field_metrics_anomaly', 'field_quality_rule_breach', 'fields_added', 'fields_changed', 'fields_removed', 'freshness_anomaly', 'freshness_sli_rule_breach', 'json_fields_added', 'json_fields_removed', 'sql_rule_breach', 'unchanged_size', 'volume_anomaly', 'volume_sli_rule_breach')


Int = sgqlc.types.Int

class IntegrationKeyScope(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CircuitBreaker`None
    * `DatabricksMetadata`None
    * `DbtCloudWebhook`None
    * `S3PresignedUrl`None
    * `Spark`None
    '''
    __schema__ = schema
    __choices__ = ('CircuitBreaker', 'DatabricksMetadata', 'DbtCloudWebhook', 'S3PresignedUrl', 'Spark')


class InvitationType(sgqlc.types.Enum):
    '''Used to select the template to use for new user invites.

    Enumeration Choices:

    * `Discovery`None
    * `Observability`None
    '''
    __schema__ = schema
    __choices__ = ('Discovery', 'Observability')


class JSONString(sgqlc.types.Scalar):
    '''Allows use of a JSON String for input / output from the GraphQL
    schema.  Use of this type is *not recommended* as you lose the
    benefits of having a defined, static schema (one of the key
    benefits of GraphQL).
    '''
    __schema__ = schema


class JobExecutionStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `FAILED`None
    * `IN_PROGRESS`None
    * `SUCCESS`None
    * `TIMEOUT`None
    '''
    __schema__ = schema
    __choices__ = ('FAILED', 'IN_PROGRESS', 'SUCCESS', 'TIMEOUT')


class LookbackRange(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `ONE_DAY`None
    * `ONE_HOUR`None
    * `SEVEN_DAY`None
    * `TWELVE_HOUR`None
    '''
    __schema__ = schema
    __choices__ = ('ONE_DAY', 'ONE_HOUR', 'SEVEN_DAY', 'TWELVE_HOUR')


class MetricMonitorSelectExpressionModelDataType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `BOOLEAN`: BOOLEAN
    * `DATETIME`: DATETIME
    * `NUMERIC`: NUMERIC
    * `STRING`: STRING
    '''
    __schema__ = schema
    __choices__ = ('BOOLEAN', 'DATETIME', 'NUMERIC', 'STRING')


class MetricMonitoringModelType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CATEGORIES`: Category distributions
    * `HOURLY_STATS`: Statistical metrics over an hour interval
    * `JSON_SCHEMA`: Samples of JSON schemas to track schema changes
    * `STATS`: Statistical metrics (e.g. avg, null rate, etc.)
    '''
    __schema__ = schema
    __choices__ = ('CATEGORIES', 'HOURLY_STATS', 'JSON_SCHEMA', 'STATS')


class MonitorAggTimeInterval(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DAY`None
    * `HOUR`None
    '''
    __schema__ = schema
    __choices__ = ('DAY', 'HOUR')


class MonitorConfigurationStatusType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `MISCONFIGURED`None
    * `NO_STATUS`None
    * `SUCCESS`None
    '''
    __schema__ = schema
    __choices__ = ('MISCONFIGURED', 'NO_STATUS', 'SUCCESS')


class MonitorLabelsMatchType(sgqlc.types.Enum):
    '''Used to select the logical operator for matching labels

    Enumeration Choices:

    * `AND`None
    * `OR`None
    '''
    __schema__ = schema
    __choices__ = ('AND', 'OR')


class MonitorRunStatusType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ERROR`None
    * `IN_PROGRESS`None
    * `NO_STATUS`None
    * `PAUSED`None
    * `SNOOZED`None
    * `SUCCESS`None
    '''
    __schema__ = schema
    __choices__ = ('ERROR', 'IN_PROGRESS', 'NO_STATUS', 'PAUSED', 'SNOOZED', 'SUCCESS')


class MonitorStatusType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ERROR`None
    * `IN_PROGRESS`None
    * `IN_TRAINING`None
    * `MISCONFIGURED`None
    * `NO_STATUS`None
    * `PAUSED`None
    * `SNOOZED`None
    * `SUCCESS`None
    '''
    __schema__ = schema
    __choices__ = ('ERROR', 'IN_PROGRESS', 'IN_TRAINING', 'MISCONFIGURED', 'NO_STATUS', 'PAUSED', 'SNOOZED', 'SUCCESS')


class MonitorTrainingStatusType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `IN_TRAINING`None
    * `NO_STATUS`None
    * `SUCCESS`None
    '''
    __schema__ = schema
    __choices__ = ('IN_TRAINING', 'NO_STATUS', 'SUCCESS')


class MutedEventType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CUSTOM_RULE_ANOM`None
    * `DELETE_TABLE`None
    * `DIST_ANOM`None
    * `FRESH_ANOM`None
    * `JSON_SCHEMA_CHANGE`None
    * `METRIC_ANOM`None
    * `QUERY_RUNTIME_ANOM`None
    * `SCHEMA_CHANGE`None
    * `SIZE_ANOM`None
    * `SIZE_DIFF`None
    * `UNCHANGED_SIZE_ANOM`None
    '''
    __schema__ = schema
    __choices__ = ('CUSTOM_RULE_ANOM', 'DELETE_TABLE', 'DIST_ANOM', 'FRESH_ANOM', 'JSON_SCHEMA_CHANGE', 'METRIC_ANOM', 'QUERY_RUNTIME_ANOM', 'SCHEMA_CHANGE', 'SIZE_ANOM', 'SIZE_DIFF', 'UNCHANGED_SIZE_ANOM')


class ObjectPropertyModelPropertySourceType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `COLLECTION`: Collection
    * `DASHBOARD`: Dashboard
    * `DBT`: DBT
    * `LINEAGE_API`: Lineage API
    * `TAGS_COLLECTION`: Tags Collection
    '''
    __schema__ = schema
    __choices__ = ('COLLECTION', 'DASHBOARD', 'DBT', 'LINEAGE_API', 'TAGS_COLLECTION')


class PeriodGrouping(sgqlc.types.Enum):
    '''Time size of the periods.

    Enumeration Choices:

    * `DAY`None
    * `MONTH`None
    * `WEEK`None
    '''
    __schema__ = schema
    __choices__ = ('DAY', 'MONTH', 'WEEK')


class Permission(sgqlc.types.Enum):
    '''Currently-defined permissions.

    Enumeration Choices:

    * `CatalogAccess`None
    * `CatalogEdit`None
    * `DashboardAccess`None
    * `DashboardEdit`None
    * `GraphqlMutate`None
    * `GraphqlQuery`None
    * `IncidentsAccess`None
    * `IncidentsEdit`None
    * `IncidentsUpdateStatus`None
    * `MonitorsAccess`None
    * `MonitorsAggregates`None
    * `MonitorsEdit`None
    * `PerformanceAccess`None
    * `PipelinesAccess`None
    * `PipelinesEdit`None
    * `ProductsAccess`None
    * `ProductsDiscoveryAccess`None
    * `ProductsObservabilityAccess`None
    * `ProductsSamplingAccess`None
    * `SettingsAccess`None
    * `SettingsApiAccess`None
    * `SettingsApiEdit`None
    * `SettingsApiTokensManage`None
    * `SettingsCollectionPreferencesEdit`None
    * `SettingsCollectionPreferencesList`None
    * `SettingsDomainsAccess`None
    * `SettingsDomainsEdit`None
    * `SettingsDomainsList`None
    * `SettingsDomainsViewDetail`None
    * `SettingsEdit`None
    * `SettingsIntegrationsAccess`None
    * `SettingsIntegrationsEdit`None
    * `SettingsMutedDataAccess`None
    * `SettingsMutedDataEdit`None
    * `SettingsNotificationsAccess`None
    * `SettingsPiiFiltersEdit`None
    * `SettingsPiiFiltersList`None
    * `SettingsPiiFiltersViewMetrics`None
    * `SettingsUsersAccess`None
    * `SettingsUsersEdit`None
    * `SettingsUsersEditSso`None
    * `SettingsUsersManageDomainsManagers`None
    * `SettingsUsersManageOwners`None
    '''
    __schema__ = schema
    __choices__ = ('CatalogAccess', 'CatalogEdit', 'DashboardAccess', 'DashboardEdit', 'GraphqlMutate', 'GraphqlQuery', 'IncidentsAccess', 'IncidentsEdit', 'IncidentsUpdateStatus', 'MonitorsAccess', 'MonitorsAggregates', 'MonitorsEdit', 'PerformanceAccess', 'PipelinesAccess', 'PipelinesEdit', 'ProductsAccess', 'ProductsDiscoveryAccess', 'ProductsObservabilityAccess', 'ProductsSamplingAccess', 'SettingsAccess', 'SettingsApiAccess', 'SettingsApiEdit', 'SettingsApiTokensManage', 'SettingsCollectionPreferencesEdit', 'SettingsCollectionPreferencesList', 'SettingsDomainsAccess', 'SettingsDomainsEdit', 'SettingsDomainsList', 'SettingsDomainsViewDetail', 'SettingsEdit', 'SettingsIntegrationsAccess', 'SettingsIntegrationsEdit', 'SettingsMutedDataAccess', 'SettingsMutedDataEdit', 'SettingsNotificationsAccess', 'SettingsPiiFiltersEdit', 'SettingsPiiFiltersList', 'SettingsPiiFiltersViewMetrics', 'SettingsUsersAccess', 'SettingsUsersEdit', 'SettingsUsersEditSso', 'SettingsUsersManageDomainsManagers', 'SettingsUsersManageOwners')


class PermissionEffect(sgqlc.types.Enum):
    '''Possible effects of a policy.

    Enumeration Choices:

    * `Allow`None
    * `Deny`None
    '''
    __schema__ = schema
    __choices__ = ('Allow', 'Deny')


class PiiFilteringFailModeType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CLOSE`None
    * `OPEN`None
    '''
    __schema__ = schema
    __choices__ = ('CLOSE', 'OPEN')


class PowerBIAuthModeEnum(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `PRIMARY_USER`None
    * `SERVICE_PRINCIPAL`None
    '''
    __schema__ = schema
    __choices__ = ('PRIMARY_USER', 'SERVICE_PRINCIPAL')


class PowerBIAuthModeEnumV2(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `PRIMARY_USER`None
    * `SERVICE_PRINCIPAL`None
    '''
    __schema__ = schema
    __choices__ = ('PRIMARY_USER', 'SERVICE_PRINCIPAL')


class QueryCategory(sgqlc.types.Enum):
    '''Possible query categories

    Enumeration Choices:

    * `alter`None
    * `clone`None
    * `copy`None
    * `create_table`None
    * `create_table_as_select`None
    * `create_view`None
    * `delete_from`None
    * `delete_using`None
    * `drop_table`None
    * `explain`None
    * `insert_into`None
    * `insert_overwrite`None
    * `load`None
    * `merge`None
    * `put`None
    * `query`None
    * `rename`None
    * `select_into`None
    * `swap`None
    * `truncate`None
    * `unload`None
    * `update`None
    '''
    __schema__ = schema
    __choices__ = ('alter', 'clone', 'copy', 'create_table', 'create_table_as_select', 'create_view', 'delete_from', 'delete_using', 'drop_table', 'explain', 'insert_into', 'insert_overwrite', 'load', 'merge', 'put', 'query', 'rename', 'select_into', 'swap', 'truncate', 'unload', 'update')


class QueryRcaType(sgqlc.types.Enum):
    '''Types of query RCAs

    Enumeration Choices:

    * `EMPTY`None
    * `FAILED`None
    * `NEW`None
    * `UPDATE`None
    * `UPSTREAM`None
    '''
    __schema__ = schema
    __choices__ = ('EMPTY', 'FAILED', 'NEW', 'UPDATE', 'UPSTREAM')


class QueryResultType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `SINGLE_NUMERIC`None
    '''
    __schema__ = schema
    __choices__ = ('SINGLE_NUMERIC',)


class QueryType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `read`: Filter for reads on the table
    * `write`: Filter for writes to the table
    '''
    __schema__ = schema
    __choices__ = ('read', 'write')


class RcaJobsModelJobType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `METRIC_CORRELATION`: Metric (Field Health) value correlation
    * `SIZE_DIFF_CORRELATION`: Size Diff value correlation
    * `SIZE_DIFF_SAMPLING`: Size Diff sampling
    * `SQL_RULE_CUSTOM_SAMPLING`: SQL Rule custom sampling
    * `SQL_RULE_PROFILING`: SQL Rule sample data profiling
    '''
    __schema__ = schema
    __choices__ = ('METRIC_CORRELATION', 'SIZE_DIFF_CORRELATION', 'SIZE_DIFF_SAMPLING', 'SQL_RULE_CUSTOM_SAMPLING', 'SQL_RULE_PROFILING')


class RcaJobsModelStatus(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CANCELED`: canceled
    * `EMPTY`: No root cause found
    * `EXPIRED`: expired
    * `FAILED`: RCA process has failed
    * `FOUND`: Root cause has been found
    * `PARTIAL_DATA`: partial_data
    '''
    __schema__ = schema
    __choices__ = ('CANCELED', 'EMPTY', 'EXPIRED', 'FAILED', 'FOUND', 'PARTIAL_DATA')


class RcaStatus(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CANCELED`None
    * `EMPTY`None
    * `EXPIRED`None
    * `FAILED`None
    * `FOUND`None
    * `PARTIAL_DATA`None
    '''
    __schema__ = schema
    __choices__ = ('CANCELED', 'EMPTY', 'EXPIRED', 'FAILED', 'FOUND', 'PARTIAL_DATA')


class RelationshipType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `EXPERT`None
    * `OWNER`None
    '''
    __schema__ = schema
    __choices__ = ('EXPERT', 'OWNER')


class ScheduleType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `DYNAMIC`None
    * `FIXED`None
    * `LOOSE`None
    * `MANUAL`None
    '''
    __schema__ = schema
    __choices__ = ('DYNAMIC', 'FIXED', 'LOOSE', 'MANUAL')


class SensitivityLevels(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `HIGH`None
    * `LOW`None
    * `MEDIUM`None
    '''
    __schema__ = schema
    __choices__ = ('HIGH', 'LOW', 'MEDIUM')


class SlackAppType(sgqlc.types.Enum):
    '''Defines OBSERVE/DISCO types to support separate Slack apps

    Enumeration Choices:

    * `DISCOVER`None
    * `OBSERVE`None
    '''
    __schema__ = schema
    __choices__ = ('DISCOVER', 'OBSERVE')


class SlackCredentialsV2ModelSlackAppType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `DISCOVER`: discover
    * `OBSERVE`: observe
    '''
    __schema__ = schema
    __choices__ = ('DISCOVER', 'OBSERVE')


class SlackEngagementEventType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CHANNEL_COMMENT`None
    * `REACTION_ADDED`None
    * `REACTION_REMOVED`None
    * `THREAD_REPLY`None
    '''
    __schema__ = schema
    __choices__ = ('CHANNEL_COMMENT', 'REACTION_ADDED', 'REACTION_REMOVED', 'THREAD_REPLY')


class SqlJobCheckpointStatus(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `EXECUTING_COMPLETE`None
    * `EXECUTING_START`None
    * `HAS_ERROR`None
    * `PROCESSING_COMPLETE`None
    * `PROCESSING_START`None
    * `REGISTERED`None
    '''
    __schema__ = schema
    __choices__ = ('EXECUTING_COMPLETE', 'EXECUTING_START', 'HAS_ERROR', 'PROCESSING_COMPLETE', 'PROCESSING_START', 'REGISTERED')


class State(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `APPLIED`None
    * `FAILED`None
    * `PENDING`None
    * `SKIPPED`None
    '''
    __schema__ = schema
    __choices__ = ('APPLIED', 'FAILED', 'PENDING', 'SKIPPED')


String = sgqlc.types.String

class TableAnomalyModelReason(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CUSTOM_RULE`: Custom Rule Anomaly
    * `DIST`: Distribution Anomaly
    * `FRESHNESS`: Freshness Anomaly
    * `METRIC`: Metric Anomaly
    * `QUERY_RUNTIME`: Query Time Anomaly
    * `SIZE`: Size Anomaly
    * `SIZE_DIFF`: Row count anomaly
    * `UNCHANGED_SIZE`: Unchanged Size Anomaly
    '''
    __schema__ = schema
    __choices__ = ('CUSTOM_RULE', 'DIST', 'FRESHNESS', 'METRIC', 'QUERY_RUNTIME', 'SIZE', 'SIZE_DIFF', 'UNCHANGED_SIZE')


class TableFieldToBiModelBiType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `TABLEAU_WORKBOOK`: Tableau Workbook
    '''
    __schema__ = schema
    __choices__ = ('TABLEAU_WORKBOOK',)


class ThresholdModifierType(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `METRIC`None
    * `PERCENTAGE`None
    '''
    __schema__ = schema
    __choices__ = ('METRIC', 'PERCENTAGE')


class ThresholdStatus(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ACTIVE`None
    * `INACTIVE`None
    * `TRAINING`None
    '''
    __schema__ = schema
    __choices__ = ('ACTIVE', 'INACTIVE', 'TRAINING')


class ThresholdType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `SIZE_DIFF`None
    * `UNCHANGED_SIZE`None
    '''
    __schema__ = schema
    __choices__ = ('SIZE_DIFF', 'UNCHANGED_SIZE')


class UUID(sgqlc.types.Scalar):
    '''Leverages the internal Python implmeentation of UUID (uuid.UUID)
    to provide native UUID objects in fields, resolvers and input.
    '''
    __schema__ = schema


class UnifiedUserAssignmentModelRelationshipType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `EXPERT`: Expert
    * `OWNER`: Owner
    '''
    __schema__ = schema
    __choices__ = ('EXPERT', 'OWNER')


class Upload(sgqlc.types.Scalar):
    '''Create scalar that ignores normal serialization/deserialization,
    since that will be handled by the multipart request spec
    '''
    __schema__ = schema


class UserDefinedMonitorModelMonitorType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CATEGORIES`: Category distributions
    * `CUSTOM_SQL`: Custom SQL Metric Rule
    * `FIELD_QUALITY`: Field Quality Rule
    * `FRESHNESS`: Freshness Rule
    * `HOURLY_STATS`: Statistical metrics over an hour interval
    * `JSON_SCHEMA`: Samples of JSON schemas to track schema changes
    * `STATS`: Statistical metrics (e.g. avg, null rate, etc.)
    * `TABLE_METRIC`: Table Metric Rule
    * `VOLUME`: Volume Rule
    '''
    __schema__ = schema
    __choices__ = ('CATEGORIES', 'CUSTOM_SQL', 'FIELD_QUALITY', 'FRESHNESS', 'HOURLY_STATS', 'JSON_SCHEMA', 'STATS', 'TABLE_METRIC', 'VOLUME')


class UserDefinedMonitorModelScheduleType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `DYNAMIC`: Dynamic
    * `FIXED`: Fixed
    * `LOOSE`: Loose
    * `MANUAL`: Manual
    '''
    __schema__ = schema
    __choices__ = ('DYNAMIC', 'FIXED', 'LOOSE', 'MANUAL')


class UserDefinedMonitorModelUdmType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `MONITOR`: MONITOR
    * `RULE`: RULE
    '''
    __schema__ = schema
    __choices__ = ('MONITOR', 'RULE')


class UserDefinedMonitorSearchFields(sgqlc.types.Enum):
    '''Defines which fields can be used for full text search in the user
    defined monitors view

    Enumeration Choices:

    * `CREATOR_ID`None
    * `ENTITIES`None
    * `MONITOR_FIELDS`None
    * `NAMESPACE`None
    * `RULE_DESCRIPTION`None
    * `RULE_NAME`None
    * `UPDATER_ID`None
    '''
    __schema__ = schema
    __choices__ = ('CREATOR_ID', 'ENTITIES', 'MONITOR_FIELDS', 'NAMESPACE', 'RULE_DESCRIPTION', 'RULE_NAME', 'UPDATER_ID')


class UserDefinedMonitors(sgqlc.types.Enum):
    '''Enumeration Choices:

    * `CATEGORIES`None
    * `CUSTOM_SQL`None
    * `FIELD_QUALITY`None
    * `FRESHNESS`None
    * `JSON_SCHEMA`None
    * `STATS`None
    * `TABLE_METRIC`None
    * `VOLUME`None
    '''
    __schema__ = schema
    __choices__ = ('CATEGORIES', 'CUSTOM_SQL', 'FIELD_QUALITY', 'FRESHNESS', 'JSON_SCHEMA', 'STATS', 'TABLE_METRIC', 'VOLUME')


class UserInviteModelInviteType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `DISCOVERY`: discovery
    * `OBSERVABILITY`: observability
    '''
    __schema__ = schema
    __choices__ = ('DISCOVERY', 'OBSERVABILITY')


class UserInviteModelState(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `ACCEPTED`: Accepted
    * `INVALIDATED`: Invalidated
    * `SENT`: Sent
    '''
    __schema__ = schema
    __choices__ = ('ACCEPTED', 'INVALIDATED', 'SENT')


class UserModelState(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `CHECK_BACK`: Check Back Soon
    * `CONNECT_DW`: Connect Data Warehouse
    * `DASHBOARD`: View Dashboard
    * `INSTALL_DC`: Install Data Collector
    * `INTEGRATIONS`: Other integrations
    * `NOT_AVAILABLE`: Not available
    * `SET_ACCOUNT_NAME`: Set Account Name
    * `SIGNED_UP`: Signed-Up
    '''
    __schema__ = schema
    __choices__ = ('CHECK_BACK', 'CONNECT_DW', 'DASHBOARD', 'INSTALL_DC', 'INTEGRATIONS', 'NOT_AVAILABLE', 'SET_ACCOUNT_NAME', 'SIGNED_UP')


class WarehouseModelConnectionType(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `AIRFLOW_LOGS_S3`: S3 Airflow logs
    * `BIGQUERY`: BigQuery
    * `DATA_LAKE`: Data Lake
    * `REDSHIFT`: Amazon Redshift
    * `S3_METADATA_EVENTS`: S3 Metadata Events
    * `SNOWFLAKE`: Snowflake
    * `TRANSACTIONAL_DB`: Transactional DB
    '''
    __schema__ = schema
    __choices__ = ('AIRFLOW_LOGS_S3', 'BIGQUERY', 'DATA_LAKE', 'REDSHIFT', 'S3_METADATA_EVENTS', 'SNOWFLAKE', 'TRANSACTIONAL_DB')


class WarehouseTableModelStatus(sgqlc.types.Enum):
    '''An enumeration.

    Enumeration Choices:

    * `G`: Green
    * `R`: Red
    * `Y`: Yellow
    '''
    __schema__ = schema
    __choices__ = ('G', 'R', 'Y')



########################################################################
# Input Objects
########################################################################
class AirflowEnvInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('env_name', 'env_id', 'version', 'base_url')
    env_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='envName')
    '''Environment name'''

    env_id = sgqlc.types.Field(String, graphql_name='envId')

    version = sgqlc.types.Field(String, graphql_name='version')

    base_url = sgqlc.types.Field(String, graphql_name='baseUrl')



class BiWarehouseSourcesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('warehouse_resource_id', 'warehouse_resource_type', 'bi_warehouse_id')
    warehouse_resource_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouseResourceId')
    '''Warehouse resource ID. This is a Monte Carlo ID'''

    warehouse_resource_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouseResourceType')
    '''Warehouse type. Examples: snowflake, redshift, etc.'''

    bi_warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='biWarehouseId')
    '''The warehouse ID in the BI instance of the customer. This is an ID
    in the customer ID space and is not a Monte Carlo ID.
    '''



class BqConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('service_json',)
    service_json = sgqlc.types.Field(String, graphql_name='serviceJson')
    '''Service account key file as a base64 string'''



class CollectionBlockInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('resource_id', 'project', 'dataset')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''The resource UUID this collection block applies to.'''

    project = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='project')
    '''Top-level object hierarchy e.g. database, catalog, etc.'''

    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    '''Intermediate object hierarchy e.g. schema, database, etc.'''



class ConnectionTestOptions(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('dc_id', 'skip_validation', 'skip_permission_tests', 'test_options')
    dc_id = sgqlc.types.Field(UUID, graphql_name='dcId')
    '''DC UUID. To disambiguate accounts with multiple collectors.'''

    skip_validation = sgqlc.types.Field(Boolean, graphql_name='skipValidation')
    '''Skip all connection tests.'''

    skip_permission_tests = sgqlc.types.Field(Boolean, graphql_name='skipPermissionTests')
    '''Skips all permission tests for the service account/role for
    anysupported integrations. Only validates network connection
    between the DC and resource can be established.
    '''

    test_options = sgqlc.types.Field('ValidatorTestOptions', graphql_name='testOptions')
    '''Specify tests to run (Redshift only).'''



class CreatedByFilters(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('created_by', 'is_template_managed', 'namespace', 'rule_name')
    created_by = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='createdBy')
    '''Emails of users who created monitors to filter by'''

    is_template_managed = sgqlc.types.Field(Boolean, graphql_name='isTemplateManaged')
    '''Filter only by monitors created with monitor-as-code (if true)'''

    namespace = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='namespace')
    '''Filter by namespace name (for monitors created via monitor-as-
    code)
    '''

    rule_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ruleName')
    '''Filter by rule names (for monitors created via monitor-as-code)'''



class CustomRuleComparisonInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('comparison_type', 'full_table_id', 'full_table_ids', 'mcon', 'field', 'metric', 'operator', 'threshold', 'baseline_agg_function', 'baseline_interval_minutes', 'is_threshold_relative', 'threshold_lookback_minutes', 'threshold_ref', 'min_buffer', 'max_buffer', 'number_of_agg_periods')
    comparison_type = sgqlc.types.Field(ComparisonType, graphql_name='comparisonType')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fullTableIds')

    mcon = sgqlc.types.Field(String, graphql_name='mcon')

    field = sgqlc.types.Field(String, graphql_name='field')

    metric = sgqlc.types.Field(String, graphql_name='metric')

    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    '''Comparison operator'''

    threshold = sgqlc.types.Field(Float, graphql_name='threshold')
    '''Threshold value'''

    baseline_agg_function = sgqlc.types.Field(AggregationFunction, graphql_name='baselineAggFunction')
    '''Function used to aggregate historical data points to calculate
    baseline
    '''

    baseline_interval_minutes = sgqlc.types.Field(Int, graphql_name='baselineIntervalMinutes')
    '''Time interval to aggregate over to calculate baseline.'''

    is_threshold_relative = sgqlc.types.Field(Boolean, graphql_name='isThresholdRelative')
    '''True, if threshold is a relative percentage change of baseline.
    False, if threshold is absolute change
    '''

    threshold_lookback_minutes = sgqlc.types.Field(Int, graphql_name='thresholdLookbackMinutes')
    '''Time to look back for rules which compare current and past values.'''

    threshold_ref = sgqlc.types.Field(String, graphql_name='thresholdRef')
    '''Key used to retrieve the threshold values from external source'''

    min_buffer = sgqlc.types.Field('ThresholdModifierInput', graphql_name='minBuffer')
    '''The lower bound buffer to modify the alert threshold.'''

    max_buffer = sgqlc.types.Field('ThresholdModifierInput', graphql_name='maxBuffer')
    '''The upper bound buffer to modify the alert threshold.'''

    number_of_agg_periods = sgqlc.types.Field(Int, graphql_name='numberOfAggPeriods')
    '''The number of periods to use in the aggregate comparison for
    Volume Growth comparisons.
    '''



class CustomRuleSnoozeInput(sgqlc.types.Input):
    '''input variables for snoozing'''
    __schema__ = schema
    __field_names__ = ('rule_uuid', 'snooze_minutes', 'conditional_snooze')
    rule_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='ruleUuid')
    '''UUID of rule to snooze'''

    snooze_minutes = sgqlc.types.Field(Int, graphql_name='snoozeMinutes')
    '''number of minutes to snooze rule'''

    conditional_snooze = sgqlc.types.Field(Boolean, graphql_name='conditionalSnooze')
    '''snooze rule until breach condition changes or is resolved'''



class DatabricksSqlWarehouseConnectionInput(sgqlc.types.Input):
    '''Credentials and connection details to a Databricks SQL warehouse
    connection
    '''
    __schema__ = schema
    __field_names__ = ('dc_id', 'databricks_config')
    dc_id = sgqlc.types.Field(UUID, graphql_name='dcId')
    '''The Data Collector UUID for a new Databricks Connection'''

    databricks_config = sgqlc.types.Field('DatabricksSqlWarehouseInput', graphql_name='databricksConfig')
    '''Configuration for Databricks.'''



class DatabricksSqlWarehouseInput(sgqlc.types.Input):
    '''Credentials to a Databricks sql warehouse.'''
    __schema__ = schema
    __field_names__ = ('databricks_workspace_url', 'databricks_warehouse_id', 'databricks_token')
    databricks_workspace_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksWorkspaceUrl')
    '''Databricks workspace URL'''

    databricks_warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksWarehouseId')
    '''Databricks warehouse ID'''

    databricks_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksToken')
    '''User token'''



class DbtArtifactsInput(sgqlc.types.Input):
    '''dbt artifacts'''
    __schema__ = schema
    __field_names__ = ('manifest', 'run_results', 'logs')
    manifest = sgqlc.types.Field(String, graphql_name='manifest')
    '''manifest file name'''

    run_results = sgqlc.types.Field(String, graphql_name='runResults')
    '''run results file name'''

    logs = sgqlc.types.Field(String, graphql_name='logs')
    '''logs file name'''



class FieldMetricFilterInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field_name', 'operator', 'value')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field to filter by'''

    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    '''Operator to filter field by'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Value to filter field by'''



class FieldMetricInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('table_mcon', 'table_mcons', 'field_name', 'field_names', 'metric_type', 'value_list', 'filters')
    table_mcon = sgqlc.types.Field(String, graphql_name='tableMcon')
    '''MCON of the table the metric is based on'''

    table_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tableMcons')
    '''MCONs of the table the metric is based on'''

    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Name of the field the metric is based on'''

    field_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fieldNames')
    '''Name of the fields the metric is based on'''

    metric_type = sgqlc.types.Field(sgqlc.types.non_null(FieldMetricType), graphql_name='metricType')
    '''Type of metric to compute'''

    value_list = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='valueList')
    '''Values for metrics that check for cardinality'''

    filters = sgqlc.types.Field(sgqlc.types.list_of(FieldMetricFilterInput), graphql_name='filters')
    '''Filters for which rows the metric is computed over'''



class FieldQueryFilterInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field_name', 'operator', 'value')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field to filter by'''

    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    '''Operator to filter field by'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Value to filter field by'''



class FieldQueryParametersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('table_mcons', 'field_names', 'query_type', 'value_list', 'filters')
    table_mcons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='tableMcons')
    '''MCONs of the table the query is based on'''

    field_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fieldNames')
    '''Name of the fields the query is based on'''

    query_type = sgqlc.types.Field(sgqlc.types.non_null(FieldQueryType), graphql_name='queryType')
    '''Type of query'''

    value_list = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='valueList')
    '''Values for queries that check for cardinality'''

    filters = sgqlc.types.Field(sgqlc.types.list_of(FieldQueryFilterInput), graphql_name='filters')
    '''Filters for which rows the query is computed over'''



class ImportanceScoreTableStatsRule(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('operator', 'value', 'value_min', 'value_max')
    operator = sgqlc.types.Field(sgqlc.types.non_null(ImportanceScoreOperator), graphql_name='operator')
    '''Comparison operator. Options include ==, >=, <=, >, <, RANGE'''

    value = sgqlc.types.Field(Float, graphql_name='value')

    value_min = sgqlc.types.Field(Float, graphql_name='valueMin')

    value_max = sgqlc.types.Field(Float, graphql_name='valueMax')



class IncidentReactionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('type', 'reasons', 'notes', 'adapt_model')
    type = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionType), graphql_name='type')

    reasons = sgqlc.types.Field(sgqlc.types.list_of(IncidentReactionReason), graphql_name='reasons')

    notes = sgqlc.types.Field(String, graphql_name='notes')
    '''Tell us more about how we can improve this incident.'''

    adapt_model = sgqlc.types.Field(Boolean, graphql_name='adaptModel')
    '''Enable if this reaction should be used to adapt our models.'''



class IndexedFieldFilterType(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field_name', 'values')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field name'''

    values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='values')
    '''Values to filter by'''



class InputObjectProperty(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mcon_id', 'property_name', 'property_value', 'property_source_type')
    mcon_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mconId')
    '''Monte Carlo full identifier for an entity'''

    property_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyName')
    '''Name of the property (AKA tag key)'''

    property_value = sgqlc.types.Field(String, graphql_name='propertyValue')
    '''Value of the property (AKA tag value)'''

    property_source_type = sgqlc.types.Field(String, graphql_name='propertySourceType')
    '''Where property originated.'''



class InviteUsersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('emails', 'client_mutation_id')
    emails = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class IsImportantTableStatsRule(sgqlc.types.Input):
    '''The key asset rule matches the is_important table stat'''
    __schema__ = schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='value')



class LookerConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('base_url', 'client_id', 'client_secret', 'verify_ssl')
    base_url = sgqlc.types.Field(String, graphql_name='baseUrl')
    '''Host url'''

    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    '''Looker client id'''

    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    '''Looker client secret'''

    verify_ssl = sgqlc.types.Field(Boolean, graphql_name='verifySsl')
    '''Verify SSL (uncheck for self-signed certs)'''



class LookerGitCloneConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('repo_url', 'username', 'token')
    repo_url = sgqlc.types.Field(String, graphql_name='repoUrl')
    '''Repository URL as https://server/project.git'''

    username = sgqlc.types.Field(String, graphql_name='username')
    '''The git username'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''The access token for git HTTPS integrations'''



class LookerGitSshConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ssh_key', 'repo_url')
    ssh_key = sgqlc.types.Field(String, graphql_name='sshKey')
    '''SSH key, base64-encoded'''

    repo_url = sgqlc.types.Field(String, graphql_name='repoUrl')
    '''Repository URL as ssh://[user@]server/project.git or the shorter
    form [user@]server:project.git
    '''



class MetricDimensionFilter(sgqlc.types.Input):
    '''Filter in key value pairs that would be applied in dimensions'''
    __schema__ = schema
    __field_names__ = ('key', 'value', 'value_str')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''name of the dimension.'''

    value = sgqlc.types.Field(Float, graphql_name='value')
    '''float value field.'''

    value_str = sgqlc.types.Field(String, graphql_name='valueStr')
    '''string value field. This field and value field should be exclusive'''



class MonitorConfigurationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mcon', 'time_fields')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''MC mcon'''

    time_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TimestampResult')), graphql_name='timeFields')
    '''field and timestamp for monitor configuration'''



class MonitorSelectExpressionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('expression', 'data_type')
    expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expression')
    '''SQL select expression, could be a raw column name or a more
    complex expression
    '''

    data_type = sgqlc.types.Field(String, graphql_name='dataType')
    '''Data type of expression. Required if expression is a complex
    expression and not a raw column name
    '''



class NodeInput(sgqlc.types.Input):
    '''Minimal information to identify a node'''
    __schema__ = schema
    __field_names__ = ('object_type', 'object_id', 'resource_id', 'resource_name')
    object_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectType')
    '''Object type'''

    object_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectId')
    '''Object identifier'''

    resource_id = sgqlc.types.Field(UUID, graphql_name='resourceId')
    '''The id of the resource containing the node'''

    resource_name = sgqlc.types.Field(String, graphql_name='resourceName')
    '''The name of the resource containing the node'''



class NotificationDigestSettings(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('start_time', 'interval_minutes', 'digest_type')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''Start time of scheduled digest. If not set, by default it is UTC
    00:00 daily
    '''

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    '''Interval of how frequently to run the schedule. If not set, by
    default it is 1440 minutes(24h)
    '''

    digest_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='digestType')
    '''Type of digest.Supported options include: anomalies_digest,
    misconf_digest, inactive_digest
    '''



class NotificationExtra(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('slack_is_private', 'webhook_shared_secret', 'webhook_encrypted_secret', 'priority', 'url', 'username', 'password', 'dc_proxy')
    slack_is_private = sgqlc.types.Field(Boolean, graphql_name='slackIsPrivate')
    '''Skip attempting to join if the channel is private. Requires a
    channel invitation first
    '''

    webhook_shared_secret = sgqlc.types.Field(String, graphql_name='webhookSharedSecret')
    '''An optional shared signing secret to use for validating the
    integrity of information when using a webhook integration
    '''

    webhook_encrypted_secret = sgqlc.types.Field(String, graphql_name='webhookEncryptedSecret')
    '''This field should be provided by the frontend when an update is
    being done to the notification setting and a shared secret key
    already existed for the web hook
    '''

    priority = sgqlc.types.Field(String, graphql_name='priority')
    '''Priority in remote notification system (Opsgenie)'''

    url = sgqlc.types.Field(String, graphql_name='url')
    '''API URL (Opsgenie, use this for regional URLs)'''

    username = sgqlc.types.Field(String, graphql_name='username')
    '''Username for external notification integration'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Password for external notification integration'''

    dc_proxy = sgqlc.types.Field(Boolean, graphql_name='dcProxy')
    '''True if HTTP requests should be proxied through the Data Collector'''



class NotificationRoutingRules(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('project_names', 'project_mcons', 'dataset_ids', 'full_table_ids', 'table_mcons', 'rule_ids', 'domain_ids', 'tag_keys', 'tag_key_values', 'all_tag_key_values', 'table_stats_rules', 'monitor_labels', 'monitor_labels_match_type', 'exclude_project_names', 'exclude_project_mcons', 'exclude_dataset_ids', 'exclude_full_table_ids', 'exclude_table_mcons', 'exclude_tag_keys', 'exclude_tag_key_values', 'exclude_all_tag_key_values', 'table_regex')
    project_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projectNames')
    '''Allowlist by project names'''

    project_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projectMcons')
    '''Allowlist by project mcons'''

    dataset_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='datasetIds')
    '''Allowlist by dataset identifiers'''

    full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fullTableIds')
    '''Allowlist by full table identifiers'''

    table_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tableMcons')
    '''Allowlist by table mcons'''

    rule_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='ruleIds')
    '''Allowlist by rule identifiers'''

    domain_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='domainIds')
    '''Allowlist by domain identifiers'''

    tag_keys = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagKeys')
    '''Allowlist by tag keys'''

    tag_key_values = sgqlc.types.Field(sgqlc.types.list_of('NotificationTagPairs'), graphql_name='tagKeyValues')
    '''Allowlist by tag key/value pairs'''

    all_tag_key_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of('NotificationTagPairs')), graphql_name='allTagKeyValues')

    table_stats_rules = sgqlc.types.Field('TableStatsRules', graphql_name='tableStatsRules')
    '''Allowlist by table stats (importance_score, is_important).'''

    monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='monitorLabels')
    '''Allowlist by monitor labels'''

    monitor_labels_match_type = sgqlc.types.Field(MonitorLabelsMatchType, graphql_name='monitorLabelsMatchType')
    '''Logic operator for matching labels. Defaults to OR.'''

    exclude_project_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeProjectNames')
    '''Denylist by project names'''

    exclude_project_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeProjectMcons')
    '''Denylist by project mcons'''

    exclude_dataset_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='excludeDatasetIds')
    '''Denylist by dataset identifiers'''

    exclude_full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeFullTableIds')
    '''Denylist by full table identifiers'''

    exclude_table_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeTableMcons')
    '''Denylist by table mcon identifiers'''

    exclude_tag_keys = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='excludeTagKeys')
    '''Denylist by tag keys'''

    exclude_tag_key_values = sgqlc.types.Field(sgqlc.types.list_of('NotificationTagPairs'), graphql_name='excludeTagKeyValues')
    '''Denylist by tag key/value pairs'''

    exclude_all_tag_key_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of('NotificationTagPairs')), graphql_name='excludeAllTagKeyValues')

    table_regex = sgqlc.types.Field(String, graphql_name='tableRegex')
    '''For use in updating regex based rules'''



class NotificationTagPairs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Tag key'''

    value = sgqlc.types.Field(String, graphql_name='value')
    '''Tag Value'''



class ObjectPropertyInput(sgqlc.types.Input):
    '''Object properties, indexed by the search service'''
    __schema__ = schema
    __field_names__ = ('property_name', 'property_value')
    property_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyName')
    '''The name (key) of the property'''

    property_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyValue')
    '''The value for the property'''



class PiiFilterStatusPair(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('filter_name', 'enabled')
    filter_name = sgqlc.types.Field(String, graphql_name='filterName')
    '''The unique name of the PII filter.'''

    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    '''Whether the PII filter should be enabled or not.'''



class PowerBIConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('tenant_id', 'auth_mode', 'client_id', 'client_secret', 'username', 'password')
    tenant_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tenantId')
    '''Azure Power BI tenant uuid'''

    auth_mode = sgqlc.types.Field(sgqlc.types.non_null(PowerBIAuthModeEnumV2), graphql_name='authMode')
    '''Authentication mode. We support two values here
    [service_principal, primary_user]
    '''

    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    '''App Client UUID'''

    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    '''Secret key for the client ID. Required if auth_mode is
    service_principal.
    '''

    username = sgqlc.types.Field(String, graphql_name='username')
    '''Username when auth as a primary user. Required if auth_mode is
    primary_user.
    '''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Password when auth as a primary user. Required if auth_mode is
    primary_user.
    '''



class QueryAfterKeyInput(sgqlc.types.Input):
    '''The after key to use for Blast Radius query data pagination'''
    __schema__ = schema
    __field_names__ = ('user', 'date', 'query_hash')
    user = sgqlc.types.Field(String, graphql_name='user')
    '''The last username retrieved'''

    date = sgqlc.types.Field(String, graphql_name='date')
    '''The last date retrieved as a string'''

    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')
    '''The last query hash'''



class QueryLogsFacetRequestType(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field_name', 'search_criteria', 'apply_mask', 'first', 'search_prefix')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field name'''

    search_criteria = sgqlc.types.Field('SearchCriteriaType', graphql_name='searchCriteria')

    apply_mask = sgqlc.types.Field(Boolean, graphql_name='applyMask')
    '''Apply mask'''

    first = sgqlc.types.Field(Int, graphql_name='first')
    '''First'''

    search_prefix = sgqlc.types.Field(String, graphql_name='searchPrefix')
    '''Search facets by prefix'''



class QueryLogsFacetRequestTypeV2(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('requests',)
    requests = sgqlc.types.Field(sgqlc.types.list_of(QueryLogsFacetRequestType), graphql_name='requests')



class QueryLogsRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('search_criteria', 'query_group_field', 'query_runtime_field', 'sort_field', 'sort_order', 'first', 'offset')
    search_criteria = sgqlc.types.Field(sgqlc.types.non_null('SearchCriteriaType'), graphql_name='searchCriteria')

    query_group_field = sgqlc.types.Field(String, graphql_name='queryGroupField')

    query_runtime_field = sgqlc.types.Field(String, graphql_name='queryRuntimeField')

    sort_field = sgqlc.types.Field(String, graphql_name='sortField')

    sort_order = sgqlc.types.Field(String, graphql_name='sortOrder')

    first = sgqlc.types.Field(Int, graphql_name='first')

    offset = sgqlc.types.Field(Int, graphql_name='offset')



class QueryRuntimeTimeSeriesRequestType(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('search_criteria', 'query_group_values', 'time_bucket_size', 'time_bucket_aggregation_function', 'query_runtime_field')
    search_criteria = sgqlc.types.Field('SearchCriteriaType', graphql_name='searchCriteria')

    query_group_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='queryGroupValues')

    time_bucket_size = sgqlc.types.Field(String, graphql_name='timeBucketSize')

    time_bucket_aggregation_function = sgqlc.types.Field(String, graphql_name='timeBucketAggregationFunction')

    query_runtime_field = sgqlc.types.Field(String, graphql_name='queryRuntimeField')



class RedshiftConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('db_name', 'host', 'port', 'user', 'password')
    db_name = sgqlc.types.Field(String, graphql_name='dbName')
    '''Name of database to add connection for'''

    host = sgqlc.types.Field(String, graphql_name='host')
    '''Hostname of the warehouse'''

    port = sgqlc.types.Field(Int, graphql_name='port')
    '''HTTP Port to use'''

    user = sgqlc.types.Field(String, graphql_name='user')
    '''User with access to the database'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''User's password'''



class ScheduleConfigInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('schedule_type', 'interval_minutes', 'interval_crontab', 'start_time', 'min_interval_minutes', 'timezone')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(ScheduleType), graphql_name='scheduleType')
    '''Type of schedule'''

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    '''Time interval between job executions, in minutes'''

    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='intervalCrontab')
    '''Time interval between job executions, using a cron expression'''

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''For schedule_type=fixed, the date the schedule should start'''

    min_interval_minutes = sgqlc.types.Field(Int, graphql_name='minIntervalMinutes')
    '''For schedule_type=dynamic, the minimum time interval between job
    executions
    '''

    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    '''Timezone for daylight savings and interpreting cron expressions.'''



class SearchCriteriaType(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('indexed_field_filters', 'query_group', 'start_time', 'end_time', 'query_group_field')
    indexed_field_filters = sgqlc.types.Field(sgqlc.types.list_of(IndexedFieldFilterType), graphql_name='indexedFieldFilters')
    '''List of indexed field filters'''

    query_group = sgqlc.types.Field(String, graphql_name='queryGroup')

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''start time, overrides days_back'''

    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')
    '''end time, overrides days_back'''

    query_group_field = sgqlc.types.Field(String, graphql_name='queryGroupField')



class SensitivityInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('level',)
    level = sgqlc.types.Field(SensitivityLevels, graphql_name='level')
    '''Low, medium or high sensitivity'''



class SetIncidentFeedbackInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('incident_id', 'feedback', 'client_mutation_id')
    incident_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='incidentId')
    '''UUID of incident to add feedback'''

    feedback = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='feedback')
    '''The feedback to be added to an incident'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class SnowflakeConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('user', 'password', 'private_key', 'private_key_passphrase', 'account', 'warehouse')
    user = sgqlc.types.Field(String, graphql_name='user')
    '''User with access to snowflake.'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''User's password if using user/password basic auth'''

    private_key = sgqlc.types.Field(String, graphql_name='privateKey')
    '''User's private key (base64 encoded) if using key pair auth.'''

    private_key_passphrase = sgqlc.types.Field(String, graphql_name='privateKeyPassphrase')
    '''User's private key passphrase if using key pair auth. This
    argument is only needed when the private key is encrypted.
    '''

    account = sgqlc.types.Field(String, graphql_name='account')
    '''Snowflake account name'''

    warehouse = sgqlc.types.Field(String, graphql_name='warehouse')
    '''Name of the warehouse for the user'''



class SparkBinaryInput(sgqlc.types.Input):
    '''Credentials to the Spark  Thrift server in binary mode'''
    __schema__ = schema
    __field_names__ = ('database', 'host', 'port', 'username', 'password')
    database = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='database')
    '''Database name'''

    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='host')
    '''Host name'''

    port = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='port')
    '''Port'''

    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''User name'''

    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    '''Password'''



class SparkDatabricksConnectionInput(sgqlc.types.Input):
    '''Credentials and connection details to a new Databricks cluster
    connection
    '''
    __schema__ = schema
    __field_names__ = ('dc_id', 'connection_type', 'databricks_config')
    dc_id = sgqlc.types.Field(UUID, graphql_name='dcId')
    '''The Data Collector UUID for a new Databricks Connection'''

    connection_type = sgqlc.types.Field(String, graphql_name='connectionType')
    '''The Databricks connection type for a new Databricks connection'''

    databricks_config = sgqlc.types.Field('SparkDatabricksInput', graphql_name='databricksConfig')
    '''Configuration for Databricks.'''



class SparkDatabricksInput(sgqlc.types.Input):
    '''Credentials to a Databricks cluster'''
    __schema__ = schema
    __field_names__ = ('databricks_workspace_url', 'databricks_workspace_id', 'databricks_cluster_id', 'databricks_token')
    databricks_workspace_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksWorkspaceUrl')
    '''Databricks workspace URL'''

    databricks_workspace_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksWorkspaceId')
    '''Databricks workspace ID'''

    databricks_cluster_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksClusterId')
    '''Databricks cluster ID'''

    databricks_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='databricksToken')
    '''User token'''



class SparkHttpInput(sgqlc.types.Input):
    '''Credentials to the Spark  Thrift server in HTTP mode'''
    __schema__ = schema
    __field_names__ = ('url', 'username', 'password')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    '''Connection URL to the Thrift server'''

    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''User name'''

    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    '''Password'''



class SslInputOptions(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ca', 'cert', 'key', 'mechanism', 'skip_verification')
    ca = sgqlc.types.Field(String, graphql_name='ca')
    '''CA bundle file'''

    cert = sgqlc.types.Field(String, graphql_name='cert')
    '''Certificate file'''

    key = sgqlc.types.Field(String, graphql_name='key')
    '''Key file'''

    mechanism = sgqlc.types.Field(String, graphql_name='mechanism')
    '''How the file is passed to the DC. Possible values are: "dc-s3" or
    "url"
    '''

    skip_verification = sgqlc.types.Field(Boolean, graphql_name='skipVerification')
    '''Whether SSL certificate verification should be skipped'''



class TableStatsRules(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('importance_score', 'is_important')
    importance_score = sgqlc.types.Field(ImportanceScoreTableStatsRule, graphql_name='importanceScore')

    is_important = sgqlc.types.Field(IsImportantTableStatsRule, graphql_name='isImportant')



class TableauConnectionDetails(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('server_name', 'username', 'password', 'token_name', 'token_value', 'site_name', 'verify_ssl')
    server_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serverName')
    '''The Tableau server name'''

    username = sgqlc.types.Field(String, graphql_name='username')
    '''Username for the Tableau user if using username/password'''

    password = sgqlc.types.Field(String, graphql_name='password')
    '''Password for the Tableau user if using username/password'''

    token_name = sgqlc.types.Field(String, graphql_name='tokenName')
    '''The personal access token name'''

    token_value = sgqlc.types.Field(String, graphql_name='tokenValue')
    '''The personal access token value'''

    site_name = sgqlc.types.Field(String, graphql_name='siteName')
    '''The Tableau site name'''

    verify_ssl = sgqlc.types.Field(Boolean, graphql_name='verifySsl')
    '''Whether to verify the SSL connection to Tableau server'''



class TagFilterInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('tag_name', 'tag_values')
    tag_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tagName')
    '''Tag name'''

    tag_values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagValues')
    '''Tag values. If empty, match all with tag_name'''



class TagKeyValuePairInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Tag key'''

    value = sgqlc.types.Field(String, graphql_name='value')
    '''Tag Value'''



class TagPair(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Tag key'''

    value = sgqlc.types.Field(String, graphql_name='value')
    '''Tag Value'''



class ThresholdModifierInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('modifier_type', 'value')
    modifier_type = sgqlc.types.Field(sgqlc.types.non_null(ThresholdModifierType), graphql_name='modifierType')
    '''The type of threshold modifier'''

    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    '''The value of the threshold modifier. If the type is PERCENTAGE,
    this should be a decimal value.
    '''



class TimestampResult(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field_name', 'timestamp')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')



class ToggleDatasetInputItem(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('dw_id', 'ds_id')
    dw_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dwId')
    '''Warehouse the dataset is contained in.'''

    ds_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dsId')
    '''ID of the dataset.'''



class ToggleMuteDatasetInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('dw_id', 'ds_id', 'mute', 'muted_event_types', 'client_mutation_id')
    dw_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dwId')
    '''Warehouse the dataset is contained in.'''

    ds_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dsId')
    '''ID of the dataset.'''

    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    '''True for muting the table, False for un-muting'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Restrict muting to the following event types (optional)'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteDatasetsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('datasets', 'mute', 'muted_event_types', 'client_mutation_id')
    datasets = sgqlc.types.Field(sgqlc.types.list_of(ToggleDatasetInputItem), graphql_name='datasets')
    '''The datasets being muted'''

    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    '''True for muting the table, False for un-muting'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Restrict muting to the following event types (optional)'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteTableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mcon', 'full_table_id', 'dw_id', 'mute', 'muted_event_types', 'client_mutation_id')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Mcon of table to toggle muting for'''

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    '''Deprecated - use mcon. Ignored if mcon is present'''

    dw_id = sgqlc.types.Field(UUID, graphql_name='dwId')
    '''Warehouse the table is contained in. Required when using a
    fullTableId
    '''

    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    '''True for muting the table, False for un-muting'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Restrict muting to the following event types (optional)'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteTablesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('tables', 'mute', 'muted_event_types', 'client_mutation_id')
    tables = sgqlc.types.Field(sgqlc.types.list_of('ToggleTableInputItem'), graphql_name='tables')
    '''The tables being muted'''

    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    '''True for muting the table, False for un-muting'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Restrict muting to the following event types (optional)'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteWithRegexInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('dw_id', 'rule_regex', 'mute', 'muted_event_types', 'client_mutation_id')
    dw_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dwId')
    '''Warehouse the dataset is contained in.'''

    rule_regex = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleRegex')
    '''Valid regex to match fullTableIds. FullTableIds have the following
    format: "PROJECT_NAME:DATASET_NAME.TABLE_ID"
    '''

    mute = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mute')
    '''True for muting the table, False for un-muting'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Restrict muting to the following event types (optional)'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleTableInputItem(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mcon', 'full_table_id', 'dw_id')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Mcon of the table to toggle muting for'''

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    '''Deprecated - use mcon. Ignored if mcon is present'''

    dw_id = sgqlc.types.Field(UUID, graphql_name='dwId')
    '''Warehouse the table is contained in. Required when using a full
    table id
    '''



class TopQueryGroupsRequestType(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('search_criteria', 'first', 'offset', 'sort_field')
    search_criteria = sgqlc.types.Field(sgqlc.types.non_null(SearchCriteriaType), graphql_name='searchCriteria')

    first = sgqlc.types.Field(Int, graphql_name='first')

    offset = sgqlc.types.Field(Int, graphql_name='offset')

    sort_field = sgqlc.types.Field(String, graphql_name='sortField')



class TrackTableInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('mcon', 'full_table_id', 'dw_id', 'track', 'client_mutation_id')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Mcon of table to toggle tracking for'''

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    '''Deprecated - use mcon. Ignored if mcon is present'''

    dw_id = sgqlc.types.Field(UUID, graphql_name='dwId')
    '''Warehouse the table is contained in. Required when using a
    fullTableId
    '''

    track = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='track')
    '''Enable or disable table tracking'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class UpdateUserStateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('state', 'client_mutation_id')
    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class UserAfterKeyInput(sgqlc.types.Input):
    '''The after key to use for Blast Radius User data pagination'''
    __schema__ = schema
    __field_names__ = ('user', 'source')
    user = sgqlc.types.Field(String, graphql_name='user')
    '''The last username retrieved'''

    source = sgqlc.types.Field(String, graphql_name='source')
    '''The last source table retrieved'''



class UserAfterKeyInput2(sgqlc.types.Input):
    '''The after key to use for Blast Radius User data pagination'''
    __schema__ = schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field(String, graphql_name='user')
    '''The last username retrieved'''



class ValidatorTestOptions(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('validate_select', 'validate_info_access', 'validate_table_metadata', 'validate_syslog')
    validate_select = sgqlc.types.Field(Boolean, graphql_name='validateSelect')
    '''Whether the validate select query should be executed'''

    validate_info_access = sgqlc.types.Field(Boolean, graphql_name='validateInfoAccess')
    '''Whether the validate info access query should be executed'''

    validate_table_metadata = sgqlc.types.Field(Boolean, graphql_name='validateTableMetadata')
    '''Whether the validate table metadata query should be executed'''

    validate_syslog = sgqlc.types.Field(Boolean, graphql_name='validateSyslog')
    '''Whether the validate syslog query should be executed'''



class WildcardTemplateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('template_name', 'template_regex')
    template_name = sgqlc.types.Field(String, graphql_name='templateName')

    template_regex = sgqlc.types.Field(String, graphql_name='templateRegex')




########################################################################
# Output Objects and Interfaces
########################################################################
class ICustomRulesMonitor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('has_custom_rule_name', 'rule_description', 'rule_comparisons', 'rule_notes', 'rule_variables', 'is_snoozed', 'snooze_until_time', 'slack_snooze_user', 'conditional_snooze', 'breach_rate', 'interval_minutes')
    has_custom_rule_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasCustomRuleName')
    '''Whether the monitor has a name given by the monitor creator'''

    rule_description = sgqlc.types.Field(String, graphql_name='ruleDescription')
    '''**DEPRECATED**'''

    rule_comparisons = sgqlc.types.Field(sgqlc.types.list_of('CustomRuleComparison'), graphql_name='ruleComparisons')

    rule_notes = sgqlc.types.Field(String, graphql_name='ruleNotes')
    '''**DEPRECATED**'''

    rule_variables = sgqlc.types.Field(JSONString, graphql_name='ruleVariables')
    '''variables defined for the sql rule'''

    is_snoozed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozed')
    '''Whether the monitor is currently snoozed'''

    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')
    '''If snoozed, the wake up time in UTC'''

    slack_snooze_user = sgqlc.types.Field(String, graphql_name='slackSnoozeUser')
    '''Slack user who snoozed rule'''

    conditional_snooze = sgqlc.types.Field(Boolean, graphql_name='conditionalSnooze')
    '''Whether the monitor is conditionally snoozed'''

    breach_rate = sgqlc.types.Field(String, graphql_name='breachRate')
    '''Percentage of last 10 runs in which the monitor's condition was
    breached
    '''

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    '''Interval between monitor runs, in minutes'''



class IMetricsMonitor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('monitor_fields', 'monitor_time_axis_field_name', 'monitor_time_axis_field_type', 'where_condition', 'use_partition_clause', 'segmented_expressions', 'history_days', 'select_expressions', 'agg_time_interval')
    monitor_fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='monitorFields')
    '''Field/s to monitor'''

    monitor_time_axis_field_name = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldName')
    '''The name of the table/view field used for establishing the table
    time
    '''

    monitor_time_axis_field_type = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldType')
    '''Type of time axis field used for establishing the table time'''

    where_condition = sgqlc.types.Field(String, graphql_name='whereCondition')
    '''Comparison predicate for the monitor SQL query'''

    use_partition_clause = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='usePartitionClause')
    '''Whether to use automatic partition filter in query'''

    segmented_expressions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='segmentedExpressions')
    '''Fields or expressions used to segment the monitored field
    (currently supports one such value)
    '''

    history_days = sgqlc.types.Field(Int, graphql_name='historyDays')
    '''Number of lookback days for each monitor execution'''

    select_expressions = sgqlc.types.Field(sgqlc.types.list_of('MetricMonitorSelectExpression'), graphql_name='selectExpressions')
    '''Monitor select expression'''

    agg_time_interval = sgqlc.types.Field(MonitorAggTimeInterval, graphql_name='aggTimeInterval')
    '''For field health and dimension monitoring, the aggregation time
    interval to use. Either HOUR or DAY
    '''



class IMonitor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('uuid', 'monitor_type', 'created_time', 'last_update_time', 'creator_id', 'updater_id', 'resource_id', 'entities', 'entity_mcons', 'schedule_type', 'name', 'rule_name', 'description', 'notes', 'labels', 'severity', 'notification_settings', 'notify_rule_run_failure', 'is_snoozeable', 'is_paused', 'is_template_managed', 'namespace', 'next_execution_time', 'prev_execution_time', 'is_transitioning_data_provider', 'schedule_config', 'seven_days_incident_count', 'incident_count_history', 'weekly_incident_count_change_rate')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Unique identifier for monitors'''

    monitor_type = sgqlc.types.Field(sgqlc.types.non_null(UserDefinedMonitors), graphql_name='monitorType')
    '''Type of monitor'''

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    '''Monitor creation time (UTC)'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''Monitor last update time (UTC)'''

    creator_id = sgqlc.types.Field(String, graphql_name='creatorId')
    '''Email of user who created the monitor'''

    updater_id = sgqlc.types.Field(String, graphql_name='updaterId')
    '''Email of user who last updated the monitor'''

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''Warehouse Unique Identifier'''

    entities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entities')
    '''Full table IDs for monitored tables/views'''

    entity_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entityMcons')
    '''MCONs for monitored tables/views'''

    schedule_type = sgqlc.types.Field(String, graphql_name='scheduleType')
    '''Monitor scheduling type'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Monitor/rule name, default or user-defined'''

    rule_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleName')
    '''DEPRECATED: Rule name, default or user-defined, null for monitors.
    Use name instead.
    '''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Monitor user-defined name'''

    notes = sgqlc.types.Field(String, graphql_name='notes')
    '''Notes defined on this monitor'''

    labels = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='labels')
    '''List of tags used to filter a monitor'''

    severity = sgqlc.types.Field(String, graphql_name='severity')
    '''Default severity for incidents involving this monitor'''

    notification_settings = sgqlc.types.Field(sgqlc.types.list_of('AccountNotificationSetting'), graphql_name='notificationSettings')
    '''Notification channels that match the monitor'''

    notify_rule_run_failure = sgqlc.types.Field(Boolean, graphql_name='notifyRuleRunFailure')
    '''Whether audiences will be notified when the rule fails to execute'''

    is_snoozeable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozeable')
    '''Whether the monitor can be snoozed'''

    is_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaused')
    '''Whether the monitor is currently paused'''

    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    '''Whether the monitor was created from through monitor-as-code'''

    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    '''The monitor-as-code namespace used when creating the monitor'''

    next_execution_time = sgqlc.types.Field(DateTime, graphql_name='nextExecutionTime')
    '''The next time (UTC) in which the monitor will run'''

    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    '''The last time (UTC) in which the monitor ran'''

    is_transitioning_data_provider = sgqlc.types.Field(Boolean, graphql_name='isTransitioningDataProvider')

    schedule_config = sgqlc.types.Field('ScheduleConfigOutput', graphql_name='scheduleConfig')

    seven_days_incident_count = sgqlc.types.Field(Int, graphql_name='sevenDaysIncidentCount')
    '''Number of incidents in the past 7 days'''

    incident_count_history = sgqlc.types.Field(sgqlc.types.list_of('IncidentDailyCount'), graphql_name='incidentCountHistory')
    '''Number of incidents per day for the past 30 days'''

    weekly_incident_count_change_rate = sgqlc.types.Field(Int, graphql_name='weeklyIncidentCountChangeRate')
    '''Change in percentage between between last 7 days and the 7 days
    before.
    '''



class IMonitorStatus(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('monitor_run_status', 'monitor_configuration_status', 'monitor_training_status', 'monitor_status', 'exceptions')
    monitor_run_status = sgqlc.types.Field(sgqlc.types.non_null(MonitorRunStatusType), graphql_name='monitorRunStatus')
    '''Monitor run status'''

    monitor_configuration_status = sgqlc.types.Field(sgqlc.types.non_null(MonitorConfigurationStatusType), graphql_name='monitorConfigurationStatus')
    '''Monitor configuration status'''

    monitor_training_status = sgqlc.types.Field(sgqlc.types.non_null(MonitorTrainingStatusType), graphql_name='monitorTrainingStatus')
    '''Monitor training status'''

    monitor_status = sgqlc.types.Field(sgqlc.types.non_null(MonitorStatusType), graphql_name='monitorStatus')
    '''Consolidated monitor status'''

    exceptions = sgqlc.types.Field(String, graphql_name='exceptions')
    '''Exceptions if any occurred during the last run'''



class Node(sgqlc.types.Interface):
    '''An object with an ID'''
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    '''The ID of the object.'''



class AccessToken(sgqlc.types.Type):
    '''Generated API Token ID and Access Key. Only available once'''
    __schema__ = schema
    __field_names__ = ('id', 'token')
    id = sgqlc.types.Field(String, graphql_name='id')
    '''Token user ID'''

    token = sgqlc.types.Field(String, graphql_name='token')
    '''Generated token'''



class Account(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'name', 'created_on', 'config', 'allow_non_sso_login', 'data_share', 'is_deleted', 'notification_settings', 'data_collectors', 'users', 'user_invites', 'user_account_before_switch', 'warehouses', 'bi', 'etl_containers', 'connections', 'tableau_accounts', 'slack_credentials', 'slack_channels', 'slack_msg_details', 'resources', 'account_domains', 'slack_credentials_v2', 'collection_preferences', 'identity_provider', 'active_collection_regions', 'internal_notifications')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''The account id'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''The account name'''

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')
    '''When the account was first created'''

    config = sgqlc.types.Field(JSONString, graphql_name='config')
    '''Account level configuration'''

    allow_non_sso_login = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowNonSsoLogin')

    data_share = sgqlc.types.Field(JSONString, graphql_name='dataShare')
    '''Information necessary to setup a Snowflake Data Share'''

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    notification_settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AccountNotificationSetting'))), graphql_name='notificationSettings')
    '''Related account to send notifications for'''

    data_collectors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DataCollector'))), graphql_name='dataCollectors')

    users = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `email` (`String`)None
    * `first_name` (`String`)None
    * `last_name` (`String`)None
    * `role` (`String`)None
    '''

    user_invites = sgqlc.types.Field(sgqlc.types.non_null('UserInviteConnection'), graphql_name='userInvites', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `state` (`String`)None
    '''

    user_account_before_switch = sgqlc.types.Field(sgqlc.types.non_null('UserInviteConnection'), graphql_name='userAccountBeforeSwitch', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `state` (`String`)None
    '''

    warehouses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Warehouse'))), graphql_name='warehouses')

    bi = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BiContainer'))), graphql_name='bi')

    etl_containers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EtlContainer'))), graphql_name='etlContainers')

    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Connection'))), graphql_name='connections')

    tableau_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableauAccount'))), graphql_name='tableauAccounts')

    slack_credentials = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SlackCredentials'))), graphql_name='slackCredentials')

    slack_channels = sgqlc.types.Field(sgqlc.types.non_null('SlackChannelV2Connection'), graphql_name='slackChannels', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''The account associated with the slack channel.

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    slack_msg_details = sgqlc.types.Field(sgqlc.types.non_null('SlackMessageDetailsConnection'), graphql_name='slackMsgDetails', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    resources = sgqlc.types.Field(sgqlc.types.non_null('ResourceConnection'), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Customer account

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    account_domains = sgqlc.types.Field(sgqlc.types.non_null('DomainRestrictionConnection'), graphql_name='accountDomains', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Related account

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    slack_credentials_v2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SlackCredentialsV2'))), graphql_name='slackCredentialsV2')

    collection_preferences = sgqlc.types.Field(sgqlc.types.non_null('CollectionBlockConnection'), graphql_name='collectionPreferences', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    identity_provider = sgqlc.types.Field('SamlIdentityProvider', graphql_name='identityProvider')

    active_collection_regions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='activeCollectionRegions')
    '''AWS Regions where a DC can be hosted'''

    internal_notifications = sgqlc.types.Field(sgqlc.types.list_of('InternalNotifications'), graphql_name='internalNotifications')
    '''MC internal account notifications.'''



class AccountNotificationDigestSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'interval_minutes', 'start_time', 'prev_execution_time', 'next_execution_time', 'created_time', 'uuid', 'digest_type', 'digest_settings')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    interval_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='intervalMinutes')
    '''Frequency interval in minutes to indicate how often to run the the
    schedule.
    '''

    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')
    '''First start time to run the schedule.'''

    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')
    '''Previous successful execution time.'''

    next_execution_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='nextExecutionTime')
    '''Scheduled time for next run.'''

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    '''Timestamp of when the schedule is created.'''

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Unique id of the digest settings.'''

    digest_type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationDigestSettingsModelDigestType), graphql_name='digestType')
    '''Type of digest.'''

    digest_settings = sgqlc.types.Field('AccountNotificationSetting', graphql_name='digestSettings')



class AccountNotificationRoutingRules(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'table_rules', 'tag_rules', 'sql_rules', 'table_stats_rules', 'domain_rules', 'monitor_labels', 'monitor_labels_match_type', 'table_id_rules', 'routing_rules')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''The route rule id'''

    table_rules = sgqlc.types.Field(String, graphql_name='tableRules')
    '''Table/dataset based rules (regex)'''

    tag_rules = sgqlc.types.Field(JSONString, graphql_name='tagRules')
    '''Key and key/value based rules'''

    sql_rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UUID)), graphql_name='sqlRules')
    '''Custom sql rules'''

    table_stats_rules = sgqlc.types.Field(JSONString, graphql_name='tableStatsRules')
    '''Rules based on table stats (importance_score, is_important).'''

    domain_rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UUID)), graphql_name='domainRules')
    '''List of domain UUIDs to match event objects against.'''

    monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UUID)), graphql_name='monitorLabels')
    '''labels'''

    monitor_labels_match_type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationRoutingRulesModelMonitorLabelsMatchType), graphql_name='monitorLabelsMatchType')
    '''Specifies what logic operator to apply when matching labels'''

    table_id_rules = sgqlc.types.Field(JSONString, graphql_name='tableIdRules')
    '''Project/dataset/table based rules'''

    routing_rules = sgqlc.types.Field('AccountNotificationSetting', graphql_name='routingRules')



class AccountNotificationSetting(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'created_by', 'created_time', 'last_updated_by', 'last_update_time', 'name', 'is_template_managed', 'namespace', 'type', 'recipient', 'recipients', 'anomaly_types', 'incident_sub_types', 'extra', 'routing_rules', 'custom_message', 'notification_schedule_type', 'digest_settings', 'specification_rule', 'notification_enabled', 'slack_msg_details', 'recipient_display_name', 'recipients_display_names', 'permalink', 'matching_incidents')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Effective ID for notification settings'''

    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    '''Creator of the notification'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the notification was first created'''

    last_updated_by = sgqlc.types.Field('User', graphql_name='lastUpdatedBy')
    '''User who last updated this notification'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the notification was last updated'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Resource name for notifications created through notifications-as-
    code
    '''

    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    '''Is this monitor managed by a configuration template
    (notifications-as-code)?
    '''

    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    '''Namespace of notification, used for notifications-as-code'''

    type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationSettingsModelType), graphql_name='type')
    '''Type of notification integration (e.g. slack)'''

    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    '''Deprecated'''

    recipients = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='recipients')
    '''Destinations to send notifications to'''

    anomaly_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='anomalyTypes')
    '''List of supported incident types to send notifications for'''

    incident_sub_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='incidentSubTypes')
    '''All the incident sub-types this notification settings will alert
    on.
    '''

    extra = sgqlc.types.Field(JSONString, graphql_name='extra')
    '''Any additional information for various notification integrations'''

    routing_rules = sgqlc.types.Field(AccountNotificationRoutingRules, graphql_name='routingRules')

    custom_message = sgqlc.types.Field(String, graphql_name='customMessage')
    '''Custom text to be included with the notification'''

    notification_schedule_type = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationSettingsModelNotificationScheduleType), graphql_name='notificationScheduleType')
    '''Indicates whether the notification is of real time or digest types'''

    digest_settings = sgqlc.types.Field(AccountNotificationDigestSettings, graphql_name='digestSettings')

    specification_rule = sgqlc.types.Field(String, graphql_name='specificationRule')
    '''DEPRECATED'''

    notification_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='notificationEnabled')
    '''When enabled notifications for this setting are sent.'''

    slack_msg_details = sgqlc.types.Field(sgqlc.types.non_null('SlackMessageDetailsConnection'), graphql_name='slackMsgDetails', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    recipient_display_name = sgqlc.types.Field(String, graphql_name='recipientDisplayName')

    recipients_display_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipientsDisplayNames')

    permalink = sgqlc.types.Field(String, graphql_name='permalink')

    matching_incidents = sgqlc.types.Field(Int, graphql_name='matchingIncidents')



class AddBiConnectionMutation(sgqlc.types.Type):
    '''Add a bi connection and setup any associated jobs'''
    __schema__ = schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')



class AddConnectionMutation(sgqlc.types.Type):
    '''Add a connection and setup any associated jobs. Creates a
    warehouse if not specified
    '''
    __schema__ = schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')



class AddDatabricksConnectionMutation(sgqlc.types.Type):
    '''Add a databricks connection and setup any associated jobs. Creates
    a warehouse if not specified
    '''
    __schema__ = schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')



class AddEtlConnectionMutation(sgqlc.types.Type):
    '''Add an etl connection and setup any associated jobs'''
    __schema__ = schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field('Connection', graphql_name='connection')



class AddTableauAccountMutation(sgqlc.types.Type):
    '''Add a tableau account'''
    __schema__ = schema
    __field_names__ = ('tableau_account',)
    tableau_account = sgqlc.types.Field('TableauAccount', graphql_name='tableauAccount')



class AddToCollectionBlockList(sgqlc.types.Type):
    '''Adds to the list of entities for which metadata collection is not
    allowed on this account.
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Whether the mutation succeeded.'''



class AdditionalData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('projects_validated', 'datasets_validated', 'tables_validated', 'queries_with_results')
    projects_validated = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projectsValidated')
    '''Projects that were validated.'''

    datasets_validated = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='datasetsValidated')
    '''Datasets that were validated.'''

    tables_validated = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tablesValidated')
    '''Tables that were validated.'''

    queries_with_results = sgqlc.types.Field(sgqlc.types.list_of('QueryWithResults'), graphql_name='queriesWithResults')
    '''Queries that were executed for validation along with their
    results.
    '''



class AggregatedQuery(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date', 'group_id', 'query_hash', 'user', 'category', 'latest_query', 'latest_query_id', 'latest_query_timestamp', 'count', 'average_run_time')
    date = sgqlc.types.Field(Date, graphql_name='date')
    '''Date the queries occurred on'''

    group_id = sgqlc.types.Field(String, graphql_name='groupId')
    '''Hash that is shared by all the aggregated queries for writes'''

    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')
    '''Hash that is shared by all the aggregated queries for reads'''

    user = sgqlc.types.Field(String, graphql_name='user')
    '''User of the aggregated queries'''

    category = sgqlc.types.Field(QueryCategory, graphql_name='category')
    '''Category of the aggregated queries'''

    latest_query = sgqlc.types.Field(String, graphql_name='latestQuery')
    '''Substring of the latest query from the aggregated group containing
    the first n characters defined by the query_characters parameter
    in the request
    '''

    latest_query_id = sgqlc.types.Field(String, graphql_name='latestQueryId')
    '''ID of the latest query'''

    latest_query_timestamp = sgqlc.types.Field(DateTime, graphql_name='latestQueryTimestamp')
    '''Timestamp of the latest query'''

    count = sgqlc.types.Field(Int, graphql_name='count')
    '''Count of the number of queries aggregated'''

    average_run_time = sgqlc.types.Field(Int, graphql_name='averageRunTime')
    '''Average run time of the aggregated queries in milliseconds'''



class AggregatedQueryResults(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('aggregated_queries', 'page_info')
    aggregated_queries = sgqlc.types.Field(sgqlc.types.list_of(AggregatedQuery), graphql_name='aggregatedQueries')
    '''List of aggregated queries which are grouped based on their group
    ID
    '''

    page_info = sgqlc.types.Field('NextPageInfo', graphql_name='pageInfo')
    '''Data necessary to paginate aggregated queries'''



class AirflowTaskInstanceConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AirflowTaskInstanceEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class AirflowTaskInstanceEdge(sgqlc.types.Type):
    '''A Relay edge containing a `AirflowTaskInstance` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('AirflowTaskInstance', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class AirflowTaskLog(sgqlc.types.Type):
    '''The logs for an Airflow task attempt'''
    __schema__ = schema
    __field_names__ = ('messages', 'total_messages', '_id')
    messages = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='messages')
    '''The log messages for an Airflow task instance'''

    total_messages = sgqlc.types.Field(Int, graphql_name='totalMessages')
    '''Total log messages available'''

    _id = sgqlc.types.Field(String, graphql_name='_id')
    '''Composite ID for frontend caching (concatenated
    dag/exec_date/task/try)
    '''



class AirflowTaskRunConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('AirflowTaskRunEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class AirflowTaskRunEdge(sgqlc.types.Type):
    '''A Relay edge containing a `AirflowTaskRun` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('AirflowTaskRun', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class AuthorRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'username', 'email')
    name = sgqlc.types.Field(String, graphql_name='name')

    username = sgqlc.types.Field(String, graphql_name='username')

    email = sgqlc.types.Field(String, graphql_name='email')



class AuthorizationGroupOutput(sgqlc.types.Type):
    '''Authorization group used to configure access and permissions for
    users.
    '''
    __schema__ = schema
    __field_names__ = ('name', 'roles', 'version', 'is_managed', 'label', 'description', 'users', 'domain_restrictions', 'sso_group')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Unique to the account, human-readable name (for use in code/policy
    reference).
    '''

    roles = sgqlc.types.Field(sgqlc.types.list_of('RoleOutput'), graphql_name='roles')
    '''List of roles that are assigned to this group.'''

    version = sgqlc.types.Field(String, graphql_name='version')
    '''Version of the permissions definitions the group is designed for,
    ex: 2022-03-17. Defaults to current.
    '''

    is_managed = sgqlc.types.Field(Boolean, graphql_name='isManaged')
    '''Indicates if this group is managed by Monte Carlo. If so, only
    changes to group membership are supported.
    '''

    label = sgqlc.types.Field(String, graphql_name='label')
    '''UI/user-friendly display name, ex: Data Consumers'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description/help text to help users understand the purpose of the
    group
    '''

    users = sgqlc.types.Field(sgqlc.types.list_of('AuthUser'), graphql_name='users')
    '''List of users  who are members of the group.'''

    domain_restrictions = sgqlc.types.Field(sgqlc.types.list_of('DomainRestriction'), graphql_name='domainRestrictions')
    '''List of domains this group is limited to.'''

    sso_group = sgqlc.types.Field(String, graphql_name='ssoGroup')
    '''SSO group name to map this authorization group to'''



class BiContainer(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'account', 'uuid', 'data_collector', 'type', 'name', 'connections')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    data_collector = sgqlc.types.Field('DataCollector', graphql_name='dataCollector')

    type = sgqlc.types.Field(sgqlc.types.non_null(BiContainerModelType), graphql_name='type')

    name = sgqlc.types.Field(String, graphql_name='name')

    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Connection'))), graphql_name='connections')



class BiLineage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('workbook_id', 'friendly_name', 'content_url', 'owner_id', 'project_id', 'project_name', 'created', 'updated', 'total_views', 'workbook_creators', 'view_id', 'category', 'mcon', 'name', 'display_name')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')

    content_url = sgqlc.types.Field(String, graphql_name='contentUrl')

    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    created = sgqlc.types.Field(DateTime, graphql_name='created')

    updated = sgqlc.types.Field(DateTime, graphql_name='updated')

    total_views = sgqlc.types.Field(Int, graphql_name='totalViews')

    workbook_creators = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='workbookCreators')

    view_id = sgqlc.types.Field(String, graphql_name='viewId')

    category = sgqlc.types.Field(String, graphql_name='category')
    '''Node type'''

    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Monte Carlo object name'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Object name (table name, report name, etc)'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Friendly display name'''



class BiMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('owner', 'site', 'uri', 'sheets', 'embedded_datasources', 'upstream_data_quality_warnings', 'view_path', 'workbook_id', 'workbook_name', 'view_id', 'dashboards', 'model_name', 'source_file', 'view_name', 'connection_name', 'lookml_model_id', 'explore_id', 'explore_name', 'query', 'is_deleted', 'user_id', 'hidden', 'deleted_at', 'last_accessed_at', 'last_viewed_at', 'description', 'favorite_count', 'view_count', 'preferred_viewer', 'readonly', 'refresh_interval', 'load_configuration', 'edit_uri', 'look_ids', 'looker_dashboard_tiles', 'importance_score', 'dashboard_folder', 'avg_daily_views_last30_days', 'total_views_since_creation', 'model_id', 'dashboard', 'chart_title', 'user_emails', 'reason', 'is_manual', 'aggregation', 'date_range', 'workspace', 'created_by', 'modified_at', 'modified_by', 'report_type', 'tiles', 'workbook', 'url', 'email', 'org', 'kind', 'project_name', 'creation_time', 'created_at')
    owner = sgqlc.types.Field('OwnerRef', graphql_name='owner')

    site = sgqlc.types.Field('SiteRef', graphql_name='site')

    uri = sgqlc.types.Field(String, graphql_name='uri')

    sheets = sgqlc.types.Field(sgqlc.types.list_of('SheetDashboardRef'), graphql_name='sheets')

    embedded_datasources = sgqlc.types.Field(sgqlc.types.list_of('NameRef'), graphql_name='embeddedDatasources')

    upstream_data_quality_warnings = sgqlc.types.Field(sgqlc.types.list_of('DataQualityWarningsRef'), graphql_name='upstreamDataQualityWarnings')

    view_path = sgqlc.types.Field(String, graphql_name='viewPath')

    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')

    workbook_name = sgqlc.types.Field(String, graphql_name='workbookName')

    view_id = sgqlc.types.Field(String, graphql_name='viewId')

    dashboards = sgqlc.types.Field(sgqlc.types.list_of('SheetDashboardRef'), graphql_name='dashboards')

    model_name = sgqlc.types.Field(String, graphql_name='modelName')

    source_file = sgqlc.types.Field(String, graphql_name='sourceFile')

    view_name = sgqlc.types.Field(String, graphql_name='viewName')

    connection_name = sgqlc.types.Field(String, graphql_name='connectionName')

    lookml_model_id = sgqlc.types.Field(String, graphql_name='lookmlModelId')

    explore_id = sgqlc.types.Field(String, graphql_name='exploreId')

    explore_name = sgqlc.types.Field(String, graphql_name='exploreName')

    query = sgqlc.types.Field('QueryRef', graphql_name='query')

    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')

    user_id = sgqlc.types.Field(String, graphql_name='userId')

    hidden = sgqlc.types.Field(String, graphql_name='hidden')

    deleted_at = sgqlc.types.Field(String, graphql_name='deletedAt')

    last_accessed_at = sgqlc.types.Field(String, graphql_name='lastAccessedAt')

    last_viewed_at = sgqlc.types.Field(String, graphql_name='lastViewedAt')

    description = sgqlc.types.Field(String, graphql_name='description')

    favorite_count = sgqlc.types.Field(Int, graphql_name='favoriteCount')

    view_count = sgqlc.types.Field(Int, graphql_name='viewCount')

    preferred_viewer = sgqlc.types.Field(String, graphql_name='preferredViewer')

    readonly = sgqlc.types.Field(Boolean, graphql_name='readonly')

    refresh_interval = sgqlc.types.Field(String, graphql_name='refreshInterval')

    load_configuration = sgqlc.types.Field(String, graphql_name='loadConfiguration')

    edit_uri = sgqlc.types.Field(String, graphql_name='editUri')

    look_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lookIds')

    looker_dashboard_tiles = sgqlc.types.Field(sgqlc.types.list_of('LookerDashboardTileRef'), graphql_name='lookerDashboardTiles')

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')

    dashboard_folder = sgqlc.types.Field(String, graphql_name='dashboardFolder')

    avg_daily_views_last30_days = sgqlc.types.Field(Float, graphql_name='avgDailyViewsLast30Days')

    total_views_since_creation = sgqlc.types.Field(Int, graphql_name='totalViewsSinceCreation')

    model_id = sgqlc.types.Field(String, graphql_name='modelId')

    dashboard = sgqlc.types.Field('SheetDashboardRef', graphql_name='dashboard')

    chart_title = sgqlc.types.Field(String, graphql_name='chartTitle')

    user_emails = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='userEmails')

    reason = sgqlc.types.Field(String, graphql_name='reason')

    is_manual = sgqlc.types.Field(String, graphql_name='isManual')

    aggregation = sgqlc.types.Field(String, graphql_name='aggregation')

    date_range = sgqlc.types.Field(String, graphql_name='dateRange')

    workspace = sgqlc.types.Field('PowerBIWorkSpaceRef', graphql_name='workspace')

    created_by = sgqlc.types.Field(String, graphql_name='createdBy')

    modified_at = sgqlc.types.Field(String, graphql_name='modifiedAt')

    modified_by = sgqlc.types.Field(String, graphql_name='modifiedBy')

    report_type = sgqlc.types.Field(String, graphql_name='reportType')

    tiles = sgqlc.types.Field(sgqlc.types.list_of('PowerBIDashboardTileRef'), graphql_name='tiles')

    workbook = sgqlc.types.Field(String, graphql_name='workbook')

    url = sgqlc.types.Field(String, graphql_name='url')

    email = sgqlc.types.Field(String, graphql_name='email')

    org = sgqlc.types.Field(String, graphql_name='org')

    kind = sgqlc.types.Field(String, graphql_name='kind')

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    creation_time = sgqlc.types.Field(String, graphql_name='creationTime')

    created_at = sgqlc.types.Field(String, graphql_name='createdAt')



class BiWarehouseSources(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('warehouse_resource_id', 'warehouse_resource_type', 'bi_warehouse_id')
    warehouse_resource_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouseResourceId')
    '''Warehouse resource ID. This is a Monte Carlo ID'''

    warehouse_resource_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouseResourceType')
    '''Warehouse type. Examples: snowflake, redshift, etc.'''

    bi_warehouse_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='biWarehouseId')
    '''The warehouse ID in the BI instance of the customer. This is an ID
    in the customer ID space and is not a Monte Carlo ID.
    '''



class BigQueryProject(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_project_id', 'friendly_name')
    full_project_id = sgqlc.types.Field(String, graphql_name='fullProjectId')

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')



class BlastRadiusCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query_count', 'user_count')
    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of queries'''

    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')
    '''The number of users'''



class BlastRadiusUserQuery(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date', 'tables', 'query_hash', 'query_count')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    '''The date the query was ran'''

    tables = sgqlc.types.Field(sgqlc.types.list_of('TableInfo'), graphql_name='tables')
    '''The impacted tables in the query'''

    query_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryHash')
    '''The query hash'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of times the query was ran'''



class BulkCreateOrUpdateObjectProperties(sgqlc.types.Type):
    '''Create or update a list of properties (tags) for objects (e.g.
    tables, fields, etc.)
    '''
    __schema__ = schema
    __field_names__ = ('object_properties',)
    object_properties = sgqlc.types.Field(sgqlc.types.list_of('ObjectProperty'), graphql_name='objectProperties')
    '''List of properties created or updated'''



class CatalogNavNode(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon_id', 'display_name', 'object_type', 'path', 'may_have_children')
    mcon_id = sgqlc.types.Field(String, graphql_name='mconId')
    '''MCON ID of the object represented by this node.'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''User-friendly display name of the catalog object.'''

    object_type = sgqlc.types.Field(String, graphql_name='objectType')
    '''The catalog object's type.'''

    path = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='path')
    '''Object's hierarchy as list of ancestors plus self, if applicable.'''

    may_have_children = sgqlc.types.Field(Boolean, graphql_name='mayHaveChildren')
    '''Whether or not the node may have children. (Does not indicate if
    it actually does.)
    '''



class CatalogNavResults(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('nodes', 'has_next_page', 'next_page_offset', 'group_object_type')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(CatalogNavNode), graphql_name='nodes')
    '''Nodes for current nav page.'''

    has_next_page = sgqlc.types.Field(Boolean, graphql_name='hasNextPage')
    '''If there are more nodes.'''

    next_page_offset = sgqlc.types.Field(Int, graphql_name='nextPageOffset')
    '''Where to start for next page, if next page exists.'''

    group_object_type = sgqlc.types.Field(String, graphql_name='groupObjectType')
    '''Object type of the group, when grouping by type.'''



class CatalogObjectMetadataConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CatalogObjectMetadataEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class CatalogObjectMetadataEdge(sgqlc.types.Type):
    '''A Relay edge containing a `CatalogObjectMetadata` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CatalogObjectMetadata', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class CategoryLabelRank(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('label', 'rank')
    label = sgqlc.types.Field(String, graphql_name='label')

    rank = sgqlc.types.Field(Float, graphql_name='rank')



class CircuitBreakerState(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('job_execution_uuid', 'account_uuid', 'resource_uuid', 'custom_rule_uuid', 'status', 'log')
    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')
    '''UUID for the job execution that identifies the circuit breaker run'''

    account_uuid = sgqlc.types.Field(UUID, graphql_name='accountUuid')
    '''UUID for the account that owns the rule'''

    resource_uuid = sgqlc.types.Field(UUID, graphql_name='resourceUuid')
    '''UUID for the warehouse that owns the rule'''

    custom_rule_uuid = sgqlc.types.Field(UUID, graphql_name='customRuleUuid')
    '''UUID for the custom rule that was run as a circuit breaker'''

    status = sgqlc.types.Field(SqlJobCheckpointStatus, graphql_name='status')
    '''Status of the circuit breaker run'''

    log = sgqlc.types.Field(JSONString, graphql_name='log')
    '''Array of JSON objects containing state for each stage of the job
    execution
    '''



class CleanupCollectorRecordInAccount(sgqlc.types.Type):
    '''Deletes an unassociated collector record in the account. This does
    not delete the CloudFormation stack and will not succeed if the
    collector is active and/or associated with a warehouse.
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''If the collector record was deleted'''



class CollectionBlockConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CollectionBlockEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class CollectionBlockEdge(sgqlc.types.Type):
    '''A Relay edge containing a `CollectionBlock` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CollectionBlock', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class CollectionDataSet(sgqlc.types.Type):
    '''Data set to collect data.'''
    __schema__ = schema
    __field_names__ = ('resource_id', 'project', 'dataset')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''The resource UUID of the dataset.'''

    project = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='project')
    '''Top-level object hierarchy e.g. database, catalog, etc.'''

    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    '''Intermediate object hierarchy e.g. schema, database, etc.'''



class CollectionDataSetConnection(sgqlc.types.relay.Connection):
    '''Datasets to collect data'''
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CollectionDataSetEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class CollectionDataSetEdge(sgqlc.types.Type):
    '''A Relay edge containing a `CollectionDataSet` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(CollectionDataSet, graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class CollectionProperties(sgqlc.types.Type):
    '''Collection infrastructure properties'''
    __schema__ = schema
    __field_names__ = ('cross_account_external_id', 'customer_account_token', 'code_bucket', 'code_version', 'platform_aws_account_id', 'docker_image_uri', 'platform_region_details')
    cross_account_external_id = sgqlc.types.Field(String, graphql_name='crossAccountExternalId')
    '''External id for cross account IAM role'''

    customer_account_token = sgqlc.types.Field(String, graphql_name='customerAccountToken')
    '''Customer account token (unique per data collector)'''

    code_bucket = sgqlc.types.Field(String, graphql_name='codeBucket')
    '''S3 bucket containing data collector code'''

    code_version = sgqlc.types.Field(String, graphql_name='codeVersion')
    '''Data collector code version'''

    platform_aws_account_id = sgqlc.types.Field(String, graphql_name='platformAwsAccountId')
    '''Monte Carlo AWS account id'''

    docker_image_uri = sgqlc.types.Field(String, graphql_name='dockerImageUri')
    '''URI of the docker image for the data colletor'''

    platform_region_details = sgqlc.types.Field('PlatformRegionProperties', graphql_name='platformRegionDetails')
    '''Region-specific properties'''



class ColumnLineage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('selected_column', 'lineage_sources')
    selected_column = sgqlc.types.Field(String, graphql_name='selectedColumn')
    '''The column on the destination table'''

    lineage_sources = sgqlc.types.Field(sgqlc.types.list_of('LineageSources'), graphql_name='lineageSources')
    '''Direct source lineage of the selected column'''



class ConfigureAirflowLogEvents(sgqlc.types.Type):
    '''Configure collection of Airflow logs via S3 events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class ConfigureMetadataEvents(sgqlc.types.Type):
    '''Configure collection of metadata via S3 events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class ConfigureQueryLogEvents(sgqlc.types.Type):
    '''Configure collection of query logs via S3 events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class Connection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'type', 'subtype', 'account', 'warehouse', 'bi_container', 'etl_container', 'job_types', 'credentials_s3_key', 'integration_gateway_credentials_key', 'data', 'created_on', 'updated_on', 'is_active', 'disabled_on', 'dbt_projects', 'connection_identifier', 'connection_identifiers', 'job_errors')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    type = sgqlc.types.Field(sgqlc.types.non_null(ConnectionModelType), graphql_name='type')

    subtype = sgqlc.types.Field(String, graphql_name='subtype')
    '''Subtype of a plugin connection'''

    account = sgqlc.types.Field(Account, graphql_name='account')

    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')

    bi_container = sgqlc.types.Field(BiContainer, graphql_name='biContainer')

    etl_container = sgqlc.types.Field('EtlContainer', graphql_name='etlContainer')

    job_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='jobTypes')

    credentials_s3_key = sgqlc.types.Field(String, graphql_name='credentialsS3Key')

    integration_gateway_credentials_key = sgqlc.types.Field(String, graphql_name='integrationGatewayCredentialsKey')

    data = sgqlc.types.Field(JSONString, graphql_name='data')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    updated_on = sgqlc.types.Field(DateTime, graphql_name='updatedOn')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')

    disabled_on = sgqlc.types.Field(DateTime, graphql_name='disabledOn')

    dbt_projects = sgqlc.types.Field(sgqlc.types.non_null('DbtProjectConnection'), graphql_name='dbtProjects', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''dbt connection

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    connection_identifier = sgqlc.types.Field('ConnectionIdentifier', graphql_name='connectionIdentifier')

    connection_identifiers = sgqlc.types.Field(sgqlc.types.list_of('ConnectionIdentifier'), graphql_name='connectionIdentifiers')

    job_errors = sgqlc.types.Field(sgqlc.types.list_of('JobError'), graphql_name='jobErrors')
    '''Errors related to the connection'''



class ConnectionIdentifier(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Connection credential key serving as an identifier'''

    value = sgqlc.types.Field(String, graphql_name='value')
    '''Value of connection identifier key'''



class ConnectionValidation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'message', 'data')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    '''Validation type'''

    message = sgqlc.types.Field(String, graphql_name='message')
    '''Message describing the validation'''

    data = sgqlc.types.Field('ConnectionValidationData', graphql_name='data')
    '''Metadata for the validation'''



class ConnectionValidationData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('database', 'table', 'error')
    database = sgqlc.types.Field(String, graphql_name='database')
    '''Database name'''

    table = sgqlc.types.Field(String, graphql_name='table')
    '''Table identifier'''

    error = sgqlc.types.Field(String, graphql_name='error')
    '''Error message'''



class CorrelationSamplingMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('time_axis', 'explanatory_field')
    time_axis = sgqlc.types.Field('TimeAxisMetadata', graphql_name='timeAxis')
    '''Field used as the time axis'''

    explanatory_field = sgqlc.types.Field('ExplanatoryFieldMetadata', graphql_name='explanatoryField')
    '''Field from which values are sampled'''



class CorrelationSamplingResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sample',)
    sample = sgqlc.types.Field(sgqlc.types.list_of('RcaPlotData'), graphql_name='sample')
    '''List of value distribution samples'''



class CreateAccessToken(sgqlc.types.Type):
    '''Generate an API Access Token and associate to user'''
    __schema__ = schema
    __field_names__ = ('access_token',)
    access_token = sgqlc.types.Field(AccessToken, graphql_name='accessToken')



class CreateCollectorRecord(sgqlc.types.Type):
    '''Create an additional collector record (with template) in the
    account.
    '''
    __schema__ = schema
    __field_names__ = ('dc',)
    dc = sgqlc.types.Field('DataCollector', graphql_name='dc')
    '''The data collector that was created'''



class CreateCustomMetricRule(sgqlc.types.Type):
    '''Deprecated, use CreateOrUpdateCustomMetricRule instead'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateCustomRule(sgqlc.types.Type):
    '''Deprecated, use CreateOrUpdateCustomRule instead'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateCustomUser(sgqlc.types.Type):
    '''Create a CustomUser'''
    __schema__ = schema
    __field_names__ = ('custom_user',)
    custom_user = sgqlc.types.Field('CustomUser', graphql_name='customUser')



class CreateDatabricksNotebookJob(sgqlc.types.Type):
    '''Create Databricks directory, upload the collection notebook and
    setup a job.
    '''
    __schema__ = schema
    __field_names__ = ('databricks',)
    databricks = sgqlc.types.Field('DatabricksJobResponse', graphql_name='databricks')
    '''The Databricks resources which were created.'''



class CreateDatabricksSecret(sgqlc.types.Type):
    '''Create Databricks scope and secret for an integration key.'''
    __schema__ = schema
    __field_names__ = ('success', 'scope_name', 'secret_name')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully.'''

    scope_name = sgqlc.types.Field(String, graphql_name='scopeName')
    '''Scope name that the secret was created with'''

    secret_name = sgqlc.types.Field(String, graphql_name='secretName')
    '''Name of the secret that was created'''



class CreateIntegrationKey(sgqlc.types.Type):
    '''Create an integration key'''
    __schema__ = schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field('IntegrationKey', graphql_name='key')
    '''Integration key id and secret (only available once).'''



class CreateJiraIntegration(sgqlc.types.Type):
    '''Create a Jira integration'''
    __schema__ = schema
    __field_names__ = ('jira_integration',)
    jira_integration = sgqlc.types.Field('JiraIntegrationOutput', graphql_name='jiraIntegration')
    '''The integration that was created'''



class CreateJiraTicketForIncident(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('jira_ticket',)
    jira_ticket = sgqlc.types.Field('JiraTicketOutput', graphql_name='jiraTicket')
    '''The created Jira ticket'''



class CreateOrUpdateAuthorizationGroup(sgqlc.types.Type):
    '''Create or update an authorization group.'''
    __schema__ = schema
    __field_names__ = ('authorization_group',)
    authorization_group = sgqlc.types.Field(AuthorizationGroupOutput, graphql_name='authorizationGroup')
    '''Created or updated authorization group.'''



class CreateOrUpdateCatalogObjectMetadata(sgqlc.types.Type):
    '''Create or update an asset's metadata'''
    __schema__ = schema
    __field_names__ = ('catalog_object_metadata',)
    catalog_object_metadata = sgqlc.types.Field('CatalogObjectMetadata', graphql_name='catalogObjectMetadata')
    '''Object metadata created or updated'''



class CreateOrUpdateCustomMetricRule(sgqlc.types.Type):
    '''Create or update a custom metric rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateOrUpdateCustomRule(sgqlc.types.Type):
    '''Create or update a custom rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateOrUpdateDataMaintenanceEntry(sgqlc.types.Type):
    '''Creates or updates a data maintenance period'''
    __schema__ = schema
    __field_names__ = ('entry',)
    entry = sgqlc.types.Field('DataMaintenanceEntry', graphql_name='entry')



class CreateOrUpdateDomain(sgqlc.types.Type):
    '''Create or update a domain'''
    __schema__ = schema
    __field_names__ = ('domain',)
    domain = sgqlc.types.Field('DomainOutput', graphql_name='domain')
    '''Created or updated domain'''



class CreateOrUpdateFieldQualityRule(sgqlc.types.Type):
    '''Create or update a field quality rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateOrUpdateFreshnessCustomRule(sgqlc.types.Type):
    '''Create or update a freshness custom rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateOrUpdateIncidentComment(sgqlc.types.Type):
    '''Creates or updates a comment on an incident'''
    __schema__ = schema
    __field_names__ = ('comment_event',)
    comment_event = sgqlc.types.Field('Event', graphql_name='commentEvent')
    '''The incident comment event.'''



class CreateOrUpdateLineageEdge(sgqlc.types.Type):
    '''Create or update a lineage edge'''
    __schema__ = schema
    __field_names__ = ('edge',)
    edge = sgqlc.types.Field('LineageGraphEdge', graphql_name='edge')



class CreateOrUpdateLineageNode(sgqlc.types.Type):
    '''Create or update a lineage node'''
    __schema__ = schema
    __field_names__ = ('node',)
    node = sgqlc.types.Field('LineageGraphNode', graphql_name='node')



class CreateOrUpdateLineageNodeBlockPattern(sgqlc.types.Type):
    '''Create or update a node block pattern'''
    __schema__ = schema
    __field_names__ = ('pattern',)
    pattern = sgqlc.types.Field('LineageNodeBlockPattern', graphql_name='pattern')



class CreateOrUpdateLineageNodeReplacementRule(sgqlc.types.Type):
    '''Create or update a node replacement rule'''
    __schema__ = schema
    __field_names__ = ('rule',)
    rule = sgqlc.types.Field('LineageNodeReplacementRule', graphql_name='rule')
    '''Replacement rule that was created or updated'''



class CreateOrUpdateMonitor(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('monitor',)
    monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='monitor')



class CreateOrUpdateMonitorLabel(sgqlc.types.Type):
    '''Create or update a monitor label'''
    __schema__ = schema
    __field_names__ = ('monitor_label',)
    monitor_label = sgqlc.types.Field('MonitorLabelObject', graphql_name='monitorLabel')
    '''The created monitor label'''



class CreateOrUpdateMonteCarloConfigTemplate(sgqlc.types.Type):
    '''Create or update a Monte Carlo Config Template'''
    __schema__ = schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('MonteCarloConfigTemplateUpdateResponse', graphql_name='response')
    '''Response'''



class CreateOrUpdateMonteCarloConfigTemplateAsync(sgqlc.types.Type):
    '''Create or update a Monte Carlo Config Template asynchronously'''
    __schema__ = schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('MonteCarloConfigTemplateUpdateAsyncResponse', graphql_name='response')
    '''Response'''



class CreateOrUpdateNotificationSetting(sgqlc.types.Type):
    '''Create or update a notification setting'''
    __schema__ = schema
    __field_names__ = ('notification_setting',)
    notification_setting = sgqlc.types.Field(AccountNotificationSetting, graphql_name='notificationSetting')
    '''Setting that was created or updated'''



class CreateOrUpdateObjectProperty(sgqlc.types.Type):
    '''Create or update properties (tags) for objects (e.g. tables,
    fields, etc.)
    '''
    __schema__ = schema
    __field_names__ = ('object_property',)
    object_property = sgqlc.types.Field('ObjectProperty', graphql_name='objectProperty')
    '''Property created or updated'''



class CreateOrUpdateRecipientName(sgqlc.types.Type):
    '''Create or update a recipient's custom name'''
    __schema__ = schema
    __field_names__ = ('recipient', 'name')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')

    name = sgqlc.types.Field(String, graphql_name='name')



class CreateOrUpdateResource(sgqlc.types.Type):
    '''Create or update a resource'''
    __schema__ = schema
    __field_names__ = ('resource',)
    resource = sgqlc.types.Field('Resource', graphql_name='resource')



class CreateOrUpdateSamlIdentityProvider(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')



class CreateOrUpdateServiceApiToken(sgqlc.types.Type):
    '''Generate a service API Access Token'''
    __schema__ = schema
    __field_names__ = ('access_token',)
    access_token = sgqlc.types.Field(AccessToken, graphql_name='accessToken')



class CreateOrUpdateUserSettings(sgqlc.types.Type):
    '''Create a new user-specific setting'''
    __schema__ = schema
    __field_names__ = ('user_settings',)
    user_settings = sgqlc.types.Field('UserSettings', graphql_name='userSettings')
    '''Response'''



class CreateOrUpdateVolumeRule(sgqlc.types.Type):
    '''Create or update a Volume Rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class CreateUnifiedUserAssignment(sgqlc.types.Type):
    '''Associate a UnifiedUser with a CatalogObject'''
    __schema__ = schema
    __field_names__ = ('unified_user_assignment',)
    unified_user_assignment = sgqlc.types.Field('UnifiedUserAssignment', graphql_name='unifiedUserAssignment')



class CustomRuleComparison(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('comparison_type', 'full_table_id', 'full_table_ids', 'field', 'metric', 'operator', 'threshold', 'baseline_agg_function', 'baseline_interval_minutes', 'is_threshold_relative', 'is_freshness_from_metadata', 'threshold_lookback_minutes', 'threshold_ref', 'min_buffer', 'max_buffer', 'number_of_agg_periods', 'data_collection_interval_minutes', 'rule_interval_minutes')
    comparison_type = sgqlc.types.Field(sgqlc.types.non_null(ComparisonType), graphql_name='comparisonType')
    '''Type of comparison'''

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    full_table_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fullTableIds')

    field = sgqlc.types.Field(String, graphql_name='field')

    metric = sgqlc.types.Field(String, graphql_name='metric')

    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    '''Comparison operator'''

    threshold = sgqlc.types.Field(Float, graphql_name='threshold')
    '''Threshold value'''

    baseline_agg_function = sgqlc.types.Field(AggregationFunction, graphql_name='baselineAggFunction')
    '''Function used to aggregate historical data points to calculate
    baseline
    '''

    baseline_interval_minutes = sgqlc.types.Field(Int, graphql_name='baselineIntervalMinutes')
    '''Time interval to aggregate over to calculate baseline.'''

    is_threshold_relative = sgqlc.types.Field(Boolean, graphql_name='isThresholdRelative')
    '''True, if threshold is a relative percentage change of baseline.
    False, if threshold is absolute change
    '''

    is_freshness_from_metadata = sgqlc.types.Field(Boolean, graphql_name='isFreshnessFromMetadata')
    '''True if freshness is calculated from metadata.'''

    threshold_lookback_minutes = sgqlc.types.Field(Int, graphql_name='thresholdLookbackMinutes')
    '''Time to look back for rules which compare current and past values.'''

    threshold_ref = sgqlc.types.Field(String, graphql_name='thresholdRef')
    '''Key used to retrieve the threshold values from external source'''

    min_buffer = sgqlc.types.Field('ThresholdModifier', graphql_name='minBuffer')
    '''The lower bound buffer to modify the alert threshold'''

    max_buffer = sgqlc.types.Field('ThresholdModifier', graphql_name='maxBuffer')
    '''The upper bound buffer to modify the alert threshold'''

    number_of_agg_periods = sgqlc.types.Field(Int, graphql_name='numberOfAggPeriods')
    '''The number of periods to use in the aggregate comparison for
    Volume Growth comparisons.
    '''

    data_collection_interval_minutes = sgqlc.types.Field(Int, graphql_name='dataCollectionIntervalMinutes')
    '''Time interval of data collection for the rule.'''

    rule_interval_minutes = sgqlc.types.Field(Int, graphql_name='ruleIntervalMinutes')
    '''Time interval for the rule evaluation.'''



class CustomRuleConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CustomRuleEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class CustomRuleEdge(sgqlc.types.Type):
    '''A Relay edge containing a `CustomRule` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CustomRule', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class CustomRuleExecutionAnalytics(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date', 'runs', 'passes', 'breaches')
    date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='date')
    '''Date for the analytics, if grouped by week/month it has the start
    of each grouping period
    '''

    runs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='runs')
    '''Number of runs'''

    passes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='passes')
    '''Number of passes'''

    breaches = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='breaches')
    '''Number of breaches'''



class CustomSQLOutputSample(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('columns', 'rows', 'sampling_disabled')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')

    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')

    sampling_disabled = sgqlc.types.Field(Boolean, graphql_name='samplingDisabled')



class CustomUserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('CustomUserEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class CustomUserEdge(sgqlc.types.Type):
    '''A Relay edge containing a `CustomUser` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('CustomUser', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DataAssetDashboard(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('data_sources_count', 'project_count', 'schema_count', 'table_count', 'view_count', 'external_table_count', 'wildcard_table_count')
    data_sources_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dataSourcesCount')
    '''The number of data sources monitored'''

    project_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='projectCount')
    '''The number of projects monitored'''

    schema_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='schemaCount')
    '''The number of schemas monitored'''

    table_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tableCount')
    '''The number of tables monitored'''

    view_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='viewCount')
    '''The number of views monitored'''

    external_table_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='externalTableCount')
    '''The number of external tables monitored'''

    wildcard_table_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='wildcardTableCount')
    '''The number of wildcard tables monitored'''



class DataCollector(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'account', 'uuid', 'api_gateway_id', 'kinesis_endpoint_id', 'cloudwatch_log_endpoint_id', 'cross_account_role_arn', 'stack_arn', 'customer_aws_account_id', 'customer_aws_region', 'template_launch_url', 'template_provider', 'template_variant', 'template_version', 'template_parameters', 'code_version', 'kinesis_access_role', 'active', 'last_updated', 'is_custom', 'oauth_credentials_s3_key', 'release_channel', 'warehouses', 'bi_container', 'etl_container', 'tableau_collector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    api_gateway_id = sgqlc.types.Field(String, graphql_name='apiGatewayId')

    kinesis_endpoint_id = sgqlc.types.Field(String, graphql_name='kinesisEndpointId')

    cloudwatch_log_endpoint_id = sgqlc.types.Field(String, graphql_name='cloudwatchLogEndpointId')

    cross_account_role_arn = sgqlc.types.Field(String, graphql_name='crossAccountRoleArn')

    stack_arn = sgqlc.types.Field(String, graphql_name='stackArn')

    customer_aws_account_id = sgqlc.types.Field(String, graphql_name='customerAwsAccountId')

    customer_aws_region = sgqlc.types.Field(String, graphql_name='customerAwsRegion')

    template_launch_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='templateLaunchUrl')

    template_provider = sgqlc.types.Field(String, graphql_name='templateProvider')

    template_variant = sgqlc.types.Field(String, graphql_name='templateVariant')

    template_version = sgqlc.types.Field(String, graphql_name='templateVersion')

    template_parameters = sgqlc.types.Field(JSONString, graphql_name='templateParameters')

    code_version = sgqlc.types.Field(String, graphql_name='codeVersion')

    kinesis_access_role = sgqlc.types.Field(String, graphql_name='kinesisAccessRole')

    active = sgqlc.types.Field(Boolean, graphql_name='active')

    last_updated = sgqlc.types.Field(DateTime, graphql_name='lastUpdated')

    is_custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCustom')

    oauth_credentials_s3_key = sgqlc.types.Field(String, graphql_name='oauthCredentialsS3Key')

    release_channel = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='releaseChannel')

    warehouses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Warehouse'))), graphql_name='warehouses')

    bi_container = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BiContainer))), graphql_name='biContainer')

    etl_container = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EtlContainer'))), graphql_name='etlContainer')

    tableau_collector = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableauAccount'))), graphql_name='tableauCollector')



class DataCollectorSchedule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'dc_id', 'resource_id', 'connection_id', 'project_id', 'output_stream', 'output_s3_bucket', 'last_job_id', 'job_type', 'schedule_type', 'created_on', 'last_run', 'interval_in_seconds', 'override', 'skip', 'is_deleted', 'friendly_name', 'notes', 'limits', 'interval_crontab', 'start_time', 'prev_execution_time', 'next_execution_time', 'timezone', 'is_dynamic_schedule_poller', 'min_interval_seconds', 'delete_reason', 'skip_reason', 'queued_at', 'metric_monitors')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    dc_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dcId')

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')

    connection_id = sgqlc.types.Field(UUID, graphql_name='connectionId')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    output_stream = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outputStream')

    output_s3_bucket = sgqlc.types.Field(String, graphql_name='outputS3Bucket')

    last_job_id = sgqlc.types.Field(String, graphql_name='lastJobId')

    job_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobType')

    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(DataCollectorScheduleModelScheduleType), graphql_name='scheduleType')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    last_run = sgqlc.types.Field(DateTime, graphql_name='lastRun')

    interval_in_seconds = sgqlc.types.Field(Int, graphql_name='intervalInSeconds')

    override = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='override')

    skip = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='skip')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')

    notes = sgqlc.types.Field(String, graphql_name='notes')

    limits = sgqlc.types.Field(JSONString, graphql_name='limits')

    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='intervalCrontab')

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')

    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')

    next_execution_time = sgqlc.types.Field(DateTime, graphql_name='nextExecutionTime')

    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')

    is_dynamic_schedule_poller = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDynamicSchedulePoller')
    '''If true, this schedule is for used to poll forfreshness to trigger
    dynamically scheduled jobs
    '''

    min_interval_seconds = sgqlc.types.Field(Int, graphql_name='minIntervalSeconds')
    '''Minimum interval between job executions. Used to preventa dynamic
    scheduled job from executing too frequently
    '''

    delete_reason = sgqlc.types.Field(DataCollectorScheduleModelDeleteReason, graphql_name='deleteReason')
    '''This field would only be set when the schedule is deleted because
    of there is no active data collector associated with it. In that
    case, the value of this field would be set as "no_collector"
    '''

    skip_reason = sgqlc.types.Field(DataCollectorScheduleModelSkipReason, graphql_name='skipReason')
    '''This field will be set when the schedule is set to skip=true froma
    manual action or when the connection is disabled.
    '''

    queued_at = sgqlc.types.Field(DateTime, graphql_name='queuedAt')
    '''The last time this schedule was added to the execution queue'''

    metric_monitors = sgqlc.types.Field(sgqlc.types.non_null('MetricMonitoringConnection'), graphql_name='metricMonitors', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''



class DataMaintenanceEntry(sgqlc.types.Type):
    '''Data maintenance entry'''
    __schema__ = schema
    __field_names__ = ('id', 'account_uuid', 'resource_uuid', 'database', 'dataset', 'full_table_id', 'maintenance_type', 'start_time', 'end_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')

    resource_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceUuid')

    database = sgqlc.types.Field(String, graphql_name='database')

    dataset = sgqlc.types.Field(String, graphql_name='dataset')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    maintenance_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maintenanceType')

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')

    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')



class DataPoint(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('timestamp', 'value')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')

    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')



class DataProfileField(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'type', 'min', 'max', 'p25', 'p50', 'p75', 'dist')
    name = sgqlc.types.Field(String, graphql_name='name')

    type = sgqlc.types.Field(String, graphql_name='type')

    min = sgqlc.types.Field(Float, graphql_name='min')

    max = sgqlc.types.Field(Float, graphql_name='max')

    p25 = sgqlc.types.Field(Float, graphql_name='p25')

    p50 = sgqlc.types.Field(Float, graphql_name='p50')

    p75 = sgqlc.types.Field(Float, graphql_name='p75')

    dist = sgqlc.types.Field(JSONString, graphql_name='dist')



class DataProfileResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sample_size', 'fields')
    sample_size = sgqlc.types.Field(Int, graphql_name='sampleSize')

    fields = sgqlc.types.Field(sgqlc.types.list_of(DataProfileField), graphql_name='fields')



class DataQualityWarningsRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'author', 'is_severe', 'is_active', 'warning_type', 'message', 'created_at', 'updated_at')
    name = sgqlc.types.Field(String, graphql_name='name')

    author = sgqlc.types.Field(AuthorRef, graphql_name='author')

    is_severe = sgqlc.types.Field(String, graphql_name='isSevere')

    is_active = sgqlc.types.Field(String, graphql_name='isActive')

    warning_type = sgqlc.types.Field(String, graphql_name='warningType')

    message = sgqlc.types.Field(String, graphql_name='message')

    created_at = sgqlc.types.Field(String, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')



class DatabricksClusterResponse(sgqlc.types.Type):
    '''Databricks cluster details.'''
    __schema__ = schema
    __field_names__ = ('cluster_id', 'state')
    cluster_id = sgqlc.types.Field(String, graphql_name='clusterId')
    '''ID of the cluster.'''

    state = sgqlc.types.Field(String, graphql_name='state')
    '''State of the cluster.'''



class DatabricksJobResponse(sgqlc.types.Type):
    '''Databricks job details.'''
    __schema__ = schema
    __field_names__ = ('workspace_job_id', 'workspace_job_name', 'workspace_notebook_path', 'notebook_source', 'notebook_version')
    workspace_job_id = sgqlc.types.Field(String, graphql_name='workspaceJobId')
    '''Generated Databricks job ID.'''

    workspace_job_name = sgqlc.types.Field(String, graphql_name='workspaceJobName')
    '''Generated Databricks job name.'''

    workspace_notebook_path = sgqlc.types.Field(String, graphql_name='workspaceNotebookPath')
    '''Uploaded Databricks notebook path.'''

    notebook_source = sgqlc.types.Field(String, graphql_name='notebookSource')
    '''Source location used to create the notebook.'''

    notebook_version = sgqlc.types.Field(String, graphql_name='notebookVersion')
    '''Version of the notebook created'''



class DatabricksNotebookLink(sgqlc.types.Type):
    '''Databricks notebook link details.'''
    __schema__ = schema
    __field_names__ = ('presigned_url', 'notebook_source')
    presigned_url = sgqlc.types.Field(String, graphql_name='presignedUrl')
    '''Temporary link containing the notebook.'''

    notebook_source = sgqlc.types.Field(String, graphql_name='notebookSource')
    '''Source location used to create the notebook link.'''



class DatabricksWarehouseResponse(sgqlc.types.Type):
    '''Databricks warehouse details.'''
    __schema__ = schema
    __field_names__ = ('warehouse_id', 'state')
    warehouse_id = sgqlc.types.Field(String, graphql_name='warehouseId')
    '''ID of the warehouse.'''

    state = sgqlc.types.Field(String, graphql_name='state')
    '''State of the warehouse.'''



class DatasetConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DatasetEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DatasetEdge(sgqlc.types.Type):
    '''A Relay edge containing a `Dataset` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Dataset', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DatasetEntity(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dataset_id',)
    dataset_id = sgqlc.types.Field(String, graphql_name='datasetId')
    '''Dataset ID'''



class DbtEdgeConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtEdgeEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DbtEdgeEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtEdge` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtEdge', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtJobConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtJobEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DbtJobEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtJob` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtJob', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtModelResult(sgqlc.types.Type):
    '''dbt model result'''
    __schema__ = schema
    __field_names__ = ('node_id', 'node_name', 'schema', 'database')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    '''dbt node id'''

    node_name = sgqlc.types.Field(String, graphql_name='nodeName')
    '''dbt node name'''

    schema = sgqlc.types.Field(String, graphql_name='schema')
    '''dbt schema name'''

    database = sgqlc.types.Field(String, graphql_name='database')
    '''dbt database name'''



class DbtModelResultsConnection(sgqlc.types.relay.Connection):
    '''dbt model results response'''
    __schema__ = schema
    __field_names__ = ('page_info', 'edges', 'edge_count', 'total_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtModelResultsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''

    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')
    '''Total number of edges returned (page count)'''

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    '''Total number of edges matching filter (total count)'''



class DbtModelResultsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtModelResults` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtRunResult', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtModelsConnection(sgqlc.types.relay.Connection):
    '''dbt models response'''
    __schema__ = schema
    __field_names__ = ('page_info', 'edges', 'edge_count', 'total_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtModelsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''

    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')
    '''Total number of edges returned (page count)'''

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    '''Total number of edges matching filter (total count)'''



class DbtModelsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtModels` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field(DbtModelResult, graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtNodeConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtNodeEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DbtNodeEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtNode` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtNode', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtProjectEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DbtProjectEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtProject` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtProject', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtRunConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtRunEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DbtRunEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtRun` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtRun', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtRunResult(sgqlc.types.Type):
    '''dbt run result'''
    __schema__ = schema
    __field_names__ = ('node_id', 'node_name', 'run_started_at', 'started_at', 'execution_time', 'status', 'run_uuid', 'mcon', 'job_name')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    '''dbt node id'''

    node_name = sgqlc.types.Field(String, graphql_name='nodeName')
    '''dbt node name'''

    run_started_at = sgqlc.types.Field(DateTime, graphql_name='runStartedAt')
    '''Time dbt run started'''

    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    '''Time dbt node execution started'''

    execution_time = sgqlc.types.Field(Float, graphql_name='executionTime')
    '''Total dbt node execution time (in seconds)'''

    status = sgqlc.types.Field(String, graphql_name='status')
    '''Execution status'''

    run_uuid = sgqlc.types.Field(UUID, graphql_name='runUuid')
    '''Internal id of dbt run'''

    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''MCON of associated table'''

    job_name = sgqlc.types.Field(String, graphql_name='jobName')
    '''Dbt job name'''



class DbtRunStepConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtRunStepEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DbtRunStepEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtRunStep` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtRunStep', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtTestResultsConnection(sgqlc.types.relay.Connection):
    '''dbt test results response'''
    __schema__ = schema
    __field_names__ = ('page_info', 'edges', 'edge_count', 'total_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DbtTestResultsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''

    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')
    '''Total number of edges returned (page count)'''

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    '''Total number of edges matching filter (total count)'''



class DbtTestResultsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DbtTestResults` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DbtTestRunResult', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DbtTestRunResult(sgqlc.types.Type):
    '''dbt test run result'''
    __schema__ = schema
    __field_names__ = ('node_id', 'node_name', 'run_started_at', 'started_at', 'execution_time', 'status', 'run_uuid', 'mcon', 'job_name', 'model_id', 'model_name')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    '''dbt node id'''

    node_name = sgqlc.types.Field(String, graphql_name='nodeName')
    '''dbt node name'''

    run_started_at = sgqlc.types.Field(DateTime, graphql_name='runStartedAt')
    '''Time dbt run started'''

    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    '''Time dbt node execution started'''

    execution_time = sgqlc.types.Field(Float, graphql_name='executionTime')
    '''Total dbt node execution time (in seconds)'''

    status = sgqlc.types.Field(String, graphql_name='status')
    '''Execution status'''

    run_uuid = sgqlc.types.Field(UUID, graphql_name='runUuid')
    '''Internal id of dbt run'''

    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''MCON of associated table'''

    job_name = sgqlc.types.Field(String, graphql_name='jobName')
    '''Dbt job name'''

    model_id = sgqlc.types.Field(String, graphql_name='modelId')
    '''Id of associated dbt model'''

    model_name = sgqlc.types.Field(String, graphql_name='modelName')
    '''Name of associated dbt model'''



class DcPingResponse(sgqlc.types.Type):
    '''Describes the result of pinging a data collector.'''
    __schema__ = schema
    __field_names__ = ('dc_id', 'trace_id')
    dc_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='dcId')
    '''The UUID identifying the data collector pinged.'''

    trace_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='traceId')
    '''A unique identifier for correlating the data collector ping.'''



class DeauthorizeSlackAppMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteAccessToken(sgqlc.types.Type):
    '''Delete an API Access Token by ID'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''If the token was successfully deleted'''



class DeleteAuthorizationGroup(sgqlc.types.Type):
    '''Delete an authorization group'''
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')
    '''Number of groups deleted.'''



class DeleteCatalogObjectMetadata(sgqlc.types.Type):
    '''Delete metadata for an asset'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteCustomRule(sgqlc.types.Type):
    '''Delete a custom rule'''
    __schema__ = schema
    __field_names__ = ('uuid',)
    uuid = sgqlc.types.Field(UUID, graphql_name='uuid')



class DeleteDataMaintenanceEntry(sgqlc.types.Type):
    '''Delete a data maintenance window'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteDomain(sgqlc.types.Type):
    '''Delete a domain'''
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')
    '''Number of domains deleted'''



class DeleteEventOnboardingData(sgqlc.types.Type):
    '''Delete stored event onboarding configuration'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the event onboarding data was deleted
    successfully
    '''



class DeleteGithubInstallation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Boolean, graphql_name='deleted')
    '''True if deleting the installation was successful'''



class DeleteIncidentComment(sgqlc.types.Type):
    '''Deletes an incident's comment'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteIntegrationKey(sgqlc.types.Type):
    '''Delete an integration key'''
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Boolean, graphql_name='deleted')
    '''True if the key was deleted, false otherwise'''



class DeleteJiraIntegration(sgqlc.types.Type):
    '''Delete a Jira integration'''
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Boolean, graphql_name='deleted')



class DeleteLineageNode(sgqlc.types.Type):
    '''Delete a lineage node and any lineage edges connected to it.'''
    __schema__ = schema
    __field_names__ = ('objects_deleted', 'nodes_deleted', 'edges_deleted')
    objects_deleted = sgqlc.types.Field(Int, graphql_name='objectsDeleted')
    '''Total number of objects (nodes + edges) deleted'''

    nodes_deleted = sgqlc.types.Field(Int, graphql_name='nodesDeleted')
    '''Total number of nodes deleted'''

    edges_deleted = sgqlc.types.Field(Int, graphql_name='edgesDeleted')
    '''Total number of edges deleted'''



class DeleteLineageNodeBlockPattern(sgqlc.types.Type):
    '''Delete a lineage node block pattern.'''
    __schema__ = schema
    __field_names__ = ('pattern',)
    pattern = sgqlc.types.Field('LineageNodeBlockPattern', graphql_name='pattern')



class DeleteLineageNodeReplacementRule(sgqlc.types.Type):
    '''Delete a lineage node replacement rule'''
    __schema__ = schema
    __field_names__ = ('rule',)
    rule = sgqlc.types.Field('LineageNodeReplacementRule', graphql_name='rule')



class DeleteMonitor(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteMonitorLabel(sgqlc.types.Type):
    '''Delete a monitor label'''
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Boolean, graphql_name='deleted')
    '''True if the monitor label was deleted'''



class DeleteMonteCarloConfigTemplate(sgqlc.types.Type):
    '''Delete a Monte Carlo Config Template'''
    __schema__ = schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('MonteCarloConfigTemplateDeleteResponse', graphql_name='response')
    '''Response'''



class DeleteNotificationSetting(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('deleted',)
    deleted = sgqlc.types.Field(Int, graphql_name='deleted')



class DeleteObjectProperty(sgqlc.types.Type):
    '''Delete properties (tags) for objects (e.g. tables, fields, etc.)'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteRecipientName(sgqlc.types.Type):
    '''Create or update a recipient's custom name'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteSamlIdentityProvider(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')



class DeleteUnifiedUserAssignment(sgqlc.types.Type):
    '''Associate a UnifiedUser with a CatalogObject'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DeleteUserInvite(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class DeltaLog(sgqlc.types.Type):
    '''Represents a single entry in the table's Delta History'''
    __schema__ = schema
    __field_names__ = ('version', 'timestamp', 'user_name', 'operation', 'operation_metrics')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')
    '''Table version generated by the operation.'''

    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')
    '''When this version was committed.'''

    user_name = sgqlc.types.Field(String, graphql_name='userName')
    '''Name of the user that ran the operation.'''

    operation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='operation')
    '''Name of the operation.'''

    operation_metrics = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='operationMetrics')
    '''Metrics of the operation (for example, number of rows and files
    modified).
    '''



class DeltaLogConnection(sgqlc.types.relay.Connection):
    '''Describes a page of DeltaLog results'''
    __schema__ = schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DeltaLogConnectionEdge')), graphql_name='edges')

    page_info = sgqlc.types.Field(sgqlc.types.non_null('DeltaLogConnectionPageInfo'), graphql_name='pageInfo')
    '''Holds details of the current results page'''



class DeltaLogConnectionEdge(sgqlc.types.Type):
    '''Describes each item in a paginated list of Delta Log results'''
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A consistent identifier for each operation in the results list'''

    node = sgqlc.types.Field(sgqlc.types.non_null(DeltaLog), graphql_name='node')
    '''The Delta Log object representing a single operation'''



class DeltaLogConnectionPageInfo(sgqlc.types.Type):
    '''Information about the current page of Delta Log results'''
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    '''The last edge's identifier, can be passed as after argument'''

    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    '''Whether there are more results to be fetched'''



class DerivedTablePartialLineage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'columns', 'source_column_used_as_non_selected', 'display_name')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Derived destination table's mcon'''

    columns = sgqlc.types.Field(sgqlc.types.list_of('SourceColumn'), graphql_name='columns')
    '''A list of columns in the derived table, that are derived from some
    source
    '''

    source_column_used_as_non_selected = sgqlc.types.Field(Boolean, graphql_name='sourceColumnUsedAsNonSelected')
    '''Indicates whether the input source column is used as a non
    selected column in the query that derives the current table
    '''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Display name for BI tables'''



class DerivedTablesLineageResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'source_column', 'destinations', 'is_last_page', 'cursor')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Source table mcon'''

    source_column = sgqlc.types.Field(String, graphql_name='sourceColumn')
    '''Source column'''

    destinations = sgqlc.types.Field(sgqlc.types.list_of(DerivedTablePartialLineage), graphql_name='destinations')
    '''Derived tables and their columns that are influenced by the source
    col
    '''

    is_last_page = sgqlc.types.Field(Boolean, graphql_name='isLastPage')
    '''Indicates whether this response the the last page of response'''

    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    '''Cursor for getting the next page of results'''



class DimensionLabel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('timestamp', 'label', 'value')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')

    label = sgqlc.types.Field(String, graphql_name='label')

    value = sgqlc.types.Field(Float, graphql_name='value')



class DimensionLabelList(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('timestamp', 'label', 'values')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')

    label = sgqlc.types.Field(String, graphql_name='label')

    values = sgqlc.types.Field(sgqlc.types.list_of('DimensionLabelListItem'), graphql_name='values')



class DimensionLabelListItem(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('measurement_timestamp', 'value')
    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')

    value = sgqlc.types.Field(Float, graphql_name='value')



class DimensionTracking(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'mn_cnt', 'mx_cnt', 'mn_fld', 'mn_fq', 'mx_fq', 'reason')
    value = sgqlc.types.Field(String, graphql_name='value')
    '''Value name'''

    mn_cnt = sgqlc.types.Field(Int, graphql_name='mnCnt')
    '''Minimum count threshold'''

    mx_cnt = sgqlc.types.Field(Int, graphql_name='mxCnt')
    '''Maximum count threshold'''

    mn_fld = sgqlc.types.Field(Float, graphql_name='mnFld')
    '''Minimum field size required to trigger anomaly'''

    mn_fq = sgqlc.types.Field(Float, graphql_name='mnFq')
    '''Minimum relative frequency threshold'''

    mx_fq = sgqlc.types.Field(Float, graphql_name='mxFq')
    '''Maximum relative frequency threshold'''

    reason = sgqlc.types.Field(String, graphql_name='reason')
    '''Reason for not providing DT thresholds'''



class DimensionTrackingSuggestionsConnection(sgqlc.types.relay.Connection):
    '''Suggestions for creating dimension tracking monitors'''
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DimensionTrackingSuggestionsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DimensionTrackingSuggestionsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DimensionTrackingSuggestions` and its
    cursor.
    '''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DimensionTrackingSuggestions', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DirectedGraph(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('vertices', 'edges')
    vertices = sgqlc.types.Field(String, graphql_name='vertices')

    edges = sgqlc.types.Field(String, graphql_name='edges')



class DisableAirflowLogEvents(sgqlc.types.Type):
    '''Disable collection of Airflow logs via S3 events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DisableMetadataEvents(sgqlc.types.Type):
    '''Disable collection of metadata via S3 events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DisableQueryLogEvents(sgqlc.types.Type):
    '''Disable collection of query logs via S3 events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class DisableUser(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field('User', graphql_name='user')



class DisplayableFieldValueType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'value_as_string', 'value_as_string_array')
    field_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fieldName')

    value_as_string = sgqlc.types.Field(String, graphql_name='valueAsString')

    value_as_string_array = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='valueAsStringArray')



class DomainOutput(sgqlc.types.Type):
    '''Domain configuration'''
    __schema__ = schema
    __field_names__ = ('uuid', 'name', 'description', 'created_by_email', 'assignments', 'tags')
    uuid = sgqlc.types.Field(UUID, graphql_name='uuid')
    '''Domain UUID'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Domain name'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Domain description'''

    created_by_email = sgqlc.types.Field(String, graphql_name='createdByEmail')
    '''Domain created by email address'''

    assignments = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='assignments')
    '''Objects assigned to domain (as MCONs)'''

    tags = sgqlc.types.Field(sgqlc.types.list_of('TagKeyValuePairOutput'), graphql_name='tags')
    '''Filter by tag key/value pairs for tables.'''



class DomainRestrictionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('DomainRestrictionEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class DomainRestrictionEdge(sgqlc.types.Type):
    '''A Relay edge containing a `DomainRestriction` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('DomainRestriction', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class DownstreamBI(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node_id', 'full_table_id', 'downstream_bi')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    downstream_bi = sgqlc.types.Field(sgqlc.types.list_of(BiLineage), graphql_name='downstreamBi')



class DownstreamImpactRadiusSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_users_affected', 'total_reports_affected')
    total_users_affected = sgqlc.types.Field(Int, graphql_name='totalUsersAffected')
    '''Number of users affected'''

    total_reports_affected = sgqlc.types.Field(Int, graphql_name='totalReportsAffected')
    '''Number of reports affected'''



class DownstreamReport(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'display_name', 'report_type', 'object_id', 'owner_id', 'is_custom', 'importance_score')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''MCON of the report.'''

    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    '''Display name of the report'''

    report_type = sgqlc.types.Field(String, graphql_name='reportType')
    '''Type of the report'''

    object_id = sgqlc.types.Field(String, graphql_name='objectId')
    '''ID of the object'''

    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')
    '''ID of the owner of this object'''

    is_custom = sgqlc.types.Field(Boolean, graphql_name='isCustom')
    '''Indicates whether this is a custom lineage node (created by a
    user)
    '''

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')
    '''Importance score of the report'''



class DownstreamReportOwners(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('owner_ids', 'has_next_page', 'limit', 'offset')
    owner_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='ownerIds')
    '''Owner ID of a BI report'''

    has_next_page = sgqlc.types.Field(Boolean, graphql_name='hasNextPage')
    '''Whether more pages of results exist. Used for pagination.'''

    limit = sgqlc.types.Field(Int, graphql_name='limit')
    '''Limit results returned'''

    offset = sgqlc.types.Field(Int, graphql_name='offset')
    '''Offset when paging'''



class DownstreamReportTypes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('downstream_report_types',)
    downstream_report_types = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='downstreamReportTypes')
    '''List of distinct downstream report types.'''



class DownstreamReports(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('downstream_reports', 'limit', 'offset', 'has_next_page')
    downstream_reports = sgqlc.types.Field(sgqlc.types.list_of(DownstreamReport), graphql_name='downstreamReports')
    '''List of downstream reports'''

    limit = sgqlc.types.Field(Int, graphql_name='limit')
    '''Limit results returned'''

    offset = sgqlc.types.Field(Int, graphql_name='offset')
    '''Offset when paging'''

    has_next_page = sgqlc.types.Field(Boolean, graphql_name='hasNextPage')
    '''Whether more pages of results exist. Used for pagination.'''



class Dynamic(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('min', 'max', 'reason')
    min = sgqlc.types.Field(Float, graphql_name='min')
    '''Minimum threshold'''

    max = sgqlc.types.Field(Float, graphql_name='max')
    '''Maximum threshold'''

    reason = sgqlc.types.Field(String, graphql_name='reason')
    '''Explanation if min/max is missing'''



class EtlContainer(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'account', 'uuid', 'data_collector', 'type', 'name', 'connections')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    data_collector = sgqlc.types.Field(DataCollector, graphql_name='dataCollector')

    type = sgqlc.types.Field(EtlType, graphql_name='type')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''A friendly name for this etl container'''

    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Connection))), graphql_name='connections')



class EventCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventCommentEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class EventCommentEdge(sgqlc.types.Type):
    '''A Relay edge containing a `EventComment` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('EventComment', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class EventConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('EventEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class EventEdge(sgqlc.types.Type):
    '''A Relay edge containing a `Event` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Event', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class EventMutingRule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'warehouse', 'rule_type', 'rule', 'is_active', 'created_time', 'last_update_time', 'event_types')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    warehouse = sgqlc.types.Field(sgqlc.types.non_null('Warehouse'), graphql_name='warehouse')

    rule_type = sgqlc.types.Field(sgqlc.types.non_null(EventMutingRuleModelRuleType), graphql_name='ruleType')

    rule = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rule')

    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    last_update_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastUpdateTime')

    event_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='eventTypes')
    '''List of event types to mute. Mutes all if empty.'''



class EventOnbardingConfig(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('account_uuid', 'config')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')

    config = sgqlc.types.Field(JSONString, graphql_name='config')
    '''Onboarding Config meant to be shared between customers and MC'''



class EventRcaStatus(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'event', 'rca', 'set_ts', 'reason', 'rca_module', 'rca_job_uuid')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    event = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='event')

    rca = sgqlc.types.Field('RcaJob', graphql_name='rca')

    set_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='setTs')

    reason = sgqlc.types.Field(sgqlc.types.non_null(EventRcaStatusModelReason), graphql_name='reason')
    '''Reason why RCA was assigned a specific status.'''

    rca_module = sgqlc.types.Field(String, graphql_name='rcaModule')
    '''The RCA module that detected the failure reason'''

    rca_job_uuid = sgqlc.types.Field(UUID, graphql_name='rcaJobUuid')
    '''UUID of the RCA job associated with the status'''



class EventRcaStatusModelType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'event', 'rca', 'set_ts', 'reason', 'rca_module')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    event = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='event')

    rca = sgqlc.types.Field('RcaJob', graphql_name='rca')

    set_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='setTs')

    reason = sgqlc.types.Field(sgqlc.types.non_null(EventRcaStatusModelReason), graphql_name='reason')
    '''Reason why RCA was assigned a specific status.'''

    rca_module = sgqlc.types.Field(String, graphql_name='rcaModule')
    '''The RCA module that detected the failure reason'''



class EventStateSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('open', 'false_positive', 'no_action_required', 'notified', 'resolved', 'user_resolved', 'system_resolved', 'muted', 'stale')
    open = sgqlc.types.Field(Int, graphql_name='open')

    false_positive = sgqlc.types.Field(Int, graphql_name='falsePositive')

    no_action_required = sgqlc.types.Field(Int, graphql_name='noActionRequired')

    notified = sgqlc.types.Field(Int, graphql_name='notified')

    resolved = sgqlc.types.Field(Int, graphql_name='resolved')

    user_resolved = sgqlc.types.Field(Int, graphql_name='userResolved')

    system_resolved = sgqlc.types.Field(Int, graphql_name='systemResolved')

    muted = sgqlc.types.Field(Int, graphql_name='muted')

    stale = sgqlc.types.Field(Int, graphql_name='stale')



class EventTopology(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'upstream')
    event = sgqlc.types.Field('Event', graphql_name='event')
    '''Reference to an event'''

    upstream = sgqlc.types.Field(sgqlc.types.list_of('Event'), graphql_name='upstream')
    '''List of events immediately upstream'''



class EventTypeSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('schema_change', 'fresh_anom', 'unchanged_size_anom', 'json_schema_change', 'delete_table', 'size_anom', 'size_diff', 'metric_anom', 'custom_rule_anom', 'dist_anom', 'query_runtime_anom', 'dbt_model_error', 'dbt_test_failure')
    schema_change = sgqlc.types.Field(Int, graphql_name='schemaChange')

    fresh_anom = sgqlc.types.Field(Int, graphql_name='freshAnom')

    unchanged_size_anom = sgqlc.types.Field(Int, graphql_name='unchangedSizeAnom')

    json_schema_change = sgqlc.types.Field(Int, graphql_name='jsonSchemaChange')

    delete_table = sgqlc.types.Field(Int, graphql_name='deleteTable')

    size_anom = sgqlc.types.Field(Int, graphql_name='sizeAnom')

    size_diff = sgqlc.types.Field(Int, graphql_name='sizeDiff')

    metric_anom = sgqlc.types.Field(Int, graphql_name='metricAnom')

    custom_rule_anom = sgqlc.types.Field(Int, graphql_name='customRuleAnom')

    dist_anom = sgqlc.types.Field(Int, graphql_name='distAnom')

    query_runtime_anom = sgqlc.types.Field(Int, graphql_name='queryRuntimeAnom')

    dbt_model_error = sgqlc.types.Field(Int, graphql_name='dbtModelError')

    dbt_test_failure = sgqlc.types.Field(Int, graphql_name='dbtTestFailure')



class ExecDashboardDataColumn(sgqlc.types.Type):
    '''A column for a table.'''
    __schema__ = schema
    __field_names__ = ('name', 'type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name associated with the column, can be used to identify it.'''

    type = sgqlc.types.Field(sgqlc.types.non_null(DataColumnTypes), graphql_name='type')
    '''Data type of the values included in the column.'''



class ExecDashboardDataPoint(sgqlc.types.Type):
    '''A single measure/data point for a metric.'''
    __schema__ = schema
    __field_names__ = ('value', 'period_start', 'dimension', 'children')
    value = sgqlc.types.Field(Float, graphql_name='value')
    '''Value of data point.'''

    period_start = sgqlc.types.Field(DateTime, graphql_name='periodStart')
    '''Start of period for data point, for time series.'''

    dimension = sgqlc.types.Field(String, graphql_name='dimension')
    '''Dimension of data point, for category series.'''

    children = sgqlc.types.Field(sgqlc.types.list_of('ExecDashboardDataPoint'), graphql_name='children')



class ExecDashboardDataRow(sgqlc.types.Type):
    '''A row with values for each column.'''
    __schema__ = schema
    __field_names__ = ('values',)
    values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='values')
    '''Values for each column in the row.'''



class ExecDashboardMetric(sgqlc.types.Type):
    '''A set of data points (or single data point) that is a named
    measure.
    '''
    __schema__ = schema
    __field_names__ = ('metric', 'data_points', 'has_error')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ExecDashboardMetrics), graphql_name='metric')
    '''Metric identifier.'''

    data_points = sgqlc.types.Field(sgqlc.types.list_of(ExecDashboardDataPoint), graphql_name='dataPoints')
    '''Data points. May only be one for single-value metrics.'''

    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')
    '''If true, indicates an error occurred trying to get metric data.'''



class ExecDashboardTable(sgqlc.types.Type):
    '''A table with measured values.'''
    __schema__ = schema
    __field_names__ = ('table', 'data_columns', 'data_rows', 'is_visible', 'has_error')
    table = sgqlc.types.Field(sgqlc.types.non_null(ExecDashboardTables), graphql_name='table')
    '''Table identifier.'''

    data_columns = sgqlc.types.Field(sgqlc.types.list_of(ExecDashboardDataColumn), graphql_name='dataColumns')
    '''Column definitions.'''

    data_rows = sgqlc.types.Field(sgqlc.types.list_of(ExecDashboardDataRow), graphql_name='dataRows')
    '''Row values.'''

    is_visible = sgqlc.types.Field(Boolean, graphql_name='isVisible')
    '''If true, indicates that the table must be shown, otherwise it
    should be hidden.
    '''

    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')
    '''If true, indicates an error occurred trying to get metric data.'''



class ExplanatoryFieldMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('candidates',)
    candidates = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='candidates')
    '''Fields which can be used as explanatory'''



class FacetEntry(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('key', 'count')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Key of facet entry'''

    count = sgqlc.types.Field(Int, graphql_name='count')
    '''Number of documents that contain key'''



class FacetResultType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'display_name', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Field value'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Display name'''

    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    '''Count'''



class FacetResults(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('facet_type', 'entries')
    facet_type = sgqlc.types.Field(FacetType, graphql_name='facetType')
    '''Facet type'''

    entries = sgqlc.types.Field(sgqlc.types.list_of(FacetEntry), graphql_name='entries')
    '''Facet entries'''



class FieldDistRcaData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('time_field', 'anom_time', 'explanatory_field', 'val')
    time_field = sgqlc.types.Field(String, graphql_name='timeField')
    '''Table field which serves as a time axis'''

    anom_time = sgqlc.types.Field(DateTime, graphql_name='anomTime')
    '''Time when the anomaly occurred'''

    explanatory_field = sgqlc.types.Field(String, graphql_name='explanatoryField')
    '''Table field containing the explanatory value'''

    val = sgqlc.types.Field(String, graphql_name='val')
    '''Explanatory value used in the analysis'''



class FieldDistRcaResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rca', 'plot_data', 'low_card_fields_wo_rca', 'available_fields')
    rca = sgqlc.types.Field(sgqlc.types.list_of(FieldDistRcaData), graphql_name='rca')

    plot_data = sgqlc.types.Field(sgqlc.types.list_of('RcaPlotData'), graphql_name='plotData', args=sgqlc.types.ArgDict((
        ('field_name', sgqlc.types.Arg(String, graphql_name='fieldName', default=None)),
))
    )
    '''Arguments:

    * `field_name` (`String`)None
    '''

    low_card_fields_wo_rca = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lowCardFieldsWoRca')

    available_fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='availableFields')



class FieldDownstreamBi(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('bi_account_id', 'bi_identifier', 'bi_name', 'bi_type', 'bi_node_id', 'last_seen')
    bi_account_id = sgqlc.types.Field(String, graphql_name='biAccountId')

    bi_identifier = sgqlc.types.Field(String, graphql_name='biIdentifier')

    bi_name = sgqlc.types.Field(String, graphql_name='biName')

    bi_type = sgqlc.types.Field(String, graphql_name='biType')

    bi_node_id = sgqlc.types.Field(String, graphql_name='biNodeId')

    last_seen = sgqlc.types.Field(DateTime, graphql_name='lastSeen')



class FieldHealth(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('lower', 'upper', 'reason')
    lower = sgqlc.types.Field(Float, graphql_name='lower')
    '''Field health lower threshold'''

    upper = sgqlc.types.Field(Float, graphql_name='upper')
    '''Field health upper threshold'''

    reason = sgqlc.types.Field(String, graphql_name='reason')
    '''Reason for not providing FH thresholds'''



class FieldHealthSampling(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('columns', 'rows', 'sampling_disabled', 'normal_records_query', 'anomalous_records_query')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')

    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')

    sampling_disabled = sgqlc.types.Field(Boolean, graphql_name='samplingDisabled')

    normal_records_query = sgqlc.types.Field(String, graphql_name='normalRecordsQuery')
    '''This is null for summary statistics such as mean, min, max, and
    percentiles
    '''

    anomalous_records_query = sgqlc.types.Field(String, graphql_name='anomalousRecordsQuery')



class FieldHealthSuggestionsConnection(sgqlc.types.relay.Connection):
    '''Suggestions for creating field health monitors'''
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FieldHealthSuggestionsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class FieldHealthSuggestionsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `FieldHealthSuggestions` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('FieldHealthSuggestions', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class FieldMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_type', 'table')
    field_type = sgqlc.types.Field(String, graphql_name='fieldType')

    table = sgqlc.types.Field('TableRef', graphql_name='table')



class FieldMetricFilterOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'operator', 'value')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field to filter by'''

    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    '''Operator to filter field by'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Value to filter field by'''



class FieldMetricOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('table_mcon', 'table_mcons', 'field_name', 'field_names', 'metric_type', 'value_list', 'filters')
    table_mcon = sgqlc.types.Field(String, graphql_name='tableMcon')
    '''MCON of the table the metric is based on'''

    table_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tableMcons')
    '''MCONs of the table the metric is based on'''

    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Name of the field the metric is based on'''

    field_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fieldNames')
    '''Name of the fields the metric is based on'''

    metric_type = sgqlc.types.Field(sgqlc.types.non_null(FieldMetricType), graphql_name='metricType')
    '''Type of metric to compute'''

    value_list = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='valueList')
    '''Values for metrics that check for cardinality'''

    filters = sgqlc.types.Field(sgqlc.types.list_of(FieldMetricFilterOutput), graphql_name='filters')
    '''Filters for which rows the metric is computed over'''



class FieldMetricQuery(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sql_query',)
    sql_query = sgqlc.types.Field(String, graphql_name='sqlQuery')
    '''SQL query for the metric'''



class FieldQuery(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sql_query',)
    sql_query = sgqlc.types.Field(String, graphql_name='sqlQuery')
    '''SQL query'''



class FieldQueryFilterOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'operator', 'value')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field to filter by'''

    operator = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleComparisonOperator), graphql_name='operator')
    '''Operator to filter field by'''

    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    '''Value to filter field by'''



class FieldQueryParametersOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('table_mcons', 'field_names', 'query_type', 'value_list', 'filters')
    table_mcons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='tableMcons')
    '''MCONs of the table the query is based on'''

    field_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fieldNames')
    '''Name of the fields the query is based on'''

    query_type = sgqlc.types.Field(sgqlc.types.non_null(FieldQueryType), graphql_name='queryType')
    '''Type of query'''

    value_list = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='valueList')
    '''Values for queries that check for cardinality'''

    filters = sgqlc.types.Field(sgqlc.types.list_of(FieldQueryFilterOutput), graphql_name='filters')
    '''Filters for which rows the query is computed over'''



class FieldValueCorrelation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'value', 'norm_rate', 'anom_rate')
    field = sgqlc.types.Field(String, graphql_name='field')

    value = sgqlc.types.Field(String, graphql_name='value')

    norm_rate = sgqlc.types.Field(Float, graphql_name='normRate')

    anom_rate = sgqlc.types.Field(Float, graphql_name='anomRate')



class FivetranConnectorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FivetranConnectorEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class FivetranConnectorEdge(sgqlc.types.Type):
    '''A Relay edge containing a `FivetranConnector` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('FivetranConnector', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class FivetranDestinationConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('FivetranDestinationEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class FivetranDestinationEdge(sgqlc.types.Type):
    '''A Relay edge containing a `FivetranDestination` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('FivetranDestination', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class FlattenedLineageGraphEdges(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'directly_connected_mcons')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''Monte Carlo full identifier for an entity'''

    directly_connected_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='directlyConnectedMcons')
    '''MCONs of nodes directly connected to the entity'''



class Freshness(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('status', 'expected', 'breach', 'reason', 'last_update', 'detector_threshold', 'threshold_low', 'threshold_medium', 'threshold_high')
    status = sgqlc.types.Field(DetectorStatus, graphql_name='status')
    '''Status of the freshness detector'''

    expected = sgqlc.types.Field(Float, graphql_name='expected')
    '''Time delta of next expected update (in seconds)'''

    breach = sgqlc.types.Field(Float, graphql_name='breach')
    '''Time delta when a delay is considered a breach (in seconds)'''

    reason = sgqlc.types.Field(String, graphql_name='reason')
    '''Explanation if expected and/or breach is missing'''

    last_update = sgqlc.types.Field(DateTime, graphql_name='lastUpdate')
    '''Last time the table was updated'''

    detector_threshold = sgqlc.types.Field(Float, graphql_name='detectorThreshold')
    '''The threshold calculated by the detector model'''

    threshold_low = sgqlc.types.Field(Float, graphql_name='thresholdLow')
    '''The "low" level threshold calculated by the detector model'''

    threshold_medium = sgqlc.types.Field(Float, graphql_name='thresholdMedium')
    '''The "medium" level threshold calculated by the detector model'''

    threshold_high = sgqlc.types.Field(Float, graphql_name='thresholdHigh')
    '''The "high" level threshold calculated by the detector model'''



class FreshnessCycleData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('periodic', 'usual_update_cycle_hours', 'maximal_update_cycle_hours')
    periodic = sgqlc.types.Field(Boolean, graphql_name='periodic')
    '''Whether or not this table is updated periodically'''

    usual_update_cycle_hours = sgqlc.types.Field(Int, graphql_name='usualUpdateCycleHours')
    '''The median update in hours'''

    maximal_update_cycle_hours = sgqlc.types.Field(Int, graphql_name='maximalUpdateCycleHours')
    '''Time delta when a delay is considered a breach (in seconds)'''



class GenerateCollectorTemplate(sgqlc.types.Type):
    '''Generate a data collector template (uploaded to S3)'''
    __schema__ = schema
    __field_names__ = ('dc',)
    dc = sgqlc.types.Field(DataCollector, graphql_name='dc')
    '''The data collector that was created or updated'''



class GithubAppInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('install_link', 'installations')
    install_link = sgqlc.types.Field(String, graphql_name='installLink')
    '''Link to click in order to install new Github integration'''

    installations = sgqlc.types.Field(sgqlc.types.list_of('GithubAppInstallation'), graphql_name='installations')
    '''Metadata about Github App installation'''



class GithubAppInstallation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('uuid', 'gh_org', 'settings_link')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Internal Github installation uuid'''

    gh_org = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ghOrg')
    '''Github Org name in which the Github App is installed'''

    settings_link = sgqlc.types.Field(String, graphql_name='settingsLink')
    '''Link to click in order to configure Github App installation'''



class GithubPullRequest(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('url', 'title', 'issue_number', 'author', 'repository_name', 'repository_owner', 'merged_at', 'number_of_files_changed', 'files_changed', 'score')
    url = sgqlc.types.Field(String, graphql_name='url')
    '''PR URL'''

    title = sgqlc.types.Field(String, graphql_name='title')
    '''PR title'''

    issue_number = sgqlc.types.Field(Int, graphql_name='issueNumber')
    '''PR issue number'''

    author = sgqlc.types.Field('GithubUser', graphql_name='author')
    '''PR author'''

    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    '''Repository name'''

    repository_owner = sgqlc.types.Field(String, graphql_name='repositoryOwner')
    '''Repository owner'''

    merged_at = sgqlc.types.Field(DateTime, graphql_name='mergedAt')
    '''Time the PR was merged at'''

    number_of_files_changed = sgqlc.types.Field(Int, graphql_name='numberOfFilesChanged')
    '''Number of files changed in the PR'''

    files_changed = sgqlc.types.Field(sgqlc.types.list_of('GithubPullRequestFile'), graphql_name='filesChanged')
    '''List of files changed in the PR'''

    score = sgqlc.types.Field(Float, graphql_name='score')
    '''Score of the PR being relevant to the incident. 100% means that
    the PR is 100% relevant to the incident.
    '''



class GithubPullRequestFile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('path', 'change_type', 'additions', 'deletions')
    path = sgqlc.types.Field(String, graphql_name='path')
    '''File path from the root of the repository'''

    change_type = sgqlc.types.Field(String, graphql_name='changeType')
    '''File change type: added, modified, removed'''

    additions = sgqlc.types.Field(Int, graphql_name='additions')
    '''Number of lines added'''

    deletions = sgqlc.types.Field(Int, graphql_name='deletions')
    '''Number of lines deleted'''



class GithubPullRequestsList(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('pull_requests',)
    pull_requests = sgqlc.types.Field(sgqlc.types.list_of(GithubPullRequest), graphql_name='pullRequests')
    '''List of pull requests'''



class GithubUser(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('login', 'avatar_url')
    login = sgqlc.types.Field(String, graphql_name='login')
    '''Github user login'''

    avatar_url = sgqlc.types.Field(String, graphql_name='avatarUrl')
    '''Github user Avatar URL'''



class HighlightSnippets(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'snippets')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field name'''

    snippets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snippets')
    '''Highlighted snippet'''



class HourlyRowCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('timestamp', 'row_count')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')

    row_count = sgqlc.types.Field(Int, graphql_name='rowCount')



class HourlyRowCountsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('hourly_counts', 'time_axis')
    hourly_counts = sgqlc.types.Field(sgqlc.types.list_of(HourlyRowCount), graphql_name='hourlyCounts')

    time_axis = sgqlc.types.Field('TimeAxis', graphql_name='timeAxis')



class ImportDbtManifest(sgqlc.types.Type):
    '''Import DBT manifest'''
    __schema__ = schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('ImportDbtManifestResponse', graphql_name='response')
    '''Response'''



class ImportDbtManifestResponse(sgqlc.types.Type):
    '''DBT Manifest Import Response'''
    __schema__ = schema
    __field_names__ = ('node_ids_imported', 'node_import_info')
    node_ids_imported = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nodeIdsImported')
    '''List of DBT node ID's imported'''

    node_import_info = sgqlc.types.Field(sgqlc.types.list_of('NodeImportInfo'), graphql_name='nodeImportInfo')
    '''List of node import information'''



class ImportDbtRunResults(sgqlc.types.Type):
    '''Import DBT run results'''
    __schema__ = schema
    __field_names__ = ('response',)
    response = sgqlc.types.Field('ImportDbtRunResultsResponse', graphql_name='response')
    '''Response'''



class ImportDbtRunResultsResponse(sgqlc.types.Type):
    '''DBT Run Results Import Response'''
    __schema__ = schema
    __field_names__ = ('num_results_imported',)
    num_results_imported = sgqlc.types.Field(Int, graphql_name='numResultsImported')
    '''Number of run results imported'''



class IncidentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IncidentEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class IncidentDailyCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('day', 'incident_count')
    day = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='day')
    '''The date for the incident count'''

    incident_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='incidentCount')
    '''The incident count'''



class IncidentDashboardData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_incident_count', 'no_status_count', 'investigating_count', 'fixed_count', 'expected_and_no_action_count')
    total_incident_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalIncidentCount')
    '''The total count of incidents over the specified weeks'''

    no_status_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='noStatusCount')
    '''The total count of incidents with no status over the specified
    weeks
    '''

    investigating_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='investigatingCount')
    '''The total count of incidents with status of investigating over the
    specified weeks
    '''

    fixed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fixedCount')
    '''The total count of incidents with fixed status over the specified
    weeks
    '''

    expected_and_no_action_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='expectedAndNoActionCount')
    '''The total count of incidents with status expected or no action
    over the specified weeks
    '''



class IncidentEdge(sgqlc.types.Type):
    '''A Relay edge containing a `Incident` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Incident', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class IncidentReactionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IncidentReactionEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class IncidentReactionEdge(sgqlc.types.Type):
    '''A Relay edge containing a `IncidentReaction` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('IncidentReaction', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class IncidentSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('incident_id', 'types', 'states', 'tables', 'key_assets', 'has_rca')
    incident_id = sgqlc.types.Field(UUID, graphql_name='incidentId')

    types = sgqlc.types.Field(EventTypeSummary, graphql_name='types')

    states = sgqlc.types.Field(EventStateSummary, graphql_name='states')

    tables = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tables')

    key_assets = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='keyAssets')
    '''Number of key assets(tables) in incident'''

    has_rca = sgqlc.types.Field(Boolean, graphql_name='hasRca')
    '''Whether an rca insight exists for this incident'''



class IncidentTableMcons(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('tables',)
    tables = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tables')
    '''The list of table mcons directly impacted by incident'''



class IncidentTimePeriodAggregateData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('start_date', 'end_date', 'values')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='startDate')
    '''The start date for the aggregated data'''

    end_date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='endDate')
    '''The end date for the aggregated data'''

    values = sgqlc.types.Field(sgqlc.types.list_of('LabelCount'), graphql_name='values')
    '''The aggregate label and count for the time time period'''



class IncidentTopology(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('root_events',)
    root_events = sgqlc.types.Field(sgqlc.types.list_of(EventTopology), graphql_name='rootEvents')
    '''List of root events in the incident'''



class IncidentTypeSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('anomalies', 'schema_changes', 'json_schema_changes', 'deleted_tables', 'metric_anomalies', 'custom_rule_anomalies', 'performance_anomalies', 'dbt_errors', 'pseudo_integration_test')
    anomalies = sgqlc.types.Field(Int, graphql_name='anomalies')

    schema_changes = sgqlc.types.Field(Int, graphql_name='schemaChanges')

    json_schema_changes = sgqlc.types.Field(Int, graphql_name='jsonSchemaChanges')

    deleted_tables = sgqlc.types.Field(Int, graphql_name='deletedTables')

    metric_anomalies = sgqlc.types.Field(Int, graphql_name='metricAnomalies')

    custom_rule_anomalies = sgqlc.types.Field(Int, graphql_name='customRuleAnomalies')

    performance_anomalies = sgqlc.types.Field(Int, graphql_name='performanceAnomalies')

    dbt_errors = sgqlc.types.Field(Int, graphql_name='dbtErrors')

    pseudo_integration_test = sgqlc.types.Field(Int, graphql_name='pseudoIntegrationTest')



class IncidentWeeklyDataDashboard(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('weekly_data',)
    weekly_data = sgqlc.types.Field(sgqlc.types.list_of(IncidentTimePeriodAggregateData), graphql_name='weeklyData')
    '''The weekly incident data'''



class IndexedFieldSpecType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'display_name', 'displayable', 'aggregatable', 'facetable', 'filterable', 'facet_searchable')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')

    display_name = sgqlc.types.Field(String, graphql_name='displayName')

    displayable = sgqlc.types.Field(Boolean, graphql_name='displayable')

    aggregatable = sgqlc.types.Field(Boolean, graphql_name='aggregatable')

    facetable = sgqlc.types.Field(Boolean, graphql_name='facetable')

    filterable = sgqlc.types.Field(Boolean, graphql_name='filterable')

    facet_searchable = sgqlc.types.Field(Boolean, graphql_name='facetSearchable')



class Insight(sgqlc.types.Type):
    '''Available data on a specific element of the system created by DS'''
    __schema__ = schema
    __field_names__ = ('name', 'title', 'usage', 'description', 'reports', 'available')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name (id) of insight'''

    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    '''Insight display name'''

    usage = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='usage')
    '''Explains what the insight data can be used for'''

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    '''Information the reports for the insight will provide'''

    reports = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Report')), graphql_name='reports')
    '''Reports available for the insight'''

    available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='available')
    '''True if this insight is currently available'''



class IntegrationKey(sgqlc.types.Type):
    '''Integration key id and secret. Only available once.'''
    __schema__ = schema
    __field_names__ = ('id', 'secret')
    id = sgqlc.types.Field(String, graphql_name='id')
    '''Key id'''

    secret = sgqlc.types.Field(String, graphql_name='secret')
    '''Key secret'''



class IntegrationKeyMetadata(sgqlc.types.Type):
    '''Metadata for an integration key (will not include the associated
    secret)
    '''
    __schema__ = schema
    __field_names__ = ('id', 'description', 'scope', 'warehouses', 'created_time', 'created_by')
    id = sgqlc.types.Field(String, graphql_name='id')
    '''Key id'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Key description'''

    scope = sgqlc.types.Field(String, graphql_name='scope')
    '''Key scope (integration it can be used for)'''

    warehouses = sgqlc.types.Field(sgqlc.types.list_of('Warehouse'), graphql_name='warehouses')
    '''Warehouses associated with key'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''Time key was created'''

    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    '''Who created the key'''



class InternalNotifications(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'friendly_message', 'details', 'is_urgent', 'expiration_date')
    type = sgqlc.types.Field(String, graphql_name='type')
    '''Type of notification.'''

    friendly_message = sgqlc.types.Field(String, graphql_name='friendlyMessage')
    '''Human readable message.'''

    details = sgqlc.types.Field(JSONString, graphql_name='details')
    '''Raw information about the message (e.g. specifics).'''

    is_urgent = sgqlc.types.Field(Boolean, graphql_name='isUrgent')
    '''Whether to display a modal or badge.'''

    expiration_date = sgqlc.types.Field(DateTime, graphql_name='expirationDate')
    '''Reserved for future use (e.g. hiding old messages).'''



class InvestigationQuery(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query', 'has_error')
    query = sgqlc.types.Field(String, graphql_name='query')

    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')



class InviteUsersPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('users', 'client_mutation_id')
    users = sgqlc.types.Field(sgqlc.types.list_of('UserInvite'), graphql_name='users')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class InviteUsersV2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('invites', 'existing_users', 'already_invited')
    invites = sgqlc.types.Field(sgqlc.types.list_of('UserInvite'), graphql_name='invites')
    '''List of users invites sent'''

    existing_users = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='existingUsers')
    '''List of email addresses of users who already exist and cannot be
    invited
    '''

    already_invited = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='alreadyInvited')
    '''List of email addresses already invited to this account or another
    account
    '''



class JiraIntegrationOutput(sgqlc.types.Type):
    '''A Jira integration'''
    __schema__ = schema
    __field_names__ = ('integration_id', 'integration_name', 'server_url', 'username', 'default_ticket_fields')
    integration_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='integrationId')
    '''The integration ID'''

    integration_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='integrationName')
    '''A short name to identify the integration'''

    server_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serverUrl')
    '''The domain name for your Jira site'''

    username = sgqlc.types.Field(String, graphql_name='username')
    '''The Jira username for basic authentication. If not provided, the
    previous value will be used.
    '''

    default_ticket_fields = sgqlc.types.Field(JSONString, graphql_name='defaultTicketFields')
    '''Default values for ticket fields.'''



class JiraIssueTypeFieldOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('key', 'name', 'required', 'has_default_value', 'has_default_value_in_jira', 'type')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    '''The field key'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The field name'''

    required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='required')
    '''If the field is required to create the issue'''

    has_default_value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDefaultValue')
    '''If the field has a default value when not set, considering
    integration level default values configured on Monte Carlo
    '''

    has_default_value_in_jira = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDefaultValueInJira')
    '''If the field has a default value in Jira when not set'''

    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    '''The field type'''



class JiraIssueTypeOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'untranslated_name', 'fields')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    '''The issue type ID'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The issue type name'''

    untranslated_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='untranslatedName')
    '''The issue type untranslated name'''

    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(JiraIssueTypeFieldOutput)), graphql_name='fields')
    '''The issue type fields'''



class JiraProjectOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'key', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    '''The project ID'''

    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    '''The project key'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The project name'''



class JiraTestCredentialsOutput(sgqlc.types.Type):
    '''A Jira test credentials result'''
    __schema__ = schema
    __field_names__ = ('valid_credentials',)
    valid_credentials = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validCredentials')
    '''Returns if the credentials are valid'''



class JiraTicketOutput(sgqlc.types.Type):
    '''A Jira ticket'''
    __schema__ = schema
    __field_names__ = ('ticket_id', 'ticket_url', 'ticket_key', 'incident_id', 'integration_id', 'created_by', 'created_at')
    ticket_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='ticketId')
    '''The ticket ID in Monte Carlo'''

    ticket_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ticketUrl')
    '''The ticket URL'''

    ticket_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ticketKey')
    '''The ticket key'''

    incident_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='incidentId')
    '''The incident ID'''

    integration_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='integrationId')
    '''The integration ID'''

    created_by = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createdBy')
    '''Email of the user that created the ticket'''

    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    '''When the ticket was created'''



class JobError(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('message', 'job_execution_uuid', 'dc_schedule_uuid', 'timestamp', 'result_count', 'job_type', 'stack_name', 'data_collector_uuid')
    message = sgqlc.types.Field(String, graphql_name='message')
    '''The error message'''

    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')
    '''The Job Execution ID'''

    dc_schedule_uuid = sgqlc.types.Field(UUID, graphql_name='dcScheduleUuid')
    '''The data collector schedule UUID'''

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    '''The timestamp of the error'''

    result_count = sgqlc.types.Field(Int, graphql_name='resultCount')
    '''The number of results returned'''

    job_type = sgqlc.types.Field(String, graphql_name='jobType')
    '''The type of job that failed'''

    stack_name = sgqlc.types.Field(String, graphql_name='stackName')
    '''The name of the stack for the data collector'''

    data_collector_uuid = sgqlc.types.Field(UUID, graphql_name='dataCollectorUuid')
    '''The data collector uuid'''



class JobExecutionException(sgqlc.types.Type):
    '''Job execution exception details'''
    __schema__ = schema
    __field_names__ = ('type', 'description', 'sql_query')
    type = sgqlc.types.Field(String, graphql_name='type')
    '''Exception type'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Exception description'''

    sql_query = sgqlc.types.Field(String, graphql_name='sqlQuery')
    '''SQL query execution that triggered the exception'''



class JobExecutionHistoryLog(sgqlc.types.Type):
    '''Job history log entry'''
    __schema__ = schema
    __field_names__ = ('job_execution_uuid', 'start_time', 'status', 'end_time', 'exceptions', 'exceptions_detail')
    job_execution_uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobExecutionUuid')
    '''UUID of job execution'''

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''When the job was scheduled'''

    status = sgqlc.types.Field(JobExecutionStatus, graphql_name='status')

    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')
    '''When the job was completed'''

    exceptions = sgqlc.types.Field(String, graphql_name='exceptions')
    '''Exceptions that were captured during this job execution (pre-
    formatted)
    '''

    exceptions_detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(JobExecutionException)), graphql_name='exceptionsDetail')
    '''Exceptions that were captured during this job execution'''



class LabelCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('label', 'count')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    '''The label value'''

    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    '''The count for the label'''



class LastSizeChange(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('timestamp', 'size')
    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    '''Timestamp when the last size change occurred'''

    size = sgqlc.types.Field(Float, graphql_name='size')
    '''Table size after the last size change occurred'''



class LastUpdates(sgqlc.types.Type):
    '''this class will be used to hold new last updates v2 results. The
    time_interval_in_sec would indicate the time bucket interval used
    for integration. For direct query result, time_interval_in_sec
    field will be set to 0
    '''
    __schema__ = schema
    __field_names__ = ('last_updates', 'time_interval_in_sec')
    last_updates = sgqlc.types.Field(sgqlc.types.list_of('TableUpdateTime'), graphql_name='lastUpdates')

    time_interval_in_sec = sgqlc.types.Field(Int, graphql_name='timeIntervalInSec')



class LineageGraph(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('base_node', 'connected_nodes', 'flattened_edges')
    base_node = sgqlc.types.Field('LineageGraphNode', graphql_name='baseNode')
    '''This is the base node for which lineage is fetched'''

    connected_nodes = sgqlc.types.Field(sgqlc.types.list_of('LineageGraphNode'), graphql_name='connectedNodes')
    '''List of nodes connected to the base node. This could be nodes that
    are multiple hops away from the base node in the graph in cases
    where nodes at multiple hops were queried.
    '''

    flattened_edges = sgqlc.types.Field(sgqlc.types.list_of(FlattenedLineageGraphEdges), graphql_name='flattenedEdges')
    '''Each entry is an mcon and a list of mcons it is directly connected
    to
    '''



class LineageGraphEdge(sgqlc.types.Type):
    '''A lineage graph edge'''
    __schema__ = schema
    __field_names__ = ('source', 'destination', 'job_ts', 'expire_at', 'is_custom')
    source = sgqlc.types.Field('LineageGraphNode', graphql_name='source')
    '''The source node'''

    destination = sgqlc.types.Field('LineageGraphNode', graphql_name='destination')
    '''The destination node'''

    job_ts = sgqlc.types.Field(DateTime, graphql_name='jobTs')
    '''The timestamp of the job run or API call that created this edge'''

    expire_at = sgqlc.types.Field(DateTime, graphql_name='expireAt')
    '''The timestamp when this edge will expire'''

    is_custom = sgqlc.types.Field(Boolean, graphql_name='isCustom')
    '''Indicates whether this is a custom lineage edge (created by a
    user)
    '''



class LineageGraphNode(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'display_name', 'has_downstream_nodes', 'has_upstream_nodes', 'object_type', 'is_custom', 'job_ts', 'expire_at')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''Monte Carlo full identifier for an entity'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Friendly name for entity'''

    has_downstream_nodes = sgqlc.types.Field(Boolean, graphql_name='hasDownstreamNodes')
    '''Indicates whether this node has downstream nodes'''

    has_upstream_nodes = sgqlc.types.Field(Boolean, graphql_name='hasUpstreamNodes')
    '''Indicates whether this node has upstream nodes'''

    object_type = sgqlc.types.Field(String, graphql_name='objectType')
    '''Type of the object that this lineage node denotes'''

    is_custom = sgqlc.types.Field(Boolean, graphql_name='isCustom')
    '''Indicates whether this is a custom lineage node (created by a
    user)
    '''

    job_ts = sgqlc.types.Field(DateTime, graphql_name='jobTs')
    '''The timestamp of the job run or API call that created this node'''

    expire_at = sgqlc.types.Field(DateTime, graphql_name='expireAt')
    '''The timestamp when this node will expire'''



class LineageNodeBlockPattern(sgqlc.types.Type):
    '''A pattern defining nodes to be blocked from lineage'''
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'account_id', 'resource_id', 'dataset_regexp', 'project_regexp', 'table_regexp', 'created_time', 'last_update_user', 'last_update_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Pattern UUID'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''Resource containing the node'''

    dataset_regexp = sgqlc.types.Field(String, graphql_name='datasetRegexp')
    '''Block nodes with dataset id matching this regexp'''

    project_regexp = sgqlc.types.Field(String, graphql_name='projectRegexp')
    '''Block nodes with project id matching this regexp'''

    table_regexp = sgqlc.types.Field(String, graphql_name='tableRegexp')
    '''Block nodes with table id matching this regexp'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the regexp was first created'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who last updated the regexp'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the regexp was last updated'''



class LineageNodeReplacementRule(sgqlc.types.Type):
    '''A replacement pattern modifying lineage node's canonical name'''
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'account_id', 'resource_id', 'pattern', 'replacement', 'case_insensitive', 'last_update_user', 'last_update_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Replacement rule UUID'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''Resource containing the node'''

    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')
    '''Modify canonical name by replacing the pattern with replacement'''

    replacement = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='replacement')
    '''Modify canonical name by replacing the pattern with replacement'''

    case_insensitive = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='caseInsensitive')
    '''Case sensitivity of the pattern matching'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who last updated the replacement rule'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the replacement rule was last updated'''



class LineageNodeReplacementRuleResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('test_input_string', 'replaced_string')
    test_input_string = sgqlc.types.Field(String, graphql_name='testInputString')
    '''The provided test input string'''

    replaced_string = sgqlc.types.Field(String, graphql_name='replacedString')
    '''The replaced string, using provided pattern/replacement'''



class LineageSources(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'source_columns')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Mcon of the source table'''

    source_columns = sgqlc.types.Field(sgqlc.types.list_of('SourceColumn'), graphql_name='sourceColumns')
    '''Source columns from this source table'''



class LinkGithubAppInstallation(sgqlc.types.Type):
    '''Called from the FE as part of the post-installation callback. The
    "code" parameter is used to validate that the request is an
    authentic Github callback and authenticates the user on the Github
    side.
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''True if linking the installation was successful'''



class LinkJiraTicketForIncident(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('jira_ticket',)
    jira_ticket = sgqlc.types.Field(JiraTicketOutput, graphql_name='jiraTicket')
    '''The created Jira ticket'''



class ListDatasetsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('datasets', 'next_page_token')
    datasets = sgqlc.types.Field(sgqlc.types.list_of(DatasetEntity), graphql_name='datasets')
    '''List of dataset IDs'''

    next_page_token = sgqlc.types.Field(String, graphql_name='nextPageToken')
    '''Page token for the next page'''



class ListProjectsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('projects', 'next_page_token')
    projects = sgqlc.types.Field(sgqlc.types.list_of('ProjectEntity'), graphql_name='projects')
    '''List of project IDs'''

    next_page_token = sgqlc.types.Field(String, graphql_name='nextPageToken')
    '''Page token for the next page'''



class LookerDashboardTileRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('tile_id', 'tile_title')
    tile_id = sgqlc.types.Field(String, graphql_name='tileId')

    tile_title = sgqlc.types.Field(String, graphql_name='tileTitle')



class MaintenanceWindow(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('start_time', 'end_time')
    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''Start of maintenance window'''

    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')
    '''End of maintenance window'''



class MatchAndCreateBiWarehouseSources(sgqlc.types.Type):
    '''Create or update a BI warehouse source. If BI warehouse source
    details are provided in thebi_warehouse_sources parameter then
    those are saved. Else, details are pulled from the BIAPIs, matched
    with warehouses in Monte Carlo and details saved only if there is
    a full match.
    '''
    __schema__ = schema
    __field_names__ = ('matching_bi_warehouse_sources',)
    matching_bi_warehouse_sources = sgqlc.types.Field('MatchingBiWarehouseSources', graphql_name='matchingBiWarehouseSources')



class MatchingBiWarehouseSources(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('match_successful', 'bi_warehouse_sources', 'raw_bi_warehouse_connections', 'raw_warehouse_connections')
    match_successful = sgqlc.types.Field(Boolean, graphql_name='matchSuccessful')
    '''Indicates whether all BI source warehouses could be matched with a
    warehouse stored in MC. Only true if all BI source warehouses
    could be matched.
    '''

    bi_warehouse_sources = sgqlc.types.Field(sgqlc.types.list_of(BiWarehouseSources), graphql_name='biWarehouseSources')
    '''Details of matched warehouses.'''

    raw_bi_warehouse_connections = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='rawBiWarehouseConnections')
    '''Raw response from customer's BI system listing the warehouses it
    is connected to. Only set if match_successful is False.
    '''

    raw_warehouse_connections = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='rawWarehouseConnections')
    '''Details of warehouses that are in MC. Only set if match_successful
    is False.
    '''



class MetricAnomalyCorrelation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'metric', 'correlations')
    field = sgqlc.types.Field(String, graphql_name='field')

    metric = sgqlc.types.Field(String, graphql_name='metric')

    correlations = sgqlc.types.Field(sgqlc.types.list_of(FieldValueCorrelation), graphql_name='correlations')



class MetricAnomalyCorrelationV2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field', 'metric', 'data', 'has_strong_correlations')
    field = sgqlc.types.Field(String, graphql_name='field')

    metric = sgqlc.types.Field(String, graphql_name='metric')

    data = sgqlc.types.Field(sgqlc.types.list_of(FieldValueCorrelation), graphql_name='data')

    has_strong_correlations = sgqlc.types.Field(Boolean, graphql_name='hasStrongCorrelations')



class MetricCorrelationResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metric_anomalies', 'metric_anomalies_v2')
    metric_anomalies = sgqlc.types.Field(sgqlc.types.list_of(MetricAnomalyCorrelation), graphql_name='metricAnomalies')

    metric_anomalies_v2 = sgqlc.types.Field(sgqlc.types.list_of(MetricAnomalyCorrelationV2), graphql_name='metricAnomaliesV2')



class MetricDimensions(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('rank', 'label')
    rank = sgqlc.types.Field(Float, graphql_name='rank')

    label = sgqlc.types.Field(String, graphql_name='label')



class MetricMonitorSelectExpression(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'metric_monitor', 'expression', 'data_type', 'is_raw_column_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    metric_monitor = sgqlc.types.Field(sgqlc.types.non_null('MetricMonitoring'), graphql_name='metricMonitor')

    expression = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expression')

    data_type = sgqlc.types.Field(MetricMonitorSelectExpressionModelDataType, graphql_name='dataType')

    is_raw_column_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRawColumnName')



class MetricMonitoringConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('MetricMonitoringEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class MetricMonitoringEdge(sgqlc.types.Type):
    '''A Relay edge containing a `MetricMonitoring` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('MetricMonitoring', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class MetricSampling(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('columns', 'rows', 'query', 'has_error')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')

    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')

    query = sgqlc.types.Field(String, graphql_name='query')

    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')



class MetricValueByTable(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'full_table_id', 'resource_id')
    value = sgqlc.types.Field(DateTime, graphql_name='value')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')



class Metrics(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metrics', 'is_partial_date_range')
    metrics = sgqlc.types.Field(sgqlc.types.list_of('TableMetricV2'), graphql_name='metrics')

    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange')



class MigrateCollectorResources(sgqlc.types.Type):
    '''Migrate resources (warehouses, BI) from one data collector to
    another
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''If the migration was successful'''



class MonitorConfiguration(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('time_field', 'aggregation_type', 'lookback_days')
    time_field = sgqlc.types.Field(String, graphql_name='timeField')
    '''Time field to use for the monitor'''

    aggregation_type = sgqlc.types.Field(MonitorAggTimeInterval, graphql_name='aggregationType')
    '''Day or Hour'''

    lookback_days = sgqlc.types.Field(Int, graphql_name='lookbackDays')
    '''The history days for the monitor'''



class MonitorDashboardData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total_monitor_count', 'paused_count', 'snoozed_count', 'active_count', 'training_count', 'misconfigured_count', 'error_count', 'in_progress_count', 'no_status_count')
    total_monitor_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalMonitorCount')
    '''Total count of monitors actively in MC account'''

    paused_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedCount')
    '''Total number of paused monitors'''

    snoozed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='snoozedCount')
    '''Total number of snoozed monitors'''

    active_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='activeCount')
    '''Total count of monitors with active status'''

    training_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='trainingCount')
    '''Total count of monitors with training status'''

    misconfigured_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='misconfiguredCount')
    '''Total count of monitors with misconfigured status'''

    error_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='errorCount')
    '''Total count of monitors with error status'''

    in_progress_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inProgressCount')
    '''Total number of monitors currently running'''

    no_status_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='noStatusCount')
    '''Total number of monitors with state no status'''



class MonitorLabel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('label',)
    label = sgqlc.types.Field(String, graphql_name='label')
    '''The monitor label name'''



class MonitorLabelObject(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('uuid', 'label', 'created_by', 'monitors', 'monitor_count', 'notification_count', 'used_in_mac')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Unique identifier of a monitor label'''

    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    '''Monitor label name'''

    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    '''Monitor label creator'''

    monitors = sgqlc.types.Field(sgqlc.types.list_of('Monitor'), graphql_name='monitors', args=sgqlc.types.ArgDict((
        ('monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(UserDefinedMonitors), graphql_name='monitorTypes', default=None)),
        ('status_types', sgqlc.types.Arg(sgqlc.types.list_of(MonitorStatusType), graphql_name='statusTypes', default=None)),
        ('description_field_or_table', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='descriptionFieldOrTable', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='uuids', default=None)),
        ('created_by_filters', sgqlc.types.Arg(CreatedByFilters, graphql_name='createdByFilters', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('search', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='search', default=None)),
        ('search_fields', sgqlc.types.Arg(sgqlc.types.list_of(UserDefinedMonitorSearchFields), graphql_name='searchFields', default=None)),
        ('namespaces', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='namespaces', default=None)),
        ('is_template_managed', sgqlc.types.Arg(Boolean, graphql_name='isTemplateManaged', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    '''List of monitors using this label

    Arguments:

    * `monitor_types` (`[UserDefinedMonitors]`): Type of monitors to
      filter by, default all
    * `status_types` (`[MonitorStatusType]`): Type of monitor status
      to filter by, default all
    * `description_field_or_table` (`[String]`): DEPRECATED
    * `domain_id` (`UUID`): Domain uuid to filter by
    * `uuids` (`[String]`): list of uuids of the monitors to filter by
    * `created_by_filters` (`CreatedByFilters`): Deprecated
    * `labels` (`[String]`): List of labels to filter by
    * `search` (`[String]`): Search criteria for filtering the
      monitors list
    * `search_fields` (`[UserDefinedMonitorSearchFields]`): Which
      fields to include during search
    * `namespaces` (`[String]`): filter by namespaces
    * `is_template_managed` (`Boolean`): Filter monitors created by
      code
    * `mcons` (`[String]`): Filter by associated entities (MCON)
    * `order_by` (`String`): Field and direction to order monitors by
    * `limit` (`Int`): Number of monitors to return
    * `offset` (`Int`): From which monitor to return the next results
    '''

    monitor_count = sgqlc.types.Field(Int, graphql_name='monitorCount')
    '''The number of monitors using this label'''

    notification_count = sgqlc.types.Field(Int, graphql_name='notificationCount')
    '''The number of notifications using this label'''

    used_in_mac = sgqlc.types.Field(Boolean, graphql_name='usedInMac')
    '''Flag for whether any MaC monitors use this label'''



class MonitorQueries(sgqlc.types.Type):
    '''A monitor query'''
    __schema__ = schema
    __field_names__ = ('queries',)
    queries = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='queries')
    '''The SQL queries executed by the monitor'''



class MonitorQueriesResults(sgqlc.types.Type):
    '''Result of executing a monitor query for test purposes'''
    __schema__ = schema
    __field_names__ = ('queries',)
    queries = sgqlc.types.Field(sgqlc.types.list_of('SQLResponse'), graphql_name='queries')
    '''The SQL queries results'''



class MonitorSchedulingConfiguration(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('schedule_type', 'interval_minutes', 'start_time')
    schedule_type = sgqlc.types.Field(String, graphql_name='scheduleType')
    '''One of fixed/dynamic or None if cannot decide automatically'''

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    '''Number of minutes between monitor runs is schedule type is fixed'''

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''Date to start the monitor if schedule type is fixed'''



class MonitorSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('resources', 'stats', 'categories', 'hourly_stats', 'json_schema', 'custom_sql', 'table_metric')
    resources = sgqlc.types.Field('TableResources', graphql_name='resources')

    stats = sgqlc.types.Field(Int, graphql_name='stats')

    categories = sgqlc.types.Field(Int, graphql_name='categories')

    hourly_stats = sgqlc.types.Field(Int, graphql_name='hourlyStats')

    json_schema = sgqlc.types.Field(Int, graphql_name='jsonSchema')

    custom_sql = sgqlc.types.Field(Int, graphql_name='customSql')

    table_metric = sgqlc.types.Field(Int, graphql_name='tableMetric')



class MonteCarloConfigTemplateConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('MonteCarloConfigTemplateEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class MonteCarloConfigTemplateDeleteResponse(sgqlc.types.Type):
    '''Monte Carlo Config Template Delete Response'''
    __schema__ = schema
    __field_names__ = ('num_deleted', 'changes_applied')
    num_deleted = sgqlc.types.Field(Int, graphql_name='numDeleted')
    '''Number of resources deleted'''

    changes_applied = sgqlc.types.Field(Boolean, graphql_name='changesApplied')
    '''Changes applied?'''



class MonteCarloConfigTemplateEdge(sgqlc.types.Type):
    '''A Relay edge containing a `MonteCarloConfigTemplate` and its
    cursor.
    '''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('MonteCarloConfigTemplate', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class MonteCarloConfigTemplateExportResponse(sgqlc.types.Type):
    '''Monte Carlo Config Template Export Response'''
    __schema__ = schema
    __field_names__ = ('config_template_as_yaml', 'errors')
    config_template_as_yaml = sgqlc.types.Field(String, graphql_name='configTemplateAsYaml')
    '''Config Template as YAML'''

    errors = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='errors')
    '''Errors encountered'''



class MonteCarloConfigTemplateUpdateAsyncResponse(sgqlc.types.Type):
    '''Monte Carlo Config Template Update Async Response'''
    __schema__ = schema
    __field_names__ = ('update_uuid', 'errors_as_json')
    update_uuid = sgqlc.types.Field(UUID, graphql_name='updateUuid')
    '''The UUID of the requested update. Used to poll for the status of
    the update. Null if the update request is invalid.
    '''

    errors_as_json = sgqlc.types.Field(String, graphql_name='errorsAsJson')
    '''Errors encountered'''



class MonteCarloConfigTemplateUpdateAsyncState(sgqlc.types.Type):
    '''Monte Carlo Config Template Update Async State'''
    __schema__ = schema
    __field_names__ = ('resource_modifications', 'changes_applied', 'errors_as_json', 'warnings_as_json', 'info_as_json', 'state')
    resource_modifications = sgqlc.types.Field(sgqlc.types.list_of('ResourceModification'), graphql_name='resourceModifications')
    '''List of resource modifications'''

    changes_applied = sgqlc.types.Field(Boolean, graphql_name='changesApplied')
    '''Changes applied?'''

    errors_as_json = sgqlc.types.Field(String, graphql_name='errorsAsJson')
    '''Errors encountered'''

    warnings_as_json = sgqlc.types.Field(String, graphql_name='warningsAsJson')
    '''Warnings encountered'''

    info_as_json = sgqlc.types.Field(String, graphql_name='infoAsJson')
    '''Informational messages'''

    state = sgqlc.types.Field(sgqlc.types.non_null(State), graphql_name='state')
    '''State of the async update'''



class MonteCarloConfigTemplateUpdateResponse(sgqlc.types.Type):
    '''Monte Carlo Config Template Update Response'''
    __schema__ = schema
    __field_names__ = ('resource_modifications', 'changes_applied', 'errors_as_json', 'warnings_as_json', 'info_as_json')
    resource_modifications = sgqlc.types.Field(sgqlc.types.list_of('ResourceModification'), graphql_name='resourceModifications')
    '''List of resource modifications'''

    changes_applied = sgqlc.types.Field(Boolean, graphql_name='changesApplied')
    '''Changes applied?'''

    errors_as_json = sgqlc.types.Field(String, graphql_name='errorsAsJson')
    '''Errors encountered'''

    warnings_as_json = sgqlc.types.Field(String, graphql_name='warningsAsJson')
    '''Warnings encountered'''

    info_as_json = sgqlc.types.Field(String, graphql_name='infoAsJson')
    '''Informational messages'''



class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('link_github_app_installation', 'delete_github_installation', 'create_jira_integration', 'update_jira_integration', 'delete_jira_integration', 'create_jira_ticket_for_incident', 'link_jira_ticket_for_incident', 'unlink_jira_ticket_for_incident', 'create_or_update_notification_setting', 'create_or_update_recipient_name', 'delete_notification_settings', 'delete_recipient_name', 'set_pii_filter_status', 'update_pii_filtering_preferences', 'update_monitor_name', 'update_monitor_notes', 'update_monitor_labels', 'create_custom_user', 'create_unified_user_assignment', 'delete_unified_user_assignment', 'import_dbt_manifest', 'upload_dbt_manifest', 'import_dbt_run_results', 'upload_dbt_run_results', 'send_dbt_artifacts_event', 'set_group_repetitive_dbt_model_failures', 'set_group_repetitive_dbt_test_failures', 'set_generates_incidents', 'set_job_generates_incidents', 'snooze_dbt_node', 'unsnooze_dbt_node', 'update_dbt_project_info', 'create_or_update_monte_carlo_config_template', 'create_or_update_monte_carlo_config_template_async', 'delete_monte_carlo_config_template', 'set_sensitivity', 'add_to_collection_block_list', 'remove_from_collection_block_list', 'create_custom_rule', 'create_or_update_custom_rule', 'create_or_update_volume_rule', 'create_custom_metric_rule', 'create_or_update_custom_metric_rule', 'update_custom_metric_rule_notes', 'update_custom_metric_severity', 'create_or_update_freshness_custom_rule', 'snooze_custom_rule', 'unsnooze_custom_rule', 'delete_custom_rule', 'trigger_custom_rule', 'trigger_circuit_breaker_rule', 'trigger_circuit_breaker_rule_v2', 'run_sql_rule', 'create_or_update_lineage_node', 'create_or_update_lineage_edge', 'create_or_update_lineage_node_block_pattern', 'create_or_update_lineage_node_replacement_rule', 'delete_lineage_node', 'delete_lineage_node_block_pattern', 'delete_lineage_node_replacement_rule', 'create_or_update_field_quality_rule', 'create_or_update_catalog_object_metadata', 'delete_catalog_object_metadata', 'create_or_update_object_property', 'delete_object_property', 'bulk_create_or_update_object_properties', 'create_or_update_monitor_label', 'delete_monitor_label', 'stop_monitor', 'delete_monitor', 'trigger_monitor', 'create_or_update_monitor', 'pause_monitor', 'validate_cron', 'create_event_comment', 'update_event_comment', 'delete_event_comment', 'set_incident_feedback', 'set_incident_reaction', 'set_incident_severity', 'set_incident_owner', 'create_or_update_incident_comment', 'delete_incident_comment', 'split_incident', 'create_or_update_domain', 'delete_domain', 'create_or_update_authorization_group', 'delete_authorization_group', 'update_user_authorization_group_membership', 'create_or_update_resource', 'match_and_create_bi_warehouse_sources', 'toggle_disable_sampling', 'toggle_disable_value_ingestion', 'toggle_disable_value_sampling_when_testing', 'toggle_enable_full_distribution_metrics', 'save_table_importance_stats', 'set_default_incident_group_interval', 'create_or_update_data_maintenance_entry', 'toggle_wildcard_aggregation', 'set_wildcard_templates', 'delete_data_maintenance_entry', 'create_or_update_user_settings', 'update_user_state', 'update_account_display_assets_search_tags', 'set_account_name', 'set_warehouse_name', 'create_or_update_saml_identity_provider', 'delete_saml_identity_provider', 'invite_users', 'invite_users_v2', 'switch_user_account', 'delete_user_invite', 'resend_user_invite', 'remove_user_from_account', 'disable_user', 'track_table', 'upload_credentials', 'save_slack_credentials', 'deauthorize_slack_app', 'test_credentials', 'test_database_credentials', 'test_presto_credentials', 'test_snowflake_credentials', 'test_hive_credentials', 'test_s3_credentials', 'test_glue_credentials', 'test_athena_credentials', 'test_looker_credentials', 'test_looker_git_credentials', 'test_looker_git_ssh_credentials', 'test_looker_git_clone_credentials', 'test_dbt_cloud_credentials', 'test_bq_credentials', 'test_spark_credentials', 'test_databricks_sql_warehouse_credentials', 'test_self_hosted_credentials', 'add_tableau_account', 'test_tableau_credentials', 'test_power_bi_credentials', 'test_fivetran_credentials', 'toggle_mute_dataset', 'toggle_mute_table', 'toggle_mute_datasets', 'toggle_mute_tables', 'toggle_mute_with_regex', 'toggle_slack_reply_warning', 'toggle_connection_enable', 'add_connection', 'remove_connection', 'add_bi_connection', 'update_bi_connection_name', 'add_etl_connection', 'toggle_event_config', 'configure_airflow_log_events', 'configure_metadata_events', 'configure_query_log_events', 'disable_airflow_log_events', 'disable_metadata_events', 'disable_query_log_events', 'create_or_update_service_api_token', 'create_access_token', 'delete_access_token', 'generate_collector_template', 'update_credentials', 'create_collector_record', 'cleanup_collector_record', 'migrate_collector_resources', 'update_slack_channels', 'create_integration_key', 'delete_integration_key', 'create_databricks_secret', 'create_databricks_notebook_job', 'update_databricks_notebook_job', 'update_databricks_notebook', 'start_databricks_cluster', 'start_databricks_warehouse', 'test_databricks_credentials', 'test_delta_credentials', 'add_databricks_connection', 'save_event_onboarding_data', 'delete_event_onboarding_data', 'test_snowflake_credentials_v2', 'test_redshift_credentials_v2', 'test_bq_credentials_v2', 'test_tableau_credentials_v2', 'test_looker_credentials_v2', 'test_looker_git_ssh_credentials_v2', 'test_looker_git_clone_credentials_v2', 'test_power_bi_credentials_v2', 'test_databricks_credentials_v2', 'test_databricks_sql_warehouse_credentials_v2', 'test_databricks_spark_credentials_v2', 'upload_airflow_dag_result', 'upload_airflow_task_result', 'upload_airflow_sla_misses')
    link_github_app_installation = sgqlc.types.Field(LinkGithubAppInstallation, graphql_name='linkGithubAppInstallation', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('installation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='installationId', default=None)),
))
    )
    '''Called from the FE as part of the post-installation callback. The
    "code" parameter is used to validate that the request is an
    authentic Github callback and authenticates the user on the Github
    side.

    Arguments:

    * `code` (`String!`): Security code passed from Github
    * `installation_id` (`String!`): Github App installation id
    '''

    delete_github_installation = sgqlc.types.Field(DeleteGithubInstallation, graphql_name='deleteGithubInstallation', args=sgqlc.types.ArgDict((
        ('installation_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='installationUuid', default=None)),
))
    )
    '''Arguments:

    * `installation_uuid` (`UUID!`): Internal UUID of the installation
      to delete
    '''

    create_jira_integration = sgqlc.types.Field(CreateJiraIntegration, graphql_name='createJiraIntegration', args=sgqlc.types.ArgDict((
        ('api_token', sgqlc.types.Arg(String, graphql_name='apiToken', default=None)),
        ('default_ticket_fields', sgqlc.types.Arg(JSONString, graphql_name='defaultTicketFields', default=None)),
        ('integration_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='integrationName', default=None)),
        ('server_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverUrl', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    '''Create a Jira integration

    Arguments:

    * `api_token` (`String`): The personal API token for basic
      authentication; if not provided, the previous value will be used
    * `default_ticket_fields` (`JSONString`): Default values for
      ticket fields
    * `integration_name` (`String!`): A short name to identify the
      integration
    * `server_url` (`String!`): The domain name for your Jira site
    * `username` (`String`): The Jira username for basic
      authentication; if not provided, the previous value will be used
    '''

    update_jira_integration = sgqlc.types.Field('UpdateJiraIntegration', graphql_name='updateJiraIntegration', args=sgqlc.types.ArgDict((
        ('api_token', sgqlc.types.Arg(String, graphql_name='apiToken', default=None)),
        ('default_ticket_fields', sgqlc.types.Arg(JSONString, graphql_name='defaultTicketFields', default=None)),
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='integrationId', default=None)),
        ('integration_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='integrationName', default=None)),
        ('server_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverUrl', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    '''Update a Jira integration

    Arguments:

    * `api_token` (`String`): The personal API token for basic
      authentication; if not provided, the previous value will be used
    * `default_ticket_fields` (`JSONString`): Default values for
      ticket fields
    * `integration_id` (`UUID!`): The integration ID
    * `integration_name` (`String!`): A short name to identify the
      integration
    * `server_url` (`String!`): The domain name for your Jira site
    * `username` (`String`): The Jira username for basic
      authentication; if not provided, the previous value will be used
    '''

    delete_jira_integration = sgqlc.types.Field(DeleteJiraIntegration, graphql_name='deleteJiraIntegration', args=sgqlc.types.ArgDict((
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='integrationId', default=None)),
))
    )
    '''Delete a Jira integration

    Arguments:

    * `integration_id` (`UUID!`): The integration ID
    '''

    create_jira_ticket_for_incident = sgqlc.types.Field(CreateJiraTicketForIncident, graphql_name='createJiraTicketForIncident', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='integrationId', default=None)),
        ('issuetype', sgqlc.types.Arg(Int, graphql_name='issuetype', default=None)),
        ('project', sgqlc.types.Arg(Int, graphql_name='project', default=None)),
        ('summary', sgqlc.types.Arg(String, graphql_name='summary', default=None)),
))
    )
    '''Arguments:

    * `description` (`String`): Jira ticket description
    * `incident_id` (`UUID!`): ID of the incident
    * `integration_id` (`UUID!`): ID of the integration
    * `issuetype` (`Int`): Jira issue type ID
    * `project` (`Int`): Jira project ID
    * `summary` (`String`): Jira ticket summary
    '''

    link_jira_ticket_for_incident = sgqlc.types.Field(LinkJiraTicketForIncident, graphql_name='linkJiraTicketForIncident', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='integrationId', default=None)),
        ('ticket_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='ticketUrl', default=None)),
))
    )
    '''Arguments:

    * `incident_id` (`UUID!`): ID of the incident
    * `integration_id` (`UUID!`): ID of the integration
    * `ticket_url` (`String!`): URL of the Jira ticket
    '''

    unlink_jira_ticket_for_incident = sgqlc.types.Field('UnlinkJiraTicketForIncident', graphql_name='unlinkJiraTicketForIncident', args=sgqlc.types.ArgDict((
        ('ticket_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='ticketId', default=None)),
))
    )
    '''Arguments:

    * `ticket_id` (`UUID!`): The ticket ID
    '''

    create_or_update_notification_setting = sgqlc.types.Field(CreateOrUpdateNotificationSetting, graphql_name='createOrUpdateNotificationSetting', args=sgqlc.types.ArgDict((
        ('anomaly_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='anomalyTypes', default=None)),
        ('custom_message', sgqlc.types.Arg(String, graphql_name='customMessage', default=None)),
        ('digest_settings', sgqlc.types.Arg(NotificationDigestSettings, graphql_name='digestSettings', default=None)),
        ('dry', sgqlc.types.Arg(Boolean, graphql_name='dry', default=False)),
        ('extra', sgqlc.types.Arg(NotificationExtra, graphql_name='extra', default=None)),
        ('incident_sub_types', sgqlc.types.Arg(sgqlc.types.list_of(IncidentSubType), graphql_name='incidentSubTypes', default=None)),
        ('notification_schedule_type', sgqlc.types.Arg(String, graphql_name='notificationScheduleType', default=None)),
        ('notification_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='notificationType', default=None)),
        ('recipient', sgqlc.types.Arg(String, graphql_name='recipient', default=None)),
        ('recipients', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='recipients', default=None)),
        ('rules', sgqlc.types.Arg(NotificationRoutingRules, graphql_name='rules', default=None)),
        ('setting_id', sgqlc.types.Arg(UUID, graphql_name='settingId', default=None)),
))
    )
    '''Create or update a notification setting

    Arguments:

    * `anomaly_types` (`[String]`): anomaliesLimit notifications to
      specific incident types (default=all). Supported options
      include: , schema_changesLimit notifications to specific
      incident types (default=all). Supported options include: ,
      json_schema_changesLimit notifications to specific incident
      types (default=all). Supported options include: ,
      deleted_tablesLimit notifications to specific incident types
      (default=all). Supported options include: ,
      metric_anomaliesLimit notifications to specific incident types
      (default=all). Supported options include: ,
      custom_rule_anomaliesLimit notifications to specific incident
      types (default=all). Supported options include: ,
      performance_anomaliesLimit notifications to specific incident
      types (default=all). Supported options include: ,
      dbt_errorsLimit notifications to specific incident types
      (default=all). Supported options include: ,
      pseudo_integration_test
    * `custom_message` (`String`): A custom message to be sent with
      triggered notification
    * `digest_settings` (`NotificationDigestSettings`): Digest
      settings. Only valid when notification schedule type is digest
    * `dry` (`Boolean`): Test destination is reachable by sending a
      sample alert. Note - setting is not saved and rules are not
      evaluated. (default: `false`)
    * `extra` (`NotificationExtra`): Any extra values
    * `incident_sub_types` (`[IncidentSubType]`): Limit notifications
      to specific incident sub types (default=all).
    * `notification_schedule_type` (`String`): realtimeSpecify the
      notification schedule type. Supported values: , digestSpecify
      the notification schedule type. Supported values: ,
      backup_or_failure
    * `notification_type` (`String!`): emailSpecify the notification
      integration to use. Supported options include: ,
      mattermostSpecify the notification integration to use. Supported
      options include: , opsgenieSpecify the notification integration
      to use. Supported options include: , pagerdutySpecify the
      notification integration to use. Supported options include: ,
      slackSpecify the notification integration to use. Supported
      options include: , slack_v2Specify the notification integration
      to use. Supported options include: , webhookSpecify the
      notification integration to use. Supported options include: ,
      msteamsSpecify the notification integration to use. Supported
      options include: , alation
    * `recipient` (`String`): Deprecated
    * `recipients` (`[String]`): Destination to send notifications to
    * `rules` (`NotificationRoutingRules`): Routing rules
    * `setting_id` (`UUID`): For updating a notification setting
    '''

    create_or_update_recipient_name = sgqlc.types.Field(CreateOrUpdateRecipientName, graphql_name='createOrUpdateRecipientName', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('recipient', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='recipient', default=None)),
))
    )
    '''Create or update a recipient's custom name

    Arguments:

    * `name` (`String!`): Custom name
    * `recipient` (`String!`): Recipient string
    '''

    delete_notification_settings = sgqlc.types.Field(DeleteNotificationSetting, graphql_name='deleteNotificationSettings', args=sgqlc.types.ArgDict((
        ('uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='uuids', default=None)),
))
    )
    '''Arguments:

    * `uuids` (`[UUID]!`)None
    '''

    delete_recipient_name = sgqlc.types.Field(DeleteRecipientName, graphql_name='deleteRecipientName', args=sgqlc.types.ArgDict((
        ('recipient', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='recipient', default=None)),
))
    )
    '''Create or update a recipient's custom name

    Arguments:

    * `recipient` (`String!`): Recipient string
    '''

    set_pii_filter_status = sgqlc.types.Field('SetPiiFilterStatus', graphql_name='setPiiFilterStatus', args=sgqlc.types.ArgDict((
        ('pii_filter_status_pairs', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(PiiFilterStatusPair)), graphql_name='piiFilterStatusPairs', default=None)),
))
    )
    '''Set PII filter status for this account.

    Arguments:

    * `pii_filter_status_pairs` (`[PiiFilterStatusPair]!`): PII Filter
      statuses to set for the account.
    '''

    update_pii_filtering_preferences = sgqlc.types.Field('UpdatePiiFilteringPreferences', graphql_name='updatePiiFilteringPreferences', args=sgqlc.types.ArgDict((
        ('enabled', sgqlc.types.Arg(Boolean, graphql_name='enabled', default=None)),
        ('fail_mode', sgqlc.types.Arg(PiiFilteringFailModeType, graphql_name='failMode', default=None)),
))
    )
    '''Update account-wide PII filtering options.

    Arguments:

    * `enabled` (`Boolean`): Whether PII filtering should be enabled
      for the account.
    * `fail_mode` (`PiiFilteringFailModeType`): Whether PII filter
      failures will allow (open) or prevent (close) data flow for this
      account.
    '''

    update_monitor_name = sgqlc.types.Field('UpdateMonitorName', graphql_name='updateMonitorName', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    '''Arguments:

    * `monitor_type` (`String!`): Type of monitor
    * `monitor_uuid` (`UUID!`): UUID of the metric monitor or custom
      rule
    * `name` (`String!`): The new monitor name (the description field)
    '''

    update_monitor_notes = sgqlc.types.Field('UpdateMonitorNotes', graphql_name='updateMonitorNotes', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('notes', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='notes', default=None)),
))
    )
    '''Arguments:

    * `monitor_type` (`String!`): Type of monitor
    * `monitor_uuid` (`UUID!`): UUID of the metric monitor or custom
      rule
    * `notes` (`String!`): The notes for the monitor
    '''

    update_monitor_labels = sgqlc.types.Field('UpdateMonitorLabels', graphql_name='updateMonitorLabels', args=sgqlc.types.ArgDict((
        ('labels', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='labels', default=None)),
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
))
    )
    '''Arguments:

    * `labels` (`[String]!`): Labels to insert on the monitor
    * `monitor_type` (`String!`): Type of monitor
    * `monitor_uuid` (`UUID!`): UUID of the metric monitor or custom
      rule
    '''

    create_custom_user = sgqlc.types.Field(CreateCustomUser, graphql_name='createCustomUser', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
))
    )
    '''Create a CustomUser

    Arguments:

    * `email` (`String!`): Email
    * `first_name` (`String`): First name
    * `last_name` (`String`): Last name
    '''

    create_unified_user_assignment = sgqlc.types.Field(CreateUnifiedUserAssignment, graphql_name='createUnifiedUserAssignment', args=sgqlc.types.ArgDict((
        ('object_mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectMcon', default=None)),
        ('relationship_type', sgqlc.types.Arg(sgqlc.types.non_null(RelationshipType), graphql_name='relationshipType', default=None)),
        ('unified_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='unifiedUserId', default=None)),
))
    )
    '''Associate a UnifiedUser with a CatalogObject

    Arguments:

    * `object_mcon` (`String!`): MCON of catalog object
    * `relationship_type` (`RelationshipType!`): Type of relationship
    * `unified_user_id` (`String!`): UUID of UnifiedUser
    '''

    delete_unified_user_assignment = sgqlc.types.Field(DeleteUnifiedUserAssignment, graphql_name='deleteUnifiedUserAssignment', args=sgqlc.types.ArgDict((
        ('object_mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectMcon', default=None)),
        ('unified_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='unifiedUserId', default=None)),
))
    )
    '''Associate a UnifiedUser with a CatalogObject

    Arguments:

    * `object_mcon` (`String!`): MCON of catalog object
    * `unified_user_id` (`String!`): UUID of UnifiedUser
    '''

    import_dbt_manifest = sgqlc.types.Field(ImportDbtManifest, graphql_name='importDbtManifest', args=sgqlc.types.ArgDict((
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('default_resource', sgqlc.types.Arg(String, graphql_name='defaultResource', default=None)),
        ('manifest_nodes_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='manifestNodesJson', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
))
    )
    '''Import DBT manifest

    Arguments:

    * `dbt_schema_version` (`String!`): DBT manifest schema version
    * `default_resource` (`String`): Warehouse name or uuid to
      associate dbt models with
    * `manifest_nodes_json` (`String!`): DBT manifest nodes in JSON
      format
    * `project_name` (`String`): dbt project name
    '''

    upload_dbt_manifest = sgqlc.types.Field('UploadDbtManifest', graphql_name='uploadDbtManifest', args=sgqlc.types.ArgDict((
        ('batch', sgqlc.types.Arg(Int, graphql_name='batch', default=1)),
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('default_resource', sgqlc.types.Arg(String, graphql_name='defaultResource', default=None)),
        ('invocation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invocationId', default=None)),
        ('manifest_nodes_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='manifestNodesJson', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
))
    )
    '''Upload DBT manifest

    Arguments:

    * `batch` (`Int`): Batch number, if a manifest file is broken up
      into smaller subsets of nodes (default: `1`)
    * `dbt_schema_version` (`String!`): DBT manifest schema version
    * `default_resource` (`String`): Associated warehouse name or uuid
    * `invocation_id` (`String!`): DBT invocation id
    * `manifest_nodes_json` (`String!`): DBT manifest nodes in JSON
      format
    * `project_name` (`String`): dbt project name
    '''

    import_dbt_run_results = sgqlc.types.Field(ImportDbtRunResults, graphql_name='importDbtRunResults', args=sgqlc.types.ArgDict((
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('run_id', sgqlc.types.Arg(String, graphql_name='runId', default=None)),
        ('run_logs', sgqlc.types.Arg(String, graphql_name='runLogs', default=None)),
        ('run_results_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='runResultsJson', default=None)),
))
    )
    '''Import DBT run results

    Arguments:

    * `dbt_schema_version` (`String!`): DBT run results schema version
    * `project_name` (`String`): dbt project name
    * `run_id` (`String`): dbt run ID
    * `run_logs` (`String`): dbt run logs
    * `run_results_json` (`String!`): DBT run results in JSON format
    '''

    upload_dbt_run_results = sgqlc.types.Field('UploadDbtRunResults', graphql_name='uploadDbtRunResults', args=sgqlc.types.ArgDict((
        ('batch', sgqlc.types.Arg(Int, graphql_name='batch', default=1)),
        ('dbt_schema_version', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dbtSchemaVersion', default=None)),
        ('invocation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invocationId', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('run_id', sgqlc.types.Arg(String, graphql_name='runId', default=None)),
        ('run_logs', sgqlc.types.Arg(String, graphql_name='runLogs', default=None)),
        ('run_results_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='runResultsJson', default=None)),
))
    )
    '''Upload DBT run results

    Arguments:

    * `batch` (`Int`): Batch number if run results are split across
      smaller files (default: `1`)
    * `dbt_schema_version` (`String!`): DBT run results schema version
    * `invocation_id` (`String!`): DBT invocation id
    * `project_name` (`String`): dbt project name
    * `run_id` (`String`): dbt run ID
    * `run_logs` (`String`): dbt run logs
    * `run_results_json` (`String!`): DBT run results in JSON format
    '''

    send_dbt_artifacts_event = sgqlc.types.Field('SendDbtArtifactsEvent', graphql_name='sendDbtArtifactsEvent', args=sgqlc.types.ArgDict((
        ('artifacts', sgqlc.types.Arg(sgqlc.types.non_null(DbtArtifactsInput), graphql_name='artifacts', default=None)),
        ('invocation_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='invocationId', default=None)),
        ('job_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jobName', default=None)),
        ('project_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectName', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
))
    )
    '''Publish a Dbt artifacts event to Kinesis stream

    Arguments:

    * `artifacts` (`DbtArtifactsInput!`): Artifacts to publish
    * `invocation_id` (`UUID!`): dbt invocation id
    * `job_name` (`String!`): dbt job name
    * `project_name` (`String!`): dbt project name
    * `resource_id` (`UUID`): Optional resource uuid
    '''

    set_group_repetitive_dbt_model_failures = sgqlc.types.Field('SetGroupRepetitiveDbtModelFailures', graphql_name='setGroupRepetitiveDbtModelFailures', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('group_repetitive_failures', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='groupRepetitiveFailures', default=None)),
))
    )
    '''Set whether to group dbt model failures with the same error
    message into the same incident

    Arguments:

    * `connection_id` (`UUID!`): dbt connection id
    * `group_repetitive_failures` (`Boolean!`): Failures with the same
      error message should be grouped together
    '''

    set_group_repetitive_dbt_test_failures = sgqlc.types.Field('SetGroupRepetitiveDbtTestFailures', graphql_name='setGroupRepetitiveDbtTestFailures', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('group_repetitive_failures', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='groupRepetitiveFailures', default=None)),
))
    )
    '''Set whether to group dbt test failures with the same error message
    into the same incident

    Arguments:

    * `connection_id` (`UUID!`): dbt connection id
    * `group_repetitive_failures` (`Boolean!`): Failures with the same
      error message should be grouped together
    '''

    set_generates_incidents = sgqlc.types.Field('SetGeneratesIncidents', graphql_name='setGeneratesIncidents', args=sgqlc.types.ArgDict((
        ('generates_incidents', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='generatesIncidents', default=None)),
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Set whether a dbt project generates incidents

    Arguments:

    * `generates_incidents` (`Boolean!`): should generate incidents
    * `uuid` (`UUID!`): dbt project uuid
    '''

    set_job_generates_incidents = sgqlc.types.Field('SetJobGeneratesIncidents', graphql_name='setJobGeneratesIncidents', args=sgqlc.types.ArgDict((
        ('generates_incidents', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='generatesIncidents', default=None)),
        ('job_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='jobId', default=None)),
))
    )
    '''Set whether a dbt job generates incidents

    Arguments:

    * `generates_incidents` (`Boolean!`): should generate incidents
    * `job_id` (`UUID!`): dbt job id
    '''

    snooze_dbt_node = sgqlc.types.Field('SnoozeDbtNode', graphql_name='snoozeDbtNode', args=sgqlc.types.ArgDict((
        ('dbt_node_uuid', sgqlc.types.Arg(UUID, graphql_name='dbtNodeUuid', default=None)),
        ('snooze_minutes', sgqlc.types.Arg(Int, graphql_name='snoozeMinutes', default=None)),
))
    )
    '''Snooze a DBT node (model/test). Data collection will continue, but
    no events will be reported.

    Arguments:

    * `dbt_node_uuid` (`UUID`): UUID for DBT node to snooze
    * `snooze_minutes` (`Int`): Number of minutes to snooze
    '''

    unsnooze_dbt_node = sgqlc.types.Field('UnsnoozeDbtNode', graphql_name='unsnoozeDbtNode', args=sgqlc.types.ArgDict((
        ('dbt_node_uuid', sgqlc.types.Arg(UUID, graphql_name='dbtNodeUuid', default=None)),
))
    )
    '''Un-snooze a DBT node (model/test).

    Arguments:

    * `dbt_node_uuid` (`UUID`): UUID for DBT node to un-snooze
    '''

    update_dbt_project_info = sgqlc.types.Field('UpdateDbtProjectInfo', graphql_name='updateDbtProjectInfo', args=sgqlc.types.ArgDict((
        ('remote_url', sgqlc.types.Arg(String, graphql_name='remoteUrl', default=None)),
        ('subdirectory', sgqlc.types.Arg(String, graphql_name='subdirectory', default=None)),
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Set extra information about dbt project

    Arguments:

    * `remote_url` (`String`): Remote location of the project sources
    * `subdirectory` (`String`): Subdirectory of the project sources
    * `uuid` (`UUID!`): dbt project id
    '''

    create_or_update_monte_carlo_config_template = sgqlc.types.Field(CreateOrUpdateMonteCarloConfigTemplate, graphql_name='createOrUpdateMonteCarloConfigTemplate', args=sgqlc.types.ArgDict((
        ('config_template_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='configTemplateJson', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=None)),
        ('misconfigured_as_warning', sgqlc.types.Arg(Boolean, graphql_name='misconfiguredAsWarning', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
        ('resource', sgqlc.types.Arg(String, graphql_name='resource', default=None)),
))
    )
    '''Create or update a Monte Carlo Config Template

    Arguments:

    * `config_template_json` (`String!`): Monte Carlo Template in JSON
      format
    * `dry_run` (`Boolean`): Dry run?
    * `misconfigured_as_warning` (`Boolean`): Misconfigured errors as
      warnings
    * `namespace` (`String!`): Namespace of config template
    * `resource` (`String`): Default resource (warehouse) ID or name
    '''

    create_or_update_monte_carlo_config_template_async = sgqlc.types.Field(CreateOrUpdateMonteCarloConfigTemplateAsync, graphql_name='createOrUpdateMonteCarloConfigTemplateAsync', args=sgqlc.types.ArgDict((
        ('config_template_json', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='configTemplateJson', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=None)),
        ('misconfigured_as_warning', sgqlc.types.Arg(Boolean, graphql_name='misconfiguredAsWarning', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
        ('resource', sgqlc.types.Arg(String, graphql_name='resource', default=None)),
))
    )
    '''Create or update a Monte Carlo Config Template asynchronously

    Arguments:

    * `config_template_json` (`String!`): Monte Carlo Template in JSON
      format
    * `dry_run` (`Boolean`): Dry run?
    * `misconfigured_as_warning` (`Boolean`): Misconfigured errors as
      warnings
    * `namespace` (`String!`): Namespace of config template
    * `resource` (`String`): Default resource (warehouse) ID or name
    '''

    delete_monte_carlo_config_template = sgqlc.types.Field(DeleteMonteCarloConfigTemplate, graphql_name='deleteMonteCarloConfigTemplate', args=sgqlc.types.ArgDict((
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
))
    )
    '''Delete a Monte Carlo Config Template

    Arguments:

    * `dry_run` (`Boolean`): Dry run?
    * `namespace` (`String!`): Namespace of config template
    '''

    set_sensitivity = sgqlc.types.Field('SetSensitivity', graphql_name='setSensitivity', args=sgqlc.types.ArgDict((
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(UUID, graphql_name='monitorUuid', default=None)),
        ('threshold', sgqlc.types.Arg(SensitivityInput, graphql_name='threshold', default=None)),
))
    )
    '''Arguments:

    * `event_type` (`String`): event type for which to get/set
      sensitivity
    * `mcon` (`String`): MCON of the object (e.g. table) for which to
      get/set sensitivity
    * `monitor_uuid` (`UUID`): UUID of an associated monitor
    * `threshold` (`SensitivityInput`): Custom threshold definition
    '''

    add_to_collection_block_list = sgqlc.types.Field(AddToCollectionBlockList, graphql_name='addToCollectionBlockList', args=sgqlc.types.ArgDict((
        ('collection_blocks', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CollectionBlockInput)), graphql_name='collectionBlocks', default=None)),
))
    )
    '''Adds to the list of entities for which metadata collection is not
    allowed on this account.

    Arguments:

    * `collection_blocks` (`[CollectionBlockInput]!`): The entries to
      be added to the collection block list.
    '''

    remove_from_collection_block_list = sgqlc.types.Field('RemoveFromCollectionBlockList', graphql_name='removeFromCollectionBlockList', args=sgqlc.types.ArgDict((
        ('collection_blocks', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CollectionBlockInput)), graphql_name='collectionBlocks', default=None)),
))
    )
    '''Removes from the list of entities for which metadata collection is
    not allowed on this account.

    Arguments:

    * `collection_blocks` (`[CollectionBlockInput]!`): The entries to
      be removed from the collection block list.
    '''

    create_custom_rule = sgqlc.types.Field(CreateCustomRule, graphql_name='createCustomRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
))
    )
    '''Deprecated, use CreateOrUpdateCustomRule instead

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `description` (`String`): Used as the name in the UI
    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `interval_minutes` (`Int`): How often to run scheduled custom
      rule check (DEPRECATED, use schedule instead)
    * `labels` (`[String]`): The monitor labels
    * `notes` (`String`): Additional context for the monitor
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `schedule_config` (`ScheduleConfigInput`): Schedule of custom
      rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `start_time` (`DateTime`): Start time of schedule (DEPRECATED,
      use schedule instead)
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    '''

    create_or_update_custom_rule = sgqlc.types.Field(CreateOrUpdateCustomRule, graphql_name='createOrUpdateCustomRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
))
    )
    '''Create or update a custom rule

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `description` (`String`): Used as the name in the UI
    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `interval_minutes` (`Int`): How often to run scheduled custom
      rule check (DEPRECATED, use schedule instead)
    * `labels` (`[String]`): The monitor labels
    * `notes` (`String`): Additional context for the monitor
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `schedule_config` (`ScheduleConfigInput`): Schedule of custom
      rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `start_time` (`DateTime`): Start time of schedule (DEPRECATED,
      use schedule instead)
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    '''

    create_or_update_volume_rule = sgqlc.types.Field(CreateOrUpdateVolumeRule, graphql_name='createOrUpdateVolumeRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('data_collection_schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='dataCollectionScheduleConfig', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('override', sgqlc.types.Arg(Boolean, graphql_name='override', default=None)),
        ('schedule_config', sgqlc.types.Arg(sgqlc.types.non_null(ScheduleConfigInput), graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
))
    )
    '''Create or update a Volume Rule

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `data_collection_schedule_config` (`ScheduleConfigInput`): Data
      Collection schedule of custom rule
    * `description` (`String!`): Description of rule
    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `labels` (`[String]`): The monitor labels
    * `notes` (`String`): Additional context for the rule
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `override` (`Boolean`): If override is set, it forces the dc
      schedule to run
    * `schedule_config` (`ScheduleConfigInput!`): Schedule of custom
      rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    '''

    create_custom_metric_rule = sgqlc.types.Field(CreateCustomMetricRule, graphql_name='createCustomMetricRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('custom_sampling_sql', sgqlc.types.Arg(String, graphql_name='customSamplingSql', default=None)),
        ('custom_sql', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customSql', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('field_metric', sgqlc.types.Arg(FieldMetricInput, graphql_name='fieldMetric', default=None)),
        ('field_query_parameters', sgqlc.types.Arg(FieldQueryParametersInput, graphql_name='fieldQueryParameters', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('query_result_type', sgqlc.types.Arg(QueryResultType, graphql_name='queryResultType', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
))
    )
    '''Deprecated, use CreateOrUpdateCustomMetricRule instead

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `connection_id` (`UUID`): Specify a connection (e.g. query-
      engine) to use
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `custom_sampling_sql` (`String`): Custom sampling SQL query to
      run on breach
    * `custom_sql` (`String!`): Custom SQL query to run
    * `description` (`String!`): Description of rule
    * `dw_id` (`UUID!`): Warehouse UUID
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `field_metric` (`FieldMetricInput`): Field metric parameters (if
      query generated by getFieldMetricQuery)
    * `field_query_parameters` (`FieldQueryParametersInput`): Field
      metric parameters (if query generated by getFieldQuery)
    * `interval_minutes` (`Int`): How often to run scheduled custom
      rule check (DEPRECATED, use schedule instead)
    * `labels` (`[String]`): The monitor labels
    * `notes` (`String`): Additional context for the rule
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `query_result_type` (`QueryResultType`): How the query result is
      used for the metric. Uses row count if unset.
    * `schedule_config` (`ScheduleConfigInput`): Schedule of custom
      rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `start_time` (`DateTime`): Start time of schedule (DEPRECATED,
      use schedule instead)
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    * `variables` (`JSONString`): Possible variable values for SQL
      query
    '''

    create_or_update_custom_metric_rule = sgqlc.types.Field(CreateOrUpdateCustomMetricRule, graphql_name='createOrUpdateCustomMetricRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('custom_sampling_sql', sgqlc.types.Arg(String, graphql_name='customSamplingSql', default=None)),
        ('custom_sql', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customSql', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('field_metric', sgqlc.types.Arg(FieldMetricInput, graphql_name='fieldMetric', default=None)),
        ('field_query_parameters', sgqlc.types.Arg(FieldQueryParametersInput, graphql_name='fieldQueryParameters', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('query_result_type', sgqlc.types.Arg(QueryResultType, graphql_name='queryResultType', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
))
    )
    '''Create or update a custom metric rule

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `connection_id` (`UUID`): Specify a connection (e.g. query-
      engine) to use
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `custom_sampling_sql` (`String`): Custom sampling SQL query to
      run on breach
    * `custom_sql` (`String!`): Custom SQL query to run
    * `description` (`String!`): Description of rule
    * `dw_id` (`UUID!`): Warehouse UUID
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `field_metric` (`FieldMetricInput`): Field metric parameters (if
      query generated by getFieldMetricQuery)
    * `field_query_parameters` (`FieldQueryParametersInput`): Field
      metric parameters (if query generated by getFieldQuery)
    * `interval_minutes` (`Int`): How often to run scheduled custom
      rule check (DEPRECATED, use schedule instead)
    * `labels` (`[String]`): The monitor labels
    * `notes` (`String`): Additional context for the rule
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `query_result_type` (`QueryResultType`): How the query result is
      used for the metric. Uses row count if unset.
    * `schedule_config` (`ScheduleConfigInput`): Schedule of custom
      rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `start_time` (`DateTime`): Start time of schedule (DEPRECATED,
      use schedule instead)
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    * `variables` (`JSONString`): Possible variable values for SQL
      query
    '''

    update_custom_metric_rule_notes = sgqlc.types.Field('UpdateCustomMetricRuleNotes', graphql_name='updateCustomMetricRuleNotes', args=sgqlc.types.ArgDict((
        ('custom_rule_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='customRuleUuid', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
))
    )
    '''Create or update notes for custom metric rule

    Arguments:

    * `custom_rule_uuid` (`UUID!`): UUID of custom rule, to update
      existing rule
    * `notes` (`String`): Additional context for the custom SQL rule
    '''

    update_custom_metric_severity = sgqlc.types.Field('UpdateCustomMetricSeverity', graphql_name='updateCustomMetricSeverity', args=sgqlc.types.ArgDict((
        ('custom_rule_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='customRuleUuid', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
))
    )
    '''Create or update default severity for custom metric rule

    Arguments:

    * `custom_rule_uuid` (`UUID!`): UUID of custom rule, to update
      existing rule
    * `severity` (`String`): System set severity when an incident for
      the rule is created
    '''

    create_or_update_freshness_custom_rule = sgqlc.types.Field(CreateOrUpdateFreshnessCustomRule, graphql_name='createOrUpdateFreshnessCustomRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
))
    )
    '''Create or update a freshness custom rule

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `description` (`String`): Used as the name in the UI
    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `interval_minutes` (`Int`): How often to run scheduled custom
      rule check (DEPRECATED, use schedule instead)
    * `labels` (`[String]`): The monitor labels
    * `notes` (`String`): Additional context for the monitor
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `schedule_config` (`ScheduleConfigInput`): Schedule of custom
      rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `start_time` (`DateTime`): Start time of schedule (DEPRECATED,
      use schedule instead)
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    '''

    snooze_custom_rule = sgqlc.types.Field('SnoozeCustomRule', graphql_name='snoozeCustomRule', args=sgqlc.types.ArgDict((
        ('snooze_minutes', sgqlc.types.Arg(Int, graphql_name='snoozeMinutes', default=None)),
        ('snooze_type', sgqlc.types.Arg(CustomRuleSnoozeInput, graphql_name='snoozeType', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Snooze a custom rule. Data collection will continue, but no
    anomalies will be reported.

    Arguments:

    * `snooze_minutes` (`Int`): Number of minutes to snooze rule -
      deprecated by snooze_type
    * `snooze_type` (`CustomRuleSnoozeInput`): Choose regular snooze
      or conditional snooze options
    * `uuid` (`UUID`): UUID for rule to snooze - deprecated by
      snooze_type
    '''

    unsnooze_custom_rule = sgqlc.types.Field('UnsnoozeCustomRule', graphql_name='unsnoozeCustomRule', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Un-snooze a custom rule.

    Arguments:

    * `uuid` (`UUID`): UUID for rule to un-snooze
    '''

    delete_custom_rule = sgqlc.types.Field(DeleteCustomRule, graphql_name='deleteCustomRule', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(UUID, graphql_name='warehouseUuid', default=None)),
))
    )
    '''Delete a custom rule

    Arguments:

    * `uuid` (`UUID`): UUID for rule to delete
    * `warehouse_uuid` (`UUID`): Deprecated
    '''

    trigger_custom_rule = sgqlc.types.Field('TriggerCustomRule', graphql_name='triggerCustomRule', args=sgqlc.types.ArgDict((
        ('custom_sql_contains', sgqlc.types.Arg(String, graphql_name='customSqlContains', default=None)),
        ('description_contains', sgqlc.types.Arg(String, graphql_name='descriptionContains', default=None)),
        ('rule_id', sgqlc.types.Arg(UUID, graphql_name='ruleId', default=None)),
))
    )
    '''Run a custom rule immediately

    Arguments:

    * `custom_sql_contains` (`String`): String to completely or
      partially match the rule SQL, case-insensitive
    * `description_contains` (`String`): String to completely or
      partially match the rule description, case-insensitive
    * `rule_id` (`UUID`): Rule id
    '''

    trigger_circuit_breaker_rule = sgqlc.types.Field('TriggerCircuitBreakerRule', graphql_name='triggerCircuitBreakerRule', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('rule_name', sgqlc.types.Arg(String, graphql_name='ruleName', default=None)),
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
))
    )
    '''Run a custom rule as a circuit breaker immediately. Supports rules
    that create a single query.

    Arguments:

    * `namespace` (`String`): Namespace
    * `rule_name` (`String`): Rule Name
    * `rule_uuid` (`UUID`): Rule UUID
    '''

    trigger_circuit_breaker_rule_v2 = sgqlc.types.Field('TriggerCircuitBreakerRuleV2', graphql_name='triggerCircuitBreakerRuleV2', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('rule_name', sgqlc.types.Arg(String, graphql_name='ruleName', default=None)),
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
))
    )
    '''Run a custom rule as a circuit breaker immediately. Supports rules
    that create multiple queries.

    Arguments:

    * `namespace` (`String`): Namespace
    * `rule_name` (`String`): Rule Name
    * `rule_uuid` (`UUID`): Rule UUID
    '''

    run_sql_rule = sgqlc.types.Field('RunSqlRule', graphql_name='runSqlRule', args=sgqlc.types.ArgDict((
        ('rule_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='ruleUuid', default=None)),
))
    )
    '''Run a SQL Rule manually

    Arguments:

    * `rule_uuid` (`UUID!`): Rule UUID
    '''

    create_or_update_lineage_node = sgqlc.types.Field(CreateOrUpdateLineageNode, graphql_name='createOrUpdateLineageNode', args=sgqlc.types.ArgDict((
        ('expire_at', sgqlc.types.Arg(DateTime, graphql_name='expireAt', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('object_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectId', default=None)),
        ('object_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='objectType', default=None)),
        ('properties', sgqlc.types.Arg(sgqlc.types.list_of(ObjectPropertyInput), graphql_name='properties', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('resource_name', sgqlc.types.Arg(String, graphql_name='resourceName', default=None)),
))
    )
    '''Create or update a lineage node

    Arguments:

    * `expire_at` (`DateTime`): When the node will expire. If not
      provided, the node will expire 7 days fromcreation.
    * `name` (`String`): Object name (table name, report name, etc)
    * `object_id` (`String!`): Object identifier
    * `object_type` (`String!`): Object type
    * `properties` (`[ObjectPropertyInput]`): A list of object
      properties to be indexed by the search service
    * `resource_id` (`UUID`): The id of the resource containing the
      node
    * `resource_name` (`String`): The name of the resource containing
      the node
    '''

    create_or_update_lineage_edge = sgqlc.types.Field(CreateOrUpdateLineageEdge, graphql_name='createOrUpdateLineageEdge', args=sgqlc.types.ArgDict((
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(NodeInput), graphql_name='destination', default=None)),
        ('expire_at', sgqlc.types.Arg(DateTime, graphql_name='expireAt', default=None)),
        ('source', sgqlc.types.Arg(sgqlc.types.non_null(NodeInput), graphql_name='source', default=None)),
))
    )
    '''Create or update a lineage edge

    Arguments:

    * `destination` (`NodeInput!`): The destination node
    * `expire_at` (`DateTime`): When the edge will expire. If not
      provided, the node will expire 7 days from creation.
    * `source` (`NodeInput!`): The source node
    '''

    create_or_update_lineage_node_block_pattern = sgqlc.types.Field(CreateOrUpdateLineageNodeBlockPattern, graphql_name='createOrUpdateLineageNodeBlockPattern', args=sgqlc.types.ArgDict((
        ('dataset_regexp', sgqlc.types.Arg(String, graphql_name='datasetRegexp', default=None)),
        ('project_regexp', sgqlc.types.Arg(String, graphql_name='projectRegexp', default=None)),
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='resourceId', default=None)),
        ('table_regexp', sgqlc.types.Arg(String, graphql_name='tableRegexp', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Create or update a node block pattern

    Arguments:

    * `dataset_regexp` (`String`): Block datasets matching the regexp
    * `project_regexp` (`String`): Block projects matching the regexp
    * `resource_id` (`UUID!`): The id of the resource containing the
      node
    * `table_regexp` (`String`): Block tables matching the regexp
    * `uuid` (`UUID`): The pattern UUID (updates only)
    '''

    create_or_update_lineage_node_replacement_rule = sgqlc.types.Field(CreateOrUpdateLineageNodeReplacementRule, graphql_name='createOrUpdateLineageNodeReplacementRule', args=sgqlc.types.ArgDict((
        ('case_insensitive', sgqlc.types.Arg(Boolean, graphql_name='caseInsensitive', default=None)),
        ('pattern', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='pattern', default=None)),
        ('replacement', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='replacement', default=None)),
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='resourceId', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Create or update a node replacement rule

    Arguments:

    * `case_insensitive` (`Boolean`): Case sensitivity of the pattern
      matching
    * `pattern` (`String!`): Modify canonical name by replacing the
      pattern with replacement
    * `replacement` (`String!`): Modify canonical name by replacing
      the pattern with replacement
    * `resource_id` (`UUID!`): The id of the resource containing the
      node
    * `uuid` (`UUID`): The rule UUID (updates only)
    '''

    delete_lineage_node = sgqlc.types.Field(DeleteLineageNode, graphql_name='deleteLineageNode', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    '''Delete a lineage node and any lineage edges connected to it.

    Arguments:

    * `mcon` (`String!`): The MCON of the node to be deleted
    '''

    delete_lineage_node_block_pattern = sgqlc.types.Field(DeleteLineageNodeBlockPattern, graphql_name='deleteLineageNodeBlockPattern', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Delete a lineage node block pattern.

    Arguments:

    * `uuid` (`UUID!`): The UUID of the pattern to delete
    '''

    delete_lineage_node_replacement_rule = sgqlc.types.Field(DeleteLineageNodeReplacementRule, graphql_name='deleteLineageNodeReplacementRule', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Delete a lineage node replacement rule

    Arguments:

    * `uuid` (`UUID!`): The UUID of the replacement rule to delete
    '''

    create_or_update_field_quality_rule = sgqlc.types.Field(CreateOrUpdateFieldQualityRule, graphql_name='createOrUpdateFieldQualityRule', args=sgqlc.types.ArgDict((
        ('comparisons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparisonInput)), graphql_name='comparisons', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(UUID, graphql_name='customRuleUuid', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('event_rollup_count', sgqlc.types.Arg(Int, graphql_name='eventRollupCount', default=None)),
        ('event_rollup_until_changed', sgqlc.types.Arg(Boolean, graphql_name='eventRollupUntilChanged', default=None)),
        ('field_names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fieldNames', default=None)),
        ('filters', sgqlc.types.Arg(sgqlc.types.list_of(FieldMetricFilterInput), graphql_name='filters', default=None)),
        ('interval_minutes', sgqlc.types.Arg(Int, graphql_name='intervalMinutes', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('metric_type', sgqlc.types.Arg(sgqlc.types.non_null(FieldMetricType), graphql_name='metricType', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('schedule_config', sgqlc.types.Arg(sgqlc.types.non_null(ScheduleConfigInput), graphql_name='scheduleConfig', default=None)),
        ('severity', sgqlc.types.Arg(String, graphql_name='severity', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='tableMcons', default=None)),
        ('timezone', sgqlc.types.Arg(String, graphql_name='timezone', default=None)),
))
    )
    '''Create or update a field quality rule

    Arguments:

    * `comparisons` (`[CustomRuleComparisonInput]!`): Custom rule
      comparisons
    * `connection_id` (`UUID`): Specify a connection (e.g. query-
      engine) to use
    * `custom_rule_uuid` (`UUID`): UUID of custom rule, to update
      existing rule
    * `description` (`String!`): Description of rule
    * `dw_id` (`UUID!`): Warehouse UUID
    * `event_rollup_count` (`Int`): The number of events to roll up
      into a single incident
    * `event_rollup_until_changed` (`Boolean`): If true, roll up
      events until the value changes
    * `field_names` (`[String]!`): Fields to monitor
    * `filters` (`[FieldMetricFilterInput]`): Filters for which rows
      the metric is computed over
    * `interval_minutes` (`Int`): How often to run scheduled custom
      rule check (DEPRECATED, use schedule instead)
    * `labels` (`[String]`): The monitor labels
    * `metric_type` (`FieldMetricType!`): Type of metric to compute
    * `notes` (`String`): Additional context for the rule
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `schedule_config` (`ScheduleConfigInput!`): Schedule of the
      field quality rule
    * `severity` (`String`): The default severity for incidents
      involving this monitor
    * `start_time` (`DateTime`): Start time of schedule (DEPRECATED,
      use schedule instead)
    * `table_mcons` (`[String]!`): MCON of tables to monitor
    * `timezone` (`String`): Timezone (DEPRECATED, use timezone in
      scheduleConfig instead
    '''

    create_or_update_catalog_object_metadata = sgqlc.types.Field(CreateOrUpdateCatalogObjectMetadata, graphql_name='createOrUpdateCatalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    '''Create or update an asset's metadata

    Arguments:

    * `description` (`String!`): Description of object
    * `mcon` (`String!`): Monte Carlo full identifier for an entity
    '''

    delete_catalog_object_metadata = sgqlc.types.Field(DeleteCatalogObjectMetadata, graphql_name='deleteCatalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    '''Delete metadata for an asset

    Arguments:

    * `mcon` (`String!`): Monte Carlo full identifier for an entity
    '''

    create_or_update_object_property = sgqlc.types.Field(CreateOrUpdateObjectProperty, graphql_name='createOrUpdateObjectProperty', args=sgqlc.types.ArgDict((
        ('mcon_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mconId', default=None)),
        ('property_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='propertyName', default=None)),
        ('property_source_type', sgqlc.types.Arg(String, graphql_name='propertySourceType', default='dashboard')),
        ('property_value', sgqlc.types.Arg(String, graphql_name='propertyValue', default=None)),
))
    )
    '''Create or update properties (tags) for objects (e.g. tables,
    fields, etc.)

    Arguments:

    * `mcon_id` (`String!`): Monte Carlo full identifier for an entity
    * `property_name` (`String!`): Name of the property (AKA tag key)
    * `property_source_type` (`String`): Where property originated.
      (default: `"dashboard"`)
    * `property_value` (`String`): Value of the property (AKA tag
      value)
    '''

    delete_object_property = sgqlc.types.Field(DeleteObjectProperty, graphql_name='deleteObjectProperty', args=sgqlc.types.ArgDict((
        ('mcon_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mconId', default=None)),
        ('property_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='propertyName', default=None)),
        ('property_source_type', sgqlc.types.Arg(String, graphql_name='propertySourceType', default='dashboard')),
))
    )
    '''Delete properties (tags) for objects (e.g. tables, fields, etc.)

    Arguments:

    * `mcon_id` (`String!`): Monte Carlo full identifier for an entity
    * `property_name` (`String!`): Name of the property (AKA tag key)
    * `property_source_type` (`String`): Where property originated.
      (default: `"dashboard"`)
    '''

    bulk_create_or_update_object_properties = sgqlc.types.Field(BulkCreateOrUpdateObjectProperties, graphql_name='bulkCreateOrUpdateObjectProperties', args=sgqlc.types.ArgDict((
        ('input_object_properties', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(InputObjectProperty)), graphql_name='inputObjectProperties', default=None)),
))
    )
    '''Create or update a list of properties (tags) for objects (e.g.
    tables, fields, etc.)

    Arguments:

    * `input_object_properties` (`[InputObjectProperty]!`): List of
      object properties to create and update
    '''

    create_or_update_monitor_label = sgqlc.types.Field(CreateOrUpdateMonitorLabel, graphql_name='createOrUpdateMonitorLabel', args=sgqlc.types.ArgDict((
        ('label', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='label', default=None)),
        ('monitor_uuids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='monitorUuids', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Create or update a monitor label

    Arguments:

    * `label` (`String!`): The monitor label name
    * `monitor_uuids` (`[UUID]`): If any monitor IDs are given, add
      this label to those monitors; additive only, does not remove the
      label from other monitors
    * `uuid` (`UUID`): The monitor label ID
    '''

    delete_monitor_label = sgqlc.types.Field(DeleteMonitorLabel, graphql_name='deleteMonitorLabel', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Delete a monitor label

    Arguments:

    * `uuid` (`UUID!`): The monitor label ID
    '''

    stop_monitor = sgqlc.types.Field('StopMonitor', graphql_name='stopMonitor', args=sgqlc.types.ArgDict((
        ('monitor_id', sgqlc.types.Arg(UUID, graphql_name='monitorId', default=None)),
))
    )
    '''Deletes a monitor

    Arguments:

    * `monitor_id` (`UUID`)None
    '''

    delete_monitor = sgqlc.types.Field(DeleteMonitor, graphql_name='deleteMonitor', args=sgqlc.types.ArgDict((
        ('monitor_id', sgqlc.types.Arg(UUID, graphql_name='monitorId', default=None)),
))
    )
    '''Deletes a monitor

    Arguments:

    * `monitor_id` (`UUID`)None
    '''

    trigger_monitor = sgqlc.types.Field('TriggerMonitor', graphql_name='triggerMonitor', args=sgqlc.types.ArgDict((
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Deletes a monitor

    Arguments:

    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Trigger monitor by mcon
    * `monitor_type` (`String`): Specify the monitor type. Required
      when using an mcon or full table id
    * `resource_id` (`UUID`): Specify the resource uuid (e.g.
      warehouse the table is contained in) when using a fullTableId
    * `uuid` (`UUID`): Trigger monitor by a UUID
    '''

    create_or_update_monitor = sgqlc.types.Field(CreateOrUpdateMonitor, graphql_name='createOrUpdateMonitor', args=sgqlc.types.ArgDict((
        ('agg_select_expression', sgqlc.types.Arg(String, graphql_name='aggSelectExpression', default=None)),
        ('agg_time_interval', sgqlc.types.Arg(MonitorAggTimeInterval, graphql_name='aggTimeInterval', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('disable_look_back_bootstrap', sgqlc.types.Arg(Boolean, graphql_name='disableLookBackBootstrap', default=False)),
        ('failed_schedule_account_notification_id', sgqlc.types.Arg(UUID, graphql_name='failedScheduleAccountNotificationId', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fields', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('lookback_days', sgqlc.types.Arg(Int, graphql_name='lookbackDays', default=1)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
        ('notes', sgqlc.types.Arg(String, graphql_name='notes', default=None)),
        ('notify_rule_run_failure', sgqlc.types.Arg(Boolean, graphql_name='notifyRuleRunFailure', default=False)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('schedule_config', sgqlc.types.Arg(ScheduleConfigInput, graphql_name='scheduleConfig', default=None)),
        ('segmented_expressions', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='segmentedExpressions', default=None)),
        ('select_expressions', sgqlc.types.Arg(sgqlc.types.list_of(MonitorSelectExpressionInput), graphql_name='selectExpressions', default=None)),
        ('time_axis_name', sgqlc.types.Arg(String, graphql_name='timeAxisName', default=None)),
        ('time_axis_type', sgqlc.types.Arg(String, graphql_name='timeAxisType', default=None)),
        ('unnest_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='unnestFields', default=None)),
        ('use_partition_clause', sgqlc.types.Arg(Boolean, graphql_name='usePartitionClause', default=False)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('where_condition', sgqlc.types.Arg(String, graphql_name='whereCondition', default=None)),
))
    )
    '''Arguments:

    * `agg_select_expression` (`String`): For dimension monitoring,
      the aggregation select expression to use (defaults to COUNT(*))
    * `agg_time_interval` (`MonitorAggTimeInterval`): For field health
      and dimension monitoring, the aggregation time interval to use.
      Either HOUR or DAY (defaults to HOUR)
    * `connection_id` (`UUID`): Specify a connection (e.g. query-
      engine) to use
    * `description` (`String`): Used as the name in the UI
    * `disable_look_back_bootstrap` (`Boolean`): The flag decides
      whether to disable look back bootstrap for new monitors. By
      default, it's False (default: `false`)
    * `failed_schedule_account_notification_id` (`UUID`): Account
      notification to be used when the monitor's scheduled executions
      fail.
    * `fields` (`[String]`): Fields to monitor. DEPRECATED, use
      select_expressions instead.
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `labels` (`[String]`): The monitor labels
    * `lookback_days` (`Int`): Look-back period in days (to be applied
      by time axis) (default: `1`)
    * `mcon` (`String`): Mcon of table to create monitor for
    * `monitor_type` (`String`): Type of monitor to create
    * `notes` (`String`): Additional context for the monitor
    * `notify_rule_run_failure` (`Boolean`): The flag decides whether
      to send run failure notifications to audiences (default:
      `false`)
    * `resource_id` (`UUID`): Resource (e.g. warehouse) the table is
      contained in. Required when using a fullTableId
    * `schedule_config` (`ScheduleConfigInput`): Schedule of monitor
    * `segmented_expressions` (`[String]`): Fields or expressions used
      to segment the monitored field (currently supports one such
      value)
    * `select_expressions` (`[MonitorSelectExpressionInput]`): Monitor
      select expressions
    * `time_axis_name` (`String`): Time axis name
    * `time_axis_type` (`String`): Time axis type
    * `unnest_fields` (`[String]`): Fields to unnest
    * `use_partition_clause` (`Boolean`): Whether to use automatic
      partition filter in query (default: `false`)
    * `uuid` (`UUID`): UUID of the monitor. If specified, it means the
      request is for update
    * `where_condition` (`String`): SQL WHERE condition to apply to
      query
    '''

    pause_monitor = sgqlc.types.Field('PauseMonitor', graphql_name='pauseMonitor', args=sgqlc.types.ArgDict((
        ('pause', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='pause', default=None)),
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Pause a monitor from collecting data.'

    Arguments:

    * `pause` (`Boolean!`): Pause state of the monitor.
    * `uuid` (`UUID!`): UUID of the monitor whose skip status is being
      changed.
    '''

    validate_cron = sgqlc.types.Field('ValidateCron', graphql_name='validateCron', args=sgqlc.types.ArgDict((
        ('allow_multiple', sgqlc.types.Arg(Boolean, graphql_name='allowMultiple', default=None)),
        ('cron', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='cron', default=None)),
))
    )
    '''Validate a CRON expression

    Arguments:

    * `allow_multiple` (`Boolean`): Allow multiple CRON expressions
    * `cron` (`String!`): CRON expression
    '''

    create_event_comment = sgqlc.types.Field('createEventComment', graphql_name='createEventComment', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='eventId', default=None)),
        ('event_text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='eventText', default=None)),
))
    )
    '''Arguments:

    * `event_id` (`UUID!`)None
    * `event_text` (`String!`)None
    '''

    update_event_comment = sgqlc.types.Field('updateEventComment', graphql_name='updateEventComment', args=sgqlc.types.ArgDict((
        ('event_comment_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='eventCommentId', default=None)),
        ('event_text', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='eventText', default=None)),
))
    )
    '''Arguments:

    * `event_comment_id` (`UUID!`)None
    * `event_text` (`String!`)None
    '''

    delete_event_comment = sgqlc.types.Field('deleteEventComment', graphql_name='deleteEventComment', args=sgqlc.types.ArgDict((
        ('event_comment_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='eventCommentId', default=None)),
))
    )
    '''Arguments:

    * `event_comment_id` (`UUID!`)None
    '''

    set_incident_feedback = sgqlc.types.Field('SetIncidentFeedbackPayload', graphql_name='setIncidentFeedback', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetIncidentFeedbackInput), graphql_name='input', default=None)),
))
    )
    '''Provide feedback for an incident

    Arguments:

    * `input` (`SetIncidentFeedbackInput!`)None
    '''

    set_incident_reaction = sgqlc.types.Field('SetIncidentReaction', graphql_name='setIncidentReaction', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('reaction', sgqlc.types.Arg(sgqlc.types.non_null(IncidentReactionInput), graphql_name='reaction', default=None)),
))
    )
    '''Arguments:

    * `incident_id` (`UUID!`): The incident's UUID
    * `reaction` (`IncidentReactionInput!`): Incident reaction input
    '''

    set_incident_severity = sgqlc.types.Field('SetIncidentSeverity', graphql_name='setIncidentSeverity', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('severity', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='severity', default=None)),
))
    )
    '''Set severity for an existing incident

    Arguments:

    * `incident_id` (`UUID!`): The incident's UUID
    * `severity` (`String!`): Incident severity to set
    '''

    set_incident_owner = sgqlc.types.Field('SetIncidentOwner', graphql_name='setIncidentOwner', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('owner', sgqlc.types.Arg(String, graphql_name='owner', default=None)),
))
    )
    '''Set an owner for an existing incident

    Arguments:

    * `incident_id` (`UUID!`): The incident's UUID
    * `owner` (`String`): Incident owner to set
    '''

    create_or_update_incident_comment = sgqlc.types.Field(CreateOrUpdateIncidentComment, graphql_name='createOrUpdateIncidentComment', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='comment', default=None)),
        ('comment_id', sgqlc.types.Arg(UUID, graphql_name='commentId', default=None)),
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''Creates or updates a comment on an incident

    Arguments:

    * `comment` (`String!`): Content of the comment
    * `comment_id` (`UUID`): UUID of the comment. If set, this call is
      for updating the comment
    * `incident_id` (`UUID!`): The incident's UUID
    '''

    delete_incident_comment = sgqlc.types.Field(DeleteIncidentComment, graphql_name='deleteIncidentComment', args=sgqlc.types.ArgDict((
        ('comment_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='commentId', default=None)),
))
    )
    '''Deletes an incident's comment

    Arguments:

    * `comment_id` (`UUID!`): UUID of the comment for update
    '''

    split_incident = sgqlc.types.Field('SplitIncident', graphql_name='splitIncident', args=sgqlc.types.ArgDict((
        ('event_uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='eventUuids', default=None)),
        ('incident_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentUuid', default=None)),
        ('send_notification', sgqlc.types.Arg(Boolean, graphql_name='sendNotification', default=False)),
))
    )
    '''Splits event/s from incident into a new incident

    Arguments:

    * `event_uuids` (`[UUID]!`): unique identifier of event/s to split
      to new incident
    * `incident_uuid` (`UUID!`): Incident unique identifier
    * `send_notification` (`Boolean`): Whether to send a notification
      for the new incident (default: `false`)
    '''

    create_or_update_domain = sgqlc.types.Field(CreateOrUpdateDomain, graphql_name='createOrUpdateDomain', args=sgqlc.types.ArgDict((
        ('assignments', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='assignments', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(TagKeyValuePairInput), graphql_name='tags', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Create or update a domain

    Arguments:

    * `assignments` (`[String]`): Objects assigned to domain (as
      MCONs)
    * `description` (`String`): Description of the domain
    * `name` (`String!`): Domain name
    * `tags` (`[TagKeyValuePairInput]`): Filter by tag key/value pairs
      for tables.
    * `uuid` (`UUID`): UUID of domain to update
    '''

    delete_domain = sgqlc.types.Field(DeleteDomain, graphql_name='deleteDomain', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Delete a domain

    Arguments:

    * `uuid` (`UUID!`): UUID of domain to delete
    '''

    create_or_update_authorization_group = sgqlc.types.Field(CreateOrUpdateAuthorizationGroup, graphql_name='createOrUpdateAuthorizationGroup', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('domain_restriction_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='domainRestrictionIds', default=None)),
        ('label', sgqlc.types.Arg(String, graphql_name='label', default=None)),
        ('member_user_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='memberUserIds', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('roles', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='roles', default=None)),
        ('sso_group', sgqlc.types.Arg(String, graphql_name='ssoGroup', default=None)),
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
))
    )
    '''Create or update an authorization group.

    Arguments:

    * `description` (`String`): Description/help text to help users
      understand the purpose of the group. If not provided on updates,
      will keep current value.
    * `domain_restriction_ids` (`[UUID]`): Optional list of domain IDs
      to restrict access to. If not provided, will clear/apply no
      restrictions.
    * `label` (`String`): UI/user-friendly display name, ex: Data
      Consumers. If not provided on updates, will keep current value.
    * `member_user_ids` (`[String]`): User IDs of group members. If
      not provided, no changes to membership will be performed.
    * `name` (`String!`): Unique to the account, human-readable name
      (for use in code/policy reference).
    * `roles` (`[String]!`): Role names assigned to the group.
    * `sso_group` (`String`): SSO group name to map this authorization
      group to
    * `version` (`String`): Version of the permissions definitions the
      group is designed for ex: 2022-03-17. Defaults to system
      current. If not provided on updates, will keep current value.
    '''

    delete_authorization_group = sgqlc.types.Field(DeleteAuthorizationGroup, graphql_name='deleteAuthorizationGroup', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Delete an authorization group

    Arguments:

    * `name` (`String`): Unique to the account, human-readable name
      name (for use in code/policy reference).
    '''

    update_user_authorization_group_membership = sgqlc.types.Field('UpdateUserAuthorizationGroupMembership', graphql_name='updateUserAuthorizationGroupMembership', args=sgqlc.types.ArgDict((
        ('group_names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='groupNames', default=None)),
        ('member_user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='memberUserId', default=None)),
))
    )
    '''Update a user's authorization group membership. Authenticated user
    must have permission to manage users.

    Arguments:

    * `group_names` (`[String]!`): List of authorization group names
      the user should be a member of.
    * `member_user_id` (`String!`): User ID for the user whose
      membership is being updated.
    '''

    create_or_update_resource = sgqlc.types.Field(CreateOrUpdateResource, graphql_name='createOrUpdateResource', args=sgqlc.types.ArgDict((
        ('is_default', sgqlc.types.Arg(Boolean, graphql_name='isDefault', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Create or update a resource

    Arguments:

    * `is_default` (`Boolean`): If the account's default resource
    * `name` (`String`): The resource name
    * `type` (`String`): The resource type
    * `uuid` (`UUID`): The resource id
    '''

    match_and_create_bi_warehouse_sources = sgqlc.types.Field(MatchAndCreateBiWarehouseSources, graphql_name='matchAndCreateBiWarehouseSources', args=sgqlc.types.ArgDict((
        ('bi_container_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='biContainerId', default=None)),
        ('bi_warehouse_sources', sgqlc.types.Arg(sgqlc.types.list_of(BiWarehouseSourcesInput), graphql_name='biWarehouseSources', default=None)),
))
    )
    '''Create or update a BI warehouse source. If BI warehouse source
    details are provided in thebi_warehouse_sources parameter then
    those are saved. Else, details are pulled from the BIAPIs, matched
    with warehouses in Monte Carlo and details saved only if there is
    a full match.

    Arguments:

    * `bi_container_id` (`UUID!`): Monte Carlo UUID of the BI
      container
    * `bi_warehouse_sources` (`[BiWarehouseSourcesInput]`): BI
      warehouse source details that should be saved in Monte Carlo.
    '''

    toggle_disable_sampling = sgqlc.types.Field('ToggleDisableSampling', graphql_name='toggleDisableSampling', args=sgqlc.types.ArgDict((
        ('disable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='disable', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    '''Enable/disable the sampling data feature

    Arguments:

    * `disable` (`Boolean!`): If true, disable the sampling data
      feature
    * `dw_id` (`UUID!`): The warehouse's UUID
    '''

    toggle_disable_value_ingestion = sgqlc.types.Field('ToggleDisableValueIngestion', graphql_name='toggleDisableValueIngestion', args=sgqlc.types.ArgDict((
        ('disable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='disable', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    '''Enable/disable the value ingestion feature

    Arguments:

    * `disable` (`Boolean!`): If true, disable the value ingestion
      feature
    * `dw_id` (`UUID!`): The warehouse's UUID
    '''

    toggle_disable_value_sampling_when_testing = sgqlc.types.Field('ToggleDisableValueSamplingWhenTesting', graphql_name='toggleDisableValueSamplingWhenTesting', args=sgqlc.types.ArgDict((
        ('disable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='disable', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    '''Enable/disable the sampling data feature when testing value-based
    sql rules

    Arguments:

    * `disable` (`Boolean!`): If true, disable the feature
    * `dw_id` (`UUID!`): The warehouse's UUID
    '''

    toggle_enable_full_distribution_metrics = sgqlc.types.Field('ToggleFullDistributionMetrics', graphql_name='toggleEnableFullDistributionMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
))
    )
    '''Enable/disable collection of full distribution metrics for a
    particular warehouse

    Arguments:

    * `dw_id` (`UUID!`): The warehouse's UUID
    * `enable` (`Boolean!`): If true, enable full distribution metrics
    '''

    save_table_importance_stats = sgqlc.types.Field('SaveTableImportanceStats', graphql_name='saveTableImportanceStats', args=sgqlc.types.ArgDict((
        ('importance_score', sgqlc.types.Arg(Float, graphql_name='importanceScore', default=None)),
        ('is_important', sgqlc.types.Arg(Boolean, graphql_name='isImportant', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    '''Save custom table stats for a table

    Arguments:

    * `importance_score` (`Float`): User-provided importance score.
    * `is_important` (`Boolean`): Whether the table is a key asset or
      not.
    * `mcon` (`String!`): The MCON of the table whose stats are being
      updated.
    '''

    set_default_incident_group_interval = sgqlc.types.Field('SetDefaultIncidentGroupInterval', graphql_name='setDefaultIncidentGroupInterval', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('interval', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='interval', default=None)),
))
    )
    '''Set default incident grouping interval (in hours) for a warehouse.

    Arguments:

    * `dw_id` (`UUID!`): The warehouse's UUID.
    * `interval` (`Int!`): Interval in hours.
    '''

    create_or_update_data_maintenance_entry = sgqlc.types.Field(CreateOrUpdateDataMaintenanceEntry, graphql_name='createOrUpdateDataMaintenanceEntry', args=sgqlc.types.ArgDict((
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
        ('maintenance_type', sgqlc.types.Arg(DataMaintenanceMetric, graphql_name='maintenanceType', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('project', sgqlc.types.Arg(String, graphql_name='project', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
))
    )
    '''Creates or updates a data maintenance period

    Arguments:

    * `dataset` (`String`): Name of dataset to to set maintenance
      period for
    * `dw_id` (`UUID!`): Warehouse UUID
    * `end_time` (`DateTime`): Start period of data maintenance. If
      not set, all future data will be ignored until updated
    * `id` (`Int`): ID of existing data maintenance entry for updating
    * `maintenance_type` (`DataMaintenanceMetric`): If not set, all
      metrics for the object will be ignored
    * `mcon` (`String`): MC Unique identifier of object to set
      maintenance period for
    * `project` (`String`): Name of database or project to to set
      maintenance period for
    * `start_time` (`DateTime`): Start period of data maintenance. If
      not set, all previous data will be ignored.
    '''

    toggle_wildcard_aggregation = sgqlc.types.Field('ToggleWildcardAggregation', graphql_name='toggleWildcardAggregation', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
))
    )
    '''Enables/disable aggregation of wildcard tables (defaults to yearly
    and monthly templates)

    Arguments:

    * `dw_id` (`UUID!`): The warehouse's UUID
    * `enable` (`Boolean!`): If true, enable full wildcard aggregation
    '''

    set_wildcard_templates = sgqlc.types.Field('SetWildcardTemplates', graphql_name='setWildcardTemplates', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('templates', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(WildcardTemplateInput)), graphql_name='templates', default=None)),
))
    )
    '''Sets the templates to use for wildcard aggregation (overrides
    existing templates)

    Arguments:

    * `dw_id` (`UUID!`): The warehouse's UUID
    * `templates` (`[WildcardTemplateInput]!`): List of templates to
      use to aggregate wildcard tables
    '''

    delete_data_maintenance_entry = sgqlc.types.Field(DeleteDataMaintenanceEntry, graphql_name='deleteDataMaintenanceEntry', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    '''Delete a data maintenance window

    Arguments:

    * `id` (`Int!`): ID of existing data maintenance entry for
      deleting
    '''

    create_or_update_user_settings = sgqlc.types.Field(CreateOrUpdateUserSettings, graphql_name='createOrUpdateUserSettings', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('value', sgqlc.types.Arg(JSONString, graphql_name='value', default=None)),
))
    )
    '''Create a new user-specific setting

    Arguments:

    * `description` (`String`): Description for this user's settings
    * `key` (`String!`): User setting key
    * `value` (`JSONString`): User settings
    '''

    update_user_state = sgqlc.types.Field('UpdateUserStatePayload', graphql_name='updateUserState', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserStateInput), graphql_name='input', default=None)),
))
    )
    '''Arguments:

    * `input` (`UpdateUserStateInput!`)None
    '''

    update_account_display_assets_search_tags = sgqlc.types.Field('UpdateAccountDisplayCatalogSearchTags', graphql_name='updateAccountDisplayAssetsSearchTags', args=sgqlc.types.ArgDict((
        ('display', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='display', default=None)),
))
    )
    '''Updates account-level setting for displaying search tags on assets
    ui

    Arguments:

    * `display` (`Boolean!`)None
    '''

    set_account_name = sgqlc.types.Field('SetAccountName', graphql_name='setAccountName', args=sgqlc.types.ArgDict((
        ('account_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='accountName', default=None)),
))
    )
    '''Arguments:

    * `account_name` (`String!`)None
    '''

    set_warehouse_name = sgqlc.types.Field('SetWarehouseName', graphql_name='setWarehouseName', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    '''Set friendly name for a warehouse.

    Arguments:

    * `dw_id` (`UUID!`): UUID of the warehouse to update.
    * `name` (`String!`): Desired name.
    '''

    create_or_update_saml_identity_provider = sgqlc.types.Field(CreateOrUpdateSamlIdentityProvider, graphql_name='createOrUpdateSamlIdentityProvider', args=sgqlc.types.ArgDict((
        ('default_authorization_groups', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='defaultAuthorizationGroups', default=None)),
        ('domains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='domains', default=None)),
        ('metadata', sgqlc.types.Arg(String, graphql_name='metadata', default=None)),
        ('metadata_url', sgqlc.types.Arg(String, graphql_name='metadataUrl', default=None)),
))
    )
    '''Arguments:

    * `default_authorization_groups` (`[String]`): One or more
      authorization group names to assign to new SSO users who do not
      have an invite. If none/not set, it means new users must wait to
      be assigned group to gain any access.
    * `domains` (`[String]!`): A list of domains authorized by the IdP
    * `metadata` (`String`): The metadata in XML format, encoded as
      base64
    * `metadata_url` (`String`): The URL of the metadata file
    '''

    delete_saml_identity_provider = sgqlc.types.Field(DeleteSamlIdentityProvider, graphql_name='deleteSamlIdentityProvider')

    invite_users = sgqlc.types.Field(InviteUsersPayload, graphql_name='inviteUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InviteUsersInput), graphql_name='input', default=None)),
))
    )
    '''DEPRECATED: use inviteUsersV2

    Arguments:

    * `input` (`InviteUsersInput!`)None
    '''

    invite_users_v2 = sgqlc.types.Field(InviteUsersV2, graphql_name='inviteUsersV2', args=sgqlc.types.ArgDict((
        ('auth_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='authGroups', default=None)),
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails', default=None)),
        ('invitation_type', sgqlc.types.Arg(InvitationType, graphql_name='invitationType', default=None)),
))
    )
    '''Invite users to the account

    Arguments:

    * `auth_groups` (`[String]!`): Names of groups to add user to upon
      acceptance.
    * `emails` (`[String]!`): List of email addresses to invite
    * `invitation_type` (`InvitationType`): Type of invitation to send
      --typically maps to product.
    '''

    switch_user_account = sgqlc.types.Field('SwitchUserAccount', graphql_name='switchUserAccount', args=sgqlc.types.ArgDict((
        ('switch_to_account_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='switchToAccountId', default=None)),
        ('verification_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='verificationToken', default=None)),
))
    )
    '''User can switch accounts if provided with valid invite

    Arguments:

    * `switch_to_account_id` (`UUID!`)None
    * `verification_token` (`String!`)None
    '''

    delete_user_invite = sgqlc.types.Field(DeleteUserInvite, graphql_name='deleteUserInvite', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails', default=None)),
))
    )
    '''Delete user invite

    Arguments:

    * `emails` (`[String]!`): List of email addresses to invite
    '''

    resend_user_invite = sgqlc.types.Field('ReInviteUsers', graphql_name='resendUserInvite', args=sgqlc.types.ArgDict((
        ('emails', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='emails', default=None)),
))
    )
    '''Resend user invite

    Arguments:

    * `emails` (`[String]!`): List of email addresses to resend the
      invitation
    '''

    remove_user_from_account = sgqlc.types.Field('RemoveUserFromAccount', graphql_name='removeUserFromAccount', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    '''Remove user from account

    Arguments:

    * `email` (`String!`): Email address of user
    '''

    disable_user = sgqlc.types.Field(DisableUser, graphql_name='disableUser', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    '''Disable a user

    Arguments:

    * `email` (`String!`): Email address of user
    '''

    track_table = sgqlc.types.Field('TrackTablePayload', graphql_name='trackTable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TrackTableInput), graphql_name='input', default=None)),
))
    )
    '''Add table to account's dashboard

    Arguments:

    * `input` (`TrackTableInput!`)None
    '''

    upload_credentials = sgqlc.types.Field('UploadWarehouseCredentialsMutation', graphql_name='uploadCredentials', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
))
    )
    '''Arguments:

    * `file` (`Upload!`)None
    '''

    save_slack_credentials = sgqlc.types.Field('SaveSlackCredentialsMutation', graphql_name='saveSlackCredentials', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(String, graphql_name='key', default=None)),
        ('slack_app_type', sgqlc.types.Arg(SlackAppType, graphql_name='slackAppType', default=None)),
        ('slack_installation_uuid', sgqlc.types.Arg(String, graphql_name='slackInstallationUuid', default=None)),
))
    )
    '''Arguments:

    * `key` (`String`): Slack installation UUID (deprecated, use
      slackInstallationUuid
    * `slack_app_type` (`SlackAppType`): Slack App Type
    * `slack_installation_uuid` (`String`): Slack installation UUID
    '''

    deauthorize_slack_app = sgqlc.types.Field(DeauthorizeSlackAppMutation, graphql_name='deauthorizeSlackApp', args=sgqlc.types.ArgDict((
        ('slack_app_type', sgqlc.types.Arg(sgqlc.types.non_null(SlackAppType), graphql_name='slackAppType', default=None)),
))
    )
    '''Arguments:

    * `slack_app_type` (`SlackAppType!`): Slack App Type
    '''

    test_credentials = sgqlc.types.Field('TestCredentialsMutation', graphql_name='testCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default='bigquery')),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('project_id', sgqlc.types.Arg(String, graphql_name='projectId', default=None)),
))
    )
    '''Test credentials where the temp key already exists (e.g. BQ)

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `connection_type` (`String`): The type of connection to add
      (default: `"bigquery"`)
    * `key` (`String!`): Temp key from testing connections
    * `project_id` (`String`): BQ project ID if adding for a specific
      project only (lists otherwise)
    '''

    test_database_credentials = sgqlc.types.Field('TestDatabaseCredentials', graphql_name='testDatabaseCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default=None)),
        ('db_name', sgqlc.types.Arg(String, graphql_name='dbName', default=None)),
        ('db_type', sgqlc.types.Arg(String, graphql_name='dbType', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('ssl_options', sgqlc.types.Arg(SslInputOptions, graphql_name='sslOptions', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
))
    )
    '''Test a generic warehouse or database connection

    Arguments:

    * `assumable_role` (`String`): AWS role that can be assumed by the
      DC
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `connection_type` (`String`): Type of connection (e.g.
      snowflake, redshift)
    * `db_name` (`String`): Name of database to add connection for
    * `db_type` (`String`): Type of database to add connection for
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `host` (`String`): Hostname of the warehouse
    * `password` (`String`): User's password
    * `port` (`Int`): HTTP Port to use
    * `ssl_options` (`SslInputOptions`): Specify any SSL options (e.g.
      certs)
    * `user` (`String`): User with access to the database
    '''

    test_presto_credentials = sgqlc.types.Field('TestPrestoCredentials', graphql_name='testPrestoCredentials', args=sgqlc.types.ArgDict((
        ('catalog', sgqlc.types.Arg(String, graphql_name='catalog', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('http_scheme', sgqlc.types.Arg(String, graphql_name='httpScheme', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('schema', sgqlc.types.Arg(String, graphql_name='schema', default=None)),
        ('ssl_options', sgqlc.types.Arg(SslInputOptions, graphql_name='sslOptions', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
))
    )
    '''Test connection to Presto

    Arguments:

    * `catalog` (`String`): Mount point to access data source
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `host` (`String`): Hostname
    * `http_scheme` (`String`): Scheme for authentication
    * `password` (`String`): User's password
    * `port` (`Int`): HTTP port
    * `schema` (`String`): Schema to access
    * `ssl_options` (`SslInputOptions`): Specify any ssl options
    * `user` (`String`): Username with access to catalog/schema
    '''

    test_snowflake_credentials = sgqlc.types.Field('TestSnowflakeCredentials', graphql_name='testSnowflakeCredentials', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(String, graphql_name='account', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('private_key', sgqlc.types.Arg(String, graphql_name='privateKey', default=None)),
        ('private_key_passphrase', sgqlc.types.Arg(String, graphql_name='privateKeyPassphrase', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
        ('warehouse', sgqlc.types.Arg(String, graphql_name='warehouse', default=None)),
))
    )
    '''Test a Snowflake connection

    Arguments:

    * `account` (`String`): Snowflake account name
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `password` (`String`): User's password if using user/password
      basic auth
    * `private_key` (`String`): User's private key (base64 encoded) if
      using key pair auth.
    * `private_key_passphrase` (`String`): User's private key
      passphrase if using key pair auth. This argument is only needed
      when the private key is encrypted.
    * `user` (`String`): User with access to snowflake.
    * `warehouse` (`String`): Name of the warehouse for the user
    '''

    test_hive_credentials = sgqlc.types.Field('TestHiveCredentials', graphql_name='testHiveCredentials', args=sgqlc.types.ArgDict((
        ('auth_mode', sgqlc.types.Arg(String, graphql_name='authMode', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('database', sgqlc.types.Arg(String, graphql_name='database', default=None)),
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    '''Test a hive sql based connection

    Arguments:

    * `auth_mode` (`String`): Authentication mode to hive. If not set
      "SASL" is used.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `database` (`String`): Name of database
    * `host` (`String`): Hostname
    * `port` (`Int`): Port
    * `username` (`String`): Username with access to hive
    '''

    test_s3_credentials = sgqlc.types.Field('TestS3Credentials', graphql_name='testS3Credentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('bucket', sgqlc.types.Arg(String, graphql_name='bucket', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default='s3')),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('prefix', sgqlc.types.Arg(String, graphql_name='prefix', default=None)),
))
    )
    '''Test a s3 based connection (e.g. presto query logs on s3)

    Arguments:

    * `assumable_role` (`String`): AWS role that can be assumed by the
      DC
    * `bucket` (`String`): S3 Bucket where relevant objects are
      contained
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `connection_type` (`String`): Type of connection (default:
      `"s3"`)
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `prefix` (`String`): Path to objects
    '''

    test_glue_credentials = sgqlc.types.Field('TestGlueCredentials', graphql_name='testGlueCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('aws_region', sgqlc.types.Arg(String, graphql_name='awsRegion', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
))
    )
    '''Test a Glue connection

    Arguments:

    * `assumable_role` (`String`): Assumable role ARN to use for
      accessing AWS resources
    * `aws_region` (`String`): Glue region
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `external_id` (`String`): An external id, per assumable role
      conditions
    '''

    test_athena_credentials = sgqlc.types.Field('TestAthenaCredentials', graphql_name='testAthenaCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('aws_region', sgqlc.types.Arg(String, graphql_name='awsRegion', default=None)),
        ('catalog', sgqlc.types.Arg(String, graphql_name='catalog', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('workgroup', sgqlc.types.Arg(String, graphql_name='workgroup', default=None)),
))
    )
    '''Test an Athena connection

    Arguments:

    * `assumable_role` (`String`): Assumable role ARN to use for
      accessing AWS resources
    * `aws_region` (`String`): Athena cluster region
    * `catalog` (`String`): Glue data catalog
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `workgroup` (`String`): Workbook for running queries and
      retrieving logs. If not specified the primary is used
    '''

    test_looker_credentials = sgqlc.types.Field('TestLookerCredentials', graphql_name='testLookerCredentials', args=sgqlc.types.ArgDict((
        ('base_url', sgqlc.types.Arg(String, graphql_name='baseUrl', default=None)),
        ('client_id', sgqlc.types.Arg(String, graphql_name='clientId', default=None)),
        ('client_secret', sgqlc.types.Arg(String, graphql_name='clientSecret', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('verify_ssl', sgqlc.types.Arg(Boolean, graphql_name='verifySsl', default=None)),
))
    )
    '''Test a Looker API connection

    Arguments:

    * `base_url` (`String`): Host url
    * `client_id` (`String`): Looker client id
    * `client_secret` (`String`): Looker client secret
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `verify_ssl` (`Boolean`): Verify SSL (uncheck for self-signed
      certs)
    '''

    test_looker_git_credentials = sgqlc.types.Field('TestLookerGitCredentials', graphql_name='testLookerGitCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('installation_id', sgqlc.types.Arg(Int, graphql_name='installationId', default=None)),
))
    )
    '''Deprecated. Do not use.

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `installation_id` (`Int`): ID response from Github
    '''

    test_looker_git_ssh_credentials = sgqlc.types.Field('TestLookerGitSshCredentials', graphql_name='testLookerGitSshCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('repo_url', sgqlc.types.Arg(String, graphql_name='repoUrl', default=None)),
        ('ssh_key', sgqlc.types.Arg(String, graphql_name='sshKey', default=None)),
))
    )
    '''Test the connection to a Git repository using the SSH protocol

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `repo_url` (`String`): Repository URL as
      ssh://[user@]server/project.git or the shorter form
      [user@]server:project.git
    * `ssh_key` (`String`): SSH key, base64-encoded
    '''

    test_looker_git_clone_credentials = sgqlc.types.Field('TestLookerGitCloneCredentials', graphql_name='testLookerGitCloneCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('repo_url', sgqlc.types.Arg(String, graphql_name='repoUrl', default=None)),
        ('ssh_key', sgqlc.types.Arg(String, graphql_name='sshKey', default=None)),
        ('token', sgqlc.types.Arg(String, graphql_name='token', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    '''Test the connection to a Git repository using the SSH or HTTPS
    protocol

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `repo_url` (`String`): Repository URL as
      ssh://[user@]server/project.git or the shorter form
      [user@]server:project.git SSH integrations and
      htts://server/project.git for HTTPS integrations
    * `ssh_key` (`String`): SSH key, base64-encoded
    * `token` (`String`): The access token for git HTTPS integrations
    * `username` (`String`): The git username for BitBucket
      integrations
    '''

    test_dbt_cloud_credentials = sgqlc.types.Field('TestDbtCloudCredentials', graphql_name='testDbtCloudCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default='dbt-cloud-v2')),
        ('dbt_cloud_account_id', sgqlc.types.Arg(String, graphql_name='dbtCloudAccountId', default=None)),
        ('dbt_cloud_api_token', sgqlc.types.Arg(String, graphql_name='dbtCloudApiToken', default=None)),
        ('dbt_cloud_base_url', sgqlc.types.Arg(String, graphql_name='dbtCloudBaseUrl', default=None)),
        ('dbt_cloud_webhook_hmac_secret', sgqlc.types.Arg(String, graphql_name='dbtCloudWebhookHmacSecret', default=None)),
))
    )
    '''Test a dbt Cloud connection

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `connection_type` (`String`): dbt Cloud connection type
      (default: `"dbt-cloud-v2"`)
    * `dbt_cloud_account_id` (`String`): dbt Cloud account ID
    * `dbt_cloud_api_token` (`String`): dbt Cloud API token
    * `dbt_cloud_base_url` (`String`): dbt Cloud base URL
    * `dbt_cloud_webhook_hmac_secret` (`String`): Provide the
      hmac_secret of a Dbt outbound webhook to setup a webhook-based
      Dbt integration
    '''

    test_bq_credentials = sgqlc.types.Field('TestBqCredentials', graphql_name='testBqCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('service_json', sgqlc.types.Arg(String, graphql_name='serviceJson', default=None)),
))
    )
    '''Test a BQ connection

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `service_json` (`String`): Service account key file as a base64
      string
    '''

    test_spark_credentials = sgqlc.types.Field('TestSparkCredentials', graphql_name='testSparkCredentials', args=sgqlc.types.ArgDict((
        ('binary_mode', sgqlc.types.Arg(SparkBinaryInput, graphql_name='binaryMode', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks', sgqlc.types.Arg(SparkDatabricksInput, graphql_name='databricks', default=None)),
        ('http_mode', sgqlc.types.Arg(SparkHttpInput, graphql_name='httpMode', default=None)),
))
    )
    '''Test Spark credentials

    Arguments:

    * `binary_mode` (`SparkBinaryInput`): Configuration for Thrift in
      binary mode
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `databricks` (`SparkDatabricksInput`): Configuration for
      Databricks
    * `http_mode` (`SparkHttpInput`): Configuration for Thrift in HTTP
      mode
    '''

    test_databricks_sql_warehouse_credentials = sgqlc.types.Field('TestDatabricksSqlWarehouseCredentials', graphql_name='testDatabricksSqlWarehouseCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(DatabricksSqlWarehouseInput), graphql_name='databricksConfig', default=None)),
))
    )
    '''Test Databricks Sql Warehouse credentials

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `databricks_config` (`DatabricksSqlWarehouseInput!`):
      Configuration for the Databricks sql warehouse.
    '''

    test_self_hosted_credentials = sgqlc.types.Field('TestSelfHostedCredentials', graphql_name='testSelfHostedCredentials', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('region', sgqlc.types.Arg(String, graphql_name='region', default=None)),
        ('self_hosting_key', sgqlc.types.Arg(String, graphql_name='selfHostingKey', default=None)),
        ('self_hosting_mechanism', sgqlc.types.Arg(String, graphql_name='selfHostingMechanism', default=None)),
))
    )
    '''Test a connection of any type with self-hosted credentials.

    Arguments:

    * `assumable_role` (`String`): Role that can be assumed by the DC
      to access the self-hosting mechanism
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `connection_type` (`String`): Type of connection
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `region` (`String`): Region where the credentials are hosted
    * `self_hosting_key` (`String`): Identifier for the credentials
      within the self-hosting mechanism (e.g. SecretManager secret
      ARN)
    * `self_hosting_mechanism` (`String`): Type of credential self-
      hosting mechanism
    '''

    add_tableau_account = sgqlc.types.Field(AddTableauAccountMutation, graphql_name='addTableauAccount', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('server_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverName', default=None)),
        ('site_name', sgqlc.types.Arg(String, graphql_name='siteName', default=None)),
        ('token_name', sgqlc.types.Arg(String, graphql_name='tokenName', default=None)),
        ('token_value', sgqlc.types.Arg(String, graphql_name='tokenValue', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('verify_ssl', sgqlc.types.Arg(Boolean, graphql_name='verifySsl', default=True)),
))
    )
    '''Add Tableau credentials to the account

    Arguments:

    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `password` (`String`): Password for the Tableau user if using
      username/password
    * `server_name` (`String!`): The Tableau server name
    * `site_name` (`String`): The Tableau site name
    * `token_name` (`String`): The personal access token name
    * `token_value` (`String`): The personal access token value
    * `username` (`String`): Username for the Tableau user if using
      username/password
    * `verify_ssl` (`Boolean`): Whether to verify the SSL connection
      to Tableau server (default: `true`)
    '''

    test_tableau_credentials = sgqlc.types.Field('TestTableauCredentialsMutation', graphql_name='testTableauCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('server_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverName', default=None)),
        ('site_name', sgqlc.types.Arg(String, graphql_name='siteName', default=None)),
        ('token_name', sgqlc.types.Arg(String, graphql_name='tokenName', default=None)),
        ('token_value', sgqlc.types.Arg(String, graphql_name='tokenValue', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
        ('verify_ssl', sgqlc.types.Arg(Boolean, graphql_name='verifySsl', default=True)),
))
    )
    '''Test Tableau credentials

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `password` (`String`): Password for the Tableau user if using
      username/password
    * `server_name` (`String!`): The Tableau server name
    * `site_name` (`String`): The Tableau site name
    * `token_name` (`String`): The personal access token name
    * `token_value` (`String`): The personal access token value
    * `username` (`String`): Username for the Tableau user if using
      username/password
    * `verify_ssl` (`Boolean`): Whether to verify the SSL connection
      to Tableau server (default: `true`)
    '''

    test_power_bi_credentials = sgqlc.types.Field('TestPowerBICredentials', graphql_name='testPowerBiCredentials', args=sgqlc.types.ArgDict((
        ('auth_mode', sgqlc.types.Arg(sgqlc.types.non_null(PowerBIAuthModeEnum), graphql_name='authMode', default=None)),
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
        ('client_secret', sgqlc.types.Arg(String, graphql_name='clientSecret', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('password', sgqlc.types.Arg(String, graphql_name='password', default=None)),
        ('tenant_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tenantId', default=None)),
        ('username', sgqlc.types.Arg(String, graphql_name='username', default=None)),
))
    )
    '''Test Power BI credentials

    Arguments:

    * `auth_mode` (`PowerBIAuthModeEnum!`): Authentication mode. We
      support two values here [service_principal, primary_user]
    * `client_id` (`String!`): App Client uuid
    * `client_secret` (`String`): Secret key for the client ID.
      Required if auth_mode is service_principal.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `password` (`String`): Password when auth as a primary user.
      Required if auth_mode is primary_user.
    * `tenant_id` (`String!`): Azure power bi tenant uuid
    * `username` (`String`): Username when auth as a primary user.
      Required if auth_mode is primary_user.
    '''

    test_fivetran_credentials = sgqlc.types.Field('TestFivetranCredentials', graphql_name='testFivetranCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('fivetran_api_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fivetranApiKey', default=None)),
        ('fivetran_api_password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fivetranApiPassword', default=None)),
        ('fivetran_base_url', sgqlc.types.Arg(String, graphql_name='fivetranBaseUrl', default=None)),
))
    )
    '''Test Fivetran credentials

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests
    * `fivetran_api_key` (`String!`): Fivetran API Key
    * `fivetran_api_password` (`String!`): Fivetran API Password
    * `fivetran_base_url` (`String`): Fivetran base URL
    '''

    toggle_mute_dataset = sgqlc.types.Field('ToggleMuteDatasetPayload', graphql_name='toggleMuteDataset', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteDatasetInput), graphql_name='input', default=None)),
))
    )
    '''Start/Stop creating incidents for the given dataset

    Arguments:

    * `input` (`ToggleMuteDatasetInput!`)None
    '''

    toggle_mute_table = sgqlc.types.Field('ToggleMuteTablePayload', graphql_name='toggleMuteTable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteTableInput), graphql_name='input', default=None)),
))
    )
    '''Start/Stop creating incidents for the given table

    Arguments:

    * `input` (`ToggleMuteTableInput!`)None
    '''

    toggle_mute_datasets = sgqlc.types.Field('ToggleMuteDatasetsPayload', graphql_name='toggleMuteDatasets', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteDatasetsInput), graphql_name='input', default=None)),
))
    )
    '''Start/Stop creating incidents for the given datasets

    Arguments:

    * `input` (`ToggleMuteDatasetsInput!`)None
    '''

    toggle_mute_tables = sgqlc.types.Field('ToggleMuteTablesPayload', graphql_name='toggleMuteTables', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteTablesInput), graphql_name='input', default=None)),
))
    )
    '''Start/Stop creating incidents for the given tables

    Arguments:

    * `input` (`ToggleMuteTablesInput!`)None
    '''

    toggle_mute_with_regex = sgqlc.types.Field('ToggleMuteWithRegexPayload', graphql_name='toggleMuteWithRegex', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ToggleMuteWithRegexInput), graphql_name='input', default=None)),
))
    )
    '''Start/Stop creating incidents for all matched elements. Use
    wildcards to match more than one table or dataset.

    Arguments:

    * `input` (`ToggleMuteWithRegexInput!`)None
    '''

    toggle_slack_reply_warning = sgqlc.types.Field('ToggleSlackReplyWarning', graphql_name='toggleSlackReplyWarning', args=sgqlc.types.ArgDict((
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
))
    )
    '''Enable/disable the Slack reply warning feature

    Arguments:

    * `enable` (`Boolean!`): If true, enable the feature
    '''

    toggle_connection_enable = sgqlc.types.Field('ToggleConnectionEnable', graphql_name='toggleConnectionEnable', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
))
    )
    '''Enable or Disable a connection. This will also skip/un-skip all
    related data collector schedules.

    Arguments:

    * `connection_id` (`UUID!`): Connection to perform the action on
    * `enable` (`Boolean!`): Indicates whether the connection should
      be enabled (true) or disabled (false)
    '''

    add_connection = sgqlc.types.Field(AddConnectionMutation, graphql_name='addConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('create_warehouse_type', sgqlc.types.Arg(String, graphql_name='createWarehouseType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('job_limits', sgqlc.types.Arg(JSONString, graphql_name='jobLimits', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Add a connection and setup any associated jobs. Creates a
    warehouse if not specified

    Arguments:

    * `connection_type` (`String!`): The type of connection to add
    * `create_warehouse_type` (`String`): Create a new warehouse for
      the connection
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `dw_id` (`UUID`): Add connection to an existing warehouse
    * `job_limits` (`JSONString`): Customize job operations for all
      job types
    * `job_types` (`[String]`): Specify job types for the connection.
      Uses connection default otherwise
    * `key` (`String!`): Temp key from testing connections
    * `name` (`String`): Provide a friendly name for the warehouse
      when creating
    '''

    remove_connection = sgqlc.types.Field('RemoveConnectionMutation', graphql_name='removeConnection', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
))
    )
    '''Remove an integration connection and deschedule any associated
    jobs

    Arguments:

    * `connection_id` (`UUID!`): ID of the connection to remove
    '''

    add_bi_connection = sgqlc.types.Field(AddBiConnectionMutation, graphql_name='addBiConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
))
    )
    '''Add a bi connection and setup any associated jobs

    Arguments:

    * `connection_type` (`String!`): The type of connection to add
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `job_types` (`[String]`): Specify job types for the connection.
      Uses connection default otherwise
    * `key` (`String!`): Temp key from testing connections
    * `name` (`String`): Provide a friendly name for the BI connection
    * `resource_id` (`UUID`): BI Container UUID. Add the connection
      under the same resource UUID.
    '''

    update_bi_connection_name = sgqlc.types.Field('UpdateBiConnectionNameMutation', graphql_name='updateBiConnectionName', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='resourceId', default=None)),
))
    )
    '''Update the name of an existing bi connection

    Arguments:

    * `name` (`String!`): Provide a friendly name for the BI
      connection
    * `resource_id` (`UUID!`): Existing BI Container UUID.
    '''

    add_etl_connection = sgqlc.types.Field(AddEtlConnectionMutation, graphql_name='addEtlConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    '''Add an etl connection and setup any associated jobs

    Arguments:

    * `connection_type` (`String!`): The type of connection to add
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `key` (`String!`): Temp key from testing connections
    * `name` (`String!`): Provide a friendly name for the ETL
      connection
    '''

    toggle_event_config = sgqlc.types.Field('ToggleEventConfig', graphql_name='toggleEventConfig', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(String, graphql_name='assumableRole', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('connection_type', sgqlc.types.Arg(String, graphql_name='connectionType', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('enable', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='enable', default=None)),
        ('event_type', sgqlc.types.Arg(sgqlc.types.non_null(DataCollectorEventTypes), graphql_name='eventType', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('format_type', sgqlc.types.Arg(String, graphql_name='formatType', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('mapping', sgqlc.types.Arg(JSONString, graphql_name='mapping', default=None)),
        ('source_format', sgqlc.types.Arg(String, graphql_name='sourceFormat', default=None)),
))
    )
    '''Enable / disable the configuration for data collection via events

    Arguments:

    * `assumable_role` (`String`): AWS role that can be assumed by the
      DC
    * `connection_id` (`UUID`): The connection id. Cannot be present
      with DW ID
    * `connection_type` (`String`): Type of connection (e.g. hive-s3),
      required if connection id not set
    * `dw_id` (`UUID`): The warehouse id. Cannot be present with
      connection ID
    * `enable` (`Boolean!`): If true enable the connection, otherwise
      disable it
    * `event_type` (`DataCollectorEventTypes!`): Type of event (e.g.
      metadata)
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `format_type` (`String`): Log file format (e.g. hive-emr)
    * `location` (`String`): Location of the log files
    * `mapping` (`JSONString`): A map where keys are the attributes in
      the destinationschema and values are the keys in the source
      schema
    * `source_format` (`String`): File format (e.g. "json")
    '''

    configure_airflow_log_events = sgqlc.types.Field(ConfigureAirflowLogEvents, graphql_name='configureAirflowLogEvents', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='assumableRole', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Configure collection of Airflow logs via S3 events

    Arguments:

    * `assumable_role` (`String!`): AWS role that can be assumed by
      the DC
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `name` (`String`): Provide a friendly name for the warehouse
      when creating
    '''

    configure_metadata_events = sgqlc.types.Field(ConfigureMetadataEvents, graphql_name='configureMetadataEvents', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Configure collection of metadata via S3 events

    Arguments:

    * `connection_type` (`String!`): Type of data lake connection
      (e.g. hive-s3)
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `name` (`String`): Provide a friendly name for the warehouse
      when creating
    '''

    configure_query_log_events = sgqlc.types.Field(ConfigureQueryLogEvents, graphql_name='configureQueryLogEvents', args=sgqlc.types.ArgDict((
        ('assumable_role', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='assumableRole', default=None)),
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('external_id', sgqlc.types.Arg(String, graphql_name='externalId', default=None)),
        ('format_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='formatType', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('mapping', sgqlc.types.Arg(JSONString, graphql_name='mapping', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('source_format', sgqlc.types.Arg(String, graphql_name='sourceFormat', default=None)),
))
    )
    '''Configure collection of query logs via S3 events

    Arguments:

    * `assumable_role` (`String!`): AWS role that can be assumed by
      the DC
    * `connection_type` (`String!`): Type of data lake connection
      (e.g. hive-s3)
    * `external_id` (`String`): An external id, per assumable role
      conditions
    * `format_type` (`String!`): Log file format (e.g. hive-emr)
    * `location` (`String`): Location of the log files
    * `mapping` (`JSONString`): A map where keys are the attributes in
      the destinationschema and values are the keys in the source
      schema
    * `name` (`String`): Provide a friendly name for the warehouse
      when creating
    * `source_format` (`String`): File format (e.g. "json")
    '''

    disable_airflow_log_events = sgqlc.types.Field(DisableAirflowLogEvents, graphql_name='disableAirflowLogEvents', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Disable collection of Airflow logs via S3 events

    Arguments:

    * `name` (`String`): Resource name (required if more than one is
      present
    '''

    disable_metadata_events = sgqlc.types.Field(DisableMetadataEvents, graphql_name='disableMetadataEvents', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Disable collection of metadata via S3 events

    Arguments:

    * `name` (`String`): Resource name (required if more than one is
      present
    '''

    disable_query_log_events = sgqlc.types.Field(DisableQueryLogEvents, graphql_name='disableQueryLogEvents', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Disable collection of query logs via S3 events

    Arguments:

    * `name` (`String`): Resource name (required if more than one is
      present
    '''

    create_or_update_service_api_token = sgqlc.types.Field(CreateOrUpdateServiceApiToken, graphql_name='createOrUpdateServiceApiToken', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('display_name', sgqlc.types.Arg(String, graphql_name='displayName', default=None)),
        ('expiration_in_days', sgqlc.types.Arg(Int, graphql_name='expirationInDays', default=None)),
        ('groups', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='groups', default=None)),
        ('token_id', sgqlc.types.Arg(String, graphql_name='tokenId', default=None)),
))
    )
    '''Generate a service API Access Token

    Arguments:

    * `comment` (`String`): Any comment or description to help
      identify the token
    * `display_name` (`String`): A name to show when displaying the
      user name
    * `expiration_in_days` (`Int`): Number of days before the token
      auto expires
    * `groups` (`[String]`): Names of the groups for the API token.
    * `token_id` (`String`): Token ID to edit
    '''

    create_access_token = sgqlc.types.Field(CreateAccessToken, graphql_name='createAccessToken', args=sgqlc.types.ArgDict((
        ('comment', sgqlc.types.Arg(String, graphql_name='comment', default=None)),
        ('expiration_in_days', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='expirationInDays', default=None)),
))
    )
    '''Generate an API Access Token and associate to user

    Arguments:

    * `comment` (`String`): Any comment or description to help
      identify the token
    * `expiration_in_days` (`Int!`): Number of days before the token
      auto expires
    '''

    delete_access_token = sgqlc.types.Field(DeleteAccessToken, graphql_name='deleteAccessToken', args=sgqlc.types.ArgDict((
        ('token_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenId', default=None)),
))
    )
    '''Delete an API Access Token by ID

    Arguments:

    * `token_id` (`String!`): ID of the token to delete
    '''

    generate_collector_template = sgqlc.types.Field(GenerateCollectorTemplate, graphql_name='generateCollectorTemplate', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('region', sgqlc.types.Arg(String, graphql_name='region', default='us-east-1')),
        ('template_variant', sgqlc.types.Arg(String, graphql_name='templateVariant', default=None)),
        ('update_infra', sgqlc.types.Arg(Boolean, graphql_name='updateInfra', default=False)),
))
    )
    '''Generate a data collector template (uploaded to S3)

    Arguments:

    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `region` (`String`): Region where the DC is hosted (default:
      `"us-east-1"`)
    * `template_variant` (`String`): DC template variant.
    * `update_infra` (`Boolean`): Use latest version of the collector
      template, with any infrastructure changes it might include.
      Otherwise, only the lambda code version will be updated.
      (default: `false`)
    '''

    update_credentials = sgqlc.types.Field('UpdateCredentials', graphql_name='updateCredentials', args=sgqlc.types.ArgDict((
        ('changes', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='changes', default=None)),
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('should_replace', sgqlc.types.Arg(Boolean, graphql_name='shouldReplace', default=False)),
        ('should_validate', sgqlc.types.Arg(Boolean, graphql_name='shouldValidate', default=True)),
))
    )
    '''Update credentials for a connection

    Arguments:

    * `changes` (`JSONString!`): JSON Key/values with fields to update
    * `connection_id` (`UUID!`): ID for connection to update
    * `should_replace` (`Boolean`): Set true to replace all
      credentials with changes. Otherwise inserts/replaces (default:
      `false`)
    * `should_validate` (`Boolean`): Set to true to test changes
      before saving (default: `true`)
    '''

    create_collector_record = sgqlc.types.Field(CreateCollectorRecord, graphql_name='createCollectorRecord', args=sgqlc.types.ArgDict((
        ('region', sgqlc.types.Arg(String, graphql_name='region', default='us-east-1')),
        ('template_provider', sgqlc.types.Arg(String, graphql_name='templateProvider', default='cloudformation')),
        ('template_variant', sgqlc.types.Arg(String, graphql_name='templateVariant', default='janus')),
))
    )
    '''Create an additional collector record (with template) in the
    account.

    Arguments:

    * `region` (`String`): Region where the DC is hosted (default:
      `"us-east-1"`)
    * `template_provider` (`String`): DC template IaC provider
      (default: `"cloudformation"`)
    * `template_variant` (`String`): DC template variant (default:
      `"janus"`)
    '''

    cleanup_collector_record = sgqlc.types.Field(CleanupCollectorRecordInAccount, graphql_name='cleanupCollectorRecord', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dcId', default=None)),
))
    )
    '''Deletes an unassociated collector record in the account. This does
    not delete the CloudFormation stack and will not succeed if the
    collector is active and/or associated with a warehouse.

    Arguments:

    * `dc_id` (`UUID!`): DC UUID
    '''

    migrate_collector_resources = sgqlc.types.Field(MigrateCollectorResources, graphql_name='migrateCollectorResources', args=sgqlc.types.ArgDict((
        ('resource_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='resourceIds', default=None)),
        ('source_dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='sourceDcId', default=None)),
        ('target_dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='targetDcId', default=None)),
))
    )
    '''Migrate resources (warehouses, BI) from one data collector to
    another

    Arguments:

    * `resource_ids` (`[UUID]`): List of resource UUIDs to migrate. By
      default all resources will be migrated.
    * `source_dc_id` (`UUID!`): Source DC UUID
    * `target_dc_id` (`UUID!`): Target DC UUID
    '''

    update_slack_channels = sgqlc.types.Field('UpdateSlackChannelsMutation', graphql_name='updateSlackChannels')
    '''Update the slack channels cache for the account'''

    create_integration_key = sgqlc.types.Field(CreateIntegrationKey, graphql_name='createIntegrationKey', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('scope', sgqlc.types.Arg(sgqlc.types.non_null(IntegrationKeyScope), graphql_name='scope', default=None)),
        ('warehouse_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='warehouseIds', default=None)),
))
    )
    '''Create an integration key

    Arguments:

    * `description` (`String!`): Key description
    * `scope` (`IntegrationKeyScope!`): Key scope (integration it can
      be used for)
    * `warehouse_ids` (`[UUID]`): UUID(s) of warehouse(s) associated
      with key
    '''

    delete_integration_key = sgqlc.types.Field(DeleteIntegrationKey, graphql_name='deleteIntegrationKey', args=sgqlc.types.ArgDict((
        ('key_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='keyId', default=None)),
))
    )
    '''Delete an integration key

    Arguments:

    * `key_id` (`String!`): Integration key id
    '''

    create_databricks_secret = sgqlc.types.Field(CreateDatabricksSecret, graphql_name='createDatabricksSecret', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
        ('scope_name', sgqlc.types.Arg(String, graphql_name='scopeName', default=None)),
        ('scope_principal', sgqlc.types.Arg(String, graphql_name='scopePrincipal', default=None)),
        ('secret_name', sgqlc.types.Arg(String, graphql_name='secretName', default=None)),
))
    )
    '''Create Databricks scope and secret for an integration key.

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `databricks_config` (`SparkDatabricksInput!`): Configuration for
      Databricks.
    * `scope_name` (`String`): Override default scope name from DC.
    * `scope_principal` (`String`): Override default principal name
      from DC.
    * `secret_name` (`String`): Override default secret name from DC.
    '''

    create_databricks_notebook_job = sgqlc.types.Field(CreateDatabricksNotebookJob, graphql_name='createDatabricksNotebookJob', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
))
    )
    '''Create Databricks directory, upload the collection notebook and
    setup a job.

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `databricks_config` (`SparkDatabricksInput!`): Configuration for
      Databricks.
    '''

    update_databricks_notebook_job = sgqlc.types.Field('UpdateDatabricksNotebookJob', graphql_name='updateDatabricksNotebookJob', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    '''Update Databricks collection notebook and job.

    Arguments:

    * `connection_id` (`UUID`): A Databricks connection UUID
    '''

    update_databricks_notebook = sgqlc.types.Field('UpdateDatabricksNotebook', graphql_name='updateDatabricksNotebook', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    '''Update Databricks notebook.

    Arguments:

    * `connection_id` (`UUID`): A Databricks connection UUID
    '''

    start_databricks_cluster = sgqlc.types.Field('StartDatabricksCluster', graphql_name='startDatabricksCluster', args=sgqlc.types.ArgDict((
        ('connection_config', sgqlc.types.Arg(SparkDatabricksConnectionInput, graphql_name='connectionConfig', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    '''Start Databricks Cluster.

    Arguments:

    * `connection_config` (`SparkDatabricksConnectionInput`):
      Connection config for new Databricks cluster connection
    * `connection_id` (`UUID`): A Databricks connection UUID of an
      existing connection
    '''

    start_databricks_warehouse = sgqlc.types.Field('StartDatabricksWarehouse', graphql_name='startDatabricksWarehouse', args=sgqlc.types.ArgDict((
        ('connection_config', sgqlc.types.Arg(DatabricksSqlWarehouseConnectionInput, graphql_name='connectionConfig', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    '''Start Databricks Warehouse.

    Arguments:

    * `connection_config` (`DatabricksSqlWarehouseConnectionInput`):
      Connection config for new Databricks SQL warehouse connection
    * `connection_id` (`UUID`): A Databricks connection UUID
    '''

    test_databricks_credentials = sgqlc.types.Field('TestDatabricksCredentials', graphql_name='testDatabricksCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
))
    )
    '''Test a Databricks connection

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `databricks_config` (`SparkDatabricksInput!`): Configuration for
      Databricks.
    '''

    test_delta_credentials = sgqlc.types.Field('TestDatabricksCredentials', graphql_name='testDeltaCredentials', args=sgqlc.types.ArgDict((
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('databricks_config', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='databricksConfig', default=None)),
))
    )
    '''Test a Databricks connection

    Arguments:

    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `databricks_config` (`SparkDatabricksInput!`): Configuration for
      Databricks.
    '''

    add_databricks_connection = sgqlc.types.Field(AddDatabricksConnectionMutation, graphql_name='addDatabricksConnection', args=sgqlc.types.ArgDict((
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
        ('create_warehouse_type', sgqlc.types.Arg(String, graphql_name='createWarehouseType', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('job_limits', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='jobLimits', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Add a databricks connection and setup any associated jobs. Creates
    a warehouse if not specified

    Arguments:

    * `connection_type` (`String!`): The type of connection to add
    * `create_warehouse_type` (`String`): Create a new warehouse for
      the connection
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    * `dw_id` (`UUID`): Add connection to an existing warehouse
    * `job_limits` (`JSONString!`): Customize job operations for all
      job types
    * `job_types` (`[String]`): Specify job types for the connection.
      Uses connection default otherwise
    * `key` (`String!`): Temp key from testing connections
    * `name` (`String`): Provide a friendly name for the warehouse
      when creating
    '''

    save_event_onboarding_data = sgqlc.types.Field('SaveEventOnboardingData', graphql_name='saveEventOnboardingData', args=sgqlc.types.ArgDict((
        ('config', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='config', default=None)),
))
    )
    '''Save event onboarding configuration

    Arguments:

    * `config` (`JSONString!`): JSON Key/values with event config to
      store
    '''

    delete_event_onboarding_data = sgqlc.types.Field(DeleteEventOnboardingData, graphql_name='deleteEventOnboardingData')
    '''Delete stored event onboarding configuration'''

    test_snowflake_credentials_v2 = sgqlc.types.Field('TestSnowflakeCredentialsV2', graphql_name='testSnowflakeCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(SnowflakeConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Snowflake credentials

    Arguments:

    * `connection_details` (`SnowflakeConnectionDetails!`): Connection
      parameters.
    * `connection_id` (`UUID`): If updating an existing connection,
      the ID of the connection to test.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_redshift_credentials_v2 = sgqlc.types.Field('TestRedshiftCredentialsV2', graphql_name='testRedshiftCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(RedshiftConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Redshift credentials

    Arguments:

    * `connection_details` (`RedshiftConnectionDetails!`): Connection
      parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_bq_credentials_v2 = sgqlc.types.Field('TestBqCredentialsV2', graphql_name='testBqCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(BqConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test BigQuery credentials

    Arguments:

    * `connection_details` (`BqConnectionDetails!`): Connection
      parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_tableau_credentials_v2 = sgqlc.types.Field('TestTableauCredentialsV2', graphql_name='testTableauCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(TableauConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Tableau credentials

    Arguments:

    * `connection_details` (`TableauConnectionDetails!`): Connection
      parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_looker_credentials_v2 = sgqlc.types.Field('TestLookerCredentialsV2', graphql_name='testLookerCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(LookerConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Looker API credentials

    Arguments:

    * `connection_details` (`LookerConnectionDetails!`): Connection
      parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_looker_git_ssh_credentials_v2 = sgqlc.types.Field('TestLookerGitSshCredentialsV2', graphql_name='testLookerGitSshCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(LookerGitSshConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test the connection to a Git repository using the SSH protocol

    Arguments:

    * `connection_details` (`LookerGitSshConnectionDetails!`):
      Connection parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_looker_git_clone_credentials_v2 = sgqlc.types.Field('TestLookerGitCloneCredentialsV2', graphql_name='testLookerGitCloneCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(LookerGitCloneConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test the connection to a Git repository using the HTTPS protocol

    Arguments:

    * `connection_details` (`LookerGitCloneConnectionDetails!`):
      Connection parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_power_bi_credentials_v2 = sgqlc.types.Field('TestPowerBICredentialsV2', graphql_name='testPowerBiCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(PowerBIConnectionDetails), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Databricks SQL Warehouse credentials

    Arguments:

    * `connection_details` (`PowerBIConnectionDetails!`): Connection
      parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_databricks_credentials_v2 = sgqlc.types.Field('TestDatabricksCredentialsV2', graphql_name='testDatabricksCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('job_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='jobId', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Databricks credentials

    Arguments:

    * `connection_details` (`SparkDatabricksInput!`): Configuration
      for Databricks.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `job_id` (`String!`): Databricks Job Id to validate.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_databricks_sql_warehouse_credentials_v2 = sgqlc.types.Field('TestDatabricksSqlWarehouseCredentialsV2', graphql_name='testDatabricksSqlWarehouseCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(DatabricksSqlWarehouseInput), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Power BI credentials

    Arguments:

    * `connection_details` (`DatabricksSqlWarehouseInput!`):
      Connection parameters.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    test_databricks_spark_credentials_v2 = sgqlc.types.Field('TestDatabricksSparkCredentialsV2', graphql_name='testDatabricksSparkCredentialsV2', args=sgqlc.types.ArgDict((
        ('connection_details', sgqlc.types.Arg(sgqlc.types.non_null(SparkDatabricksInput), graphql_name='connectionDetails', default=None)),
        ('connection_options', sgqlc.types.Arg(ConnectionTestOptions, graphql_name='connectionOptions', default=None)),
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
))
    )
    '''Test Databricks AP Cluster credentials

    Arguments:

    * `connection_details` (`SparkDatabricksInput!`): Configuration
      for Databricks.
    * `connection_options` (`ConnectionTestOptions`): Common options
      for integration tests.
    * `validation_name` (`String!`): Name of the validation test that
      should be run.
    '''

    upload_airflow_dag_result = sgqlc.types.Field('UploadAirflowDagResult', graphql_name='uploadAirflowDagResult', args=sgqlc.types.ArgDict((
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('end_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endDate', default=None)),
        ('env', sgqlc.types.Arg(sgqlc.types.non_null(AirflowEnvInput), graphql_name='env', default=None)),
        ('execution_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='executionDate', default=None)),
        ('payload', sgqlc.types.Arg(sgqlc.types.non_null(GenericScalar), graphql_name='payload', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('run_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='runId', default=None)),
        ('start_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startDate', default=None)),
        ('state', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='state', default=None)),
        ('success', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='success', default=None)),
))
    )
    '''Upload Airflow DAG run result

    Arguments:

    * `dag_id` (`String!`): DAG identifier
    * `end_date` (`DateTime!`): 'end_date' as returned by Airflow
    * `env` (`AirflowEnvInput!`): Airflow environment information
    * `execution_date` (`DateTime!`): 'execution_date' as returned by
      Airflow
    * `payload` (`GenericScalar!`): Payload for the result, a JSON
      object containing all data gathered form Airflow on the
      callbacks.
    * `reason` (`String`): 'reason' field from Airflow Run
    * `run_id` (`String!`): DAG Run Identifier
    * `start_date` (`DateTime!`): 'start_date' as returned by Airflow
    * `state` (`String!`): Airflow state, for example success, failed,
      up_for_retry, etc.
    * `success` (`Boolean!`): Flag indicating if the result was
      successful or not
    '''

    upload_airflow_task_result = sgqlc.types.Field('UploadAirflowTaskResult', graphql_name='uploadAirflowTaskResult', args=sgqlc.types.ArgDict((
        ('attempt_number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='attemptNumber', default=None)),
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('duration', sgqlc.types.Arg(Float, graphql_name='duration', default=None)),
        ('end_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endDate', default=None)),
        ('env', sgqlc.types.Arg(sgqlc.types.non_null(AirflowEnvInput), graphql_name='env', default=None)),
        ('exception_message', sgqlc.types.Arg(String, graphql_name='exceptionMessage', default=None)),
        ('execution_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='executionDate', default=None)),
        ('log_url', sgqlc.types.Arg(String, graphql_name='logUrl', default=None)),
        ('next_retry_date', sgqlc.types.Arg(DateTime, graphql_name='nextRetryDate', default=None)),
        ('payload', sgqlc.types.Arg(sgqlc.types.non_null(GenericScalar), graphql_name='payload', default=None)),
        ('run_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='runId', default=None)),
        ('start_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startDate', default=None)),
        ('state', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='state', default=None)),
        ('success', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='success', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='taskId', default=None)),
))
    )
    '''Upload Airflow Task run result

    Arguments:

    * `attempt_number` (`Int!`): Attempt number for this Task Run, 1
      for the first attempt.
    * `dag_id` (`String!`): DAG identifier
    * `duration` (`Float`): Task Run duration in seconds
    * `end_date` (`DateTime!`): 'end_date' as returned by Airflow
    * `env` (`AirflowEnvInput!`): Airflow environment information
    * `exception_message` (`String`): Exception message obtained from
      Airflow 'exception' attribute
    * `execution_date` (`DateTime!`): 'execution_date' as returned by
      Airflow
    * `log_url` (`String`): URL to access the log for this Task Run
    * `next_retry_date` (`DateTime`): Datetime for the next retry as
      returned by Airflow
    * `payload` (`GenericScalar!`): Payload for the result, a JSON
      object containing all data gathered form Airflow on the
      callbacks.
    * `run_id` (`String!`): DAG Run Identifier
    * `start_date` (`DateTime!`): 'start_date' as returned by Airflow
    * `state` (`String!`): Airflow state, for example success, failed,
      up_for_retry, etc.
    * `success` (`Boolean!`): Flag indicating if the result was
      successful or not
    * `task_id` (`String!`): Airflow Task ID
    '''

    upload_airflow_sla_misses = sgqlc.types.Field('UploadAirflowSlaMisses', graphql_name='uploadAirflowSlaMisses', args=sgqlc.types.ArgDict((
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('env', sgqlc.types.Arg(sgqlc.types.non_null(AirflowEnvInput), graphql_name='env', default=None)),
        ('payload', sgqlc.types.Arg(sgqlc.types.non_null(GenericScalar), graphql_name='payload', default=None)),
))
    )
    '''Upload Airflow SLA misses

    Arguments:

    * `dag_id` (`String!`): DAG identifier
    * `env` (`AirflowEnvInput!`): Airflow environment information
    * `payload` (`GenericScalar!`): Payload for the result, a JSON
      object containing all data gathered form Airflow on the
      callbacks.
    '''



class NameRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')



class NestedHighlightSnippets(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('offset', 'inner_hit_snippets')
    offset = sgqlc.types.Field(Int, graphql_name='offset')
    '''Offset into nested field'''

    inner_hit_snippets = sgqlc.types.Field(sgqlc.types.list_of(HighlightSnippets), graphql_name='innerHitSnippets')
    '''Highlighted snippet of inner hit'''



class NextPageInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_next_page', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    '''When paginating forwards, are there more items?'''

    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    '''If there is next page, use this cursor to continue'''



class NodeImportInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('node_id', 'resource_type', 'global_id', 'description_imported', 'tags_imported', 'columns_description_imported', 'columns_tags_imported')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    '''dbt node ID'''

    resource_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resourceType')
    '''dbt resource type'''

    global_id = sgqlc.types.Field(String, graphql_name='globalId')
    '''Resolved global_id of MC table'''

    description_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='descriptionImported')
    '''Description imported for this node?'''

    tags_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tagsImported')
    '''Tags imported for this node?'''

    columns_description_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='columnsDescriptionImported')
    '''At least one column with description imported for this node?'''

    columns_tags_imported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='columnsTagsImported')
    '''At least one column with description imported for this node?'''



class NodeProperties(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('workbook_id', 'friendly_name', 'content_url', 'owner_id', 'project_id', 'project_name', 'created', 'updated', 'total_views', 'workbook_creators', 'view_id', 'category', 'mcon', 'name', 'display_name', 'table_id', 'data_set', 'node_id', 'resource', 'sampling')
    workbook_id = sgqlc.types.Field(String, graphql_name='workbookId')

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')

    content_url = sgqlc.types.Field(String, graphql_name='contentUrl')

    owner_id = sgqlc.types.Field(String, graphql_name='ownerId')

    project_id = sgqlc.types.Field(String, graphql_name='projectId')

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    created = sgqlc.types.Field(DateTime, graphql_name='created')

    updated = sgqlc.types.Field(DateTime, graphql_name='updated')

    total_views = sgqlc.types.Field(Int, graphql_name='totalViews')

    workbook_creators = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='workbookCreators')

    view_id = sgqlc.types.Field(String, graphql_name='viewId')

    category = sgqlc.types.Field(String, graphql_name='category')
    '''Node type'''

    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Monte Carlo object name'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''Object name (table name, report name, etc)'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Friendly display name'''

    table_id = sgqlc.types.Field(String, graphql_name='tableId')

    data_set = sgqlc.types.Field(String, graphql_name='dataSet')

    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    '''Lineage node id, to be deprecated in favor of MCONs'''

    resource = sgqlc.types.Field(String, graphql_name='resource')
    '''Resource containing this object (warehouse, Tableau account, etc)'''

    sampling = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sampling')
    '''A subset of the nodes that were collapsed into a node, only
    present on nodes of type collapsed-etl or collapsed-ext
    '''



class NonTableMetric(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metric', 'value', 'measurement_timestamp', 'dimensions', 'job_execution_uuid')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    '''Metric for which to fetch results. E.g; custom_metric_uuid'''

    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    '''Measurement value for the metric'''

    measurement_timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='measurementTimestamp')
    '''Time when measurement value was obtained'''

    dimensions = sgqlc.types.Field(MetricDimensions, graphql_name='dimensions')
    '''List of key/value dimension pairs applied as filters'''

    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')
    '''UUID of the job execution that produced the measurement'''



class NonTableMetrics(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metrics', 'is_partial_date_range')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(NonTableMetric), graphql_name='metrics')

    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange')



class ObjectDocument(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'resource_id', 'object_id', 'object_type', 'display_name', 'field_metadata', 'table_metadata', 'bi_metadata', 'properties')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')

    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')

    object_id = sgqlc.types.Field(String, graphql_name='objectId')

    object_type = sgqlc.types.Field(String, graphql_name='objectType')

    display_name = sgqlc.types.Field(String, graphql_name='displayName')

    field_metadata = sgqlc.types.Field(FieldMetadata, graphql_name='fieldMetadata')

    table_metadata = sgqlc.types.Field('TableMetadata', graphql_name='tableMetadata')

    bi_metadata = sgqlc.types.Field(BiMetadata, graphql_name='biMetadata')

    properties = sgqlc.types.Field(sgqlc.types.list_of('ObjectPropertyEntry'), graphql_name='properties')



class ObjectPropertyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ObjectPropertyEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class ObjectPropertyEdge(sgqlc.types.Type):
    '''A Relay edge containing a `ObjectProperty` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('ObjectProperty', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class ObjectPropertyEntry(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')

    value = sgqlc.types.Field(String, graphql_name='value')



class OwnerRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'username', 'email')
    name = sgqlc.types.Field(String, graphql_name='name')

    username = sgqlc.types.Field(String, graphql_name='username')

    email = sgqlc.types.Field(String, graphql_name='email')



class PageInfo(sgqlc.types.Type):
    '''The Relay compliant `PageInfo` type, containing data necessary to
    paginate this connection.
    '''
    __schema__ = schema
    __field_names__ = ('has_next_page', 'has_previous_page', 'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    '''When paginating forwards, are there more items?'''

    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    '''When paginating backwards, are there more items?'''

    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    '''When paginating backwards, the cursor to continue.'''

    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    '''When paginating forwards, the cursor to continue.'''



class PaginateQueriesBlastRadius(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('QueryAfterKey', graphql_name='afterKey')
    '''The after key to use for pagination'''

    data = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadius'), graphql_name='data')
    '''The user blast radius data'''



class PaginateQueriesBlastRadius2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey2', graphql_name='afterKey')
    '''The after key to user for pagination'''

    data = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadius2'), graphql_name='data')
    '''The user blast radius data'''



class PaginateQueriesBlastRadiusSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey2', graphql_name='afterKey')
    '''The after key to user for pagination'''

    data = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadiusSummary'), graphql_name='data')
    '''The user blast radius data'''



class PaginateUsersBlastRadius(sgqlc.types.Type):
    '''Deprecated'''
    __schema__ = schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey', graphql_name='afterKey')
    '''The after key to use for pagination. Deprecated.'''

    data = sgqlc.types.Field(sgqlc.types.list_of('UserBlastRadius'), graphql_name='data')
    '''The user blast radius data. Deprecated.'''



class PaginateUsersBlastRadius2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('after_key', 'data')
    after_key = sgqlc.types.Field('UserAfterKey2', graphql_name='afterKey')
    '''The after key to use for pagination'''

    data = sgqlc.types.Field(sgqlc.types.list_of('UserBlastRadius2'), graphql_name='data')
    '''The user blast radius data'''



class ParsedQueryResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('parsed_query',)
    parsed_query = sgqlc.types.Field(String, graphql_name='parsedQuery')
    '''Query, based on which the table's created'''



class PauseMonitor(sgqlc.types.Type):
    '''Pause a monitor from collecting data.' '''
    __schema__ = schema
    __field_names__ = ('monitor',)
    monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='monitor')
    '''The monitor whose pause property has been toggled.'''



class PiiFilterMetricOutput(sgqlc.types.Type):
    '''A container for PII filter metrics per completed job execution
    aggregated by job type, warehouse and PII filter name.
    '''
    __schema__ = schema
    __field_names__ = ('filter_name', 'job_type', 'resource_id', 'total_replacements')
    filter_name = sgqlc.types.Field(String, graphql_name='filterName')
    '''The unique name for the filter that was run.'''

    job_type = sgqlc.types.Field(String, graphql_name='jobType')
    '''The type of job the PII filter run was a part of.'''

    resource_id = sgqlc.types.Field(UUID, graphql_name='resourceId')
    '''The UUID of the resource the PII filtering ran on.'''

    total_replacements = sgqlc.types.Field(Int, graphql_name='totalReplacements')
    '''Total number of text occurrences replaced by this filter across
    the job runs.
    '''



class PiiFilterOutput(sgqlc.types.Type):
    '''A container for a regex pattern used to match data for redaction
    of PII information.
    '''
    __schema__ = schema
    __field_names__ = ('name', 'description', 'pattern', 'on_by_default', 'enabled')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''The unique name of the PII filter.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''The explanation of the PII filter's purpose.'''

    pattern = sgqlc.types.Field(String, graphql_name='pattern')
    '''The regex matching pattern of the PII filter.'''

    on_by_default = sgqlc.types.Field(Boolean, graphql_name='onByDefault')
    '''Whether this PII filter is on by default globally.'''

    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    '''Whether this PII filter is enabled for this account.'''



class PiiFilteringPreferencesOutput(sgqlc.types.Type):
    '''A container describing this account's PII filtering customizations
    and settings.
    '''
    __schema__ = schema
    __field_names__ = ('enabled', 'fail_mode')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    '''Whether PII filtering is enabled for this account.'''

    fail_mode = sgqlc.types.Field(PiiFilteringFailModeType, graphql_name='failMode')
    '''Whether PII filter failures will allow (open) or prevent (close)
    data flow for this account.
    '''



class PipelineFreshness(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metric_values_by_table', 'is_partial_date_range')
    metric_values_by_table = sgqlc.types.Field(sgqlc.types.list_of(MetricValueByTable), graphql_name='metricValuesByTable')

    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange')



class PlatformRegionProperties(sgqlc.types.Type):
    '''Region-specific platform properties'''
    __schema__ = schema
    __field_names__ = ('gateway_endpoint', 'gateway_vpce', 'linker_arn', 'log_arn', 'template_launch_url')
    gateway_endpoint = sgqlc.types.Field(String, graphql_name='gatewayEndpoint')
    '''Gateway endpoint URL'''

    gateway_vpce = sgqlc.types.Field(String, graphql_name='gatewayVpce')
    '''Gateway VPC id'''

    linker_arn = sgqlc.types.Field(String, graphql_name='linkerArn')
    '''ARN of SNS topic used to link data collector deployment'''

    log_arn = sgqlc.types.Field(String, graphql_name='logArn')
    '''ARN of CloudWatch log destination for cross-account log
    subscriptions
    '''

    template_launch_url = sgqlc.types.Field(String, graphql_name='templateLaunchUrl')
    '''CloudFormation template launch URL'''



class PowerBIDashboardTileRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('tile_id', 'tile_title', 'tile_sub_title', 'report_name', 'report_id')
    tile_id = sgqlc.types.Field(String, graphql_name='tileId')

    tile_title = sgqlc.types.Field(String, graphql_name='tileTitle')

    tile_sub_title = sgqlc.types.Field(String, graphql_name='tileSubTitle')

    report_name = sgqlc.types.Field(String, graphql_name='reportName')

    report_id = sgqlc.types.Field(String, graphql_name='reportId')



class PowerBIWorkSpaceRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'id', 'type', 'state', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')

    id = sgqlc.types.Field(String, graphql_name='id')

    type = sgqlc.types.Field(String, graphql_name='type')

    state = sgqlc.types.Field(String, graphql_name='state')

    description = sgqlc.types.Field(String, graphql_name='description')



class ProjectEntity(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('project_id', 'friendly_name')
    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Project ID'''

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')
    '''Friendly name of the project'''



class Projects(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('projects',)
    projects = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='projects')



class PropertyNameValue(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')

    value = sgqlc.types.Field(String, graphql_name='value')



class PropertyNameValues(sgqlc.types.Type):
    '''All unique object property names/values'''
    __schema__ = schema
    __field_names__ = ('property_name_values', 'has_next_page')
    property_name_values = sgqlc.types.Field(sgqlc.types.list_of(PropertyNameValue), graphql_name='propertyNameValues')
    '''List of unique object property name/value pairs'''

    has_next_page = sgqlc.types.Field(Boolean, graphql_name='hasNextPage')
    '''there are more pages to be retrieved'''



class PropertyNames(sgqlc.types.Type):
    '''All unique object property names'''
    __schema__ = schema
    __field_names__ = ('property_names',)
    property_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='propertyNames')
    '''List of object property names'''



class PropertyValues(sgqlc.types.Type):
    '''All unique object property names'''
    __schema__ = schema
    __field_names__ = ('property_values',)
    property_values = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='propertyValues')
    '''List of object property values'''



class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('ping_data_collector', 'get_github_integrations', 'get_github_pull_requests', 'get_github_pull_requests_for_table', 'get_jira_integrations', 'get_jira_projects', 'get_jira_issue_types', 'test_jira_credentials', 'get_indexed_field_specs', 'get_query_logs', 'get_query_logs_facets_v2', 'get_query_logs_facets', 'get_query_runtime_time_series_for_groups', 'get_top_query_groups', 'get_aggregated_queries', 'get_query_changes', 'get_query_rcas', 'get_query_dimensions', 'get_notification_settings', 'get_collection_dataset_list', 'get_collection_block_list', 'get_fivetran_connectors', 'get_pii_filtering_preferences', 'get_pii_filters', 'get_pii_filter_metrics', 'get_dbt_connections', 'get_dbt_projects', 'get_dbt_jobs', 'get_dbt_nodes', 'get_dbt_runs', 'get_dbt_models', 'get_dbt_model_results', 'get_dbt_model_results_count', 'get_dbt_run_steps', 'get_dbt_test_results_count', 'get_dbt_test_results', 'get_dbt_upload_url', 'get_dbt_last_run_results', 'get_exec_dashboard_metrics', 'get_exec_dashboard_tables', 'get_custom_users', 'get_unified_users', 'get_unified_user_assignments', 'get_monte_carlo_config_templates', 'export_monte_carlo_config_templates', 'get_monte_carlo_config_template_update_state', 'get_correlation_sampling_metadata', 'detect_time_axis_intrinsic_delta', 'perform_correlation_sampling', 'perform_correlation_sampling_with_time_travel', 'perform_field_health_sampling', 'get_rca_result', 'get_rca_job_result', 'get_sensitivity', 'thresholds', 'get_thresholds', 'get_table_columns_lineage', 'get_derived_tables_partial_lineage', 'get_parsed_query', 'get_job_execution_history_logs', 'get_dimension_tracking_monitor_suggestions', 'get_field_health_monitor_suggestions', 'get_monitors', 'get_monitor_queries', 'test_monitor_queries', 'get_all_user_defined_monitors_v2', 'get_all_user_defined_monitors', 'get_custom_metrics', 'get_custom_rule', 'get_custom_rules', 'get_generated_rules', 'get_circuit_breaker_rule_state', 'get_circuit_breaker_rule_state_v2', 'get_run_sql_rule_state', 'get_tables_for_sql', 'get_notification_settings_for_rules_with', 'get_field_metric_query', 'get_field_query', 'get_custom_rule_execution_analytics', 'get_insights', 'get_insight', 'get_reports', 'get_report_url', 'get_lineage_node_block_pattern', 'get_lineage_node_block_patterns', 'get_lineage_node_replacement_rule', 'get_lineage_node_replacement_rules', 'simulate_lineage_node_replacement_rule', 'get_catalog_object_metadata', 'get_catalog_nav_level_nodes', 'get_catalog_nav_grouped_nodes', 'get_object_properties', 'get_object_property_name_values', 'get_object_property_names', 'get_object_property_values', 'get_monitor_labels', 'monitor_labels', 'get_account_monitor_labels', 'get_active_monitors', 'get_monitor_summary', 'get_monitors_by_type', 'get_monitor', 'get_monitor_configuration', 'get_monitor_scheduling_configuration', 'get_time_axis_sql_expressions', 'get_notification_settings_for_monitors_with', 'get_delta_logs', 'get_data_assets_dashboard', 'get_incident_dashboard_data', 'get_incident_data_weekly', 'get_monitor_dashboard_data', 'get_blast_radius_direct_users', 'get_blast_radius_direct_users_v2', 'get_blast_radius_direct_queries', 'get_blast_radius_direct_queries_v2', 'get_blast_radius_direct_queries_summary', 'get_incident_tables', 'get_incident_warehouse_tables', 'get_direct_blast_radius_counts', 'get_blast_radius_direct_queries_for_user', 'get_airflow_tasks', 'get_airflow_task_attempts', 'get_airflow_task_logs', 'get_events', 'get_comments_for_monitor_incidents', 'get_event', 'get_event_comments', 'get_event_type_summary', 'get_incidents', 'get_incident_reaction', 'get_incident_summaries', 'get_incident_type_summary', 'get_incident_notification_settings_used', 'get_slack_messages_for_incident', 'get_slack_engagements_for_incident', 'get_all_domains', 'get_domain', 'get_account_roles', 'get_authorization_groups', 'get_user_authorization', 'search', 'get_object', 'get_metadata', 'get_metrics_v3', 'get_non_table_metrics', 'get_aggregated_metrics', 'get_latest_table_access_timestamp_metrics', 'get_top_category_labels', 'get_segmented_where_condition_labels', 'get_first_seen_dimensions_by_labels', 'get_first_and_last_seen_dimensions_by_labels', 'get_downstream_bi', 'get_downstream_impact_radius_summary', 'get_downstream_reports', 'get_downstream_report_owners', 'get_downstream_report_types', 'get_table_lineage', 'get_connected_table_lineage', 'get_external_source_paths_sample', 'get_tableau_workbook_count', 'get_query_list', 'get_query_by_id', 'get_query_by_query_hash', 'get_query_data_by_query_hash', 'get_query_data', 'get_query_log_hashes_that_affect_these_tables', 'get_query_log_hashes_on_these_tables', 'get_related_users', 'get_lineage_node_properties', 'get_recent_timestamp', 'get_hourly_row_counts', 'get_digraph', 'get_pipeline_freshness_v2', 'get_custom_sql_output_sample', 'get_metric_sampling', 'get_fh_sampling', 'get_dt_sampling', 'get_fh_reproduction_query', 'get_dt_reproduction_query', 'run_custom_query', 'test_sql_query_part', 'test_sql_query_where_expression', 'get_table_stats', 'get_resource', 'get_resources', 'get_table_fields_importance', 'get_data_maintenance_entries', 'get_wildcard_templates', 'get_common_fields', 'get_user_settings', 'get_user', 'get_user_by_id', 'get_warehouse', 'get_collection_properties', 'get_table', 'get_tables', 'get_tables_health', 'get_bq_projects', 'get_slack_oauth_url', 'get_slack_channels', 'get_slack_channels_v2', 'get_projects', 'get_datasets_by_uuid', 'get_datasets', 'get_field_bi_lineage', 'get_event_muting_rules', 'get_users_in_account', 'get_invites_in_account', 'get_token_metadata', 'get_integration_keys', 'test_existing_connection', 'test_telnet_connection', 'test_tcp_open_connection', 'test_notification_integration', 'get_databricks_cluster_info', 'get_databricks_warehouse_info', 'get_databricks_notebook_link', 'get_databricks_metadata_job_info', 'get_current_databricks_notebook_version', 'validate_connection_type', 'get_event_onboarding_data', 'get_etl_containers', 'get_supported_validations_v2', 'get_supported_table_validations', 'validate_data_asset_access', 'test_existing_connection_v2', 'list_projects', 'list_datasets', 'get_airflow_task_results')
    ping_data_collector = sgqlc.types.Field(DcPingResponse, graphql_name='pingDataCollector', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dcId', default=None)),
        ('trace_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='traceId', default=None)),
))
    )
    '''Sends a ping request to a data collector to verify it is
    operational.

    Arguments:

    * `dc_id` (`UUID!`): The UUID identifying the data collector to
      ping.
    * `trace_id` (`UUID!`): A unique identifier for correlating the
      data collector ping.
    '''

    get_github_integrations = sgqlc.types.Field(GithubAppInfo, graphql_name='getGithubIntegrations')
    '''Github integration info'''

    get_github_pull_requests = sgqlc.types.Field(GithubPullRequestsList, graphql_name='getGithubPullRequests', args=sgqlc.types.ArgDict((
        ('incident_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentUuid', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('include_zero_score', sgqlc.types.Arg(Boolean, graphql_name='includeZeroScore', default=False)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
))
    )
    '''Get the list of pull requests related to a given incident

    Arguments:

    * `incident_uuid` (`UUID!`): Incident UUID to get PRs for
    * `mcon` (`String`): mcon of the table to get the PRs for
    * `include_zero_score` (`Boolean`): Include PRs with 0 relevance
      score (default: `false`)
    * `limit` (`Int`): Limit the number of PRs returned (default:
      `10`)
    '''

    get_github_pull_requests_for_table = sgqlc.types.Field(GithubPullRequestsList, graphql_name='getGithubPullRequestsForTable', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('include_zero_score', sgqlc.types.Arg(Boolean, graphql_name='includeZeroScore', default=False)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
))
    )
    '''Get the list of pull requests related to a given incident

    Arguments:

    * `mcon` (`String!`): mcon of the table to get the PRs for
    * `include_zero_score` (`Boolean`): Include PRs with 0 relevance
      score (default: `false`)
    * `limit` (`Int`): Limit the number of PRs returned (default:
      `10`)
    '''

    get_jira_integrations = sgqlc.types.Field(sgqlc.types.list_of(JiraIntegrationOutput), graphql_name='getJiraIntegrations', args=sgqlc.types.ArgDict((
        ('integration_id', sgqlc.types.Arg(UUID, graphql_name='integrationId', default=None)),
))
    )
    '''Get the configured Jira integrations

    Arguments:

    * `integration_id` (`UUID`): Filter by integration ID
    '''

    get_jira_projects = sgqlc.types.Field(sgqlc.types.list_of(JiraProjectOutput), graphql_name='getJiraProjects', args=sgqlc.types.ArgDict((
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='integrationId', default=None)),
))
    )
    '''Get Jira projects for the given integration

    Arguments:

    * `integration_id` (`UUID!`): Jira integration id
    '''

    get_jira_issue_types = sgqlc.types.Field(sgqlc.types.list_of(JiraIssueTypeOutput), graphql_name='getJiraIssueTypes', args=sgqlc.types.ArgDict((
        ('integration_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='integrationId', default=None)),
        ('project', sgqlc.types.Arg(Int, graphql_name='project', default=None)),
))
    )
    '''Get Jira issue types for the integration

    Arguments:

    * `integration_id` (`UUID!`): Jira integration ID
    * `project` (`Int`): Filter by Jira project ID
    '''

    test_jira_credentials = sgqlc.types.Field(JiraTestCredentialsOutput, graphql_name='testJiraCredentials', args=sgqlc.types.ArgDict((
        ('server_url', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='serverUrl', default=None)),
        ('username', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='username', default=None)),
        ('api_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='apiToken', default=None)),
))
    )
    '''Test the Jira connection credentials

    Arguments:

    * `server_url` (`String!`): The domain name for your Jira site
    * `username` (`String!`): The Jira username for basic
      authentication; if not provided, the previous value will be used
    * `api_token` (`String!`): The personal API token for basic
      authentication; if not provided, the previous value will be used
    '''

    get_indexed_field_specs = sgqlc.types.Field(sgqlc.types.list_of(IndexedFieldSpecType), graphql_name='getIndexedFieldSpecs')

    get_query_logs = sgqlc.types.Field('QueryLogsResponseType', graphql_name='getQueryLogs', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(QueryLogsRequestInput), graphql_name='request', default=None)),
))
    )
    '''Arguments:

    * `request` (`QueryLogsRequestInput!`)None
    '''

    get_query_logs_facets_v2 = sgqlc.types.Field(sgqlc.types.list_of('QueryLogsFacetResponseType'), graphql_name='getQueryLogsFacetsV2', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(QueryLogsFacetRequestTypeV2), graphql_name='request', default=None)),
))
    )
    '''Arguments:

    * `request` (`QueryLogsFacetRequestTypeV2!`)None
    '''

    get_query_logs_facets = sgqlc.types.Field('QueryLogsFacetResponseType', graphql_name='getQueryLogsFacets', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(QueryLogsFacetRequestType), graphql_name='request', default=None)),
))
    )
    '''Arguments:

    * `request` (`QueryLogsFacetRequestType!`)None
    '''

    get_query_runtime_time_series_for_groups = sgqlc.types.Field('QueryRuntimeTimeSeriesResponseType', graphql_name='getQueryRuntimeTimeSeriesForGroups', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(QueryRuntimeTimeSeriesRequestType), graphql_name='request', default=None)),
))
    )
    '''Arguments:

    * `request` (`QueryRuntimeTimeSeriesRequestType!`)None
    '''

    get_top_query_groups = sgqlc.types.Field('TopQueryGroupsResponseType', graphql_name='getTopQueryGroups', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(TopQueryGroupsRequestType), graphql_name='request', default=None)),
))
    )
    '''Arguments:

    * `request` (`TopQueryGroupsRequestType!`)None
    '''

    get_aggregated_queries = sgqlc.types.Field(AggregatedQueryResults, graphql_name='getAggregatedQueries', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('query_type', sgqlc.types.Arg(sgqlc.types.non_null(QueryType), graphql_name='queryType', default=None)),
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
        ('end_cursor', sgqlc.types.Arg(String, graphql_name='endCursor', default=None)),
        ('category', sgqlc.types.Arg(QueryCategory, graphql_name='category', default=None)),
        ('user', sgqlc.types.Arg(String, graphql_name='user', default=None)),
        ('query_characters', sgqlc.types.Arg(Int, graphql_name='queryCharacters', default=50)),
))
    )
    '''Arguments:

    * `mcon` (`String!`): MCON for the table
    * `start_time` (`DateTime!`): Filter for queries on or after this
      date
    * `end_time` (`DateTime!`): Filter for queries on or before this
      date
    * `query_type` (`QueryType!`): Filter for reads or writes to the
      table
    * `limit` (`Int!`): Number of aggregated queries to return. Up to
      a maximum of 1000
    * `end_cursor` (`String`): Cursor used to get results from the
      next page
    * `category` (`QueryCategory`): Filter queries by category
    * `user` (`String`): Filter queries by user
    * `query_characters` (`Int`): Number of characters to return for
      the sample query (default: `50`)
    '''

    get_query_changes = sgqlc.types.Field(sgqlc.types.list_of('QueryChange'), graphql_name='getQueryChanges', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''Get query changes detected for a given incident. DEPRECATED: to be
    removed in favor of `getQueryRcas`.

    Arguments:

    * `incident_id` (`UUID!`): Incident identifier
    '''

    get_query_rcas = sgqlc.types.Field(sgqlc.types.list_of('QueryRca'), graphql_name='getQueryRcas', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''Get query RCAs for a given incident.

    Arguments:

    * `incident_id` (`UUID!`): Incident identifier
    '''

    get_query_dimensions = sgqlc.types.Field('QueryDimensions', graphql_name='getQueryDimensions', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('query_type', sgqlc.types.Arg(sgqlc.types.non_null(QueryType), graphql_name='queryType', default=None)),
))
    )
    '''Arguments:

    * `mcon` (`String!`): Mcon for table to get query dimensions for
    * `start_time` (`DateTime!`): Filter for queries on or after this
      date
    * `end_time` (`DateTime!`): Filter for queries on or before this
      date
    * `query_type` (`QueryType!`): Filter for reads or writes to the
      table
    '''

    get_notification_settings = sgqlc.types.Field(sgqlc.types.list_of(AccountNotificationSetting), graphql_name='getNotificationSettings', args=sgqlc.types.ArgDict((
        ('monitor_labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='monitorLabels', default=None)),
))
    )
    '''Get notification settings

    Arguments:

    * `monitor_labels` (`[String]`): Filter by notifications that
      handle these monitor labels
    '''

    get_collection_dataset_list = sgqlc.types.Field(CollectionDataSetConnection, graphql_name='getCollectionDatasetList', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get datasets in the account, including blocked datasets and
    dataset unblocked recently

    Arguments:

    * `resource_id` (`UUID`): Filter by resource id
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_collection_block_list = sgqlc.types.Field(CollectionBlockConnection, graphql_name='getCollectionBlockList', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get entities blocked from metadata collection in my account.

    Arguments:

    * `resource_id` (`UUID`): Filter by resource id
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_fivetran_connectors = sgqlc.types.Field(FivetranConnectorConnection, graphql_name='getFivetranConnectors', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableMcons', default=None)),
        ('services', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='services', default=None)),
        ('statuses', sgqlc.types.Arg(sgqlc.types.list_of(FivetranConnectorStatuses), graphql_name='statuses', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get fivetran connectors

    Arguments:

    * `mcons` (`[String]`): Filter by a list of MCONs
    * `table_mcons` (`[String]`): Filter by a list of table MCONs
    * `services` (`[String]`): Filter by a list of fivetran connector
      sources
    * `statuses` (`[FivetranConnectorStatuses]`): Filter by a list of
      fivetran connector statuses
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_pii_filtering_preferences = sgqlc.types.Field(PiiFilteringPreferencesOutput, graphql_name='getPiiFilteringPreferences')
    '''The PII filter settings for the user's account.'''

    get_pii_filters = sgqlc.types.Field(sgqlc.types.list_of(PiiFilterOutput), graphql_name='getPiiFilters')
    '''The possible PII filters for the user's account.'''

    get_pii_filter_metrics = sgqlc.types.Field(sgqlc.types.list_of(PiiFilterMetricOutput), graphql_name='getPiiFilterMetrics', args=sgqlc.types.ArgDict((
        ('resource_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='resourceIds', default=None)),
        ('filter_names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='filterNames', default=None)),
        ('job_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='jobTypes', default=None)),
        ('earliest_job_completion_time', sgqlc.types.Arg(DateTime, graphql_name='earliestJobCompletionTime', default=None)),
        ('latest_job_completion_time', sgqlc.types.Arg(DateTime, graphql_name='latestJobCompletionTime', default=None)),
        ('number_of_jobs', sgqlc.types.Arg(Int, graphql_name='numberOfJobs', default=100)),
))
    )
    '''PII filter metrics per job run.

    Arguments:

    * `resource_ids` (`[UUID]`): UUIDs of which resources to look for.
    * `filter_names` (`[String]`): Names of specific PII filters to
      look for.
    * `job_types` (`[String]`): Specify job types to look for.
    * `earliest_job_completion_time` (`DateTime`): How far back to
      look for the job completion time.
    * `latest_job_completion_time` (`DateTime`): How recent to look
      for the job completion time.
    * `number_of_jobs` (`Int`): How many recent job runs to use in the
      metrics aggregation (maximum is 100). (default: `100`)
    '''

    get_dbt_connections = sgqlc.types.Field(sgqlc.types.list_of(Connection), graphql_name='getDbtConnections')
    '''Get dbt connections'''

    get_dbt_projects = sgqlc.types.Field(DbtProjectConnection, graphql_name='getDbtProjects', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('connection_id', sgqlc.types.Arg(String, graphql_name='connectionId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get dbt projects

    Arguments:

    * `uuid` (`String`): dbt project id
    * `project_name` (`String`): dbt project name
    * `connection_id` (`String`): dbt connection id
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_dbt_jobs = sgqlc.types.Field(DbtJobConnection, graphql_name='getDbtJobs', args=sgqlc.types.ArgDict((
        ('project_id', sgqlc.types.Arg(UUID, graphql_name='projectId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get dbt jobs

    Arguments:

    * `project_id` (`UUID`): dbt project id
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_dbt_nodes = sgqlc.types.Field(DbtNodeConnection, graphql_name='getDbtNodes', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('dbt_project_uuid', sgqlc.types.Arg(String, graphql_name='dbtProjectUuid', default=None)),
        ('table_mcon', sgqlc.types.Arg(String, graphql_name='tableMcon', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableMcons', default=None)),
        ('dbt_unique_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='dbtUniqueIds', default=None)),
        ('resource_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='resourceTypes', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get dbt nodes

    Arguments:

    * `uuid` (`String`): Filter by UUID of dbt node
    * `dbt_project_uuid` (`String`): Filter by UUID of dbt project
    * `table_mcon` (`String`): Filter by table MCON (deprecated, use
      tableMcons instead)
    * `table_mcons` (`[String]`): Filter by list of table MCON
    * `dbt_unique_ids` (`[String]`): Filter by list of dbt node
      unique_id
    * `resource_types` (`[String]`): Filter by dbt node resource type
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_dbt_runs = sgqlc.types.Field(DbtRunConnection, graphql_name='getDbtRuns', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('dbt_project_uuid', sgqlc.types.Arg(String, graphql_name='dbtProjectUuid', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get dbt runs

    Arguments:

    * `uuid` (`String`): Filter by UUID of dbt node
    * `dbt_project_uuid` (`String`): Filter by UUID of dbt project
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_dbt_models = sgqlc.types.Field(DbtModelsConnection, graphql_name='getDbtModels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('name_filter', sgqlc.types.Arg(String, graphql_name='nameFilter', default=None)),
))
    )
    '''Get dbt models

    Arguments:

    * `first` (`Int`): When paging forward: the number of items to
      return (page size)
    * `after` (`String`): When paging forward: the cursor of the last
      item on the previous page of results
    * `last` (`Int`): When paging backward: the number of items to
      return (page size)
    * `before` (`String`): When paging backward: the cursor of the
      first item on the next page of results
    * `name_filter` (`String`): Filter the models for which the name
      start with this string
    '''

    get_dbt_model_results = sgqlc.types.Field(DbtModelResultsConnection, graphql_name='getDbtModelResults', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
        ('model', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='model', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcon', default=None)),
))
    )
    '''Get dbt model results

    Arguments:

    * `first` (`Int`): When paging forward: the number of items to
      return (page size)
    * `after` (`String`): When paging forward: the cursor of the last
      item on the previous page of results
    * `last` (`Int`): When paging backward: the number of items to
      return (page size)
    * `before` (`String`): When paging backward: the cursor of the
      first item on the next page of results
    * `run_start_time` (`DateTime!`): Beginning of time window to
      filter run start times
    * `run_end_time` (`DateTime!`): End of time window to filter run
      start times
    * `status` (`[String]`): Status(es) to filter run results
    * `model` (`[String]`): dbt model ids to filter run results
    * `mcon` (`[String]`): Associated table MCONs to filter run
      results
    '''

    get_dbt_model_results_count = sgqlc.types.Field(Int, graphql_name='getDbtModelResultsCount', args=sgqlc.types.ArgDict((
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
))
    )
    '''Get the count of dbt model results

    Arguments:

    * `run_start_time` (`DateTime!`): Beginning of time window to
      filter run start times
    * `run_end_time` (`DateTime!`): End of time window to filter run
      start times
    * `status` (`[String]`): Status(es) to filter run results
    '''

    get_dbt_run_steps = sgqlc.types.Field(sgqlc.types.list_of('DbtRunStep'), graphql_name='getDbtRunSteps', args=sgqlc.types.ArgDict((
        ('node_unique_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='nodeUniqueId', default=None)),
        ('table_mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tableMcon', default=None)),
        ('completed_at_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='completedAtStartTime', default=None)),
        ('completed_at_end_time', sgqlc.types.Arg(DateTime, graphql_name='completedAtEndTime', default=None)),
        ('status', sgqlc.types.Arg(String, graphql_name='status', default=None)),
))
    )
    '''Get dbt run steps

    Arguments:

    * `node_unique_id` (`String!`): dbt test id
    * `table_mcon` (`String!`): MCON of the associated table
    * `completed_at_start_time` (`DateTime!`): Filter the results by
      those that completed on or after this time
    * `completed_at_end_time` (`DateTime`): Filter the results by
      those that completed before this time
    * `status` (`String`): Filter results by completion status
    '''

    get_dbt_test_results_count = sgqlc.types.Field(Int, graphql_name='getDbtTestResultsCount', args=sgqlc.types.ArgDict((
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
))
    )
    '''Get the count of dbt test results

    Arguments:

    * `run_start_time` (`DateTime!`): Beginning of time window to
      filter run start times
    * `run_end_time` (`DateTime!`): End of time window to filter run
      start times
    * `status` (`[String]`): Status(es) to filter run results
    '''

    get_dbt_test_results = sgqlc.types.Field(DbtTestResultsConnection, graphql_name='getDbtTestResults', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
        ('model', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='model', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcon', default=None)),
))
    )
    '''Get dbt test results

    Arguments:

    * `first` (`Int`): When paging forward: the number of items to
      return (page size)
    * `after` (`String`): When paging forward: the cursor of the last
      item on the previous page of results
    * `last` (`Int`): When paging backward: the number of items to
      return (page size)
    * `before` (`String`): When paging backward: the cursor of the
      first item on the next page of results
    * `run_start_time` (`DateTime!`): Beginning of time window to
      match run start times
    * `run_end_time` (`DateTime!`): End of time window to match run
      start times
    * `status` (`[String]`): Status(es) to match run results
    * `model` (`[String]`): dbt model ids to filter run results
    * `mcon` (`[String]`): Associated table MCONs to filter run
      results
    '''

    get_dbt_upload_url = sgqlc.types.Field(String, graphql_name='getDbtUploadUrl', args=sgqlc.types.ArgDict((
        ('project_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectName', default=None)),
        ('invocation_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invocationId', default=None)),
        ('file_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fileName', default=None)),
))
    )
    '''Get the Dbt artifacts presigned upload url

    Arguments:

    * `project_name` (`String!`): dbt project name
    * `invocation_id` (`String!`): dbt invocation id
    * `file_name` (`String!`): name of the file for the upload
    '''

    get_dbt_last_run_results = sgqlc.types.Field(DbtModelResultsConnection, graphql_name='getDbtLastRunResults', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('run_start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='runEndTime', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='mcons', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='status', default=None)),
))
    )
    '''Get dbt model results for latest relevant run

    Arguments:

    * `first` (`Int`): When paging forward: the number of items to
      return (page size)
    * `after` (`String`): When paging forward: the cursor of the last
      item on the previous page of results
    * `last` (`Int`): When paging backward: the number of items to
      return (page size)
    * `before` (`String`): When paging backward: the cursor of the
      first item on the next page of results
    * `run_start_time` (`DateTime!`): Beginning of time window to
      filter run start times
    * `run_end_time` (`DateTime!`): End of time window to filter run
      start times
    * `mcons` (`[String]!`): Associated table MCONs to filter run
      results
    * `status` (`[String]!`): Status(es) to filter run results
    '''

    get_exec_dashboard_metrics = sgqlc.types.Field(sgqlc.types.list_of(ExecDashboardMetric), graphql_name='getExecDashboardMetrics', args=sgqlc.types.ArgDict((
        ('metrics', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(ExecDashboardMetrics)), graphql_name='metrics', default=None)),
        ('period_count', sgqlc.types.Arg(Int, graphql_name='periodCount', default=None)),
        ('period_unit', sgqlc.types.Arg(PeriodGrouping, graphql_name='periodUnit', default=None)),
        ('period_grouping', sgqlc.types.Arg(PeriodGrouping, graphql_name='periodGrouping', default=None)),
        ('period_total', sgqlc.types.Arg(Boolean, graphql_name='periodTotal', default=None)),
        ('period_include_current', sgqlc.types.Arg(Boolean, graphql_name='periodIncludeCurrent', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('key_assets_only', sgqlc.types.Arg(Boolean, graphql_name='keyAssetsOnly', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(TagKeyValuePairInput), graphql_name='tags', default=None)),
        ('incident_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='incidentTypes', default=None)),
))
    )
    '''Get one or more exec dashboard metrics.

    Arguments:

    * `metrics` (`[ExecDashboardMetrics]!`)None
    * `period_count` (`Int`): Number of periods to get time-bound
      values for.
    * `period_unit` (`PeriodGrouping`): Time unit to use with the
      period_count, if not defined use period_grouping.
    * `period_grouping` (`PeriodGrouping`): Time buckets to group
      time-bound metrics by.
    * `period_total` (`Boolean`): Indicates if must return a single
      value with the total.
    * `period_include_current` (`Boolean`): Indicates if must include
      until current days (otherwise will include only full
      weeks/months).
    * `resource_id` (`UUID`): Resource id to filter.
    * `domain_id` (`UUID`): Domain id to filter.
    * `key_assets_only` (`Boolean`): Only include key assets.
    * `tags` (`[TagKeyValuePairInput]`): Tags to filter.
    * `incident_types` (`[String]`): Filter by type of incident (e.g.
      anomalies)
    '''

    get_exec_dashboard_tables = sgqlc.types.Field(sgqlc.types.list_of(ExecDashboardTable), graphql_name='getExecDashboardTables', args=sgqlc.types.ArgDict((
        ('tables', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(ExecDashboardTables)), graphql_name='tables', default=None)),
        ('period_count', sgqlc.types.Arg(Int, graphql_name='periodCount', default=None)),
        ('period_unit', sgqlc.types.Arg(PeriodGrouping, graphql_name='periodUnit', default=None)),
        ('period_grouping', sgqlc.types.Arg(PeriodGrouping, graphql_name='periodGrouping', default=None)),
        ('period_total', sgqlc.types.Arg(Boolean, graphql_name='periodTotal', default=None)),
        ('period_include_current', sgqlc.types.Arg(Boolean, graphql_name='periodIncludeCurrent', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('key_assets_only', sgqlc.types.Arg(Boolean, graphql_name='keyAssetsOnly', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(TagKeyValuePairInput), graphql_name='tags', default=None)),
        ('incident_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='incidentTypes', default=None)),
))
    )
    '''Get one or more exec dashboard metrics.

    Arguments:

    * `tables` (`[ExecDashboardTables]!`)None
    * `period_count` (`Int`): Number of periods to get time-bound
      values for.
    * `period_unit` (`PeriodGrouping`): Time unit to use with the
      period_count, if not defined use period_grouping.
    * `period_grouping` (`PeriodGrouping`): Time buckets to group
      time-bound metrics by.
    * `period_total` (`Boolean`): Indicates if must return a single
      value with the total.
    * `period_include_current` (`Boolean`): Indicates if must include
      until current days (otherwise will include only full
      weeks/months).
    * `resource_id` (`UUID`): Resource id to filter.
    * `domain_id` (`UUID`): Domain id to filter.
    * `key_assets_only` (`Boolean`): Only include key assets.
    * `tags` (`[TagKeyValuePairInput]`): Tags to filter.
    * `incident_types` (`[String]`): Filter by type of incident (e.g.
      anomalies)
    '''

    get_custom_users = sgqlc.types.Field(CustomUserConnection, graphql_name='getCustomUsers', args=sgqlc.types.ArgDict((
        ('custom_user_id', sgqlc.types.Arg(String, graphql_name='customUserId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get all unified users

    Arguments:

    * `custom_user_id` (`String`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_unified_users = sgqlc.types.Field('UnifiedUserConnection', graphql_name='getUnifiedUsers', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(String, graphql_name='uuid', default=None)),
        ('display_name_search', sgqlc.types.Arg(String, graphql_name='displayNameSearch', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get all unified users

    Arguments:

    * `uuid` (`String`)None
    * `display_name_search` (`String`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_unified_user_assignments = sgqlc.types.Field('UnifiedUserAssignmentConnection', graphql_name='getUnifiedUserAssignments', args=sgqlc.types.ArgDict((
        ('unified_user_id', sgqlc.types.Arg(String, graphql_name='unifiedUserId', default=None)),
        ('object_mcon', sgqlc.types.Arg(String, graphql_name='objectMcon', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get all unified user assignments

    Arguments:

    * `unified_user_id` (`String`)None
    * `object_mcon` (`String`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_monte_carlo_config_templates = sgqlc.types.Field(MonteCarloConfigTemplateConnection, graphql_name='getMonteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    '''Get existing Monte Carlo config templates

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `namespace` (`String`)None
    '''

    export_monte_carlo_config_templates = sgqlc.types.Field(MonteCarloConfigTemplateExportResponse, graphql_name='exportMonteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('monitor_uuids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='monitorUuids', default=None)),
        ('notification_uuids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='notificationUuids', default=None)),
        ('export_name', sgqlc.types.Arg(Boolean, graphql_name='exportName', default=False)),
))
    )
    '''Export Monte Carlo config templates from existing custom monitors

    Arguments:

    * `monitor_uuids` (`[UUID]`): List of custom monitor uuids to
      export
    * `notification_uuids` (`[UUID]`): List of notifications uuids to
      export
    * `export_name` (`Boolean`): Include the resource name in the
      export (default: `false`)
    '''

    get_monte_carlo_config_template_update_state = sgqlc.types.Field(MonteCarloConfigTemplateUpdateAsyncState, graphql_name='getMonteCarloConfigTemplateUpdateState', args=sgqlc.types.ArgDict((
        ('update_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='updateUuid', default=None)),
))
    )
    '''Get result of async Monte Carlo config template update

    Arguments:

    * `update_uuid` (`UUID!`): UUID of update to fetch result for
    '''

    get_correlation_sampling_metadata = sgqlc.types.Field(CorrelationSamplingMetadata, graphql_name='getCorrelationSamplingMetadata', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default='Table MCON')),
))
    )
    '''Provides initial information for sampling requests (e.g. time axis
    candidates, explanatory fields, etc.

    Arguments:

    * `mcon` (`String!`)None (default: `"Table MCON"`)
    '''

    detect_time_axis_intrinsic_delta = sgqlc.types.Field('TimeAxisDeltaDetectionResult', graphql_name='detectTimeAxisIntrinsicDelta', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default='Table MCON')),
        ('time_axis', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timeAxis', default='Time axis field name')),
        ('anchor_event', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='anchorEvent', default='Anomaly event used for finding the time axis and intrinsic time overlap')),
))
    )
    '''Detects time delta between the selected time axis and intrinsic
    time

    Arguments:

    * `mcon` (`String!`)None (default: `"Table MCON"`)
    * `time_axis` (`String!`)None (default: `"Time axis field name"`)
    * `anchor_event` (`UUID!`)None (default: `"Anomaly event used for
      finding the time axis and intrinsic time overlap"`)
    '''

    perform_correlation_sampling = sgqlc.types.Field(CorrelationSamplingResult, graphql_name='performCorrelationSampling', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('time_axis', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='timeAxis', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('max_values', sgqlc.types.Arg(Int, graphql_name='maxValues', default=5)),
        ('max_rows', sgqlc.types.Arg(Int, graphql_name='maxRows', default=1000)),
))
    )
    '''Samples value distribution data alongside the time axis

    Arguments:

    * `mcon` (`String!`): MCON of the sampled table
    * `field` (`String!`): Field to be sampled
    * `time_axis` (`String!`): Time axis field used for sampling
    * `start_time` (`DateTime!`): Start time for sampling
    * `end_time` (`DateTime!`): End time for sampling
    * `max_values` (`Int`): Maximum number of top values (the rest is
      aggregated in "others") (default: `5`)
    * `max_rows` (`Int`): Maximum number of rows returned (default:
      `1000`)
    '''

    perform_correlation_sampling_with_time_travel = sgqlc.types.Field(CorrelationSamplingResult, graphql_name='performCorrelationSamplingWithTimeTravel', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('max_values', sgqlc.types.Arg(Int, graphql_name='maxValues', default=5)),
        ('max_rows', sgqlc.types.Arg(Int, graphql_name='maxRows', default=1000)),
))
    )
    '''Samples value distribution data alongside the time axis

    Arguments:

    * `mcon` (`String!`): MCON of the sampled table
    * `field` (`String!`): Field to be sampled
    * `start_time` (`DateTime!`): Start time for sampling
    * `end_time` (`DateTime!`): End time for sampling
    * `max_values` (`Int`): Maximum number of top values (the rest is
      aggregated in "others") (default: `5`)
    * `max_rows` (`Int`): Maximum number of rows returned (default:
      `1000`)
    '''

    perform_field_health_sampling = sgqlc.types.Field(FieldHealthSampling, graphql_name='performFieldHealthSampling', args=sgqlc.types.ArgDict((
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('max_rows', sgqlc.types.Arg(Int, graphql_name='maxRows', default=1000)),
        ('event_uuid', sgqlc.types.Arg(UUID, graphql_name='eventUuid', default=None)),
))
    )
    '''Samples value distribution data alongside the time axis

    Arguments:

    * `field` (`String!`): Field to be sampled
    * `metric` (`String!`): Metric to be sampled
    * `monitor_uuid` (`UUID!`): The Monitor UUID that monitors the
      field health
    * `start_time` (`DateTime!`): Start time for sampling
    * `end_time` (`DateTime!`): End time for sampling
    * `max_rows` (`Int`): Maximum number of rows returned (default:
      `1000`)
    * `event_uuid` (`UUID`): Optional UUID of an event that contains
      field metric anomaly
    '''

    get_rca_result = sgqlc.types.Field('RcaResult', graphql_name='getRcaResult', args=sgqlc.types.ArgDict((
        ('event_uuid', sgqlc.types.Arg(UUID, graphql_name='eventUuid', default=None)),
))
    )
    '''Arguments:

    * `event_uuid` (`UUID`)None
    '''

    get_rca_job_result = sgqlc.types.Field('RcaResult', graphql_name='getRcaJobResult', args=sgqlc.types.ArgDict((
        ('job_uuid', sgqlc.types.Arg(UUID, graphql_name='jobUuid', default=None)),
))
    )
    '''Arguments:

    * `job_uuid` (`UUID`)None
    '''

    get_sensitivity = sgqlc.types.Field('SensitivityThreshold', graphql_name='getSensitivity', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(UUID, graphql_name='monitorUuid', default=None)),
))
    )
    '''Arguments:

    * `mcon` (`String`)None
    * `event_type` (`String`)None
    * `monitor_uuid` (`UUID`)None
    '''

    thresholds = sgqlc.types.Field('ThresholdsData', graphql_name='thresholds')
    '''Section describing various anomaly thresholds for the table'''

    get_thresholds = sgqlc.types.Field('ThresholdsData', graphql_name='getThresholds')
    '''Section describing various anomaly thresholds for the table'''

    get_table_columns_lineage = sgqlc.types.Field('TableColumnsLineageResult', graphql_name='getTableColumnsLineage', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Column level lineage for a destination table

    Arguments:

    * `mcon` (`String`): Destination table mcon
    '''

    get_derived_tables_partial_lineage = sgqlc.types.Field(DerivedTablesLineageResult, graphql_name='getDerivedTablesPartialLineage', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('column', sgqlc.types.Arg(String, graphql_name='column', default=None)),
        ('cursor', sgqlc.types.Arg(String, graphql_name='cursor', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=20)),
))
    )
    '''Tables and its columns that are influenced by the source table and
    column. Note we only return columns that are influenced by the
    source column in the response.

    Arguments:

    * `mcon` (`String`): source table mcon
    * `column` (`String`): source column
    * `cursor` (`String`): cursor for getting the next page
    * `page_size` (`Int`): number of derived tables to return in a
      call (default: `20`)
    '''

    get_parsed_query = sgqlc.types.Field(ParsedQueryResult, graphql_name='getParsedQuery', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''The query, based on which the table's created

    Arguments:

    * `mcon` (`String`): Source table mcon
    '''

    get_job_execution_history_logs = sgqlc.types.Field(sgqlc.types.list_of(JobExecutionHistoryLog), graphql_name='getJobExecutionHistoryLogs', args=sgqlc.types.ArgDict((
        ('job_schedule_uuid', sgqlc.types.Arg(String, graphql_name='jobScheduleUuid', default=None)),
        ('monitor_uuid', sgqlc.types.Arg(String, graphql_name='monitorUuid', default=None)),
        ('custom_rule_uuid', sgqlc.types.Arg(String, graphql_name='customRuleUuid', default=None)),
        ('history_days', sgqlc.types.Arg(Int, graphql_name='historyDays', default=None)),
        ('include_snoozed', sgqlc.types.Arg(Boolean, graphql_name='includeSnoozed', default=False)),
        ('include_data_collection_only', sgqlc.types.Arg(Boolean, graphql_name='includeDataCollectionOnly', default=False)),
))
    )
    '''Arguments:

    * `job_schedule_uuid` (`String`): UUID of job schedule
    * `monitor_uuid` (`String`): UUID of monitor
    * `custom_rule_uuid` (`String`): UUID of custom rule
    * `history_days` (`Int`): Number of days back
    * `include_snoozed` (`Boolean`): Include snoozed jobs (default:
      `false`)
    * `include_data_collection_only` (`Boolean`): Include data
      collection only jobs (default: `false`)
    '''

    get_dimension_tracking_monitor_suggestions = sgqlc.types.Field(DimensionTrackingSuggestionsConnection, graphql_name='getDimensionTrackingMonitorSuggestions', args=sgqlc.types.ArgDict((
        ('entities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entities', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Return all dimension tracking monitor suggestions for the account,
    filtering the ones that already exist for the table+field

    Arguments:

    * `entities` (`[String]`): Filter by associated entities (tables)
    * `order_by` (`String`): Sorting of results
    * `domain_id` (`UUID`): Filter by domain UUID
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_field_health_monitor_suggestions = sgqlc.types.Field(FieldHealthSuggestionsConnection, graphql_name='getFieldHealthMonitorSuggestions', args=sgqlc.types.ArgDict((
        ('entities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entities', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Return all field health monitor suggestions for the account,
    filtering the ones that already exist for the table

    Arguments:

    * `entities` (`[String]`): Filter by associated entities (tables)
    * `order_by` (`String`): Sorting of results
    * `domain_id` (`UUID`): Filter by domain UUID
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_monitors = sgqlc.types.Field(sgqlc.types.list_of('Monitor'), graphql_name='getMonitors', args=sgqlc.types.ArgDict((
        ('monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(UserDefinedMonitors), graphql_name='monitorTypes', default=None)),
        ('status_types', sgqlc.types.Arg(sgqlc.types.list_of(MonitorStatusType), graphql_name='statusTypes', default=None)),
        ('description_field_or_table', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='descriptionFieldOrTable', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('uuids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='uuids', default=None)),
        ('created_by_filters', sgqlc.types.Arg(CreatedByFilters, graphql_name='createdByFilters', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('search', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='search', default=None)),
        ('search_fields', sgqlc.types.Arg(sgqlc.types.list_of(UserDefinedMonitorSearchFields), graphql_name='searchFields', default=None)),
        ('namespaces', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='namespaces', default=None)),
        ('is_template_managed', sgqlc.types.Arg(Boolean, graphql_name='isTemplateManaged', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    '''List of monitors

    Arguments:

    * `monitor_types` (`[UserDefinedMonitors]`): Type of monitors to
      filter by, default all
    * `status_types` (`[MonitorStatusType]`): Type of monitor status
      to filter by, default all
    * `description_field_or_table` (`[String]`): DEPRECATED
    * `domain_id` (`UUID`): Domain uuid to filter by
    * `uuids` (`[String]`): list of uuids of the monitors to filter by
    * `created_by_filters` (`CreatedByFilters`): Deprecated
    * `labels` (`[String]`): List of labels to filter by
    * `search` (`[String]`): Search criteria for filtering the
      monitors list
    * `search_fields` (`[UserDefinedMonitorSearchFields]`): Which
      fields to include during search
    * `namespaces` (`[String]`): filter by namespaces
    * `is_template_managed` (`Boolean`): Filter monitors created by
      code
    * `mcons` (`[String]`): Filter by associated entities (MCON)
    * `order_by` (`String`): Field and direction to order monitors by
    * `limit` (`Int`): Number of monitors to return
    * `offset` (`Int`): From which monitor to return the next results
    '''

    get_monitor_queries = sgqlc.types.Field(MonitorQueries, graphql_name='getMonitorQueries', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('bootstrap', sgqlc.types.Arg(Boolean, graphql_name='bootstrap', default=None)),
        ('format_sql', sgqlc.types.Arg(Boolean, graphql_name='formatSql', default=True)),
        ('strip_metadata_comment', sgqlc.types.Arg(Boolean, graphql_name='stripMetadataComment', default=False)),
))
    )
    '''Arguments:

    * `monitor_uuid` (`UUID!`): UUID of monitor
    * `bootstrap` (`Boolean`): Return the bootstrap query
    * `format_sql` (`Boolean`): Pretty-print the SQL query (default:
      `true`)
    * `strip_metadata_comment` (`Boolean`): Strip the leading metadata
      comment (default: `false`)
    '''

    test_monitor_queries = sgqlc.types.Field(MonitorQueriesResults, graphql_name='testMonitorQueries', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
))
    )
    '''Arguments:

    * `monitor_uuid` (`UUID!`): UUID of monitor
    '''

    get_all_user_defined_monitors_v2 = sgqlc.types.Field('UserDefinedMonitorConnectionV2Connection', graphql_name='getAllUserDefinedMonitorsV2', args=sgqlc.types.ArgDict((
        ('user_defined_monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='userDefinedMonitorTypes', default=None)),
        ('created_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='createdBy', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('entities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entities', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('description_field_or_table', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='descriptionFieldOrTable', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('is_template_managed', sgqlc.types.Arg(Boolean, graphql_name='isTemplateManaged', default=None)),
        ('namespace', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='namespace', default=None)),
        ('rule_name', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ruleName', default=None)),
        ('search', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='search', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `user_defined_monitor_types` (`[String]`): Filter by monitor
      type
    * `created_by` (`[String]`): Filter by creator
    * `order_by` (`String`): Sorting of results
    * `entities` (`[String]`): Filter by associated entities (full
      table ID)
    * `mcons` (`[String]`): Filter by associated entities (MCON)
    * `description_field_or_table` (`[String]`): Match text on rule
      description, table, or field
    * `domain_id` (`UUID`): Filter by domain UUID
    * `is_template_managed` (`Boolean`): Filter monitors created by
      code
    * `namespace` (`[String]`): Filter by namespace -> used in
      monitors created by code
    * `rule_name` (`[String]`): Filter by rule_name -> used in
      monitors created by code
    * `search` (`[String]`): Filter by: description, field, table,
      rule name, creator, namespace
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_all_user_defined_monitors = sgqlc.types.Field('UserDefinedMonitorConnection', graphql_name='getAllUserDefinedMonitors', args=sgqlc.types.ArgDict((
        ('user_defined_monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='userDefinedMonitorTypes', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `user_defined_monitor_types` (`[String]`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_custom_metrics = sgqlc.types.Field(Metrics, graphql_name='getCustomMetrics', args=sgqlc.types.ArgDict((
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=5000)),
))
    )
    '''Retrieve custom metrics based on a custom rule

    Arguments:

    * `rule_uuid` (`UUID`): A custom rule UUID
    * `start_time` (`DateTime`): Beginning of time range to retrieve
      metrics for
    * `end_time` (`DateTime`): End of time range to retrieve metrics
      for
    * `first` (`Int`): Limit of number of metrics retrieved (default:
      `5000`)
    '''

    get_custom_rule = sgqlc.types.Field('CustomRule', graphql_name='getCustomRule', args=sgqlc.types.ArgDict((
        ('rule_id', sgqlc.types.Arg(UUID, graphql_name='ruleId', default=None)),
        ('description_contains', sgqlc.types.Arg(String, graphql_name='descriptionContains', default=None)),
        ('custom_sql_contains', sgqlc.types.Arg(String, graphql_name='customSqlContains', default=None)),
))
    )
    '''Get a custom rule

    Arguments:

    * `rule_id` (`UUID`): Rule id
    * `description_contains` (`String`): String to completely or
      partially match the rule description, case-insensitive
    * `custom_sql_contains` (`String`): String to completely or
      partially match the rule SQL, case-insensitive
    '''

    get_custom_rules = sgqlc.types.Field(CustomRuleConnection, graphql_name='getCustomRules', args=sgqlc.types.ArgDict((
        ('entity_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='entityMcons', default=None)),
        ('metadata_keys', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='metadataKeys', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('rule_type', sgqlc.types.Arg(String, graphql_name='ruleType', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(UUID, graphql_name='warehouseUuid', default=None)),
))
    )
    '''Arguments:

    * `entity_mcons` (`[String]`): Return rules associated with any of
      these table MCONs
    * `metadata_keys` (`[String]`): Return rules with all these keys
      in their metadata
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `rule_type` (`String`)None
    * `warehouse_uuid` (`UUID`)None
    '''

    get_generated_rules = sgqlc.types.Field(sgqlc.types.list_of('CustomRule'), graphql_name='getGeneratedRules', args=sgqlc.types.ArgDict((
        ('generated_by_uuid', sgqlc.types.Arg(UUID, graphql_name='generatedByUuid', default=None)),
))
    )
    '''Arguments:

    * `generated_by_uuid` (`UUID`): Parent CustomRule UUID
    '''

    get_circuit_breaker_rule_state = sgqlc.types.Field(CircuitBreakerState, graphql_name='getCircuitBreakerRuleState', args=sgqlc.types.ArgDict((
        ('job_execution_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='jobExecutionUuid', default=None)),
))
    )
    '''State for the circuit breaker rule job execution

    Arguments:

    * `job_execution_uuid` (`UUID!`): The UUID of the job execution to
      get the state for
    '''

    get_circuit_breaker_rule_state_v2 = sgqlc.types.Field(sgqlc.types.list_of(CircuitBreakerState), graphql_name='getCircuitBreakerRuleStateV2', args=sgqlc.types.ArgDict((
        ('job_execution_uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='jobExecutionUuids', default=None)),
))
    )
    '''State for the circuit breaker rule job executions

    Arguments:

    * `job_execution_uuids` (`[UUID]!`): The UUIDs of the job
      executions to get the state for
    '''

    get_run_sql_rule_state = sgqlc.types.Field(sgqlc.types.list_of(CircuitBreakerState), graphql_name='getRunSqlRuleState', args=sgqlc.types.ArgDict((
        ('job_execution_uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='jobExecutionUuids', default=None)),
))
    )
    '''State for the sql rule job executions

    Arguments:

    * `job_execution_uuids` (`[UUID]!`): The UUID of the job execution
      to get the state for
    '''

    get_tables_for_sql = sgqlc.types.Field(sgqlc.types.list_of('SqlQueryTable'), graphql_name='getTablesForSql', args=sgqlc.types.ArgDict((
        ('warehouse_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid', default=None)),
        ('custom_sql', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='customSql', default=None)),
        ('custom_sampling_sql', sgqlc.types.Arg(String, graphql_name='customSamplingSql', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
))
    )
    '''The full table ids calculated from the sql query

    Arguments:

    * `warehouse_uuid` (`UUID!`): Warehouse UUID.
    * `custom_sql` (`String!`): Custom SQL query to run
    * `custom_sampling_sql` (`String`): Custom sampling SQL query to
      run on breach
    * `variables` (`JSONString`): Possible variable values for SQL
      query
    '''

    get_notification_settings_for_rules_with = sgqlc.types.Field(sgqlc.types.list_of(AccountNotificationSetting), graphql_name='getNotificationSettingsForRulesWith', args=sgqlc.types.ArgDict((
        ('rule_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='ruleType', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('label_names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labelNames', default=None)),
))
    )
    '''The notification settings that will be used in a rule with the
    specified data

    Arguments:

    * `rule_type` (`String!`): Rule type.
    * `warehouse_uuid` (`UUID!`): Warehouse UUID.
    * `full_table_ids` (`[String]`): Full table ids.
    * `label_names` (`[String]`): Monitor labels.
    '''

    get_field_metric_query = sgqlc.types.Field(FieldMetricQuery, graphql_name='getFieldMetricQuery', args=sgqlc.types.ArgDict((
        ('field_metric', sgqlc.types.Arg(sgqlc.types.non_null(FieldMetricInput), graphql_name='fieldMetric', default=None)),
))
    )
    '''Build Field Metric query from parameters

    Arguments:

    * `field_metric` (`FieldMetricInput!`): Field Metric query
      parameters
    '''

    get_field_query = sgqlc.types.Field(FieldQuery, graphql_name='getFieldQuery', args=sgqlc.types.ArgDict((
        ('field_query_parameters', sgqlc.types.Arg(sgqlc.types.non_null(FieldQueryParametersInput), graphql_name='fieldQueryParameters', default=None)),
))
    )
    '''Build Field Metric query from parameters

    Arguments:

    * `field_query_parameters` (`FieldQueryParametersInput!`): Field
      Metric query parameters
    '''

    get_custom_rule_execution_analytics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CustomRuleExecutionAnalytics))), graphql_name='getCustomRuleExecutionAnalytics', args=sgqlc.types.ArgDict((
        ('rule_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='ruleId', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('group_by', sgqlc.types.Arg(sgqlc.types.non_null(PeriodGrouping), graphql_name='groupBy', default=None)),
))
    )
    '''Return analytics for the executions of the custom rules

    Arguments:

    * `rule_id` (`UUID!`): Rule id
    * `start_time` (`DateTime!`): Beginning of time range to calculate
      the execution analytics
    * `end_time` (`DateTime`): End of time range to calculate the
      execution analytics
    * `group_by` (`PeriodGrouping!`): Time buckets to group time-bound
      analytics by.
    '''

    get_insights = sgqlc.types.Field(sgqlc.types.list_of(Insight), graphql_name='getInsights')
    '''List of available insights'''

    get_insight = sgqlc.types.Field(Insight, graphql_name='getInsight', args=sgqlc.types.ArgDict((
        ('insight_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='insightName', default=None)),
))
    )
    '''Arguments:

    * `insight_name` (`String!`): Name (id) of insight to fetch
    '''

    get_reports = sgqlc.types.Field(sgqlc.types.list_of('Report'), graphql_name='getReports', args=sgqlc.types.ArgDict((
        ('insight_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='insightName', default=None)),
))
    )
    '''Arguments:

    * `insight_name` (`String!`): Name (id) of insight for which to
      fetch reports
    '''

    get_report_url = sgqlc.types.Field('ResponseURL', graphql_name='getReportUrl', args=sgqlc.types.ArgDict((
        ('insight_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='insightName', default=None)),
        ('report_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reportName', default=None)),
        ('created_before', sgqlc.types.Arg(DateTime, graphql_name='createdBefore', default=None)),
))
    )
    '''Name (id) of insight to fetch

    Arguments:

    * `insight_name` (`String!`)None
    * `report_name` (`String!`): Name of report to fetch
    * `created_before` (`DateTime`): Version of the report created
      before specific date
    '''

    get_lineage_node_block_pattern = sgqlc.types.Field(LineageNodeBlockPattern, graphql_name='getLineageNodeBlockPattern', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
))
    )
    '''Retrieve a node block pattern

    Arguments:

    * `uuid` (`String!`): Node block pattern id
    '''

    get_lineage_node_block_patterns = sgqlc.types.Field(sgqlc.types.list_of(LineageNodeBlockPattern), graphql_name='getLineageNodeBlockPatterns', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='resourceId', default=None)),
))
    )
    '''Retrieve a list of node block patterns

    Arguments:

    * `resource_id` (`String!`): Resource id of the resources
    '''

    get_lineage_node_replacement_rule = sgqlc.types.Field(LineageNodeReplacementRule, graphql_name='getLineageNodeReplacementRule', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Retrieve a node replacement rule

    Arguments:

    * `uuid` (`UUID!`): Replacement rule UUID
    '''

    get_lineage_node_replacement_rules = sgqlc.types.Field(sgqlc.types.list_of(LineageNodeReplacementRule), graphql_name='getLineageNodeReplacementRules', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='resourceId', default=None)),
))
    )
    '''Retrieve a list of node replacement rules

    Arguments:

    * `resource_id` (`UUID!`): Resource id of the resources
    '''

    simulate_lineage_node_replacement_rule = sgqlc.types.Field(sgqlc.types.list_of(LineageNodeReplacementRuleResult), graphql_name='simulateLineageNodeReplacementRule', args=sgqlc.types.ArgDict((
        ('pattern', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='pattern', default=None)),
        ('replacement', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='replacement', default=None)),
        ('test_input_strings', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='testInputStrings', default=None)),
        ('case_insensitive', sgqlc.types.Arg(Boolean, graphql_name='caseInsensitive', default=None)),
))
    )
    '''Simulate a replacement pattern

    Arguments:

    * `pattern` (`String!`): Input regex pattern
    * `replacement` (`String!`): Replacement pattern
    * `test_input_strings` (`[String]!`): Input to test
    * `case_insensitive` (`Boolean`): Case sensitivity of the pattern
      matching
    '''

    get_catalog_object_metadata = sgqlc.types.Field(CatalogObjectMetadataConnection, graphql_name='getCatalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `mcon` (`String`)None
    '''

    get_catalog_nav_level_nodes = sgqlc.types.Field(CatalogNavResults, graphql_name='getCatalogNavLevelNodes', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('parent_mcon', sgqlc.types.Arg(String, graphql_name='parentMcon', default=None)),
        ('object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='objectTypes', default=None)),
        ('exclude_object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='excludeObjectTypes', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Get nodes for navigating the catalog by type and hierarchy.

    Arguments:

    * `mcon` (`String`): Filter by mcon, returns this single object
    * `parent_mcon` (`String`): Only include children of this catalog
      object. If not given, will get top-level objects.
    * `object_types` (`[String]`): Only include objects of these
      types.
    * `exclude_object_types` (`[String]`): Exclude objects of these
      types.
    * `domain_id` (`UUID`): Only include objects in this domain or its
      hierarchy.
    * `offset` (`Int`): Starting node index for current page.
    * `limit` (`Int`): Max nodes to get for page.
    '''

    get_catalog_nav_grouped_nodes = sgqlc.types.Field(sgqlc.types.list_of(CatalogNavResults), graphql_name='getCatalogNavGroupedNodes', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('parent_mcon', sgqlc.types.Arg(String, graphql_name='parentMcon', default=None)),
        ('object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='objectTypes', default=None)),
        ('exclude_object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='excludeObjectTypes', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Get nodes for navigating the catalog by type and hierarchy.

    Arguments:

    * `mcon` (`String`): Filter by mcon, returns this single object
    * `parent_mcon` (`String`): Only include children of this catalog
      object. If not given, will get top-level objects.
    * `object_types` (`[String]`): Only include objects of these
      types.
    * `exclude_object_types` (`[String]`): Exclude objects of these
      types.
    * `domain_id` (`UUID`): Only include objects in this domain or its
      hierarchy.
    * `offset` (`Int`): Starting node index for current page.
    * `limit` (`Int`): Max nodes to get for page.
    '''

    get_object_properties = sgqlc.types.Field(ObjectPropertyConnection, graphql_name='getObjectProperties', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon_id', sgqlc.types.Arg(String, graphql_name='mconId', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `mcon_id` (`String`)None
    '''

    get_object_property_name_values = sgqlc.types.Field(PropertyNameValues, graphql_name='getObjectPropertyNameValues', args=sgqlc.types.ArgDict((
        ('search_string', sgqlc.types.Arg(String, graphql_name='searchString', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    '''Return all unique property names/values for an account

    Arguments:

    * `search_string` (`String`)None
    * `first` (`Int`)None (default: `100`)
    * `offset` (`Int`)None (default: `0`)
    '''

    get_object_property_names = sgqlc.types.Field(PropertyNames, graphql_name='getObjectPropertyNames', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('search_string', sgqlc.types.Arg(String, graphql_name='searchString', default=None)),
))
    )
    '''Return all unique property names for an account

    Arguments:

    * `limit` (`Int`)None (default: `100`)
    * `offset` (`Int`)None (default: `0`)
    * `search_string` (`String`): Filter property names by search
      string
    '''

    get_object_property_values = sgqlc.types.Field(PropertyValues, graphql_name='getObjectPropertyValues', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('property_name', sgqlc.types.Arg(String, graphql_name='propertyName', default=None)),
        ('search_string', sgqlc.types.Arg(String, graphql_name='searchString', default=None)),
))
    )
    '''Return all unique property values for an account

    Arguments:

    * `limit` (`Int`)None (default: `100`)
    * `offset` (`Int`)None (default: `0`)
    * `property_name` (`String`): Filter by property name
    * `search_string` (`String`): Filter property values by search
      string
    '''

    get_monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(MonitorLabelObject), graphql_name='getMonitorLabels')
    '''Get monitor labels'''

    monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(MonitorLabel), graphql_name='monitorLabels')
    '''Get monitor labels'''

    get_account_monitor_labels = sgqlc.types.Field(sgqlc.types.list_of(MonitorLabelObject), graphql_name='getAccountMonitorLabels')
    '''Get monitor labels'''

    get_active_monitors = sgqlc.types.Field(MetricMonitoringConnection, graphql_name='getActiveMonitors', args=sgqlc.types.ArgDict((
        ('entities', sgqlc.types.Arg(String, graphql_name='entities', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Get all active monitors

    Arguments:

    * `entities` (`String`): Filter by full table id or mcon
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    get_monitor_summary = sgqlc.types.Field(MonitorSummary, graphql_name='getMonitorSummary', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
))
    )
    '''Arguments:

    * `resource_id` (`UUID`): Filter by resource UUID
    * `domain_id` (`UUID`): Filter by domain UUID
    '''

    get_monitors_by_type = sgqlc.types.Field(MetricMonitoringConnection, graphql_name='getMonitorsByType', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
        ('monitor_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='monitorTypes', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Arguments:

    * `monitor_type` (`String`)None
    * `monitor_types` (`[String]`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    get_monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='getMonitor', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
))
    )
    '''Retrieve information about a monitor

    Arguments:

    * `uuid` (`UUID`): Get monitor by UUID
    * `resource_id` (`UUID`): Specify the resource uuid (e.g.
      warehouse the table is contained in) when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Get monitor by mcon
    * `monitor_type` (`String`): Specify the monitor type. Required
      when using an mcon or full table id
    '''

    get_monitor_configuration = sgqlc.types.Field(MonitorConfiguration, graphql_name='getMonitorConfiguration', args=sgqlc.types.ArgDict((
        ('configuration_data', sgqlc.types.Arg(MonitorConfigurationInput, graphql_name='configurationData', default=None)),
))
    )
    '''The time axis data for the monitor

    Arguments:

    * `configuration_data` (`MonitorConfigurationInput`)
    '''

    get_monitor_scheduling_configuration = sgqlc.types.Field(MonitorSchedulingConfiguration, graphql_name='getMonitorSchedulingConfiguration', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    '''The scheduling configuration for the monitor

    Arguments:

    * `mcon` (`String!`): mcon for table to fetch scheduling for
    '''

    get_time_axis_sql_expressions = sgqlc.types.Field(sgqlc.types.list_of('SqlExpression'), graphql_name='getTimeAxisSqlExpressions')
    '''The SQL expressions used in time axis in monitors for the account'''

    get_notification_settings_for_monitors_with = sgqlc.types.Field(sgqlc.types.list_of(AccountNotificationSetting), graphql_name='getNotificationSettingsForMonitorsWith', args=sgqlc.types.ArgDict((
        ('monitor_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='monitorType', default=None)),
        ('label_names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labelNames', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''The notification settings that will be used in a monitor with the
    specified data

    Arguments:

    * `monitor_type` (`String!`): Monitor type.
    * `label_names` (`[String]`): Label names.
    * `mcon` (`String`): MCON of the table associated with the
      monitor.
    '''

    get_delta_logs = sgqlc.types.Field(DeltaLogConnection, graphql_name='getDeltaLogs', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    '''Get Delta logs for the provided table. Due to Databricks'
    limitations, this query field only supports forwards pagination
    with first and after, but not backwards with last and before.

    Arguments:

    * `mcon` (`String!`): MCON for table to get delta logs for
    * `start_time` (`DateTime`): Beginning of time window to filter
      to. Defaults to the 10 most recent delta logs.
    * `end_time` (`DateTime`): End of time window to filter to.
      Defaults to the 10 most recent delta logs.
    * `first` (`Int`): The number of items to return (default: 10).
    * `after` (`String`): Cursor of the last item on the previous page
    '''

    get_data_assets_dashboard = sgqlc.types.Field(DataAssetDashboard, graphql_name='getDataAssetsDashboard', args=sgqlc.types.ArgDict((
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
))
    )
    '''Dashboard counts for monitored data assets

    Arguments:

    * `domain_uuid` (`UUID`): The domain id to filter by
    '''

    get_incident_dashboard_data = sgqlc.types.Field(IncidentDashboardData, graphql_name='getIncidentDashboardData', args=sgqlc.types.ArgDict((
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
        ('lookback_weeks', sgqlc.types.Arg(Int, graphql_name='lookbackWeeks', default=None)),
))
    )
    '''Dashboard counts for incidents occurring over specified weeks

    Arguments:

    * `domain_uuid` (`UUID`): The domain id to filter by
    * `lookback_weeks` (`Int`): The number of weeks to aggregate data
      over
    '''

    get_incident_data_weekly = sgqlc.types.Field(IncidentWeeklyDataDashboard, graphql_name='getIncidentDataWeekly', args=sgqlc.types.ArgDict((
        ('group_by', sgqlc.types.Arg(sgqlc.types.non_null(IncidentGroupBy), graphql_name='groupBy', default=None)),
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
        ('lookback_weeks', sgqlc.types.Arg(Int, graphql_name='lookbackWeeks', default=None)),
))
    )
    '''Dashboard counts for incidents occurring over specified weeks

    Arguments:

    * `group_by` (`IncidentGroupBy!`): The value to group the
      incidents by
    * `domain_uuid` (`UUID`): The domain id to filter by
    * `lookback_weeks` (`Int`): The number of weeks to aggregate data
      over
    '''

    get_monitor_dashboard_data = sgqlc.types.Field(MonitorDashboardData, graphql_name='getMonitorDashboardData', args=sgqlc.types.ArgDict((
        ('domain_uuid', sgqlc.types.Arg(UUID, graphql_name='domainUuid', default=None)),
))
    )
    '''Dashboard counts for mmonitors

    Arguments:

    * `domain_uuid` (`UUID`): The domain id to filter by
    '''

    get_blast_radius_direct_users = sgqlc.types.Field(PaginateUsersBlastRadius, graphql_name='getBlastRadiusDirectUsers', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    '''User information for direct blast radius of an incident.
    DEPRECATED - please use getBlastRadiusDirectUsersV2

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    * `after_key` (`UserAfterKeyInput`): The key for pagination
    * `size` (`Int`): The max number of results to fetch
    '''

    get_blast_radius_direct_users_v2 = sgqlc.types.Field(PaginateUsersBlastRadius2, graphql_name='getBlastRadiusDirectUsersV2', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput2, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    '''User information for direct blast radius of an incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    * `after_key` (`UserAfterKeyInput2`): The key for pagination
    * `size` (`Int`): The max number of results to fetch
    '''

    get_blast_radius_direct_queries = sgqlc.types.Field(PaginateQueriesBlastRadius, graphql_name='getBlastRadiusDirectQueries', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(QueryAfterKeyInput, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    '''Direct queries for blast radius of incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    * `after_key` (`QueryAfterKeyInput`): The key for pagination
    * `size` (`Int`): The max number of results to fetch
    '''

    get_blast_radius_direct_queries_v2 = sgqlc.types.Field(PaginateQueriesBlastRadius2, graphql_name='getBlastRadiusDirectQueriesV2', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput2, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    '''Direct queries for blast radius of incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    * `after_key` (`UserAfterKeyInput2`): The key for pagination
    * `size` (`Int`): The max number of results to fetch
    '''

    get_blast_radius_direct_queries_summary = sgqlc.types.Field(PaginateQueriesBlastRadiusSummary, graphql_name='getBlastRadiusDirectQueriesSummary', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
        ('after_key', sgqlc.types.Arg(UserAfterKeyInput2, graphql_name='afterKey', default=None)),
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    '''Direct queries for blast radius of incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    * `after_key` (`UserAfterKeyInput2`): The key for pagination
    * `size` (`Int`): The max number of results to fetch
    '''

    get_incident_tables = sgqlc.types.Field(IncidentTableMcons, graphql_name='getIncidentTables', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''The MCONS directly impacted by the incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    '''

    get_incident_warehouse_tables = sgqlc.types.Field(sgqlc.types.list_of('WarehouseTable'), graphql_name='getIncidentWarehouseTables', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''The Warehouse Tables associated with an incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    '''

    get_direct_blast_radius_counts = sgqlc.types.Field(BlastRadiusCount, graphql_name='getDirectBlastRadiusCounts', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
))
    )
    '''The aggregated counts for tables directly impacted by the incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    '''

    get_blast_radius_direct_queries_for_user = sgqlc.types.Field(sgqlc.types.list_of(BlastRadiusUserQuery), graphql_name='getBlastRadiusDirectQueriesForUser', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('username', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='username', default=None)),
        ('lookback', sgqlc.types.Arg(sgqlc.types.non_null(LookbackRange), graphql_name='lookback', default=None)),
))
    )
    '''The queries for the lookback period provided for the given user

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    * `username` (`String!`): The username to get queries for
    * `lookback` (`LookbackRange!`): The lookback period for the blast
      radius [ONE_HOUR, TWELVE_HOUR, ONE_DAY, SEVEN_DAY]
    '''

    get_airflow_tasks = sgqlc.types.Field(AirflowTaskInstanceConnection, graphql_name='getAirflowTasks', args=sgqlc.types.ArgDict((
        ('task_states', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='taskStates', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableMcons', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get latest attempt for airflow tasks from the 72 hours prior to
    end_time

    Arguments:

    * `task_states` (`[String]`): Filter by these task states
    * `end_time` (`DateTime`): Filter for data older than this
    * `table_mcons` (`[String]`): Filter by the DAG IDs tagged on
      these tables
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_airflow_task_attempts = sgqlc.types.Field(AirflowTaskInstanceConnection, graphql_name='getAirflowTaskAttempts', args=sgqlc.types.ArgDict((
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('execution_date', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='executionDate', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='taskId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get all attempts for an airflow task

    Arguments:

    * `dag_id` (`String!`): DAG ID
    * `execution_date` (`String!`): DAG execution date (should be
      treated as an ID string)
    * `task_id` (`String!`): Task ID
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_airflow_task_logs = sgqlc.types.Field(AirflowTaskLog, graphql_name='getAirflowTaskLogs', args=sgqlc.types.ArgDict((
        ('dag_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='dagId', default=None)),
        ('execution_date', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='executionDate', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='taskId', default=None)),
        ('try_number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='tryNumber', default=None)),
        ('task_timestamp', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='taskTimestamp', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=1000)),
))
    )
    '''Get the logs for an Airflow task instance

    Arguments:

    * `dag_id` (`String!`): DAG ID
    * `execution_date` (`String!`): DAG execution date (should be
      treated as an ID string
    * `task_id` (`String!`): Task ID
    * `try_number` (`Int!`): Task try number (1 for first attempt)
    * `task_timestamp` (`DateTime!`): Task created_time to find ES
      index
    * `offset` (`Int`): Line offset for pagination (default: `0`)
    * `limit` (`Int`): Line limit for pagination (default: `1000`)
    '''

    get_events = sgqlc.types.Field(EventConnection, graphql_name='getEvents', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('event_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventTypes', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('tables_older_than_days', sgqlc.types.Arg(Int, graphql_name='tablesOlderThanDays', default=None)),
        ('event_states', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventStates', default=None)),
        ('exclude_state', sgqlc.types.Arg(String, graphql_name='excludeState', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('incident_id', sgqlc.types.Arg(UUID, graphql_name='incidentId', default=None)),
        ('include_timeline_events', sgqlc.types.Arg(Boolean, graphql_name='includeTimelineEvents', default=None)),
        ('include_anomaly_events', sgqlc.types.Arg(Boolean, graphql_name='includeAnomalyEvents', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get events (i.e. anomalies, changes, etc.) in my account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `full_table_id` (`String`): Filter by the full table id (e.g.
      project:dataset.table)
    * `event_type` (`String`): Filter by the type of event
    * `event_types` (`[String]`): Filter by a list of types
    * `dataset` (`String`): Filter by the dataset
    * `tables_older_than_days` (`Int`): Filter for events based on
      table age
    * `event_states` (`[String]`): Filter by a list of states
    * `exclude_state` (`String`): Exclude a specific state
    * `start_time` (`DateTime`): Filter for events newer than this
    * `end_time` (`DateTime`): Filter for events older than this
    * `incident_id` (`UUID`): Filter by incident (grouping of related
      events)
    * `include_timeline_events` (`Boolean`): Flag that decides whether
      to include incident timeline related events. If event_types
      specified, this will be ignored.
    * `include_anomaly_events` (`Boolean`): Flag that decides whether
      to include anomaly timeline related events. If event_types
      sepcified, this will be ignored
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_comments_for_monitor_incidents = sgqlc.types.Field(EventConnection, graphql_name='getCommentsForMonitorIncidents', args=sgqlc.types.ArgDict((
        ('monitor_uuids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='monitorUuids', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get comments associated with incidents that have events created by
    the monitors

    Arguments:

    * `monitor_uuids` (`[UUID]`): Monitor uuids
    * `start_time` (`DateTime`): Filter for comments newer than this
    * `end_time` (`DateTime`): Filter for comments older than this
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_event = sgqlc.types.Field('Event', graphql_name='getEvent', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Arguments:

    * `uuid` (`UUID`)None
    '''

    get_event_comments = sgqlc.types.Field(EventCommentConnection, graphql_name='getEventComments', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(UUID, graphql_name='eventId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `event_id` (`UUID`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_event_type_summary = sgqlc.types.Field(EventTypeSummary, graphql_name='getEventTypeSummary', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(UUID, graphql_name='resourceId', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Arguments:

    * `resource_id` (`UUID`)None
    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    '''

    get_incidents = sgqlc.types.Field(IncidentConnection, graphql_name='getIncidents', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('incident_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='incidentTypes', default=None)),
        ('incident_sub_types', sgqlc.types.Arg(sgqlc.types.list_of(IncidentSubType), graphql_name='incidentSubTypes', default=None)),
        ('event_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventTypes', default=None)),
        ('event_states', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='eventStates', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('incident_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='incidentIds', default=None)),
        ('owners', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='owners', default=None)),
        ('severities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='severities', default=None)),
        ('include_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='includeFeedback', default=None)),
        ('exclude_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='excludeFeedback', default=None)),
        ('projects', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='projects', default=None)),
        ('datasets', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='datasets', default=None)),
        ('tables', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tables', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('include_timeline_events', sgqlc.types.Arg(Boolean, graphql_name='includeTimelineEvents', default=None)),
        ('include_anomaly_events', sgqlc.types.Arg(Boolean, graphql_name='includeAnomalyEvents', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('monitor_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='monitorIds', default=None)),
        ('reaction_types', sgqlc.types.Arg(sgqlc.types.list_of(IncidentReactionType), graphql_name='reactionTypes', default=None)),
        ('rule_id', sgqlc.types.Arg(UUID, graphql_name='ruleId', default=None)),
        ('tag_key_value_pairs', sgqlc.types.Arg(sgqlc.types.list_of(TagKeyValuePairInput), graphql_name='tagKeyValuePairs', default=None)),
        ('tag_key_values', sgqlc.types.Arg(sgqlc.types.list_of(TagPair), graphql_name='tagKeyValues', default=None)),
        ('tag_keys', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tagKeys', default=None)),
        ('min_event_count', sgqlc.types.Arg(Int, graphql_name='minEventCount', default=None)),
        ('max_event_count', sgqlc.types.Arg(Int, graphql_name='maxEventCount', default=None)),
        ('contains_key_asset', sgqlc.types.Arg(Boolean, graphql_name='containsKeyAsset', default=None)),
        ('include_normalized', sgqlc.types.Arg(Boolean, graphql_name='includeNormalized', default=None)),
        ('has_jira_tickets', sgqlc.types.Arg(Boolean, graphql_name='hasJiraTickets', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get incidents (i.e. a collection of related events) in my account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `incident_types` (`[String]`): Filter by type of incident (e.g.
      anomalies)
    * `incident_sub_types` (`[IncidentSubType]`): Filter by incident
      sub type (e.g. freshness_anomaly)
    * `event_types` (`[String]`): Filter by type of event as an
      incident can have multiple event types
    * `event_states` (`[String]`): Filter by the state individual
      events are in
    * `start_time` (`DateTime`): Filter for incidents newer than this
    * `end_time` (`DateTime`): Filter for incidents older than this
    * `incident_ids` (`[UUID]`): Filter for specific incidents
    * `owners` (`[String]`): Filter for specific owners
    * `severities` (`[String]`): Filter for specific severities
    * `include_feedback` (`[String]`): Filter by user feedback
    * `exclude_feedback` (`[String]`): Exclude by user feedback
    * `projects` (`[String]`): Filter by projects
    * `datasets` (`[String]`): Filter by datasets
    * `tables` (`[String]`): Filter by tables
    * `full_table_ids` (`[String]`): Filter by full table ids
    * `include_timeline_events` (`Boolean`): Flag decides whether to
      include timeline events or not. By default it's false. If
      event_types field set, this will be ignored too.
    * `include_anomaly_events` (`Boolean`): Flag decides whether to
      include anomaly events or not. By default it's false. If
      event_types field set, this will be ignored too.
    * `domain_id` (`UUID`): Filter by domain UUID
    * `monitor_ids` (`[UUID]`): Filter for specific monitors
    * `reaction_types` (`[IncidentReactionType]`): Filter for specific
      reaction types
    * `rule_id` (`UUID`): Filter by custom rule UUID
    * `tag_key_value_pairs` (`[TagKeyValuePairInput]`): Filter by tag
      key values
    * `tag_key_values` (`[TagPair]`): (Deprecated, use
      `tag_key_value_pairs` instead) Filter by tag key values
    * `tag_keys` (`[String]`): (Deprecated, use `tag_key_value_pairs`
      instead) Filter by tag keys
    * `min_event_count` (`Int`): Filter to incidents with at least
      this many events
    * `max_event_count` (`Int`): Filter to incidents with at most this
      many events
    * `contains_key_asset` (`Boolean`): If true, filter to incidents
      containining a key asset
    * `include_normalized` (`Boolean`): If false, filter out
      normalized events.
    * `has_jira_tickets` (`Boolean`): If false, include incidents
      without jira tickets. If true, include incidents with jira
      tickets. If null, return all incidents.
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_incident_reaction = sgqlc.types.Field('IncidentReaction', graphql_name='getIncidentReaction', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(UUID, graphql_name='incidentId', default=None)),
))
    )
    '''Arguments:

    * `incident_id` (`UUID`)None
    '''

    get_incident_summaries = sgqlc.types.Field(sgqlc.types.list_of(IncidentSummary), graphql_name='getIncidentSummaries', args=sgqlc.types.ArgDict((
        ('incident_ids', sgqlc.types.Arg(sgqlc.types.list_of(UUID), graphql_name='incidentIds', default=None)),
))
    )
    '''Arguments:

    * `incident_ids` (`[UUID]`)None
    '''

    get_incident_type_summary = sgqlc.types.Field(IncidentTypeSummary, graphql_name='getIncidentTypeSummary', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
))
    )
    '''Get a summary of counts by type for incidents in the account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `start_time` (`DateTime`): Filter for incidents newer than this
    * `end_time` (`DateTime`): Filter for incidents older than this
    * `domain_id` (`UUID`): Filter by domain UUID
    '''

    get_incident_notification_settings_used = sgqlc.types.Field(sgqlc.types.list_of(AccountNotificationSetting), graphql_name='getIncidentNotificationSettingsUsed', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''The notification settings that were used to send notifications for
    the incident

    Arguments:

    * `incident_id` (`UUID!`): The incident UUID
    '''

    get_slack_messages_for_incident = sgqlc.types.Field(sgqlc.types.list_of('SlackMessageDetails'), graphql_name='getSlackMessagesForIncident', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
))
    )
    '''Arguments:

    * `incident_id` (`UUID!`): Filter by incident id
    '''

    get_slack_engagements_for_incident = sgqlc.types.Field(sgqlc.types.list_of('SlackEngagement'), graphql_name='getSlackEngagementsForIncident', args=sgqlc.types.ArgDict((
        ('incident_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='incidentId', default=None)),
        ('event_types', sgqlc.types.Arg(sgqlc.types.list_of(SlackEngagementEventType), graphql_name='eventTypes', default=None)),
        ('exclude_bot_engagements', sgqlc.types.Arg(Boolean, graphql_name='excludeBotEngagements', default=None)),
))
    )
    '''Arguments:

    * `incident_id` (`UUID!`): Filter by incident id
    * `event_types` (`[SlackEngagementEventType]`): Filter by
      event_type (e.g. thread_reply, reaction_added)
    * `exclude_bot_engagements` (`Boolean`): Exclude bot engagements
    '''

    get_all_domains = sgqlc.types.Field(sgqlc.types.list_of(DomainOutput), graphql_name='getAllDomains')
    '''Get all available domains'''

    get_domain = sgqlc.types.Field(DomainOutput, graphql_name='getDomain', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='uuid', default=None)),
))
    )
    '''Get domain by id

    Arguments:

    * `uuid` (`UUID!`): Domain UUID
    '''

    get_account_roles = sgqlc.types.Field(sgqlc.types.list_of('RoleOutput'), graphql_name='getAccountRoles')
    '''Get roles available for current user's account.'''

    get_authorization_groups = sgqlc.types.Field(sgqlc.types.list_of(AuthorizationGroupOutput), graphql_name='getAuthorizationGroups')
    '''Get authorization group list for the user's account.'''

    get_user_authorization = sgqlc.types.Field('UserAuthorizationOutput', graphql_name='getUserAuthorization')
    '''Get resolved authorization info for the user.'''

    search = sgqlc.types.Field('SearchResponse', graphql_name='search', args=sgqlc.types.ArgDict((
        ('object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='objectTypes', default=None)),
        ('ignore_object_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='ignoreObjectTypes', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=50)),
        ('full_results', sgqlc.types.Arg(Boolean, graphql_name='fullResults', default=True)),
        ('operator', sgqlc.types.Arg(String, graphql_name='operator', default='OR')),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('parent_mcon', sgqlc.types.Arg(String, graphql_name='parentMcon', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('tags_only', sgqlc.types.Arg(Boolean, graphql_name='tagsOnly', default=False)),
        ('include_facet_types', sgqlc.types.Arg(sgqlc.types.list_of(FacetType), graphql_name='includeFacetTypes', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tags', default=None)),
        ('tag_name_query', sgqlc.types.Arg(String, graphql_name='tagNameQuery', default=None)),
        ('tag_value_query', sgqlc.types.Arg(String, graphql_name='tagValueQuery', default=None)),
        ('resource_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='resourceIds', default=None)),
        ('tag_filters', sgqlc.types.Arg(sgqlc.types.list_of(TagFilterInput), graphql_name='tagFilters', default=None)),
        ('monitor_type', sgqlc.types.Arg(String, graphql_name='monitorType', default=None)),
))
    )
    '''Search catalog for an entity

    Arguments:

    * `object_types` (`[String]`): Filter by object type (e.g. table,
      view, etc.)
    * `ignore_object_types` (`[String]`): Filter out by object type
    * `query` (`String`): Entity to search for
    * `offset` (`Int`): Offset when paging (default: `0`)
    * `limit` (`Int`): Max results (default: `50`)
    * `full_results` (`Boolean`): Full search mode, used to search all
      available fields, not just display_name (default: `true`)
    * `operator` (`String`): Search operator to use, either OR or AND
      (DEPRECATED) (default: `"OR"`)
    * `mcon` (`String`): Filter on mcon
    * `parent_mcon` (`String`): Filter on parent_mcon
    * `domain_id` (`UUID`): Filter by domain UUID
    * `tags_only` (`Boolean`): Search only tags and descriptions (no
      display_name) (default: `false`)
    * `include_facet_types` (`[FacetType]`): Facet types to include
      (tags, tag_names, tag_values)
    * `tags` (`[String]`): Filter by tags (DEPRECATED, use tagFilters)
    * `tag_name_query` (`String`): Query tag names (DEPRECATED)
    * `tag_value_query` (`String`): Query tag values (DEPRECATED)
    * `resource_ids` (`[String]`): Filter by resource ID
    * `tag_filters` (`[TagFilterInput]`): List of tag filters
    * `monitor_type` (`String`): Exclude from results objects that do
      not support this monitor type
    '''

    get_object = sgqlc.types.Field(ObjectDocument, graphql_name='getObject', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Arguments:

    * `mcon` (`String`)None
    '''

    get_metadata = sgqlc.types.Field(sgqlc.types.list_of(ObjectDocument), graphql_name='getMetadata', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
))
    )
    '''Arguments:

    * `mcons` (`[String]`)None
    '''

    get_metrics_v3 = sgqlc.types.Field(Metrics, graphql_name='getMetricsV3', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('dimension_filters', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionFilters', default=None)),
))
    )
    '''Retrieves field-level metric values in a given time range AND in a
    given measurement time range

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `metric` (`String`): Type of metric (e.g. row_count)
    * `start_time` (`DateTime`): Filter for data newer than this
    * `field` (`String`): Filter by a specific field
    * `end_time` (`DateTime`): Filter for data older than this
    * `first` (`Int`): Number of metrics to retrieve
    * `dimension_filters` (`[MetricDimensionFilter]`): Filter by a
      list of key/value dimension pairs
    '''

    get_non_table_metrics = sgqlc.types.Field(NonTableMetrics, graphql_name='getNonTableMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('dimension_filters', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionFilters', default=None)),
))
    )
    '''Retrieves metric values in a given time range AND in a given
    measurement time range

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in
    * `mcon` (`String`): the mcon associated with the metric
    * `metric` (`String`): Type of metric (e.g. row_count)
    * `start_time` (`DateTime`): Filter for data newer than this
    * `end_time` (`DateTime`): Filter for data older than this
    * `first` (`Int`): Number of metrics to retrieve
    * `dimension_filters` (`[MetricDimensionFilter]`): Filter by a
      list of key/value dimension pairs
    '''

    get_aggregated_metrics = sgqlc.types.Field(Metrics, graphql_name='getAggregatedMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('full_table_id_list', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fullTableIdList', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('date_aggregation_bucket_size', sgqlc.types.Arg(String, graphql_name='dateAggregationBucketSize', default='day')),
))
    )
    '''Retrieves field-level metric values in a given time range AND in a
    given measurement time range

    Arguments:

    * `dw_id` (`UUID!`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id_list` (`[String]!`): Full table ID
    * `metric` (`String!`): Type of metric
    * `start_time` (`DateTime`): Filter for data newer than this
    * `end_time` (`DateTime`): Filter for data older than this
    * `date_aggregation_bucket_size` (`String`)None (default: `"day"`)
    '''

    get_latest_table_access_timestamp_metrics = sgqlc.types.Field(Metrics, graphql_name='getLatestTableAccessTimestampMetrics', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('full_table_id_list', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='fullTableIdList', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
))
    )
    '''Retrieves field-level metric values in a given time range AND in a
    given measurement time range

    Arguments:

    * `dw_id` (`UUID!`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id_list` (`[String]!`): Full table ID
    * `metric` (`String!`): Type of metric
    '''

    get_top_category_labels = sgqlc.types.Field(sgqlc.types.list_of(CategoryLabelRank), graphql_name='getTopCategoryLabels', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('monitor_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='monitorIds', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Get the top distribution labels. For use in
    getFirstSeenDimensionsByLabels

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `monitor_ids` (`[String]`): Filter results by monitor ID
    * `field` (`String`): Field (column) to get labels for
    * `start_time` (`DateTime`): Filter for data newer than this
    * `limit` (`Int`): Limit results retrieved
    * `end_time` (`DateTime`): Filter for data older than this
    '''

    get_segmented_where_condition_labels = sgqlc.types.Field(sgqlc.types.list_of('WhereConditionSegments'), graphql_name='getSegmentedWhereConditionLabels', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid', default=None)),
        ('full_table_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fullTableId', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Get top segmented where_conditions for monitor of sub-type
    segmented

    Arguments:

    * `monitor_uuid` (`UUID!`): The monitor for which to locate labels
    * `warehouse_uuid` (`UUID!`): The warehouse uuid the monitor is
      being run on
    * `full_table_id` (`String!`): The table being monitored
    * `start_time` (`DateTime!`): Filter for labels from this date
    * `end_time` (`DateTime`): Filter for labels until and including
      this date
    '''

    get_first_seen_dimensions_by_labels = sgqlc.types.Field(sgqlc.types.list_of(DimensionLabel), graphql_name='getFirstSeenDimensionsByLabels', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('dimensions_filter', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionsFilter', default=None)),
))
    )
    '''Get the first measurements of the provided labels across a time
    range

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `field` (`String`): Field (column) to get measurements for
    * `labels` (`[String]`): Labels to get measurements for. Can be
      retrieved using getFirstSeenDimensionsByLabels
    * `start_time` (`DateTime`): Filter for data newer than this
    * `end_time` (`DateTime`): Filter for data older than this
    * `dimensions_filter` (`[MetricDimensionFilter]`): Filter by a
      list of key/value dimension pairs
    '''

    get_first_and_last_seen_dimensions_by_labels = sgqlc.types.Field(sgqlc.types.list_of(DimensionLabelList), graphql_name='getFirstAndLastSeenDimensionsByLabels', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='labels', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('dimensions_filter', sgqlc.types.Arg(sgqlc.types.list_of(MetricDimensionFilter), graphql_name='dimensionsFilter', default=None)),
))
    )
    '''Get the first and last measurements per timestamp of the provided
    labels across a time range

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `field` (`String`): Field (column) to get measurements for
    * `labels` (`[String]`): Labels to get measurements for. Can be
      retrieved using getFirstSeenDimensionsByLabels
    * `start_time` (`DateTime`): Filter for data newer than this
    * `end_time` (`DateTime`): Filter for data older than this
    * `dimensions_filter` (`[MetricDimensionFilter]`): Filter by a
      list of key/value dimension pairs
    '''

    get_downstream_bi = sgqlc.types.Field(sgqlc.types.list_of(DownstreamBI), graphql_name='getDownstreamBi', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('node_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='nodeIds', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Arguments:

    * `dw_id` (`UUID`)None
    * `node_ids` (`[String]`)None
    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    '''

    get_downstream_impact_radius_summary = sgqlc.types.Field(DownstreamImpactRadiusSummary, graphql_name='getDownstreamImpactRadiusSummary', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='mcons', default=None)),
))
    )
    '''Arguments:

    * `mcons` (`[String]!`): List of MCONs where each MCON identifies
      a table whose downstream reports are being queried.
    '''

    get_downstream_reports = sgqlc.types.Field(DownstreamReports, graphql_name='getDownstreamReports', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='mcons', default=None)),
        ('name_matcher', sgqlc.types.Arg(String, graphql_name='nameMatcher', default=None)),
        ('report_types', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='reportTypes', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('sort_by', sgqlc.types.Arg(String, graphql_name='sortBy', default=None)),
        ('sort_desc', sgqlc.types.Arg(Boolean, graphql_name='sortDesc', default=None)),
))
    )
    '''Gets downstream reports for a list of tables.

    Arguments:

    * `mcons` (`[String]!`): List of MCONs where each MCON identifies
      a table whose downstream reports are being queried.
    * `name_matcher` (`String`): A string to filter names by
      performing substring match.
    * `report_types` (`[String]`): Report types to query.
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    * `sort_by` (`String`): Sort by property: [last_updated, owner_id,
      display_name, type, importance_score]
    * `sort_desc` (`Boolean`): Sort in descending order
    '''

    get_downstream_report_owners = sgqlc.types.Field(DownstreamReportOwners, graphql_name='getDownstreamReportOwners', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='mcons', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    '''Gets owners of downstream reports for a list of tables.

    Arguments:

    * `mcons` (`[String]!`): List of MCONs where each MCON identifies
      a table whose downstream report owners are being queried.
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    '''

    get_downstream_report_types = sgqlc.types.Field(DownstreamReportTypes, graphql_name='getDownstreamReportTypes', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
))
    )
    '''Gets all report types of downstream reports for a table.

    Arguments:

    * `mcon` (`String`): MCON of the table whose downstream reports
      are being queried.
    * `mcons` (`[String]`): List of MCONs of the tables whose
      downstream reports are being queried.
    '''

    get_table_lineage = sgqlc.types.Field(LineageGraph, graphql_name='getTableLineage', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('direction', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='direction', default=None)),
        ('hops', sgqlc.types.Arg(Int, graphql_name='hops', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Gets the lineage for a table up to specified number of hops in the
    lineage graph.

    Arguments:

    * `mcon` (`String!`): MCON of the table whose lineage is being
      queried.
    * `direction` (`String!`): This can be either 'upstream' or
      'downstream' based on the direction in which to traverse the
      lineage graph
    * `hops` (`Int`): The number of hops to query in the lineage
      graph. Defaults to 1.
    * `start_time` (`DateTime`): Filter for lineage data newer than
      this. Defaults to no date filtering.
    * `end_time` (`DateTime`): Filter for lineage data older than
      this. Defaults to no date filtering.
    '''

    get_connected_table_lineage = sgqlc.types.Field(sgqlc.types.list_of(FlattenedLineageGraphEdges), graphql_name='getConnectedTableLineage', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='mcons', default=None)),
))
    )
    '''Get mcon and and directly connected mcons

    Arguments:

    * `mcons` (`[String]!`)None
    '''

    get_external_source_paths_sample = sgqlc.types.Field('TableSourceSample', graphql_name='getExternalSourcePathsSample', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('max_results', sgqlc.types.Arg(Int, graphql_name='maxResults', default=20)),
))
    )
    '''Gets sample of table sources, typically external files

    Arguments:

    * `mcon` (`String!`)None
    * `max_results` (`Int`)None (default: `20`)
    '''

    get_tableau_workbook_count = sgqlc.types.Field('TableauWorkbookCount', graphql_name='getTableauWorkbookCount', args=sgqlc.types.ArgDict((
        ('bi_container_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='biContainerId', default=None)),
))
    )
    '''Gets the number of workbooks in a Tableau instance.

    Arguments:

    * `bi_container_id` (`UUID!`): Monte Carlo UUID of the Tableau BI
      container
    '''

    get_query_list = sgqlc.types.Field(sgqlc.types.list_of('QueryListResponse'), graphql_name='getQueryList', args=sgqlc.types.ArgDict((
        ('query_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryType', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('user_name', sgqlc.types.Arg(String, graphql_name='userName', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    '''Gets the queries on this table according to query type

    Arguments:

    * `query_type` (`String!`): source (reads on the table) or
      destination (writes on this table)
    * `mcon` (`String!`): Monte Carlo object name
    * `start_time` (`DateTime!`): Filter for queries newer than this
    * `end_time` (`DateTime!`): Filter for queries older than this
    * `user_name` (`String`): Filter by user name
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    '''

    get_query_by_id = sgqlc.types.Field(sgqlc.types.list_of('QueryDataObject'), graphql_name='getQueryById', args=sgqlc.types.ArgDict((
        ('query_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryId', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='timestamp', default=None)),
        ('query_format', sgqlc.types.Arg(String, graphql_name='queryFormat', default=None)),
))
    )
    '''Gets the query by query ID

    Arguments:

    * `query_id` (`String!`): Query unique identifier
    * `timestamp` (`DateTime!`): Query execution time (can be reduced
      to day on which it ran)
    * `query_format` (`String`): 'raw' or 'base64' format
    '''

    get_query_by_query_hash = sgqlc.types.Field(sgqlc.types.list_of('QueryDataObject'), graphql_name='getQueryByQueryHash', args=sgqlc.types.ArgDict((
        ('query_hash', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryHash', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='day', default=None)),
        ('query_format', sgqlc.types.Arg(String, graphql_name='queryFormat', default=None)),
))
    )
    '''Gets the query by query hash

    Arguments:

    * `query_hash` (`String!`): The query_hash for which to fetch
      query data
    * `day` (`Date!`): The day on which the query ran
    * `query_format` (`String`): 'raw' or 'base64' format
    '''

    get_query_data_by_query_hash = sgqlc.types.Field(sgqlc.types.list_of('QueryLogResponse'), graphql_name='getQueryDataByQueryHash', args=sgqlc.types.ArgDict((
        ('query_hash', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='queryHash', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='day', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    '''Fetch query metadata for a single query for all daily occurrences

    Arguments:

    * `query_hash` (`String!`): The query_hash for which to fetch the
      queries
    * `day` (`Date!`): The day for which to fetch the query metadata
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    '''

    get_query_data = sgqlc.types.Field(sgqlc.types.list_of('QueryLogResponse'), graphql_name='getQueryData', args=sgqlc.types.ArgDict((
        ('query_id', sgqlc.types.Arg(String, graphql_name='queryId', default=None)),
        ('query_hash', sgqlc.types.Arg(String, graphql_name='queryHash', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Date), graphql_name='day', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('group_id', sgqlc.types.Arg(String, graphql_name='groupId', default=None)),
))
    )
    '''Fetch query metadata for a single query for all daily occurrences

    Arguments:

    * `query_id` (`String`): The query_id for which to fetch the
      queries
    * `query_hash` (`String`): The query_hash for which to fetch the
      queries
    * `day` (`Date!`): The day for which to fetch the query metadata
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    * `group_id` (`String`): Fetch queries that share the same
      group_id
    '''

    get_query_log_hashes_that_affect_these_tables = sgqlc.types.Field(sgqlc.types.list_of('QueryLogHashes'), graphql_name='getQueryLogHashesThatAffectTheseTables', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('users', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='users', default=None)),
        ('query_characters', sgqlc.types.Arg(Int, graphql_name='queryCharacters', default=None)),
))
    )
    '''Get query log aggregates (AKA updates to these tables)

    Arguments:

    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `full_table_ids` (`[String]`): Deprecated - use mcons. Ignored
      if mcons are present
    * `mcons` (`[String]`): List of mcons to get details for
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    * `start_time` (`DateTime`): Filter for queries newer than this
    * `end_time` (`DateTime`): Filter for queries older than this
    * `users` (`[String]`): List of users to get details for
    * `query_characters` (`Int`): The number of characters in the
      query to return
    '''

    get_query_log_hashes_on_these_tables = sgqlc.types.Field(sgqlc.types.list_of('QueryLogHashes'), graphql_name='getQueryLogHashesOnTheseTables', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('users', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='users', default=None)),
        ('query_characters', sgqlc.types.Arg(Int, graphql_name='queryCharacters', default=None)),
))
    )
    '''Get query log aggregates (AKA queries on these tables)

    Arguments:

    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `full_table_ids` (`[String]`): Deprecated - use mcons. Ignored
      if mcons are present
    * `mcons` (`[String]`): List of mcons to get details for
    * `limit` (`Int`): Limit results returned
    * `offset` (`Int`): Offset when paging
    * `start_time` (`DateTime`): Filter for queries newer than this
    * `end_time` (`DateTime`): Filter for queries older than this
    * `users` (`[String]`): List of users to get details for
    * `query_characters` (`Int`): The number of characters to return
      of the query
    '''

    get_related_users = sgqlc.types.Field(sgqlc.types.list_of('RelatedUserCount'), graphql_name='getRelatedUsers', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('query_type', sgqlc.types.Arg(String, graphql_name='queryType', default=None)),
))
    )
    '''Get users related to object

    Arguments:

    * `mcon` (`String!`): Monte Carlo object name
    * `start_time` (`DateTime`): Filter for queries newer than this.
      By default, endTime - 3 weeks
    * `end_time` (`DateTime`): Filter for queries older than this. By
      default, now
    * `query_type` (`String`): source (reads on the table) or
      destination (writes on this table)
    '''

    get_lineage_node_properties = sgqlc.types.Field(sgqlc.types.list_of(NodeProperties), graphql_name='getLineageNodeProperties', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('node_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='nodeIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
))
    )
    '''Get properties (metadata) from nodes (DEPRECATED, use GetMetadata
    instead!)

    Arguments:

    * `dw_id` (`UUID`): Warehouse the asset is contained within. Not
      required when using an mcon as node id
    * `node_ids` (`[String]`): Deprecated - use mcon. Ignored if mcon
      is present
    * `mcons` (`[String]`): List of mcons to get properties for
    '''

    get_recent_timestamp = sgqlc.types.Field(sgqlc.types.list_of('RecentTimestamp'), graphql_name='getRecentTimestamp', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Get most recent timestamps for time axis fields (AKA live
    freshness)

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    '''

    get_hourly_row_counts = sgqlc.types.Field(HourlyRowCountsResponse, graphql_name='getHourlyRowCounts', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('interval_days', sgqlc.types.Arg(Int, graphql_name='intervalDays', default=2)),
        ('field_name', sgqlc.types.Arg(String, graphql_name='fieldName', default=None)),
))
    )
    '''Get hourly row counts by a time axis

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `interval_days` (`Int`): Number of days to retrieve row counts
      for (default: `2`)
    * `field_name` (`String`): Time axis to use - If not specified,
      first found is used
    '''

    get_digraph = sgqlc.types.Field(DirectedGraph, graphql_name='getDigraph', args=sgqlc.types.ArgDict((
        ('metadata_version', sgqlc.types.Arg(String, graphql_name='metadataVersion', default=None)),
))
    )
    '''Arguments:

    * `metadata_version` (`String`)None
    '''

    get_pipeline_freshness_v2 = sgqlc.types.Field(PipelineFreshness, graphql_name='getPipelineFreshnessV2', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Get latest freshness for multiple tables

    Arguments:

    * `dw_id` (`UUID`): Warehouse the tables are contained in.
      Required when using fullTableIds
    * `full_table_ids` (`[String]`): Deprecated - use mcons. Ignored
      if mcons are present
    * `mcons` (`[String]`): List of mcons to get details for
    * `start_time` (`DateTime`): Filter for data newer than this
    * `end_time` (`DateTime`): Filter for data older than this
    '''

    get_custom_sql_output_sample = sgqlc.types.Field(CustomSQLOutputSample, graphql_name='getCustomSqlOutputSample', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
        ('job_execution_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='jobExecutionUuid', default=None)),
))
    )
    '''Retrieve output sample for custom SQL job execution

    Arguments:

    * `dw_id` (`UUID!`): Warehouse the custom SQL ran in
    * `job_execution_uuid` (`UUID!`): JobExecution to fetch the output
      sample for
    '''

    get_metric_sampling = sgqlc.types.Field(MetricSampling, graphql_name='getMetricSampling', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('time_axis', sgqlc.types.Arg(String, graphql_name='timeAxis', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=False)),
        ('monitor_uuid', sgqlc.types.Arg(UUID, graphql_name='monitorUuid', default=None)),
))
    )
    '''Get sample rows for metrics

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `time_axis` (`String`): Time field (column) to use when for date
      range
    * `field` (`String`): Field to sample for
    * `metric` (`String`): Type of metric to sample for
    * `start_time` (`DateTime`): Filter for data newer than this
    * `end_time` (`DateTime`): Filter for data older than this
    * `limit` (`Int`): Limit results
    * `dry_run` (`Boolean`): Generate sample query without running
      (default: `false`)
    * `monitor_uuid` (`UUID`): Monitor uuid is used for extracting an
      accurate time axis
    '''

    get_fh_sampling = sgqlc.types.Field(MetricSampling, graphql_name='getFhSampling', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('event_created_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='eventCreatedTime', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
        ('dimension', sgqlc.types.Arg(String, graphql_name='dimension', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=True)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Generates and/or runs a FH sampling query

    Arguments:

    * `monitor_uuid` (`UUID!`): Monitor uuid is used for creating the
      sampling query
    * `event_created_time` (`DateTime!`): When the anomaly occurred
    * `field` (`String!`): The field on which the anomaly was found
    * `metric` (`String!`): The metric which measured the anomaly
    * `dimension` (`String`): FH segment if segmented monitor
    * `dry_run` (`Boolean`): Generate sample query without running
      (default: `true`)
    * `limit` (`Int`): Limit results
    '''

    get_dt_sampling = sgqlc.types.Field(MetricSampling, graphql_name='getDtSampling', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('dimension', sgqlc.types.Arg(String, graphql_name='dimension', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=False)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    '''Generates and/or runs a Dimension Tracking investigation query

    Arguments:

    * `monitor_uuid` (`UUID!`): Monitor uuid is used for creating the
      sampling query
    * `start_time` (`DateTime`): Event start time
    * `dimension` (`String`): FH segment if segmented monitor
    * `dry_run` (`Boolean`): Generate sample query without running
      (default: `false`)
    * `limit` (`Int`): Limit results
    '''

    get_fh_reproduction_query = sgqlc.types.Field(InvestigationQuery, graphql_name='getFhReproductionQuery', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('event_created_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='eventCreatedTime', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='metric', default=None)),
        ('dimension', sgqlc.types.Arg(String, graphql_name='dimension', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=True)),
))
    )
    '''Generates a SQL query that will reproduce the anomalous data on a
    table

    Arguments:

    * `monitor_uuid` (`UUID!`): UUID of the monitor on which the
      anomaly occurred
    * `event_created_time` (`DateTime!`): When the anomaly occurred
    * `field` (`String!`): The field on which the anomaly was found
    * `metric` (`String!`): The metric which measured the anomaly
    * `dimension` (`String`): FH segment if segmented monitor
    * `dry_run` (`Boolean`): Generate sample query without running
      (default: `true`)
    '''

    get_dt_reproduction_query = sgqlc.types.Field(InvestigationQuery, graphql_name='getDtReproductionQuery', args=sgqlc.types.ArgDict((
        ('monitor_uuid', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='monitorUuid', default=None)),
        ('event_created_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='eventCreatedTime', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('field_val', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='fieldVal', default=None)),
        ('dimension', sgqlc.types.Arg(String, graphql_name='dimension', default=None)),
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=True)),
))
    )
    '''Generates a SQL query that will reproduce the anomalous data on a
    table

    Arguments:

    * `monitor_uuid` (`UUID!`): UUID of the monitor on which the
      anomaly occurred
    * `event_created_time` (`DateTime!`): When the anomaly occurred
    * `field` (`String!`): The field on which the anomaly was found
    * `field_val` (`String!`): The value for which the anomaly was
      found
    * `dimension` (`String`): FH segment if segmented monitor
    * `dry_run` (`Boolean`): Generate sample query without running
      (default: `true`)
    '''

    run_custom_query = sgqlc.types.Field('SQLResponse', graphql_name='runCustomQuery', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('variables', sgqlc.types.Arg(JSONString, graphql_name='variables', default=None)),
        ('query_result_type', sgqlc.types.Arg(QueryResultType, graphql_name='queryResultType', default=None)),
))
    )
    '''Arguments:

    * `dw_id` (`UUID`)None
    * `query` (`String`)None
    * `variables` (`JSONString`)None
    * `query_result_type` (`QueryResultType`): How the query result is
      used for the metric. Uses row count if unset.
    '''

    test_sql_query_part = sgqlc.types.Field('SQLResponse', graphql_name='testSqlQueryPart', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('query_part', sgqlc.types.Arg(String, graphql_name='queryPart', default=None)),
))
    )
    '''Test part of query

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `query_part` (`String`): Part of query (e.g. select options)
    '''

    test_sql_query_where_expression = sgqlc.types.Field('SQLResponse', graphql_name='testSqlQueryWhereExpression', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('where_expression', sgqlc.types.Arg(String, graphql_name='whereExpression', default=None)),
))
    )
    '''Test WHERE expression

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    * `where_expression` (`String`): body of the where expression
      (without WHERE prefix)
    '''

    get_table_stats = sgqlc.types.Field('TableStatsConnection', graphql_name='getTableStats', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_ids', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='fullTableIds', default=None)),
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `dw_id` (`UUID`): Filter by warehouse. Required when using a
      fullTableId
    * `full_table_ids` (`[String]`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcons` (`[String]`): Get stats for specific tables by mcon
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    get_resource = sgqlc.types.Field('Resource', graphql_name='getResource', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    '''Retrieve a specific resource

    Arguments:

    * `uuid` (`UUID`): The resource id
    * `name` (`String`): The resource name
    '''

    get_resources = sgqlc.types.Field(sgqlc.types.list_of('Resource'), graphql_name='getResources')
    '''Retrieve all resources in an account'''

    get_table_fields_importance = sgqlc.types.Field('TableFieldsImportance', graphql_name='getTableFieldsImportance', args=sgqlc.types.ArgDict((
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
))
    )
    '''Arguments:

    * `mcon` (`String!`)
    '''

    get_data_maintenance_entries = sgqlc.types.Field(sgqlc.types.list_of(DataMaintenanceEntry), graphql_name='getDataMaintenanceEntries', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    '''Fetch data maintenance entries for warehouse

    Arguments:

    * `dw_id` (`UUID!`): Warehouse UUID
    '''

    get_wildcard_templates = sgqlc.types.Field('WildcardTemplates', graphql_name='getWildcardTemplates', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dwId', default=None)),
))
    )
    '''List of templates used for aggregating wildcard tables

    Arguments:

    * `dw_id` (`UUID!`): UUID of the warehouse to fetch templates for
    '''

    get_common_fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='getCommonFields', args=sgqlc.types.ArgDict((
        ('mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='mcons', default=None)),
))
    )
    '''Get fields that are common across a set of tables.

    Arguments:

    * `mcons` (`[String]`): The tables to inspect. All tables must
      belong to the same warehouse.
    '''

    get_user_settings = sgqlc.types.Field(sgqlc.types.list_of('UserSettings'), graphql_name='getUserSettings', args=sgqlc.types.ArgDict((
        ('keys', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='keys', default=None)),
))
    )
    '''Get user-specific settings. Return only the settings that have
    value.

    Arguments:

    * `keys` (`[String]!`): User setting's keys
    '''

    get_user = sgqlc.types.Field('User', graphql_name='getUser')

    get_user_by_id = sgqlc.types.Field('User', graphql_name='getUserById')

    get_warehouse = sgqlc.types.Field('Warehouse', graphql_name='getWarehouse', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
))
    )
    '''Arguments:

    * `uuid` (`UUID`)None
    '''

    get_collection_properties = sgqlc.types.Field(CollectionProperties, graphql_name='getCollectionProperties', args=sgqlc.types.ArgDict((
        ('region', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='region', default=None)),
))
    )
    '''Get infrastructure properties for a new data collector deployment

    Arguments:

    * `region` (`String!`): AWS region
    '''

    get_table = sgqlc.types.Field('WarehouseTable', graphql_name='getTable', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Get information about a table

    Arguments:

    * `dw_id` (`UUID`): Warehouse the table is contained in. Required
      when using a fullTableId
    * `full_table_id` (`String`): Deprecated - use mcon. Ignored if
      mcon is present
    * `mcon` (`String`): Mcon for table to get details for
    '''

    get_tables = sgqlc.types.Field('WarehouseTableConnection', graphql_name='getTables', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='status', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('table_id', sgqlc.types.Arg(String, graphql_name='tableId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('warehouse', sgqlc.types.Arg(ID, graphql_name='warehouse', default=None)),
        ('discovered_time', sgqlc.types.Arg(DateTime, graphql_name='discoveredTime', default=None)),
        ('friendly_name', sgqlc.types.Arg(String, graphql_name='friendlyName', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('table_type', sgqlc.types.Arg(String, graphql_name='tableType', default=None)),
        ('is_encrypted', sgqlc.types.Arg(Boolean, graphql_name='isEncrypted', default=None)),
        ('created_time', sgqlc.types.Arg(DateTime, graphql_name='createdTime', default=None)),
        ('last_modified', sgqlc.types.Arg(DateTime, graphql_name='lastModified', default=None)),
        ('view_query', sgqlc.types.Arg(String, graphql_name='viewQuery', default=None)),
        ('path', sgqlc.types.Arg(String, graphql_name='path', default=None)),
        ('priority', sgqlc.types.Arg(Int, graphql_name='priority', default=None)),
        ('tracked', sgqlc.types.Arg(Boolean, graphql_name='tracked', default=None)),
        ('freshness_anomaly', sgqlc.types.Arg(Boolean, graphql_name='freshnessAnomaly', default=None)),
        ('size_anomaly', sgqlc.types.Arg(Boolean, graphql_name='sizeAnomaly', default=None)),
        ('freshness_size_anomaly', sgqlc.types.Arg(Boolean, graphql_name='freshnessSizeAnomaly', default=None)),
        ('metric_anomaly', sgqlc.types.Arg(Boolean, graphql_name='metricAnomaly', default=None)),
        ('dynamic_table', sgqlc.types.Arg(Boolean, graphql_name='dynamicTable', default=None)),
        ('is_deleted', sgqlc.types.Arg(Boolean, graphql_name='isDeleted', default=None)),
        ('deleted_at', sgqlc.types.Arg(DateTime, graphql_name='deletedAt', default=None)),
        ('last_observed', sgqlc.types.Arg(DateTime, graphql_name='lastObserved', default=None)),
        ('is_excluded', sgqlc.types.Arg(Boolean, graphql_name='isExcluded', default=None)),
        ('data_provider', sgqlc.types.Arg(String, graphql_name='dataProvider', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('last_observed__gt', sgqlc.types.Arg(DateTime, graphql_name='lastObserved_Gt', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    '''Get tables in account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `search` (`String`): Filter by partial asset names (e.g.
      dataset)
    * `status` (`[String]`): Filter by table statuses
    * `domain_id` (`UUID`): Filter by domain UUID
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `table_id` (`String`)None
    * `full_table_id` (`String`)None
    * `warehouse` (`ID`)None
    * `discovered_time` (`DateTime`)None
    * `friendly_name` (`String`)None
    * `location` (`String`)None
    * `project_name` (`String`)None
    * `dataset` (`String`)None
    * `description` (`String`)None
    * `table_type` (`String`)None
    * `is_encrypted` (`Boolean`)None
    * `created_time` (`DateTime`)None
    * `last_modified` (`DateTime`)None
    * `view_query` (`String`)None
    * `path` (`String`)None
    * `priority` (`Int`)None
    * `tracked` (`Boolean`)None
    * `freshness_anomaly` (`Boolean`)None
    * `size_anomaly` (`Boolean`)None
    * `freshness_size_anomaly` (`Boolean`)None
    * `metric_anomaly` (`Boolean`)None
    * `dynamic_table` (`Boolean`)None
    * `is_deleted` (`Boolean`)None
    * `deleted_at` (`DateTime`)None
    * `last_observed` (`DateTime`)None
    * `is_excluded` (`Boolean`)None
    * `data_provider` (`String`)None
    * `mcon` (`String`)None
    * `last_observed__gt` (`DateTime`)None
    * `order_by` (`String`): Ordering
    '''

    get_tables_health = sgqlc.types.Field('WarehouseTableHealthConnection', graphql_name='getTablesHealth', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('table_mcons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableMcons', default=None)),
        ('table_contains', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tableContains', default=None)),
        ('tags_contains', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='tagsContains', default=None)),
        ('tag_key_value_pairs', sgqlc.types.Arg(sgqlc.types.list_of(TagKeyValuePairInput), graphql_name='tagKeyValuePairs', default=None)),
        ('key_assets_only', sgqlc.types.Arg(Boolean, graphql_name='keyAssetsOnly', default=None)),
        ('has_incidents_only', sgqlc.types.Arg(Boolean, graphql_name='hasIncidentsOnly', default=None)),
        ('has_incidents_start_time', sgqlc.types.Arg(DateTime, graphql_name='hasIncidentsStartTime', default=None)),
        ('has_incidents_end_time', sgqlc.types.Arg(DateTime, graphql_name='hasIncidentsEndTime', default=None)),
        ('has_incidents_include_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='hasIncidentsIncludeFeedback', default=None)),
        ('has_incidents_exclude_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='hasIncidentsExcludeFeedback', default=None)),
        ('has_incidents_include_normalized', sgqlc.types.Arg(Boolean, graphql_name='hasIncidentsIncludeNormalized', default=None)),
        ('has_incidents_severities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='hasIncidentsSeverities', default=None)),
        ('incident_categories', sgqlc.types.Arg(sgqlc.types.list_of(IncidentCategory), graphql_name='incidentCategories', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('table_id', sgqlc.types.Arg(String, graphql_name='tableId', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('warehouse', sgqlc.types.Arg(ID, graphql_name='warehouse', default=None)),
        ('discovered_time', sgqlc.types.Arg(DateTime, graphql_name='discoveredTime', default=None)),
        ('friendly_name', sgqlc.types.Arg(String, graphql_name='friendlyName', default=None)),
        ('location', sgqlc.types.Arg(String, graphql_name='location', default=None)),
        ('project_name', sgqlc.types.Arg(String, graphql_name='projectName', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('table_type', sgqlc.types.Arg(String, graphql_name='tableType', default=None)),
        ('is_encrypted', sgqlc.types.Arg(Boolean, graphql_name='isEncrypted', default=None)),
        ('created_time', sgqlc.types.Arg(DateTime, graphql_name='createdTime', default=None)),
        ('last_modified', sgqlc.types.Arg(DateTime, graphql_name='lastModified', default=None)),
        ('view_query', sgqlc.types.Arg(String, graphql_name='viewQuery', default=None)),
        ('path', sgqlc.types.Arg(String, graphql_name='path', default=None)),
        ('priority', sgqlc.types.Arg(Int, graphql_name='priority', default=None)),
        ('tracked', sgqlc.types.Arg(Boolean, graphql_name='tracked', default=None)),
        ('freshness_anomaly', sgqlc.types.Arg(Boolean, graphql_name='freshnessAnomaly', default=None)),
        ('size_anomaly', sgqlc.types.Arg(Boolean, graphql_name='sizeAnomaly', default=None)),
        ('freshness_size_anomaly', sgqlc.types.Arg(Boolean, graphql_name='freshnessSizeAnomaly', default=None)),
        ('metric_anomaly', sgqlc.types.Arg(Boolean, graphql_name='metricAnomaly', default=None)),
        ('dynamic_table', sgqlc.types.Arg(Boolean, graphql_name='dynamicTable', default=None)),
        ('is_deleted', sgqlc.types.Arg(Boolean, graphql_name='isDeleted', default=None)),
        ('deleted_at', sgqlc.types.Arg(DateTime, graphql_name='deletedAt', default=None)),
        ('last_observed', sgqlc.types.Arg(DateTime, graphql_name='lastObserved', default=None)),
        ('is_excluded', sgqlc.types.Arg(Boolean, graphql_name='isExcluded', default=None)),
        ('data_provider', sgqlc.types.Arg(String, graphql_name='dataProvider', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    '''Get tables health in account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `search` (`String`): Filter by partial asset names (e.g.
      dataset)
    * `domain_id` (`UUID`): Filter by domain UUID
    * `table_mcons` (`[String]`): List of table MCONS to filter the
      result
    * `table_contains` (`[String]`): List of terms to filter the
      result on full name (project/schema/name) of the tables
    * `tags_contains` (`[String]`): List of terms to filter the result
      on tags (both tag keys and values)
    * `tag_key_value_pairs` (`[TagKeyValuePairInput]`): Filter by tag
      key values
    * `key_assets_only` (`Boolean`): Filter by key assets only
    * `has_incidents_only` (`Boolean`): Filter by tables that have
      incidents
    * `has_incidents_start_time` (`DateTime`): Filter tables without
      incidents newer than this
    * `has_incidents_end_time` (`DateTime`): Filter tables without
      incidents older than this
    * `has_incidents_include_feedback` (`[String]`): Filter tables
      without incidents with user feedback
    * `has_incidents_exclude_feedback` (`[String]`): Filter tables
      without incidents excluding user feedback
    * `has_incidents_include_normalized` (`Boolean`): Filter tables
      without incidents excluding normalized incidents if False is
      indicate
    * `has_incidents_severities` (`[String]`): Filter tables without
      incidents with severity
    * `incident_categories` (`[IncidentCategory]`): Include only
      selected incident categories. Or all categories if not
      specified.
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `table_id` (`String`)None
    * `full_table_id` (`String`)None
    * `warehouse` (`ID`)None
    * `discovered_time` (`DateTime`)None
    * `friendly_name` (`String`)None
    * `location` (`String`)None
    * `project_name` (`String`)None
    * `dataset` (`String`)None
    * `description` (`String`)None
    * `table_type` (`String`)None
    * `is_encrypted` (`Boolean`)None
    * `created_time` (`DateTime`)None
    * `last_modified` (`DateTime`)None
    * `view_query` (`String`)None
    * `path` (`String`)None
    * `priority` (`Int`)None
    * `tracked` (`Boolean`)None
    * `freshness_anomaly` (`Boolean`)None
    * `size_anomaly` (`Boolean`)None
    * `freshness_size_anomaly` (`Boolean`)None
    * `metric_anomaly` (`Boolean`)None
    * `dynamic_table` (`Boolean`)None
    * `is_deleted` (`Boolean`)None
    * `deleted_at` (`DateTime`)None
    * `last_observed` (`DateTime`)None
    * `is_excluded` (`Boolean`)None
    * `data_provider` (`String`)None
    * `mcon` (`String`)None
    * `order_by` (`String`): Ordering
    '''

    get_bq_projects = sgqlc.types.Field(sgqlc.types.list_of(BigQueryProject), graphql_name='getBqProjects', args=sgqlc.types.ArgDict((
        ('credentials_key', sgqlc.types.Arg(String, graphql_name='credentialsKey', default=None)),
))
    )
    '''Arguments:

    * `credentials_key` (`String`)None
    '''

    get_slack_oauth_url = sgqlc.types.Field('SlackOauthUrlResponse', graphql_name='getSlackOauthUrl', args=sgqlc.types.ArgDict((
        ('slack_app_type', sgqlc.types.Arg(SlackAppType, graphql_name='slackAppType', default=None)),
))
    )
    '''Returns a Slack OAuth URL

    Arguments:

    * `slack_app_type` (`SlackAppType`): Slack app type
    '''

    get_slack_channels = sgqlc.types.Field('SlackChannelResponse', graphql_name='getSlackChannels', args=sgqlc.types.ArgDict((
        ('exclude_archived', sgqlc.types.Arg(Boolean, graphql_name='excludeArchived', default=None)),
        ('ignore_cached', sgqlc.types.Arg(Boolean, graphql_name='ignoreCached', default=None)),
))
    )
    '''Arguments:

    * `exclude_archived` (`Boolean`): Specify whether to include
      archived Slack Channels
    * `ignore_cached` (`Boolean`): Specify whether to ignore the
      cached versions and attempt to pull directly from Slack API.
    '''

    get_slack_channels_v2 = sgqlc.types.Field('SlackChannelV2Connection', graphql_name='getSlackChannelsV2', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('name__iexact', sgqlc.types.Arg(String, graphql_name='name_Iexact', default=None)),
        ('name__icontains', sgqlc.types.Arg(String, graphql_name='name_Icontains', default=None)),
        ('name__istartswith', sgqlc.types.Arg(String, graphql_name='name_Istartswith', default=None)),
))
    )
    '''Arguments:

    * `order_by` (`String`): Ordering
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `name__iexact` (`String`)None
    * `name__icontains` (`String`)None
    * `name__istartswith` (`String`)None
    '''

    get_projects = sgqlc.types.Field(Projects, graphql_name='getProjects', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('warehouse_type', sgqlc.types.Arg(String, graphql_name='warehouseType', default=None)),
))
    )
    '''Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `search` (`String`): Filter by project name
    * `warehouse_type` (`String`): Filter by a specific warehouse type
    '''

    get_datasets_by_uuid = sgqlc.types.Field(sgqlc.types.list_of('Dataset'), graphql_name='getDatasetsByUuid', args=sgqlc.types.ArgDict((
        ('dataset_uuids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(UUID)), graphql_name='datasetUuids', default=None)),
))
    )
    '''Get datasets by UUID

    Arguments:

    * `dataset_uuids` (`[UUID]!`)None
    '''

    get_datasets = sgqlc.types.Field(DatasetConnection, graphql_name='getDatasets', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('allow_search_on_project', sgqlc.types.Arg(Boolean, graphql_name='allowSearchOnProject', default=None)),
        ('domain_id', sgqlc.types.Arg(UUID, graphql_name='domainId', default=None)),
        ('include_table_count', sgqlc.types.Arg(Boolean, graphql_name='includeTableCount', default=False)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
))
    )
    '''Get datasets in the account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    * `search` (`String`): Filter by a dataset
    * `allow_search_on_project` (`Boolean`): Apply search filter on
      project name
    * `domain_id` (`UUID`): Filter by domain UUID
    * `include_table_count` (`Boolean`): Include table count for each
      dataset (default: `false`)
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `dataset` (`String`)None
    '''

    get_field_bi_lineage = sgqlc.types.Field(sgqlc.types.list_of(FieldDownstreamBi), graphql_name='getFieldBiLineage', args=sgqlc.types.ArgDict((
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
        ('field_name', sgqlc.types.Arg(String, graphql_name='fieldName', default=None)),
        ('last_seen_range_start', sgqlc.types.Arg(DateTime, graphql_name='lastSeenRangeStart', default=None)),
))
    )
    '''Arguments:

    * `full_table_id` (`String`)None
    * `field_name` (`String`)None
    * `last_seen_range_start` (`DateTime`)None
    '''

    get_event_muting_rules = sgqlc.types.Field(sgqlc.types.list_of(EventMutingRule), graphql_name='getEventMutingRules', args=sgqlc.types.ArgDict((
        ('dw_id', sgqlc.types.Arg(UUID, graphql_name='dwId', default=None)),
))
    )
    '''Get muting rules in the account

    Arguments:

    * `dw_id` (`UUID`): Filter by a specific warehouse
    '''

    get_users_in_account = sgqlc.types.Field('UserConnection', graphql_name='getUsersInAccount', args=sgqlc.types.ArgDict((
        ('roles', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='roles', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('email', sgqlc.types.Arg(String, graphql_name='email', default=None)),
        ('first_name', sgqlc.types.Arg(String, graphql_name='firstName', default=None)),
        ('last_name', sgqlc.types.Arg(String, graphql_name='lastName', default=None)),
        ('role', sgqlc.types.Arg(String, graphql_name='role', default=None)),
))
    )
    '''Arguments:

    * `roles` (`[String]`): Filter by user roles
    * `search` (`String`): Filter by first name, last name or email
      address
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `email` (`String`)None
    * `first_name` (`String`)None
    * `last_name` (`String`)None
    * `role` (`String`)None
    '''

    get_invites_in_account = sgqlc.types.Field('UserInviteConnection', graphql_name='getInvitesInAccount', args=sgqlc.types.ArgDict((
        ('roles', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='roles', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    '''Arguments:

    * `roles` (`[String]`): Filter by user role membership
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `state` (`String`)None
    '''

    get_token_metadata = sgqlc.types.Field(sgqlc.types.list_of('TokenMetadata'), graphql_name='getTokenMetadata', args=sgqlc.types.ArgDict((
        ('index', sgqlc.types.Arg(sgqlc.types.non_null(AccessKeyIndexEnum), graphql_name='index', default=None)),
        ('is_service_api_token', sgqlc.types.Arg(Boolean, graphql_name='isServiceApiToken', default=False)),
))
    )
    '''Retrieve access token metadata for current user or account

    Arguments:

    * `index` (`AccessKeyIndexEnum!`): Specifies which metadata index
      to use
    * `is_service_api_token` (`Boolean`): Filter by token type.
      (default: `false`)
    '''

    get_integration_keys = sgqlc.types.Field(sgqlc.types.list_of(IntegrationKeyMetadata), graphql_name='getIntegrationKeys')
    '''Retrieve integration keys in the current user's account'''

    test_existing_connection = sgqlc.types.Field('TestConnectionResponse', graphql_name='testExistingConnection', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    '''Test an existing connection's credentials against the account's
    data collector

    Arguments:

    * `connection_id` (`UUID`): An existing connection's UUID
    '''

    test_telnet_connection = sgqlc.types.Field('TestConnectionResponse', graphql_name='testTelnetConnection', args=sgqlc.types.ArgDict((
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('timeout', sgqlc.types.Arg(Int, graphql_name='timeout', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
))
    )
    '''Checks if telnet connection is usable.

    Arguments:

    * `host` (`String`): Host to check
    * `port` (`Int`): Port to check
    * `timeout` (`Int`): Timeout in seconds
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    '''

    test_tcp_open_connection = sgqlc.types.Field('TestConnectionResponse', graphql_name='testTcpOpenConnection', args=sgqlc.types.ArgDict((
        ('host', sgqlc.types.Arg(String, graphql_name='host', default=None)),
        ('port', sgqlc.types.Arg(Int, graphql_name='port', default=None)),
        ('timeout', sgqlc.types.Arg(Int, graphql_name='timeout', default=None)),
        ('dc_id', sgqlc.types.Arg(UUID, graphql_name='dcId', default=None)),
))
    )
    '''Tests if a destination exists and accepts requests. Opens a TCP
    Socket to a specific port.

    Arguments:

    * `host` (`String`): Host to check
    * `port` (`Int`): Port to check
    * `timeout` (`Int`): Timeout in seconds
    * `dc_id` (`UUID`): DC UUID. To disambiguate accounts with
      multiple collectors
    '''

    test_notification_integration = sgqlc.types.Field(Boolean, graphql_name='testNotificationIntegration', args=sgqlc.types.ArgDict((
        ('setting_id', sgqlc.types.Arg(UUID, graphql_name='settingId', default=None)),
))
    )
    '''Tests an integration is reachable by sending a sample alert. Note
    - rules are not evaluated.

    Arguments:

    * `setting_id` (`UUID`): UUID for the notification setting.
    '''

    get_databricks_cluster_info = sgqlc.types.Field(DatabricksClusterResponse, graphql_name='getDatabricksClusterInfo', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('connection_config', sgqlc.types.Arg(SparkDatabricksConnectionInput, graphql_name='connectionConfig', default=None)),
))
    )
    '''Get the state of the databricks cluster.

    Arguments:

    * `connection_id` (`UUID`): A Databricks connection UUID.
    * `connection_config` (`SparkDatabricksConnectionInput`):
      Connection config for new Databricks cluster connection
    '''

    get_databricks_warehouse_info = sgqlc.types.Field(DatabricksWarehouseResponse, graphql_name='getDatabricksWarehouseInfo', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
        ('connection_config', sgqlc.types.Arg(DatabricksSqlWarehouseConnectionInput, graphql_name='connectionConfig', default=None)),
))
    )
    '''Get the state of the databricks warehouse.

    Arguments:

    * `connection_id` (`UUID`): A Databricks connection UUID.
    * `connection_config` (`DatabricksSqlWarehouseConnectionInput`):
      Connection config for new Databricks SQL Warehouse connection
    '''

    get_databricks_notebook_link = sgqlc.types.Field(DatabricksNotebookLink, graphql_name='getDatabricksNotebookLink')
    '''Get a temporary link to the latest collection notebook.'''

    get_databricks_metadata_job_info = sgqlc.types.Field(sgqlc.types.list_of(DatabricksJobResponse), graphql_name='getDatabricksMetadataJobInfo', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(UUID, graphql_name='connectionId', default=None)),
))
    )
    '''The Databricks job information for the connection.

    Arguments:

    * `connection_id` (`UUID`): A Databricks connection UUID.
    '''

    get_current_databricks_notebook_version = sgqlc.types.Field(String, graphql_name='getCurrentDatabricksNotebookVersion')
    '''Current Version of the Databricks Collection Notebook'''

    validate_connection_type = sgqlc.types.Field(Boolean, graphql_name='validateConnectionType', args=sgqlc.types.ArgDict((
        ('warehouse_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='warehouseType', default=None)),
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
))
    )
    '''Validate that the connection type can be added to the warehouse
    type

    Arguments:

    * `warehouse_type` (`String!`): The type of the warehouse to add
      the connection to
    * `connection_type` (`String!`): The type of the connection to add
    '''

    get_event_onboarding_data = sgqlc.types.Field(EventOnbardingConfig, graphql_name='getEventOnboardingData')

    get_etl_containers = sgqlc.types.Field(sgqlc.types.list_of(EtlContainer), graphql_name='getEtlContainers')
    '''Retrieve the list of ETL containers in the current user's account'''

    get_supported_validations_v2 = sgqlc.types.Field('SupportedValidationsResponse', graphql_name='getSupportedValidationsV2', args=sgqlc.types.ArgDict((
        ('dc_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='dcId', default=None)),
        ('connection_type', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='connectionType', default=None)),
))
    )
    '''Arguments:

    * `dc_id` (`UUID!`): DC UUID. To disambiguate accounts with
      multiple collectors.
    * `connection_type` (`String!`): The type of connection to query
      supported validations for.
    '''

    get_supported_table_validations = sgqlc.types.Field('SupportedTableValidationsResponse', graphql_name='getSupportedTableValidations', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
))
    )
    '''Arguments:

    * `connection_id` (`UUID!`): UUID of the connection to check for
      supported table validations.
    '''

    validate_data_asset_access = sgqlc.types.Field('ValidateDataAssetAccessResponse', graphql_name='validateDataAssetAccess', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('validation_names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='validationNames', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
        ('asset_id', sgqlc.types.Arg(String, graphql_name='assetId', default=None)),
        ('project', sgqlc.types.Arg(String, graphql_name='project', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
        ('asset_name', sgqlc.types.Arg(String, graphql_name='assetName', default=None)),
        ('asset_type', sgqlc.types.Arg(DataAssetTypeEnum, graphql_name='assetType', default='ASSET_TYPE_TABLE')),
))
    )
    '''Arguments:

    * `connection_id` (`UUID!`): The connection UUID
    * `validation_names` (`[String]`): Name of the table validation to
      run.
    * `mcon` (`String`): MCON of the table to validate
    * `asset_id` (`String`): Full ID of the table to validate in the
      format: project:dataset.table, ignored if mcon is specified
    * `project` (`String`): Project (or database) containing the asset
      to validate. Ignored if mcon or asset_id are specified
    * `dataset` (`String`): Dataset (or schema) containing the asset
      to validate. Ignored if mcon or asset_id are specified
    * `asset_name` (`String`): Name of the asset to validate, for
      example table name. Ignored if mcon or asset_id are specified
    * `asset_type` (`DataAssetTypeEnum`): Asset type to validate, it
      could be table, external, snowflake_stream, etc., ignored if
      mcon is specified (default: `"table"`)
    '''

    test_existing_connection_v2 = sgqlc.types.Field('TestCredentialsV2Response', graphql_name='testExistingConnectionV2', args=sgqlc.types.ArgDict((
        ('validation_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='validationName', default=None)),
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
))
    )
    '''Execute a validation test on an integration

    Arguments:

    * `validation_name` (`String!`): Name of the validation that
      should be run.
    * `connection_id` (`UUID!`): An existing connection's UUID
    '''

    list_projects = sgqlc.types.Field(ListProjectsResponse, graphql_name='listProjects', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('page_token', sgqlc.types.Arg(String, graphql_name='pageToken', default=None)),
))
    )
    '''Lists projects for a given connection

    Arguments:

    * `connection_id` (`UUID!`): A connection ID
    * `page_size` (`Int`): The size of the page being requested.
    * `page_token` (`String`): The token for the page being requested.
    '''

    list_datasets = sgqlc.types.Field(ListDatasetsResponse, graphql_name='listDatasets', args=sgqlc.types.ArgDict((
        ('connection_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='connectionId', default=None)),
        ('project_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='projectId', default=None)),
        ('page_size', sgqlc.types.Arg(Int, graphql_name='pageSize', default=None)),
        ('page_token', sgqlc.types.Arg(String, graphql_name='pageToken', default=None)),
))
    )
    '''Lists datasets for a given connection

    Arguments:

    * `connection_id` (`UUID!`): A connection ID
    * `project_id` (`String!`): The ID of the project whose datasets
      are being queried
    * `page_size` (`Int`): The size of the page being requested.
    * `page_token` (`String`): The token for the page being requested.
    '''

    get_airflow_task_results = sgqlc.types.Field(AirflowTaskRunConnection, graphql_name='getAirflowTaskResults', args=sgqlc.types.ArgDict((
        ('from_date', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='fromDate', default=None)),
        ('to_date', sgqlc.types.Arg(DateTime, graphql_name='toDate', default=None)),
        ('success', sgqlc.types.Arg(Boolean, graphql_name='success', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
        ('dag_id', sgqlc.types.Arg(String, graphql_name='dagId', default=None)),
        ('task_id', sgqlc.types.Arg(String, graphql_name='taskId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Get Airflow Task runs

    Arguments:

    * `from_date` (`DateTime!`): Filter date range start
    * `to_date` (`DateTime`): Filter date range end
    * `success` (`Boolean`): Filter by success or failure
    * `state` (`String`): Filter by state
    * `dag_id` (`String`): Filter by DAG ID
    * `task_id` (`String`): Filter by Task ID
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class QueryAfterKey(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user', 'date', 'query_hash')
    user = sgqlc.types.Field(String, graphql_name='user')
    '''The username'''

    date = sgqlc.types.Field(String, graphql_name='date')
    '''The date as a string'''

    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')
    '''The query hash'''



class QueryBlastRadius(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date', 'username', 'query_hash', 'query_count', 'tables')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    '''The date when the query was performed'''

    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''The user who ran the query'''

    query_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryHash')
    '''The query hash'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of times the query was ran'''

    tables = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='tables')
    '''The list of tables in the incident queried'''



class QueryBlastRadius2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('username', 'last_accessed_date', 'distinct_query_count', 'query_count', 'queries')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''The user who ran the query'''

    last_accessed_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastAccessedDate')
    '''The date when the query was performed'''

    distinct_query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distinctQueryCount')
    '''The number of unique queries the user ran'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of times the query was ran'''

    queries = sgqlc.types.Field(sgqlc.types.list_of('QueryBlastRadiusData'), graphql_name='queries')
    '''The query data'''



class QueryBlastRadiusData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date', 'query_hash', 'query_count', 'tables')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    '''The date when the query was performed'''

    query_hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryHash')
    '''The query hash'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of times the query was ran'''

    tables = sgqlc.types.Field(sgqlc.types.list_of('TableInfo'), graphql_name='tables')
    '''The list of tables in the incident queried'''



class QueryBlastRadiusSummary(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('username', 'last_accessed_date', 'distinct_query_count', 'query_count')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''The user who ran the query'''

    last_accessed_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastAccessedDate')
    '''The date when the query was performed'''

    distinct_query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='distinctQueryCount')
    '''The number of unique queries the user ran'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of times the query was ran'''



class QueryChange(sgqlc.types.Type):
    '''Detected query change'''
    __schema__ = schema
    __field_names__ = ('group_id', 'timestamp', 'change_type')
    group_id = sgqlc.types.Field(String, graphql_name='groupId')
    '''Identifier for a grouping of like/same queries'''

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    '''Time a change was detected'''

    change_type = sgqlc.types.Field(QueryRcaType, graphql_name='changeType')
    '''Type of change detected'''



class QueryDataObject(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query_id', 'user_name', 'timestamp', 'query', 'source_display_name', 'destination_display_name', 'error_code', 'error_msg')
    query_id = sgqlc.types.Field(String, graphql_name='queryId')

    user_name = sgqlc.types.Field(String, graphql_name='userName')

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')

    query = sgqlc.types.Field(String, graphql_name='query')

    source_display_name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sourceDisplayName')

    destination_display_name = sgqlc.types.Field(String, graphql_name='destinationDisplayName')

    error_code = sgqlc.types.Field(String, graphql_name='errorCode')

    error_msg = sgqlc.types.Field(String, graphql_name='errorMsg')



class QueryDimensions(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('users', 'categories')
    users = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='users')
    '''A distinct list of users for a list of queries'''

    categories = sgqlc.types.Field(sgqlc.types.list_of(QueryCategory), graphql_name='categories')
    '''A distinct list of query categories for a list of queries'''



class QueryGroupSummaryType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query_group_field', 'query_group_value', 'query_snippet', 'user_email', 'query_count', 'avg_runtime', 'max_runtime', 'sum_runtime', 'warehouse_uuid', 'destination', 'destination_mcon')
    query_group_field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryGroupField')

    query_group_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryGroupValue')

    query_snippet = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='querySnippet')

    user_email = sgqlc.types.Field(String, graphql_name='userEmail')

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')

    avg_runtime = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='avgRuntime')

    max_runtime = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='maxRuntime')

    sum_runtime = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='sumRuntime')

    warehouse_uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouseUuid')

    destination = sgqlc.types.Field(String, graphql_name='destination')

    destination_mcon = sgqlc.types.Field(String, graphql_name='destinationMcon')



class QueryListObject(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query_id', 'user_name', 'timestamp', 'query_length', 'query_hash', 'sub_category')
    query_id = sgqlc.types.Field(String, graphql_name='queryId')

    user_name = sgqlc.types.Field(String, graphql_name='userName')

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')

    query_length = sgqlc.types.Field(Int, graphql_name='queryLength')

    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')

    sub_category = sgqlc.types.Field(String, graphql_name='subCategory')



class QueryListResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('queries', 'queries_by_type', 'offset')
    queries = sgqlc.types.Field(sgqlc.types.list_of(QueryListObject), graphql_name='queries')

    queries_by_type = sgqlc.types.Field(sgqlc.types.list_of('QueryMapObject'), graphql_name='queriesByType')

    offset = sgqlc.types.Field(Int, graphql_name='offset')



class QueryLogHash(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query', 'query_hash', 'user_email', 'day', 'count', 'category', 'average_elapsed_time')
    query = sgqlc.types.Field(String, graphql_name='query')
    '''A substring of the query containing the first n characters defined
    by the query_characters parameter in the query
    '''

    query_hash = sgqlc.types.Field(String, graphql_name='queryHash')
    '''Hash of the query'''

    user_email = sgqlc.types.Field(String, graphql_name='userEmail')
    '''User email'''

    day = sgqlc.types.Field(DateTime, graphql_name='day')
    '''Day of the query log hash'''

    count = sgqlc.types.Field(Int, graphql_name='count')
    '''Count of the number of queries with the same hash in the day'''

    category = sgqlc.types.Field(String, graphql_name='category')
    '''Category of the query log hash'''

    average_elapsed_time = sgqlc.types.Field(Int, graphql_name='averageElapsedTime')
    '''Average elapsed time of the query log hash in milliseconds'''



class QueryLogHashes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_table_id', 'offset', 'query_hashes')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    offset = sgqlc.types.Field(Int, graphql_name='offset')

    query_hashes = sgqlc.types.Field(sgqlc.types.list_of(QueryLogHash), graphql_name='queryHashes')



class QueryLogMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metadata', 'timestamp')
    metadata = sgqlc.types.Field(String, graphql_name='metadata')

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')



class QueryLogResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query_data', 'queries', 'offset')
    query_data = sgqlc.types.Field(QueryDataObject, graphql_name='queryData')

    queries = sgqlc.types.Field(sgqlc.types.list_of(QueryLogMetadata), graphql_name='queries')

    offset = sgqlc.types.Field(Int, graphql_name='offset')



class QueryLogResultType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('timestamp', 'warehouse_uuid', 'query_snippet', 'query', 'query_group', 'user', 'status', 'destination', 'runtime', 'displayable_field_values')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')

    warehouse_uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='warehouseUuid')

    query_snippet = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='querySnippet')

    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')

    query_group = sgqlc.types.Field(String, graphql_name='queryGroup')

    user = sgqlc.types.Field(String, graphql_name='user')
    '''DEPRECATED, use displayableFieldValues'''

    status = sgqlc.types.Field(String, graphql_name='status')
    '''DEPRECATED, use displayableFieldValues'''

    destination = sgqlc.types.Field(String, graphql_name='destination')
    '''DEPRECATED, use displayableFieldValues'''

    runtime = sgqlc.types.Field(Int, graphql_name='runtime')

    displayable_field_values = sgqlc.types.Field(sgqlc.types.list_of(DisplayableFieldValueType), graphql_name='displayableFieldValues')



class QueryLogsFacetResponseType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'facet_results')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    '''Field name'''

    facet_results = sgqlc.types.Field(sgqlc.types.list_of(FacetResultType), graphql_name='facetResults')
    '''Facet results'''



class QueryLogsResponseType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total', 'results')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')

    results = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(QueryLogResultType)), graphql_name='results')



class QueryMapObject(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('queries', 'query_length')
    queries = sgqlc.types.Field(sgqlc.types.list_of(QueryListObject), graphql_name='queries')

    query_length = sgqlc.types.Field(Int, graphql_name='queryLength')



class QueryRca(sgqlc.types.Type):
    '''Query RCA result'''
    __schema__ = schema
    __field_names__ = ('table_mcon', 'group_id', 'timestamp', 'type', 'rca_data')
    table_mcon = sgqlc.types.Field(String, graphql_name='tableMcon')
    '''MCON of affected table'''

    group_id = sgqlc.types.Field(String, graphql_name='groupId')
    '''Identifier for a grouping of like/same queries'''

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    '''Time RCA was executed'''

    type = sgqlc.types.Field(QueryRcaType, graphql_name='type')
    '''Type of query RCA'''

    rca_data = sgqlc.types.Field(JSONString, graphql_name='rcaData')
    '''Get full rca data'''



class QueryRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('dynamic_fields', 'fields', 'filters', 'model', 'query_timezone', 'url', 'view')
    dynamic_fields = sgqlc.types.Field(String, graphql_name='dynamicFields')

    fields = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fields')

    filters = sgqlc.types.Field(String, graphql_name='filters')

    model = sgqlc.types.Field(String, graphql_name='model')

    query_timezone = sgqlc.types.Field(String, graphql_name='queryTimezone')

    url = sgqlc.types.Field(String, graphql_name='url')

    view = sgqlc.types.Field(String, graphql_name='view')



class QueryRuntimeTimeSeriesResponseType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query_group_field', 'query_group_values', 'time_series_list', 'time_bucket_size', 'time_bucket_aggregation_function')
    query_group_field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='queryGroupField')

    query_group_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='queryGroupValues')

    time_series_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TimeSeries')), graphql_name='timeSeriesList')

    time_bucket_size = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timeBucketSize')

    time_bucket_aggregation_function = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timeBucketAggregationFunction')



class QueryWithResults(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query', 'rows')
    query = sgqlc.types.Field(String, graphql_name='query')
    '''The query that was executed.'''

    rows = sgqlc.types.Field(String, graphql_name='rows')
    '''Result of the query that was run. Either number of rows or the
    serialized representation of the rows themselves.
    '''



class RcaJob(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'job_type', 'event', 'set_ts', 'status', 'execution_stats', 'status_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    job_type = sgqlc.types.Field(sgqlc.types.non_null(RcaJobsModelJobType), graphql_name='jobType')

    event = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='event')

    set_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='setTs')

    status = sgqlc.types.Field(RcaJobsModelStatus, graphql_name='status')
    '''Status of the RCA cached for fast look-up'''

    execution_stats = sgqlc.types.Field(JSONString, graphql_name='executionStats')

    status_reason = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EventRcaStatusModelType))), graphql_name='statusReason')



class RcaPlotData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('label', 'timestamp', 'value')
    label = sgqlc.types.Field(String, graphql_name='label')
    '''Plot point label'''

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    '''Plot point position on the time axis'''

    value = sgqlc.types.Field(Int, graphql_name='value')
    '''Plot point value'''



class RcaResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('status', 'job_type', 'status_reasons', 'rca_data', 'rca_data_v2')
    status = sgqlc.types.Field(RcaStatus, graphql_name='status')

    job_type = sgqlc.types.Field(sgqlc.types.non_null(RcaJobsModelJobType), graphql_name='jobType')

    status_reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EventRcaStatusModelReason)), graphql_name='statusReasons', args=sgqlc.types.ArgDict((
        ('event_uuid', sgqlc.types.Arg(UUID, graphql_name='eventUuid', default=None)),
))
    )
    '''Arguments:

    * `event_uuid` (`UUID`)None
    '''

    rca_data = sgqlc.types.Field(FieldDistRcaResult, graphql_name='rcaData')

    rca_data_v2 = sgqlc.types.Field('RcaData', graphql_name='rcaDataV2')



class ReInviteUsers(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('invites', 'existing_users')
    invites = sgqlc.types.Field(sgqlc.types.list_of('UserInvite'), graphql_name='invites')
    '''List of users to resend invites'''

    existing_users = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='existingUsers')
    '''List of email addresses of users who already exist and cannot be
    invited
    '''



class ReadWriteStatsData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('table_read_percentile', 'table_write_percentile')
    table_read_percentile = sgqlc.types.Field(Float, graphql_name='tableReadPercentile')
    '''Based on the amount of daily reads from the table'''

    table_write_percentile = sgqlc.types.Field(Float, graphql_name='tableWritePercentile')
    '''Based on the amount of daily writes to the table'''



class RecentTimestamp(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('field_name', 'timestamp', 'is_time_axis')
    field_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fieldName')

    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')

    is_time_axis = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTimeAxis')



class RelatedUserCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user', 'count')
    user = sgqlc.types.Field(String, graphql_name='user')

    count = sgqlc.types.Field(Int, graphql_name='count')



class RemoveConnectionMutation(sgqlc.types.Type):
    '''Remove an integration connection and deschedule any associated
    jobs
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class RemoveFromCollectionBlockList(sgqlc.types.Type):
    '''Removes from the list of entities for which metadata collection is
    not allowed on this account.
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Whether the mutation succeeded.'''



class RemoveUserFromAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field('User', graphql_name='user')



class Report(sgqlc.types.Type):
    '''Available report for an insight'''
    __schema__ = schema
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of report'''

    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    '''Information about report content'''



class ResourceConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ResourceEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class ResourceEdge(sgqlc.types.Type):
    '''A Relay edge containing a `Resource` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('Resource', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class ResourceModification(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'description', 'resource_as_json', 'is_significant_change')
    type = sgqlc.types.Field(String, graphql_name='type')

    description = sgqlc.types.Field(String, graphql_name='description')

    resource_as_json = sgqlc.types.Field(String, graphql_name='resourceAsJson')

    is_significant_change = sgqlc.types.Field(Boolean, graphql_name='isSignificantChange')



class ResponseURL(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('url', 'created_at')
    url = sgqlc.types.Field(String, graphql_name='url')
    '''Pre-signed URL for fetching report, expiration time is 1 minute'''

    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    '''Report creation time in UTC'''



class RoleOutput(sgqlc.types.Type):
    '''A named set of permissions that can be assigned to principals.'''
    __schema__ = schema
    __field_names__ = ('name', 'version', 'is_managed', 'label', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Unique, human-readable name name with format of [company-
    name]/[role-name]
    '''

    version = sgqlc.types.Field(String, graphql_name='version')
    '''Version of the permissions definitions the group is designed for,
    ex: 2022-03-17. Defaults to current.
    '''

    is_managed = sgqlc.types.Field(Boolean, graphql_name='isManaged')
    '''Indicates if this role is managed by Monte Carlo. If so, it may
    not be modified by clients.
    '''

    label = sgqlc.types.Field(String, graphql_name='label')
    '''UI/user-friendly display name, ex: Editor'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description/help text to help users understand the purpose of the
    role
    '''



class RunSqlRule(sgqlc.types.Type):
    '''Run a SQL Rule manually'''
    __schema__ = schema
    __field_names__ = ('job_execution_uuids',)
    job_execution_uuids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='jobExecutionUuids')



class SQLQueryResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('columns', 'rows')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')

    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')



class SQLResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('columns', 'rows', 'query', 'has_error', 'error', 'sampling_disabled', 'idempotent_status')
    columns = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='columns')

    rows = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(String)), graphql_name='rows')

    query = sgqlc.types.Field(String, graphql_name='query')

    has_error = sgqlc.types.Field(Boolean, graphql_name='hasError')

    error = sgqlc.types.Field(String, graphql_name='error')

    sampling_disabled = sgqlc.types.Field(Boolean, graphql_name='samplingDisabled')

    idempotent_status = sgqlc.types.Field(IdempotentStatus, graphql_name='idempotentStatus')



class SamlIdentityProvider(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('federation_type', 'cognito_name', 'domains', 'default_authorization_groups', 'metadata_url', 'metadata')
    federation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='federationType')
    '''SAML (constant)'''

    cognito_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cognitoName')
    '''Cognito name / Identity Provider name'''

    domains = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='domains')
    '''A list of domains authorized by the IdP'''

    default_authorization_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='defaultAuthorizationGroups')
    '''List of authorization group names assigned to new SSO users by
    default.
    '''

    metadata_url = sgqlc.types.Field(String, graphql_name='metadataUrl')
    '''The URL of the metadata file'''

    metadata = sgqlc.types.Field(String, graphql_name='metadata')
    '''The metadata in XML format'''



class SaveEventOnboardingData(sgqlc.types.Type):
    '''Save event onboarding configuration'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the event onboarding data was saved successfully'''



class SaveSlackCredentialsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('slack_credentials',)
    slack_credentials = sgqlc.types.Field('SlackCredentialsV2', graphql_name='slackCredentials')



class SaveTableImportanceStats(sgqlc.types.Type):
    '''Save custom table stats for a table'''
    __schema__ = schema
    __field_names__ = ('stats',)
    stats = sgqlc.types.Field('TableImportanceStatsResponse', graphql_name='stats')



class ScheduleConfigOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('schedule_type', 'interval_minutes', 'interval_crontab', 'start_time', 'min_interval_minutes', 'timezone')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(ScheduleType), graphql_name='scheduleType')
    '''Type of schedule'''

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')
    '''Time interval between job executions, in minutes'''

    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='intervalCrontab')
    '''For schedule_type=fixed, one or more cron schedules to determine
    the next execution, each time uses the closest value of all
    schedules
    '''

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')
    '''For schedule_type=fixed, the date the schedule should start'''

    min_interval_minutes = sgqlc.types.Field(Int, graphql_name='minIntervalMinutes')
    '''For schedule_type=dynamic, the minimum time interval between job
    executions
    '''

    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    '''Timezone for daylight savings and interpreting cron expressions.'''



class SearchResponse(sgqlc.types.Type):
    '''List of search results that match the query'''
    __schema__ = schema
    __field_names__ = ('total_hits', 'offset', 'results', 'facet_results')
    total_hits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalHits')
    '''Number of results'''

    offset = sgqlc.types.Field(Int, graphql_name='offset')
    '''Offset for paginating results'''

    results = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SearchResult')), graphql_name='results')
    '''List of matching results'''

    facet_results = sgqlc.types.Field(sgqlc.types.list_of(FacetResults), graphql_name='facetResults')
    '''Facet results'''



class SearchResult(sgqlc.types.Type):
    '''An individual result. Part of the SearchResponse'''
    __schema__ = schema
    __field_names__ = ('mcon', 'lineage_node_id', 'object_type', 'object_id', 'display_name', 'parent_mcon', 'path', 'project_id', 'dataset', 'table_id', 'properties', 'resource_id', 'warehouse_display_name', 'description', 'field_type', 'highlight', 'highlight_properties', 'field_names', 'is_important', 'upstream_resource_ids')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''Monte Carlo full identifier for an entity'''

    lineage_node_id = sgqlc.types.Field(String, graphql_name='lineageNodeId')
    '''Identifier for lineage nodes. Warning - To be deprecated soon'''

    object_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectType')
    '''Type of object (e.g. table, view, etc.)'''

    object_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectId')
    '''Partial identifier (e.g. project:dataset.table)'''

    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    '''Friendly name for entity'''

    parent_mcon = sgqlc.types.Field(String, graphql_name='parentMcon')
    '''Identifier for any parents (e.g. field belonging to a table)'''

    path = sgqlc.types.Field(String, graphql_name='path')
    '''Path to node'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''Name of project (database or catalog in some warehouses)'''

    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    '''Name of dataset (schema in some warehouses)'''

    table_id = sgqlc.types.Field(String, graphql_name='tableId')
    '''Name of the table'''

    properties = sgqlc.types.Field(sgqlc.types.list_of('SearchResultProperty'), graphql_name='properties')
    '''Any attached labels'''

    resource_id = sgqlc.types.Field(String, graphql_name='resourceId')
    '''Resource identifier (e.g. warehouse). Warning - To be deprecated
    soon
    '''

    warehouse_display_name = sgqlc.types.Field(String, graphql_name='warehouseDisplayName')
    '''Name of warehouse'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of object'''

    field_type = sgqlc.types.Field(String, graphql_name='fieldType')
    '''Data type of field. Only populated if object_type=field'''

    highlight = sgqlc.types.Field(sgqlc.types.list_of(HighlightSnippets), graphql_name='highlight')
    '''Highlight snippets'''

    highlight_properties = sgqlc.types.Field(sgqlc.types.list_of(NestedHighlightSnippets), graphql_name='highlightProperties')
    '''Highlight snippets for object properties'''

    field_names = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='fieldNames')
    '''Field names (if object_type=table)'''

    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')
    '''Whether the table or field is important'''

    upstream_resource_ids = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='upstreamResourceIds')
    '''Upstream resource ids'''



class SearchResultProperty(sgqlc.types.Type):
    '''An individual label. Part of the SearchResult'''
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Name of label'''

    value = sgqlc.types.Field(String, graphql_name='value')
    '''Value of label'''



class SendDbtArtifactsEvent(sgqlc.types.Type):
    '''Publish a Dbt artifacts event to Kinesis stream'''
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')



class SensitivityThreshold(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('level',)
    level = sgqlc.types.Field(SensitivityLevels, graphql_name='level')
    '''Low, medium or high sensitivity'''



class SetAccountName(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')



class SetDefaultIncidentGroupInterval(sgqlc.types.Type):
    '''Set default incident grouping interval (in hours) for a warehouse.'''
    __schema__ = schema
    __field_names__ = ('warehouse_config',)
    warehouse_config = sgqlc.types.Field(JSONString, graphql_name='warehouseConfig')
    '''Warehouse configuration.'''



class SetGeneratesIncidents(sgqlc.types.Type):
    '''Set whether a dbt project generates incidents'''
    __schema__ = schema
    __field_names__ = ('dbt_project',)
    dbt_project = sgqlc.types.Field('DbtProject', graphql_name='dbtProject')



class SetGroupRepetitiveDbtModelFailures(sgqlc.types.Type):
    '''Set whether to group dbt model failures with the same error
    message into the same incident
    '''
    __schema__ = schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field(Connection, graphql_name='connection')



class SetGroupRepetitiveDbtTestFailures(sgqlc.types.Type):
    '''Set whether to group dbt test failures with the same error message
    into the same incident
    '''
    __schema__ = schema
    __field_names__ = ('connection',)
    connection = sgqlc.types.Field(Connection, graphql_name='connection')



class SetIncidentFeedbackPayload(sgqlc.types.Type):
    '''Provide feedback for an incident'''
    __schema__ = schema
    __field_names__ = ('incident', 'client_mutation_id')
    incident = sgqlc.types.Field('Incident', graphql_name='incident')
    '''Incident details, for which feedback was given'''

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class SetIncidentOwner(sgqlc.types.Type):
    '''Set an owner for an existing incident'''
    __schema__ = schema
    __field_names__ = ('incident',)
    incident = sgqlc.types.Field('Incident', graphql_name='incident')
    '''The updated incident'''



class SetIncidentReaction(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('incident',)
    incident = sgqlc.types.Field('Incident', graphql_name='incident')
    '''The updated incident'''



class SetIncidentSeverity(sgqlc.types.Type):
    '''Set severity for an existing incident'''
    __schema__ = schema
    __field_names__ = ('incident',)
    incident = sgqlc.types.Field('Incident', graphql_name='incident')
    '''The updated incident'''



class SetJobGeneratesIncidents(sgqlc.types.Type):
    '''Set whether a dbt job generates incidents'''
    __schema__ = schema
    __field_names__ = ('dbt_job',)
    dbt_job = sgqlc.types.Field('DbtJob', graphql_name='dbtJob')



class SetPiiFilterStatus(sgqlc.types.Type):
    '''Set PII filter status for this account.'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Whether the mutation succeeded.'''



class SetSensitivity(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class SetWarehouseName(sgqlc.types.Type):
    '''Set friendly name for a warehouse.'''
    __schema__ = schema
    __field_names__ = ('warehouse',)
    warehouse = sgqlc.types.Field('Warehouse', graphql_name='warehouse')
    '''Warehouse where name was set.'''



class SetWildcardTemplates(sgqlc.types.Type):
    '''Sets the templates to use for wildcard aggregation (overrides
    existing templates)
    '''
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field(sgqlc.types.list_of('WildcardTemplate'), graphql_name='templates')



class SheetDashboardRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'path', 'created_at', 'updated_at', 'id', 'dashboard_id', 'dashboard_title')
    name = sgqlc.types.Field(String, graphql_name='name')

    path = sgqlc.types.Field(String, graphql_name='path')

    created_at = sgqlc.types.Field(String, graphql_name='createdAt')

    updated_at = sgqlc.types.Field(String, graphql_name='updatedAt')

    id = sgqlc.types.Field(String, graphql_name='id')

    dashboard_id = sgqlc.types.Field(String, graphql_name='dashboardId')

    dashboard_title = sgqlc.types.Field(String, graphql_name='dashboardTitle')



class SiteRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'uri')
    name = sgqlc.types.Field(String, graphql_name='name')

    uri = sgqlc.types.Field(String, graphql_name='uri')



class Size(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metric', 'ucs_upper', 'ucs_lower', 'ucs_threshold_low', 'ucs_threshold_medium', 'ucs_threshold_high', 'ucs_min_size_change', 'ucs_reason', 'ucs_status', 'sd_upper', 'sd_lower', 'sd_reason', 'sd_status', 'last_size_change', 'detector_threshold', 'sd_upper_high', 'sd_lower_high', 'sd_upper_medium', 'sd_lower_medium', 'sd_upper_low', 'sd_lower_low')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    '''The type of size metric. (Values: "total_byte_count",
    "total_row_count", "write_throughput")
    '''

    ucs_upper = sgqlc.types.Field(Float, graphql_name='ucsUpper')
    '''Unchanged size upper threshold'''

    ucs_lower = sgqlc.types.Field(Float, graphql_name='ucsLower')
    '''Unchanged size lower threshold'''

    ucs_threshold_low = sgqlc.types.Field(Float, graphql_name='ucsThresholdLow')
    '''Unchanged size "low" level threshold'''

    ucs_threshold_medium = sgqlc.types.Field(Float, graphql_name='ucsThresholdMedium')
    '''Unchanged size "medium" level threshold'''

    ucs_threshold_high = sgqlc.types.Field(Float, graphql_name='ucsThresholdHigh')
    '''Unchanged size "high" level threshold'''

    ucs_min_size_change = sgqlc.types.Field(Float, graphql_name='ucsMinSizeChange')
    '''Minimal difference in size to be considered a change'''

    ucs_reason = sgqlc.types.Field(String, graphql_name='ucsReason')
    '''Reason for not providing the ucs threshold'''

    ucs_status = sgqlc.types.Field(DetectorStatus, graphql_name='ucsStatus')
    '''Status of the unchanged size detector'''

    sd_upper = sgqlc.types.Field(Float, graphql_name='sdUpper')
    '''Size diff upper threshold'''

    sd_lower = sgqlc.types.Field(Float, graphql_name='sdLower')
    '''Size diff lower threshold'''

    sd_reason = sgqlc.types.Field(String, graphql_name='sdReason')
    '''Reason for not providing the sd threshold'''

    sd_status = sgqlc.types.Field(DetectorStatus, graphql_name='sdStatus')
    '''Status of the size diff detector'''

    last_size_change = sgqlc.types.Field(LastSizeChange, graphql_name='lastSizeChange')
    '''Time and volume of the last significant change'''

    detector_threshold = sgqlc.types.Field(Float, graphql_name='detectorThreshold')
    '''The threshold calculated by the detector model'''

    sd_upper_high = sgqlc.types.Field(Float, graphql_name='sdUpperHigh')
    '''Size diff upper High Sensitivity threshold'''

    sd_lower_high = sgqlc.types.Field(Float, graphql_name='sdLowerHigh')
    '''Size diff lower High Sensitivity threshold'''

    sd_upper_medium = sgqlc.types.Field(Float, graphql_name='sdUpperMedium')
    '''Size diff upper Medium Sensitivity threshold'''

    sd_lower_medium = sgqlc.types.Field(Float, graphql_name='sdLowerMedium')
    '''Size diff lower Medium Sensitivity threshold'''

    sd_upper_low = sgqlc.types.Field(Float, graphql_name='sdUpperLow')
    '''Size diff upper Low Sensitivity threshold'''

    sd_lower_low = sgqlc.types.Field(Float, graphql_name='sdLowerLow')
    '''Size diff lower Low Sensitivity threshold'''



class SlackChannel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'id', 'topic', 'purpose')
    name = sgqlc.types.Field(String, graphql_name='name')

    id = sgqlc.types.Field(String, graphql_name='id')

    topic = sgqlc.types.Field(String, graphql_name='topic')

    purpose = sgqlc.types.Field(String, graphql_name='purpose')



class SlackChannelResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('channels',)
    channels = sgqlc.types.Field(sgqlc.types.list_of(SlackChannel), graphql_name='channels')



class SlackChannelV2Connection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SlackChannelV2Edge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class SlackChannelV2Edge(sgqlc.types.Type):
    '''A Relay edge containing a `SlackChannelV2` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('SlackChannelV2', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class SlackCredentials(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'account', 'credentials_s3_key')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    credentials_s3_key = sgqlc.types.Field(String, graphql_name='credentialsS3Key')



class SlackCredentialsV2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'account', 'installed_by', 'slack_app_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    installed_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='installedBy')
    '''User that installed the Slack app'''

    slack_app_type = sgqlc.types.Field(sgqlc.types.non_null(SlackCredentialsV2ModelSlackAppType), graphql_name='slackAppType')
    '''Type of Slack app'''



class SlackEngagementConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SlackEngagementEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class SlackEngagementEdge(sgqlc.types.Type):
    '''A Relay edge containing a `SlackEngagement` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('SlackEngagement', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class SlackMessageDetailsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('SlackMessageDetailsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class SlackMessageDetailsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `SlackMessageDetails` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('SlackMessageDetails', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class SlackOauthUrlResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(String, graphql_name='url')



class SnoozeCustomRule(sgqlc.types.Type):
    '''Snooze a custom rule. Data collection will continue, but no
    anomalies will be reported.
    '''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class SnoozeDbtNode(sgqlc.types.Type):
    '''Snooze a DBT node (model/test). Data collection will continue, but
    no events will be reported.
    '''
    __schema__ = schema
    __field_names__ = ('node',)
    node = sgqlc.types.Field('DbtNode', graphql_name='node')



class SourceColumn(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('column_name', 'column_type')
    column_name = sgqlc.types.Field(String, graphql_name='columnName')
    '''Name of the source column'''

    column_type = sgqlc.types.Field(String, graphql_name='columnType')
    '''Type of the source column'''



class SplitIncident(sgqlc.types.Type):
    '''Splits event/s from incident into a new incident'''
    __schema__ = schema
    __field_names__ = ('incident_uuid',)
    incident_uuid = sgqlc.types.Field(UUID, graphql_name='incidentUuid')



class SqlExpression(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('expression',)
    expression = sgqlc.types.Field(String, graphql_name='expression')



class SqlQueryTable(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_table_id',)
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    '''Full table id of the table'''



class StartDatabricksCluster(sgqlc.types.Type):
    '''Start Databricks Cluster.'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully.'''



class StartDatabricksWarehouse(sgqlc.types.Type):
    '''Start Databricks Warehouse.'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully.'''



class StopMonitor(sgqlc.types.Type):
    '''Deprecated: use DeleteMonitor instead'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class SupportedTableValidationsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('supported_validations',)
    supported_validations = sgqlc.types.Field(sgqlc.types.list_of('TableValidation'), graphql_name='supportedValidations')
    '''A list of supported asset validations.'''



class SupportedValidationsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('supported_validations',)
    supported_validations = sgqlc.types.Field(sgqlc.types.list_of('Validation'), graphql_name='supportedValidations')
    '''A list of supported validations.'''



class SwitchUserAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('new_account',)
    new_account = sgqlc.types.Field(Account, graphql_name='newAccount')



class TableAnomalyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableAnomalyEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class TableAnomalyEdge(sgqlc.types.Type):
    '''A Relay edge containing a `TableAnomaly` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableAnomaly', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class TableCapabilitiesResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('supports_freshness', 'supports_bytes', 'supports_rows', 'supports_write_throughput', 'supports_query_logs', 'supports_lineage', 'supports_lineage_pipeline', 'supports_field_lineage', 'supports_objects_deleted', 'supports_total_row_count_change', 'supports_dynamic_schedule', 'supports_delta_logs', 'supports_schema', 'supports_stats_monitor', 'supports_categories_monitor', 'supports_hourly_stats_monitor', 'supports_json_schema_monitor', 'supports_volume_slo', 'supports_freshness_slo', 'supports_custom_sql_rule', 'supports_field_quality_rule', 'supports_volume', 'has_bytes', 'has_freshness', 'has_objects_deleted', 'has_rows', 'has_total_row_count_change', 'has_write_throughput')
    supports_freshness = sgqlc.types.Field(Boolean, graphql_name='supportsFreshness')
    '''indicates whether the table could possibly have freshness'''

    supports_bytes = sgqlc.types.Field(Boolean, graphql_name='supportsBytes')
    '''indicates whether the table could possibly provide events with
    byte counts
    '''

    supports_rows = sgqlc.types.Field(Boolean, graphql_name='supportsRows')
    '''indicates whether the table could possibly provide events with
    number of rows
    '''

    supports_write_throughput = sgqlc.types.Field(Boolean, graphql_name='supportsWriteThroughput')
    '''indicates whether the table could possibly provide write
    throughput events
    '''

    supports_query_logs = sgqlc.types.Field(Boolean, graphql_name='supportsQueryLogs')
    '''indicates whether the table could possibly provide query logs'''

    supports_lineage = sgqlc.types.Field(Boolean, graphql_name='supportsLineage')
    '''indicates whether the table could possibly provide lineage'''

    supports_lineage_pipeline = sgqlc.types.Field(Boolean, graphql_name='supportsLineagePipeline')
    '''indicates whether the table could possibly provide lineage
    pipeline events
    '''

    supports_field_lineage = sgqlc.types.Field(Boolean, graphql_name='supportsFieldLineage')
    '''indicates whether the table could possibly provide field lineage'''

    supports_objects_deleted = sgqlc.types.Field(Boolean, graphql_name='supportsObjectsDeleted')
    '''indicates whether the table could possibly provide the number of
    objects deleted
    '''

    supports_total_row_count_change = sgqlc.types.Field(Boolean, graphql_name='supportsTotalRowCountChange')
    '''indicates whether the table could possibly provide
    total_row_count_change events
    '''

    supports_dynamic_schedule = sgqlc.types.Field(Boolean, graphql_name='supportsDynamicSchedule')
    '''indicates whether the table could supports a dynamic schedule'''

    supports_delta_logs = sgqlc.types.Field(Boolean, graphql_name='supportsDeltaLogs')
    '''indicates whether the table could supports delta history logs'''

    supports_schema = sgqlc.types.Field(Boolean, graphql_name='supportsSchema')
    '''indicates whether the table supports schema'''

    supports_stats_monitor = sgqlc.types.Field(Boolean, graphql_name='supportsStatsMonitor')
    '''indicates whether the table could possibly be used for defining
    stats monitors
    '''

    supports_categories_monitor = sgqlc.types.Field(Boolean, graphql_name='supportsCategoriesMonitor')
    '''indicates whether the table could possibly be used for defining
    category monitors
    '''

    supports_hourly_stats_monitor = sgqlc.types.Field(Boolean, graphql_name='supportsHourlyStatsMonitor')
    '''indicates whether the table could possibly be used for defining
    hourly stats monitors
    '''

    supports_json_schema_monitor = sgqlc.types.Field(Boolean, graphql_name='supportsJsonSchemaMonitor')
    '''indicates whether the table could possibly be used for defining
    json schema monitors
    '''

    supports_volume_slo = sgqlc.types.Field(Boolean, graphql_name='supportsVolumeSlo')
    '''indicates whether the table could possibly be used for defining
    volume rules
    '''

    supports_freshness_slo = sgqlc.types.Field(Boolean, graphql_name='supportsFreshnessSlo')
    '''indicates whether the table could possibly be used for defining
    freshness rules
    '''

    supports_custom_sql_rule = sgqlc.types.Field(Boolean, graphql_name='supportsCustomSqlRule')
    '''indicates whether the table could possibly be used for defining
    custom sql rules
    '''

    supports_field_quality_rule = sgqlc.types.Field(Boolean, graphql_name='supportsFieldQualityRule')
    '''indicates whether the table could possibly be used for defining
    field quality rules
    '''

    supports_volume = sgqlc.types.Field(Boolean, graphql_name='supportsVolume')
    '''Indicates whether the table could possibly have any volume metrics'''

    has_bytes = sgqlc.types.Field(Boolean, graphql_name='hasBytes')
    '''indicates whether the table has byte count metric data points'''

    has_freshness = sgqlc.types.Field(Boolean, graphql_name='hasFreshness')
    '''indicates whether the table has freshness metric data points'''

    has_objects_deleted = sgqlc.types.Field(Boolean, graphql_name='hasObjectsDeleted')
    '''indicates whether the table has object deleted metric data points'''

    has_rows = sgqlc.types.Field(Boolean, graphql_name='hasRows')
    '''indicates whether the table has total row count metric data points'''

    has_total_row_count_change = sgqlc.types.Field(Boolean, graphql_name='hasTotalRowCountChange')
    '''indicates whether the table has total row count change metric data
    points
    '''

    has_write_throughput = sgqlc.types.Field(Boolean, graphql_name='hasWriteThroughput')
    '''indicates whether the table has write throughput metric data
    points
    '''



class TableColumnsLineageResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('mcon', 'columns_lineage', 'non_selected_source_columns', 'timestamp', 'display_name')
    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''Destination(current) table mcon'''

    columns_lineage = sgqlc.types.Field(sgqlc.types.list_of(ColumnLineage), graphql_name='columnsLineage')
    '''Lineage of the columns in the table'''

    non_selected_source_columns = sgqlc.types.Field(sgqlc.types.list_of(LineageSources), graphql_name='nonSelectedSourceColumns')
    '''Other columns used in conditions for the current table'''

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')
    '''Timestamp when the query that generated the lineage happened'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Display name for BI tables'''



class TableFieldConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableFieldEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class TableFieldEdge(sgqlc.types.Type):
    '''A Relay edge containing a `TableField` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableField', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class TableFieldImportance(sgqlc.types.Type):
    '''Information about the table fields with an important flag'''
    __schema__ = schema
    __field_names__ = ('field_name', 'is_important', 'importance_score', 'field_type_db', 'field_type')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')

    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')

    field_type_db = sgqlc.types.Field(String, graphql_name='fieldTypeDb')
    '''Field type as fetched from the warehouse metadata'''

    field_type = sgqlc.types.Field(FieldType, graphql_name='fieldType')
    '''Display field type'''



class TableFieldToBiConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableFieldToBiEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class TableFieldToBiEdge(sgqlc.types.Type):
    '''A Relay edge containing a `TableFieldToBi` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableFieldToBi', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class TableFieldsImportance(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('table_fields',)
    table_fields = sgqlc.types.Field(sgqlc.types.list_of(TableFieldImportance), graphql_name='tableFields')



class TableImportanceStatsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('is_important', 'importance_score')
    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')



class TableInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_table_id', 'mcon')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    '''The incident table that was queried'''

    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''The table mcon'''



class TableMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('table_path', 'is_wildcard', 'view_query', 'external_data_sources', 'created_on')
    table_path = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tablePath')

    is_wildcard = sgqlc.types.Field(Boolean, graphql_name='isWildcard')

    view_query = sgqlc.types.Field(String, graphql_name='viewQuery')

    external_data_sources = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='externalDataSources')

    created_on = sgqlc.types.Field(String, graphql_name='createdOn')



class TableMetricExistence(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('metric_name', 'exist')
    metric_name = sgqlc.types.Field(String, graphql_name='metricName')
    '''metric name, to see if the metric exists on a table or not'''

    exist = sgqlc.types.Field(Boolean, graphql_name='exist')
    '''indicates whether the metric exists for table or not'''



class TableMetricV2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_table_id', 'metric', 'value', 'field', 'timestamp', 'measurement_timestamp', 'dimensions', 'thresholds')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')

    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')

    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')

    field = sgqlc.types.Field(String, graphql_name='field')

    timestamp = sgqlc.types.Field(DateTime, graphql_name='timestamp')

    measurement_timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='measurementTimestamp')

    dimensions = sgqlc.types.Field(MetricDimensions, graphql_name='dimensions')

    thresholds = sgqlc.types.Field(sgqlc.types.list_of('Threshold'), graphql_name='thresholds')
    '''Thresholds'''



class TableObjectsDeleted(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'measurement_timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')

    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')
    '''the start time of a time interval'''



class TableRef(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_table_id', 'table_path')
    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    table_path = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tablePath')



class TableResources(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('table', 'view', 'external', 'wildcard_table')
    table = sgqlc.types.Field(Int, graphql_name='table')

    view = sgqlc.types.Field(Int, graphql_name='view')

    external = sgqlc.types.Field(Int, graphql_name='external')

    wildcard_table = sgqlc.types.Field(Int, graphql_name='wildcardTable')



class TableSchemaVersionConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableSchemaVersionEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class TableSchemaVersionEdge(sgqlc.types.Type):
    '''A Relay edge containing a `TableSchemaVersion` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableSchemaVersion', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class TableSourceSample(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('sources',)
    sources = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='sources')
    '''List of unique sources'''



class TableStatsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableStatsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class TableStatsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `TableStats` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableStats', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class TableTagConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TableTagEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class TableTagEdge(sgqlc.types.Type):
    '''A Relay edge containing a `TableTag` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('TableTag', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class TableTotalByteCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'measurement_timestamp', 'thresholds')
    value = sgqlc.types.Field(Float, graphql_name='value')

    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')

    thresholds = sgqlc.types.Field(sgqlc.types.list_of('Threshold'), graphql_name='thresholds')
    '''Thresholds'''



class TableTotalRowCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'measurement_timestamp', 'thresholds')
    value = sgqlc.types.Field(Float, graphql_name='value')

    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')

    thresholds = sgqlc.types.Field(sgqlc.types.list_of('Threshold'), graphql_name='thresholds')
    '''Thresholds'''



class TableUpdateTime(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'measurement_timestamp')
    value = sgqlc.types.Field(DateTime, graphql_name='value')

    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')



class TableUsageStatsData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('freshness_cycle', 'read_write_stats')
    freshness_cycle = sgqlc.types.Field(FreshnessCycleData, graphql_name='freshnessCycle')
    '''Table update cycle stats'''

    read_write_stats = sgqlc.types.Field(ReadWriteStatsData, graphql_name='readWriteStats')
    '''Table read/write stats'''



class TableValidation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'enabled_by_default')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of the validation.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of the validation.'''

    enabled_by_default = sgqlc.types.Field(Boolean, graphql_name='enabledByDefault')
    '''Whether this validation will run if no validationNames are
    specified (valid only for asset validations).
    '''



class TableWriteThroughputInBytes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('value', 'measurement_timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')

    measurement_timestamp = sgqlc.types.Field(DateTime, graphql_name='measurementTimestamp')
    '''the start time of a time interval'''



class TableauAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'server_name', 'username', 'token_name', 'site_name', 'verify_ssl', 'account', 'created_on', 'data_collector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    server_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serverName')

    username = sgqlc.types.Field(String, graphql_name='username')

    token_name = sgqlc.types.Field(String, graphql_name='tokenName')

    site_name = sgqlc.types.Field(String, graphql_name='siteName')

    verify_ssl = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verifySsl')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    data_collector = sgqlc.types.Field(DataCollector, graphql_name='dataCollector')



class TableauWorkbookCount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('workbook_count',)
    workbook_count = sgqlc.types.Field(Int, graphql_name='workbookCount')
    '''Total number of workbooks in the Tableau instance.'''



class TagKeyValuePairOutput(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Tag key'''

    value = sgqlc.types.Field(String, graphql_name='value')
    '''Tag Value'''



class TestAthenaCredentials(sgqlc.types.Type):
    '''Test an Athena connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestBqCredentials(sgqlc.types.Type):
    '''Test a BQ connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestBqCredentialsV2(sgqlc.types.Type):
    '''Test a BigQuery connection.'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field('TestCredentialsV2Response', graphql_name='validationResult')
    '''Result of the validation.'''



class TestConnectionResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'validations', 'warnings')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestCredentialsMutation(sgqlc.types.Type):
    '''Test credentials where the temp key already exists (e.g. BQ)'''
    __schema__ = schema
    __field_names__ = ('success', 'validations', 'warnings')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestCredentialsV2Response(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'validation_name', 'description', 'errors', 'warnings', 'additional_data')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the validation test was successful.'''

    validation_name = sgqlc.types.Field(String, graphql_name='validationName')
    '''Name of the validation test that was run.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of the validation test that was run.'''

    errors = sgqlc.types.Field(sgqlc.types.list_of('ValidationFailure'), graphql_name='errors')
    '''List of errors of failed validations.'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of('ValidationFailure'), graphql_name='warnings')
    '''List of warnings of failed validations.'''

    additional_data = sgqlc.types.Field(AdditionalData, graphql_name='additionalData')
    '''Optional additional data about the validations that were run.'''



class TestDatabaseCredentials(sgqlc.types.Type):
    '''Test a generic warehouse or database connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestDatabricksCredentials(sgqlc.types.Type):
    '''Test a Databricks connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection.'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully.'''



class TestDatabricksCredentialsV2(sgqlc.types.Type):
    '''Test a Databricks connection'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestDatabricksSparkCredentialsV2(sgqlc.types.Type):
    '''Test a Databricks AP Cluster connection'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestDatabricksSqlWarehouseCredentials(sgqlc.types.Type):
    '''Test the connection to a Databricks sql warehouse.'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestDatabricksSqlWarehouseCredentialsV2(sgqlc.types.Type):
    '''Test a Databricks SQL Warehouse connection.'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestDbtCloudCredentials(sgqlc.types.Type):
    '''Test a dbt Cloud connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestFivetranCredentials(sgqlc.types.Type):
    '''Test a Fivetran connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestGlueCredentials(sgqlc.types.Type):
    '''Test a Glue connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestHiveCredentials(sgqlc.types.Type):
    '''Test a hive sql based connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestLookerCredentials(sgqlc.types.Type):
    '''Test a Looker API connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestLookerCredentialsV2(sgqlc.types.Type):
    '''Test a Looker API connection'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestLookerGitCloneCredentials(sgqlc.types.Type):
    '''Test the connection to a Git repository using the SSH or HTTPS
    protocol
    '''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestLookerGitCloneCredentialsV2(sgqlc.types.Type):
    '''Test the connection to a Git repository using the HTTPS protocol'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestLookerGitCredentials(sgqlc.types.Type):
    '''Deprecated. Do not use.'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestLookerGitSshCredentials(sgqlc.types.Type):
    '''Test the connection to a Git repository using the SSH protocol'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestLookerGitSshCredentialsV2(sgqlc.types.Type):
    '''Test the connection to a Git repository using the SSH protocol'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestPowerBICredentials(sgqlc.types.Type):
    '''Test the Power BI connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestPowerBICredentialsV2(sgqlc.types.Type):
    '''Test a PowerBI connection.'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestPrestoCredentials(sgqlc.types.Type):
    '''Test connection to Presto'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestRedshiftCredentialsV2(sgqlc.types.Type):
    '''Test a Redshift connection.'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestS3Credentials(sgqlc.types.Type):
    '''Test a s3 based connection (e.g. presto query logs on s3)'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestSelfHostedCredentials(sgqlc.types.Type):
    '''Test a connection of any type with self-hosted credentials.'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestSnowflakeCredentials(sgqlc.types.Type):
    '''Test a Snowflake connection'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestSnowflakeCredentialsV2(sgqlc.types.Type):
    '''Test a Snowflake connection.'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection.This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class TestSparkCredentials(sgqlc.types.Type):
    '''Test the connection to a Spark Thrift server.'''
    __schema__ = schema
    __field_names__ = ('key', 'success')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''



class TestTableauCredentialsMutation(sgqlc.types.Type):
    '''Test a tableau account before adding'''
    __schema__ = schema
    __field_names__ = ('key', 'success', 'validations', 'warnings')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection'''

    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validations = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='validations')
    '''List of validations that passed'''

    warnings = sgqlc.types.Field(sgqlc.types.list_of(ConnectionValidation), graphql_name='warnings')
    '''List of warnings of failed validations'''



class TestTableauCredentialsV2(sgqlc.types.Type):
    '''Test a Tableau connection.'''
    __schema__ = schema
    __field_names__ = ('key', 'validation_result')
    key = sgqlc.types.Field(String, graphql_name='key')
    '''Path to key for adding a connection. This key is only generated
    when calling the SAVE_CREDENTIALS validation.
    '''

    validation_result = sgqlc.types.Field(TestCredentialsV2Response, graphql_name='validationResult')
    '''Result of the validation.'''



class Threshold(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('type', 'upper', 'lower', 'reason', 'status', 'upper_high', 'lower_high', 'upper_medium', 'lower_medium', 'upper_low', 'lower_low')
    type = sgqlc.types.Field(sgqlc.types.non_null(ThresholdType), graphql_name='type')
    '''Threshold type'''

    upper = sgqlc.types.Field(Float, graphql_name='upper')
    '''Upper threshold'''

    lower = sgqlc.types.Field(Float, graphql_name='lower')
    '''Lower threshold'''

    reason = sgqlc.types.Field(String, graphql_name='reason')
    '''Reason for missing threshold'''

    status = sgqlc.types.Field(sgqlc.types.non_null(ThresholdStatus), graphql_name='status')
    '''Threshold status'''

    upper_high = sgqlc.types.Field(Float, graphql_name='upperHigh')
    '''Upper High-Sensitivity threshold'''

    lower_high = sgqlc.types.Field(Float, graphql_name='lowerHigh')
    '''Lower High-Sensitivity threshold'''

    upper_medium = sgqlc.types.Field(Float, graphql_name='upperMedium')
    '''Upper Medium-Sensitivity threshold'''

    lower_medium = sgqlc.types.Field(Float, graphql_name='lowerMedium')
    '''Lower Medium-Sensitivity threshold'''

    upper_low = sgqlc.types.Field(Float, graphql_name='upperLow')
    '''Upper Low-Sensitivity threshold'''

    lower_low = sgqlc.types.Field(Float, graphql_name='lowerLow')
    '''Lower Low-Sensitivity threshold'''



class ThresholdModifier(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('modifier_type', 'value')
    modifier_type = sgqlc.types.Field(sgqlc.types.non_null(ThresholdModifierType), graphql_name='modifierType')
    '''The type of threshold modifier'''

    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    '''The value of the threshold modifier. If the type is PERCENTAGE,
    this should be a decimal value.
    '''



class ThresholdsData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('freshness', 'size', 'field_health', 'dimension_tracking', 'dynamic')
    freshness = sgqlc.types.Field(Freshness, graphql_name='freshness')
    '''Freshness anomaly threshold'''

    size = sgqlc.types.Field(Size, graphql_name='size')
    '''Size anomaly threshold'''

    field_health = sgqlc.types.Field(FieldHealth, graphql_name='fieldHealth', args=sgqlc.types.ArgDict((
        ('monitor', sgqlc.types.Arg(String, graphql_name='monitor', default=None)),
        ('field', sgqlc.types.Arg(String, graphql_name='field', default=None)),
        ('metric', sgqlc.types.Arg(String, graphql_name='metric', default=None)),
))
    )
    '''Arguments:

    * `monitor` (`String`)None
    * `field` (`String`)None
    * `metric` (`String`)None
    '''

    dimension_tracking = sgqlc.types.Field(sgqlc.types.list_of(DimensionTracking), graphql_name='dimensionTracking', args=sgqlc.types.ArgDict((
        ('monitor', sgqlc.types.Arg(String, graphql_name='monitor', default=None)),
))
    )
    '''Arguments:

    * `monitor` (`String`)None
    '''

    dynamic = sgqlc.types.Field(Dynamic, graphql_name='dynamic', args=sgqlc.types.ArgDict((
        ('rule', sgqlc.types.Arg(String, graphql_name='rule', default=None)),
))
    )
    '''Arguments:

    * `rule` (`String`)None
    '''



class TimeAxis(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'type')
    name = sgqlc.types.Field(String, graphql_name='name')

    type = sgqlc.types.Field(String, graphql_name='type')



class TimeAxisDeltaDetectionResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('delta',)
    delta = sgqlc.types.Field(Int, graphql_name='delta')
    '''time delta between the time axis and intrinsic time'''



class TimeAxisMetadata(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('candidates', 'suggested')
    candidates = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='candidates')
    '''Fields which can be used as time axis'''

    suggested = sgqlc.types.Field(String, graphql_name='suggested')
    '''Field most likely to be the time axis'''



class TimeSeries(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('group_value', 'data')
    group_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupValue')

    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(DataPoint)), graphql_name='data')



class ToggleConnectionEnable(sgqlc.types.Type):
    '''Enable or Disable a connection. This will also skip/un-skip all
    related data collector schedules.
    '''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the connection was enabled or disabled
    successfully
    '''



class ToggleDisableSampling(sgqlc.types.Type):
    '''Enable/disable the sampling data feature'''
    __schema__ = schema
    __field_names__ = ('disabled',)
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')



class ToggleDisableValueIngestion(sgqlc.types.Type):
    '''Enable/disable the value ingestion feature'''
    __schema__ = schema
    __field_names__ = ('disabled',)
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')



class ToggleDisableValueSamplingWhenTesting(sgqlc.types.Type):
    '''Enable/disable the sampling data feature when testing value-based
    sql rules
    '''
    __schema__ = schema
    __field_names__ = ('disabled',)
    disabled = sgqlc.types.Field(Boolean, graphql_name='disabled')



class ToggleEventConfig(sgqlc.types.Type):
    '''Enable / disable the configuration for data collection via events'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class ToggleFullDistributionMetrics(sgqlc.types.Type):
    '''Enable/disable collection of full distribution metrics for a
    particular warehouse
    '''
    __schema__ = schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')



class ToggleMuteDatasetPayload(sgqlc.types.Type):
    '''Start/Stop creating incidents for the given dataset'''
    __schema__ = schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field('Dataset', graphql_name='muted')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteDatasetsPayload(sgqlc.types.Type):
    '''Start/Stop creating incidents for the given datasets'''
    __schema__ = schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field(sgqlc.types.list_of('Dataset'), graphql_name='muted')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteTablePayload(sgqlc.types.Type):
    '''Start/Stop creating incidents for the given table'''
    __schema__ = schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field('WarehouseTable', graphql_name='muted')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteTablesPayload(sgqlc.types.Type):
    '''Start/Stop creating incidents for the given tables'''
    __schema__ = schema
    __field_names__ = ('muted', 'client_mutation_id')
    muted = sgqlc.types.Field(sgqlc.types.list_of('WarehouseTable'), graphql_name='muted')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleMuteWithRegexPayload(sgqlc.types.Type):
    '''Start/Stop creating incidents for all matched elements. Use
    wildcards to match more than one table or dataset.
    '''
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class ToggleSlackReplyWarning(sgqlc.types.Type):
    '''Enable/disable the Slack reply warning feature'''
    __schema__ = schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    '''The resulting enabled/disabled state for the feature'''



class ToggleWildcardAggregation(sgqlc.types.Type):
    '''Enables/disable aggregation of wildcard tables (defaults to yearly
    and monthly templates)
    '''
    __schema__ = schema
    __field_names__ = ('enabled',)
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')



class TokenMetadata(sgqlc.types.Type):
    '''Metadata for the API Access Token'''
    __schema__ = schema
    __field_names__ = ('id', 'first_name', 'last_name', 'email', 'creation_time', 'created_by', 'expiration_time', 'comment', 'is_service_api_token', 'groups')
    id = sgqlc.types.Field(String, graphql_name='id')
    '''Token id'''

    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    '''First name for the owner of the token'''

    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    '''Last name for the owner of the token'''

    email = sgqlc.types.Field(String, graphql_name='email')
    '''Email for the owner of the token'''

    creation_time = sgqlc.types.Field(DateTime, graphql_name='creationTime')
    '''When the token was created'''

    created_by = sgqlc.types.Field(String, graphql_name='createdBy')
    '''Who created the token'''

    expiration_time = sgqlc.types.Field(DateTime, graphql_name='expirationTime')
    '''When the token is set to expire'''

    comment = sgqlc.types.Field(String, graphql_name='comment')
    '''Any comments or description for the token'''

    is_service_api_token = sgqlc.types.Field(Boolean, graphql_name='isServiceApiToken')
    '''True if this is an account service token; false if it's a personal
    token
    '''

    groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='groups')
    '''Names of the groups for the API token (for service API tokens).'''



class TopQueryGroupsResponseType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('total', 'top_query_groups')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')

    top_query_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(QueryGroupSummaryType)), graphql_name='topQueryGroups')



class TrackTablePayload(sgqlc.types.Type):
    '''Add table to account's dashboard'''
    __schema__ = schema
    __field_names__ = ('table', 'client_mutation_id')
    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class TriggerCircuitBreakerRule(sgqlc.types.Type):
    '''Run a custom rule as a circuit breaker immediately. Supports rules
    that create a single query.
    '''
    __schema__ = schema
    __field_names__ = ('job_execution_uuid',)
    job_execution_uuid = sgqlc.types.Field(UUID, graphql_name='jobExecutionUuid')



class TriggerCircuitBreakerRuleV2(sgqlc.types.Type):
    '''Run a custom rule as a circuit breaker immediately. Supports rules
    that create multiple queries.
    '''
    __schema__ = schema
    __field_names__ = ('job_execution_uuids',)
    job_execution_uuids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='jobExecutionUuids')
    '''The UUIDs of the triggered rule job executions.'''



class TriggerCustomRule(sgqlc.types.Type):
    '''Run a custom rule immediately'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class TriggerMonitor(sgqlc.types.Type):
    '''Run a monitor immediately'''
    __schema__ = schema
    __field_names__ = ('monitor',)
    monitor = sgqlc.types.Field('MetricMonitoring', graphql_name='monitor')



class UnifiedUserAssignmentConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UnifiedUserAssignmentEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class UnifiedUserAssignmentEdge(sgqlc.types.Type):
    '''A Relay edge containing a `UnifiedUserAssignment` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UnifiedUserAssignment', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UnifiedUserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UnifiedUserEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class UnifiedUserEdge(sgqlc.types.Type):
    '''A Relay edge containing a `UnifiedUser` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UnifiedUser', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UnlinkJiraTicketForIncident(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('unlinked',)
    unlinked = sgqlc.types.Field(Boolean, graphql_name='unlinked')
    '''True if the ticket was unlinked'''



class UnsnoozeCustomRule(sgqlc.types.Type):
    '''Un-snooze a custom rule.'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class UnsnoozeDbtNode(sgqlc.types.Type):
    '''Un-snooze a DBT node (model/test).'''
    __schema__ = schema
    __field_names__ = ('node',)
    node = sgqlc.types.Field('DbtNode', graphql_name='node')



class UpdateAccountDisplayCatalogSearchTags(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(Account, graphql_name='account')



class UpdateBiConnectionNameMutation(sgqlc.types.Type):
    '''Update the name of an existing bi connection'''
    __schema__ = schema
    __field_names__ = ('bi_container',)
    bi_container = sgqlc.types.Field(BiContainer, graphql_name='biContainer')



class UpdateCredentials(sgqlc.types.Type):
    '''Update credentials for a connection'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''If the credentials were successfully updated'''



class UpdateCustomMetricRuleNotes(sgqlc.types.Type):
    '''Create or update notes for custom metric rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class UpdateCustomMetricSeverity(sgqlc.types.Type):
    '''Create or update default severity for custom metric rule'''
    __schema__ = schema
    __field_names__ = ('custom_rule',)
    custom_rule = sgqlc.types.Field('CustomRule', graphql_name='customRule')



class UpdateDatabricksNotebook(sgqlc.types.Type):
    '''Update Databricks notebook.'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully.'''



class UpdateDatabricksNotebookJob(sgqlc.types.Type):
    '''Update Databricks collection notebook and job.'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully.'''



class UpdateDbtProjectInfo(sgqlc.types.Type):
    '''Set extra information about dbt project'''
    __schema__ = schema
    __field_names__ = ('project',)
    project = sgqlc.types.Field('DbtProject', graphql_name='project')
    '''dbt project after the update'''



class UpdateJiraIntegration(sgqlc.types.Type):
    '''Update a Jira integration'''
    __schema__ = schema
    __field_names__ = ('jira_integration',)
    jira_integration = sgqlc.types.Field(JiraIntegrationOutput, graphql_name='jiraIntegration')
    '''The integration that was created'''



class UpdateMonitorLabels(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class UpdateMonitorName(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class UpdateMonitorNotes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class UpdatePiiFilteringPreferences(sgqlc.types.Type):
    '''Update account-wide PII filtering options.'''
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Whether the mutation succeeded.'''



class UpdateSlackChannelsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class UpdateUserAuthorizationGroupMembership(sgqlc.types.Type):
    '''Update a user's authorization group membership. Authenticated user
    must have permission to manage users.
    '''
    __schema__ = schema
    __field_names__ = ('added_to_groups', 'removed_from_groups')
    added_to_groups = sgqlc.types.Field(sgqlc.types.list_of(AuthorizationGroupOutput), graphql_name='addedToGroups')
    '''List of groups user was added to.'''

    removed_from_groups = sgqlc.types.Field(sgqlc.types.list_of(AuthorizationGroupOutput), graphql_name='removedFromGroups')
    '''List of groups user was removed from.'''



class UpdateUserStatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user', 'client_mutation_id')
    user = sgqlc.types.Field('User', graphql_name='user')

    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')



class UploadAirflowDagResult(sgqlc.types.Type):
    '''Uploads the result for a DAG run.'''
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')
    '''Result'''



class UploadAirflowSlaMisses(sgqlc.types.Type):
    '''Uploads a list of SLAs missed for a DAG.'''
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')
    '''Result'''



class UploadAirflowTaskResult(sgqlc.types.Type):
    '''Uploads the result for a DAG run.'''
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')
    '''Result'''



class UploadDbtManifest(sgqlc.types.Type):
    '''Upload DBT manifest'''
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')



class UploadDbtRunResults(sgqlc.types.Type):
    '''Upload DBT run results'''
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')



class UploadWarehouseCredentialsMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('key',)
    key = sgqlc.types.Field(String, graphql_name='key')



class UserAfterKey(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user', 'source')
    user = sgqlc.types.Field(String, graphql_name='user')
    '''The username'''

    source = sgqlc.types.Field(String, graphql_name='source')
    '''The source table'''



class UserAfterKey2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user',)
    user = sgqlc.types.Field(String, graphql_name='user')
    '''The username'''



class UserAuthorizationOutput(sgqlc.types.Type):
    '''The aggregate authorization policy for a user.'''
    __schema__ = schema
    __field_names__ = ('groups', 'domain_restrictions', 'permissions')
    groups = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='groups')
    '''List of the groups this user is a member of.'''

    domain_restrictions = sgqlc.types.Field(sgqlc.types.list_of('DomainRestriction'), graphql_name='domainRestrictions')
    '''Union of all discovered domain restrictions for the user. If
    empty, user has no restrictions. Note this list may not
    necessarily match the domain restrictions for a particular
    permission. This is simply a complete list of all discovered
    restrictions for the user--always check the restrictions on a
    permission against its own list of restrictions.
    '''

    permissions = sgqlc.types.Field(sgqlc.types.list_of('UserPermission'), graphql_name='permissions')
    '''Full list of permissions with resolved policy for the user.'''



class UserBlastRadius(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('username', 'query_count', 'table')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''The username who performed the query'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of queries performed by user in the timeframe'''

    table = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='table')
    '''The incident tables that was queried'''



class UserBlastRadius2(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('username', 'query_count', 'tables')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    '''The username who performed the query'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of queries performed by user in the timeframe'''

    tables = sgqlc.types.Field(sgqlc.types.list_of('UserTableBlastRadius'), graphql_name='tables')
    '''The table information for the user'''



class UserConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges', 'total_count', 'edge_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')

    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')



class UserDefinedMonitorConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserDefinedMonitorEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class UserDefinedMonitorConnectionV2Connection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserDefinedMonitorConnectionV2Edge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class UserDefinedMonitorConnectionV2Edge(sgqlc.types.Type):
    '''A Relay edge containing a `UserDefinedMonitorConnectionV2` and its
    cursor.
    '''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserDefinedMonitorV2', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UserDefinedMonitorEdge(sgqlc.types.Type):
    '''A Relay edge containing a `UserDefinedMonitor` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserDefinedMonitor', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UserEdge(sgqlc.types.Type):
    '''A Relay edge containing a `User` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UserInviteConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges', 'total_count', 'edge_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserInviteEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')

    edge_count = sgqlc.types.Field(Int, graphql_name='edgeCount')



class UserInviteEdge(sgqlc.types.Type):
    '''A Relay edge containing a `UserInvite` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserInvite', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UserPermission(sgqlc.types.Type):
    '''An individual permission policy for a user.'''
    __schema__ = schema
    __field_names__ = ('permission', 'effect', 'domain_restriction_ids')
    permission = sgqlc.types.Field(Permission, graphql_name='permission')
    '''Enum name of permission this policy applies to.'''

    effect = sgqlc.types.Field(PermissionEffect, graphql_name='effect')
    '''The effective policy for this permission for the user.'''

    domain_restriction_ids = sgqlc.types.Field(sgqlc.types.list_of(UUID), graphql_name='domainRestrictionIds')
    '''If permission allowed and user is restricted, union of domain IDs
    for which user has this permission.
    '''



class UserSettingsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('UserSettingsEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class UserSettingsEdge(sgqlc.types.Type):
    '''A Relay edge containing a `UserSettings` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('UserSettings', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class UserTableBlastRadius(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('full_table_id', 'query_count', 'mcon')
    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')
    '''The incident table that was queried'''

    query_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queryCount')
    '''The number of queries performed by user in the timeframe'''

    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')
    '''The table mcon'''



class ValidateCron(sgqlc.types.Type):
    '''Validate a CRON expression'''
    __schema__ = schema
    __field_names__ = ('success', 'error')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the CRON expression is valid'''

    error = sgqlc.types.Field(String, graphql_name='error')
    '''Error message if the CRON expression is not valid'''



class ValidateDataAssetAccessResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success', 'validation_results')
    success = sgqlc.types.Field(Boolean, graphql_name='success')
    '''Indicates whether the operation was completed successfully'''

    validation_results = sgqlc.types.Field(sgqlc.types.list_of(TestCredentialsV2Response), graphql_name='validationResults')
    '''List of validation results'''



class Validation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('name', 'description', 'is_prerequisite')
    name = sgqlc.types.Field(String, graphql_name='name')
    '''Name of the validation.'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Description of the validation.'''

    is_prerequisite = sgqlc.types.Field(Boolean, graphql_name='isPrerequisite')
    '''Whether this is an essential prerequisite for other validations to
    be run. Prerequisite validations should be run serially before
    non-prerequisite validations are run.
    '''



class ValidationFailure(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cause', 'stack_trace', 'friendly_message', 'resolution')
    cause = sgqlc.types.Field(String, graphql_name='cause')
    '''Cause of the validation failure.'''

    stack_trace = sgqlc.types.Field(String, graphql_name='stackTrace')
    '''Stack trace of the failure.'''

    friendly_message = sgqlc.types.Field(String, graphql_name='friendlyMessage')
    '''A friendly error message.'''

    resolution = sgqlc.types.Field(String, graphql_name='resolution')
    '''Helpful instructions on how to resolve the validation failure.'''



class Warehouse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'uuid', 'name', 'connection_type', 'credentials_s3_key', 'bq_project_id', 'account', 'data_collector', 'created_on', 'is_deleted', 'deleted_at', 'deleted_by', 'config', 'connections', 'tables', 'incidents', 'events', 'datasets', 'mute_rule', 'fivetran_destinations', 'data_sampling_enabled', 'data_sampling_restricted', 'value_ingestion_enabled', 'value_based_threshold_enabled', 'custom_sql_sampling_supported', 'custom_sql_sampling_enabled', 'supports_reproduction_queries', 'supports_sampling')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    name = sgqlc.types.Field(String, graphql_name='name')

    connection_type = sgqlc.types.Field(sgqlc.types.non_null(WarehouseModelConnectionType), graphql_name='connectionType')

    credentials_s3_key = sgqlc.types.Field(String, graphql_name='credentialsS3Key')

    bq_project_id = sgqlc.types.Field(String, graphql_name='bqProjectId')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    data_collector = sgqlc.types.Field(DataCollector, graphql_name='dataCollector')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    deleted_at = sgqlc.types.Field(DateTime, graphql_name='deletedAt')

    deleted_by = sgqlc.types.Field('User', graphql_name='deletedBy')

    config = sgqlc.types.Field(JSONString, graphql_name='config')

    connections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Connection))), graphql_name='connections')

    tables = sgqlc.types.Field(sgqlc.types.non_null('WarehouseTableConnection'), graphql_name='tables', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `full_table_id` (`String`)None
    '''

    incidents = sgqlc.types.Field(sgqlc.types.non_null(IncidentConnection), graphql_name='incidents', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Warehouse an incident belongs to

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    events = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='events', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    datasets = sgqlc.types.Field(sgqlc.types.non_null(DatasetConnection), graphql_name='datasets', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('dataset', sgqlc.types.Arg(String, graphql_name='dataset', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `dataset` (`String`)None
    '''

    mute_rule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EventMutingRule))), graphql_name='muteRule')

    fivetran_destinations = sgqlc.types.Field(sgqlc.types.non_null(FivetranDestinationConnection), graphql_name='fivetranDestinations', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    data_sampling_enabled = sgqlc.types.Field(Boolean, graphql_name='dataSamplingEnabled')
    '''Indicates whether the customer has opted out of sampling for the
    warehouse
    '''

    data_sampling_restricted = sgqlc.types.Field(Boolean, graphql_name='dataSamplingRestricted')
    '''Indicates whether the customer has opted into sampling
    restrictions for the warehouse
    '''

    value_ingestion_enabled = sgqlc.types.Field(Boolean, graphql_name='valueIngestionEnabled')
    '''Indicates whether the customer has opted out of value ingestion
    for the warehouse (opting out of sampling disables this as well)
    '''

    value_based_threshold_enabled = sgqlc.types.Field(Boolean, graphql_name='valueBasedThresholdEnabled')
    '''Indicates whether rules with value-based thresholds can be created
    and executed
    '''

    custom_sql_sampling_supported = sgqlc.types.Field(Boolean, graphql_name='customSqlSamplingSupported')
    '''Indicates whether the DC version for this warehouse supports
    custom SQL sampling
    '''

    custom_sql_sampling_enabled = sgqlc.types.Field(Boolean, graphql_name='customSqlSamplingEnabled')
    '''Indicates whether output of qualifying custom SQL rules in this
    warehouse will be sampled
    '''

    supports_reproduction_queries = sgqlc.types.Field(Boolean, graphql_name='supportsReproductionQueries')

    supports_sampling = sgqlc.types.Field(Boolean, graphql_name='supportsSampling')



class WarehouseTableConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('WarehouseTableEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''



class WarehouseTableEdge(sgqlc.types.Type):
    '''A Relay edge containing a `WarehouseTable` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('WarehouseTable', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class WarehouseTableHealthConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('page_info', 'edges', 'total_count')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    '''Pagination data for this connection.'''

    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('WarehouseTableHealthEdge')), graphql_name='edges')
    '''Contains the nodes in this connection.'''

    total_count = sgqlc.types.Field(Int, graphql_name='totalCount')
    '''Total count of elements in the result set.'''



class WarehouseTableHealthEdge(sgqlc.types.Type):
    '''A Relay edge containing a `WarehouseTableHealth` and its cursor.'''
    __schema__ = schema
    __field_names__ = ('node', 'cursor')
    node = sgqlc.types.Field('WarehouseTableHealth', graphql_name='node')
    '''The item at the end of the edge'''

    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    '''A cursor for use in pagination'''



class WarehouseTableIncident(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('uuid', 'category', 'feedback')
    uuid = sgqlc.types.Field(UUID, graphql_name='uuid')
    '''UUID of the incident'''

    category = sgqlc.types.Field(IncidentCategory, graphql_name='category')
    '''Category used to classify the incident'''

    feedback = sgqlc.types.Field(String, graphql_name='feedback')
    '''Status for the incident'''



class WhereConditionSegments(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('where_conditions',)
    where_conditions = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='whereConditions')



class WildcardTemplate(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('template_name', 'template_regex')
    template_name = sgqlc.types.Field(String, graphql_name='templateName')
    '''Name describing the template format (i.e. _YYYYMMD'''

    template_regex = sgqlc.types.Field(String, graphql_name='templateRegex')
    '''Regex used to match the template format'''



class WildcardTemplates(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('templates',)
    templates = sgqlc.types.Field(sgqlc.types.list_of(WildcardTemplate), graphql_name='templates')



class createEventComment(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class deleteEventComment(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class updateEventComment(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('success',)
    success = sgqlc.types.Field(Boolean, graphql_name='success')



class AirflowTaskInstance(sgqlc.types.Type, Node):
    '''Airflow task attempt details'''
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'account_uuid', 'dag_id', 'execution_date', 'task_id', 'try_number', 'state')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')
    '''Account identifier'''

    dag_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dagId')
    '''Airflow DAG identifier'''

    execution_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='executionDate')
    '''Airflow DAG execution date (should be treated as an ID string)'''

    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')
    '''Airflow task identifier'''

    try_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tryNumber')
    '''Airflow task execution attempt'''

    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    '''Airflow task state'''



class AirflowTaskRun(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'dag_id', 'run_id', 'task_id', 'env_name', 'execution_date', 'start_date', 'end_date', 'duration', 'next_retry_date', 'attempt_number', 'success', 'state', 'exception_message', 'log_url', 'payload')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of Task Run'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    dag_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dagId')
    '''DAG ID'''

    run_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='runId')
    '''DAG Run ID'''

    task_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='taskId')
    '''Task ID'''

    env_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='envName')
    '''AirFlow environment name'''

    execution_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='executionDate')
    '''Task run execution_date'''

    start_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startDate')
    '''Task run start_date'''

    end_date = sgqlc.types.Field(DateTime, graphql_name='endDate')
    '''Task run end_date'''

    duration = sgqlc.types.Field(Float, graphql_name='duration')
    '''Task run duration'''

    next_retry_date = sgqlc.types.Field(DateTime, graphql_name='nextRetryDate')
    '''Task next retry datetime'''

    attempt_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attemptNumber')
    '''Task attempt number'''

    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    '''Task run was successful or not'''

    state = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='state')
    '''Task run state'''

    exception_message = sgqlc.types.Field(String, graphql_name='exceptionMessage')
    '''Task failure error message'''

    log_url = sgqlc.types.Field(String, graphql_name='logUrl')
    '''Task log url'''

    payload = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='payload')
    '''Task run payload'''



class AuthUser(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('cognito_user_id', 'email', 'first_name', 'last_name', 'display_name', 'state', 'created_on', 'is_sso', 'sso_groups', 'sso_groups_updated_at', 'token_id', 'is_deleted', 'notification_settings_added', 'notification_settings_modified', 'user_settings', 'invitees', 'warehouse_deleted_by', 'monitor_labels_created', 'eventmodel_set', 'incident_reactions_created', 'incident_reactions_modified', 'user_comments', 'creator', 'metricmonitoringmodel_set', 'combinedtablestatsmodel_set', 'object_properties', 'catalog_object_metadata', 'resources', 'lineage_block_patterns', 'lineage_repl_rules', 'monte_carlo_config_templates', 'domain_created_by', 'slack_credentials_v2', 'custom_users', 'unified_users', 'last_updated_unified_users', 'collection_preference_created_by', 'collection_preference_last_updated_by', 'collection_preference_deleted_by', 'gh_installations')
    cognito_user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cognitoUserId')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    first_name = sgqlc.types.Field(String, graphql_name='firstName')

    last_name = sgqlc.types.Field(String, graphql_name='lastName')

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Text to use when displaying the user.'''

    state = sgqlc.types.Field(sgqlc.types.non_null(UserModelState), graphql_name='state')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    is_sso = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSso')

    sso_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ssoGroups')
    '''Groups provided by the IdP in the last login'''

    sso_groups_updated_at = sgqlc.types.Field(DateTime, graphql_name='ssoGroupsUpdatedAt')
    '''Last time the SSO groups where updated'''

    token_id = sgqlc.types.Field(String, graphql_name='tokenId')
    '''For role=service accounts, the associated API token ID'''

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    notification_settings_added = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsAdded')
    '''Creator of the notification'''

    notification_settings_modified = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsModified')
    '''User who last updated this notification'''

    user_settings = sgqlc.types.Field(sgqlc.types.non_null(UserSettingsConnection), graphql_name='userSettings', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated user

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    invitees = sgqlc.types.Field(sgqlc.types.non_null(UserInviteConnection), graphql_name='invitees', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `state` (`String`)None
    '''

    warehouse_deleted_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Warehouse))), graphql_name='warehouseDeletedBy')

    monitor_labels_created = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MonitorLabelObject))), graphql_name='monitorLabelsCreated')
    '''Monitor label creator'''

    eventmodel_set = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='eventmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    incident_reactions_created = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsCreated', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    incident_reactions_modified = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsModified', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    user_comments = sgqlc.types.Field(sgqlc.types.non_null(EventCommentConnection), graphql_name='userComments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    creator = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='creator', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Who added the monitor

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    metricmonitoringmodel_set = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='metricmonitoringmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Who was the last user to update the monitor

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    combinedtablestatsmodel_set = sgqlc.types.Field(sgqlc.types.non_null(TableStatsConnection), graphql_name='combinedtablestatsmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    object_properties = sgqlc.types.Field(sgqlc.types.non_null(ObjectPropertyConnection), graphql_name='objectProperties', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon_id', sgqlc.types.Arg(String, graphql_name='mconId', default=None)),
))
    )
    '''Who last updated the property

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `mcon_id` (`String`)None
    '''

    catalog_object_metadata = sgqlc.types.Field(sgqlc.types.non_null(CatalogObjectMetadataConnection), graphql_name='catalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Who last updated the object

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `mcon` (`String`)None
    '''

    resources = sgqlc.types.Field(sgqlc.types.non_null(ResourceConnection), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Who last updated the resource

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    lineage_block_patterns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNodeBlockPattern))), graphql_name='lineageBlockPatterns')
    '''Who last updated the regexp'''

    lineage_repl_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNodeReplacementRule))), graphql_name='lineageReplRules')
    '''Who last updated the replacement rule'''

    monte_carlo_config_templates = sgqlc.types.Field(sgqlc.types.non_null(MonteCarloConfigTemplateConnection), graphql_name='monteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `namespace` (`String`)None
    '''

    domain_created_by = sgqlc.types.Field(sgqlc.types.non_null(DomainRestrictionConnection), graphql_name='domainCreatedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    slack_credentials_v2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SlackCredentialsV2))), graphql_name='slackCredentialsV2')
    '''User that installed the Slack app'''

    custom_users = sgqlc.types.Field(sgqlc.types.non_null(CustomUserConnection), graphql_name='customUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Who last updated the object

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='unifiedUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated MC user

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    last_updated_unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='lastUpdatedUnifiedUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Who last updated the object

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    collection_preference_created_by = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferenceCreatedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    collection_preference_last_updated_by = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferenceLastUpdatedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    collection_preference_deleted_by = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferenceDeletedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    gh_installations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GithubAppInstallation))), graphql_name='ghInstallations')
    '''User that installed the Github app'''



class CatalogObjectMetadata(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('mcon', 'account_id', 'resource_id', 'description', 'created_time', 'last_update_user', 'last_update_time', 'source')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''Customer resource id (e.g. warehouse)'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Markdown description of object'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the object was first created'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who last updated the object'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the object was last updated'''

    source = sgqlc.types.Field(String, graphql_name='source')
    '''The source of this metadata (e.g. dbt, snowflake, bigquery, etc.)'''



class CollectionBlock(sgqlc.types.Type, Node):
    '''Describes entities with a defined metadata collection preference.'''
    __schema__ = schema
    __field_names__ = ('project', 'dataset', 'resource_id')
    project = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='project')
    '''Top-level object hierarchy e.g. database, catalog, etc.'''

    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    '''Intermediate object hierarchy e.g. schema, database, etc.'''

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')
    '''The resource UUID this collection block applies to.'''



class CustomRule(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'account_uuid', 'projects', 'datasets', 'description', 'notes', 'labels', 'is_template_managed', 'namespace', 'severity', 'rule_type', 'warehouse_uuid', 'comparisons', 'interval_minutes', 'interval_crontab', 'start_time', 'timezone', 'creator_id', 'updater_id', 'prev_execution_time', 'next_execution_time', 'last_check_timestamp', 'created_time', 'updated_time', 'is_deleted', 'snooze_until_time', 'slack_snooze_user', 'conditional_snooze', 'event_rollup_until_changed', 'event_rollup_count', 'notify_rule_run_failure', 'dc_schedule_uuid', 'data_collection_dc_schedule_uuid', 'custom_sql', 'override', 'variables', 'fields', 'generated_by', 'entities', 'rule_name', 'sequence_number', 'system_snooze_until_time', 'query_result_type', 'custom_sampling_sql', 'generated_rules', 'entity_mcons', 'rendered_custom_sql', 'schedule_config', 'data_collection_schedule_config', 'notification_settings', 'is_snoozed', 'field_metric', 'field_query_parameters')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    account_uuid = sgqlc.types.Field(UUID, graphql_name='accountUuid')
    '''Customer account id'''

    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='projects')
    '''Projects associated with the monitor'''

    datasets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='datasets')
    '''Datasets associated with the monitor'''

    description = sgqlc.types.Field(String, graphql_name='description')

    notes = sgqlc.types.Field(String, graphql_name='notes')

    labels = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='labels')
    '''Monitor labels'''

    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    '''Is this monitor managed by a configuration template (monitors-as-
    code)?
    '''

    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    '''Namespace of rule, used for monitors-as-code'''

    severity = sgqlc.types.Field(String, graphql_name='severity')
    '''The default severity for incidents involving this monitor'''

    rule_type = sgqlc.types.Field(CustomRuleModelRuleType, graphql_name='ruleType')

    warehouse_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid')

    comparisons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CustomRuleComparison)), graphql_name='comparisons')

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')

    interval_crontab = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='intervalCrontab')

    start_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startTime')

    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')

    creator_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='creatorId')
    '''The email of the user that created the monitor'''

    updater_id = sgqlc.types.Field(String, graphql_name='updaterId')
    '''The email of the user that last updated the monitor'''

    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')

    next_execution_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='nextExecutionTime')

    last_check_timestamp = sgqlc.types.Field(DateTime, graphql_name='lastCheckTimestamp')

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')

    slack_snooze_user = sgqlc.types.Field(String, graphql_name='slackSnoozeUser')
    '''The slack user who last snoozed the rule'''

    conditional_snooze = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='conditionalSnooze')

    event_rollup_until_changed = sgqlc.types.Field(Boolean, graphql_name='eventRollupUntilChanged')
    '''If true, roll up events until the condition changes'''

    event_rollup_count = sgqlc.types.Field(Int, graphql_name='eventRollupCount')
    '''The number of events to roll up into a single incident'''

    notify_rule_run_failure = sgqlc.types.Field(Boolean, graphql_name='notifyRuleRunFailure')
    '''Flag to indicate whether or not to send a notification if the rule
    fails to run
    '''

    dc_schedule_uuid = sgqlc.types.Field(UUID, graphql_name='dcScheduleUuid')

    data_collection_dc_schedule_uuid = sgqlc.types.Field(UUID, graphql_name='dataCollectionDcScheduleUuid')

    custom_sql = sgqlc.types.Field(String, graphql_name='customSql')

    override = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='override')

    variables = sgqlc.types.Field(JSONString, graphql_name='variables')

    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields')
    '''Fields used in predefined SQL rules'''

    generated_by = sgqlc.types.Field('CustomRule', graphql_name='generatedBy')

    entities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='entities')
    '''Tables referenced in query'''

    rule_name = sgqlc.types.Field(String, graphql_name='ruleName')
    '''Name of rule, must be unique per account, used for rule
    identityresolution for monitors-as-code, just a random UUID by
    default
    '''

    sequence_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sequenceNumber')
    '''Last sequence number, used by growth volume SLIs'''

    system_snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='systemSnoozeUntilTime')
    '''Snoozes rule execution, but not available to users as
    snooze_until_time
    '''

    query_result_type = sgqlc.types.Field(CustomRuleModelQueryResultType, graphql_name='queryResultType')
    '''Specifies the expected result type of the custom SQL query (e.g. a
    single numeric value)
    '''

    custom_sampling_sql = sgqlc.types.Field(String, graphql_name='customSamplingSql')
    '''Custom query to sample the data on breach'''

    generated_rules = sgqlc.types.Field(sgqlc.types.non_null(CustomRuleConnection), graphql_name='generatedRules', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('rule_type', sgqlc.types.Arg(String, graphql_name='ruleType', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(UUID, graphql_name='warehouseUuid', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `rule_type` (`String`)None
    * `warehouse_uuid` (`UUID`)None
    '''

    entity_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entityMcons')
    '''MCONs for monitored tables/views'''

    rendered_custom_sql = sgqlc.types.Field(String, graphql_name='renderedCustomSql')

    schedule_config = sgqlc.types.Field(ScheduleConfigOutput, graphql_name='scheduleConfig')

    data_collection_schedule_config = sgqlc.types.Field(ScheduleConfigOutput, graphql_name='dataCollectionScheduleConfig')

    notification_settings = sgqlc.types.Field(sgqlc.types.list_of(AccountNotificationSetting), graphql_name='notificationSettings')

    is_snoozed = sgqlc.types.Field(Boolean, graphql_name='isSnoozed')
    '''True if rule is currently snoozed'''

    field_metric = sgqlc.types.Field(FieldMetricOutput, graphql_name='fieldMetric')
    '''Field metric parameters (if query generated by
    getFieldMetricQuery)
    '''

    field_query_parameters = sgqlc.types.Field(FieldQueryParametersOutput, graphql_name='fieldQueryParameters')
    '''Field query parameters (if query generated by getFieldQuery)'''



class CustomUser(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'account_id', 'email', 'first_name', 'last_name', 'created_time', 'last_update_user', 'last_update_time', 'is_deleted', 'unified_users')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of custom user'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    email = sgqlc.types.Field(String, graphql_name='email')
    '''Email'''

    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    '''First name'''

    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    '''Last name'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the object was first created'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who last updated the object'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the object was last updated'''

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='unifiedUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated custom user

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class Dataset(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'warehouse', 'project', 'dataset', 'is_muted', 'table_count', 'muted_event_types')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')

    project = sgqlc.types.Field(String, graphql_name='project')

    dataset = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dataset')

    is_muted = sgqlc.types.Field(Boolean, graphql_name='isMuted')
    '''No incidents will be created for this table if muted.'''

    table_count = sgqlc.types.Field(Int, graphql_name='tableCount')
    '''Number of tables in the dataset'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Muting is active for the specified event types.'''



class DbtEdge(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'source_unique_id', 'destination_unique_id', 'dbt_project')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of dbt project'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    source_unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceUniqueId')
    '''source dbt unique ID'''

    destination_unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='destinationUniqueId')
    '''destination dbt unique ID'''

    dbt_project = sgqlc.types.Field(sgqlc.types.non_null('DbtProject'), graphql_name='dbtProject')
    '''Associated dbt project'''



class DbtJob(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'job_id', 'job_name', 'dbt_project', 'generates_incidents', 'dbt_runs')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of dbt job'''

    job_id = sgqlc.types.Field(String, graphql_name='jobId')
    '''External dbt job identifier'''

    job_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jobName')
    '''dbt job name'''

    dbt_project = sgqlc.types.Field(sgqlc.types.non_null('DbtProject'), graphql_name='dbtProject')
    '''Associated dbt project'''

    generates_incidents = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='generatesIncidents')
    '''Generate incidents for errors'''

    dbt_runs = sgqlc.types.Field(sgqlc.types.non_null(DbtRunConnection), graphql_name='dbtRuns', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated dbt job

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class DbtNode(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'unique_id', 'database', 'schema', 'name', 'alias', 'description', 'path', 'resource_type', 'raw_sql', 'raw_node_json', 'dbt_project', 'table', 'snooze_until_time', 'dbt_run_steps', 'test_dbt_run_steps')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of dbt project'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uniqueId')
    '''dbt unique ID for node'''

    database = sgqlc.types.Field(String, graphql_name='database')
    '''dbt model database'''

    schema = sgqlc.types.Field(String, graphql_name='schema')
    '''dbt model schema'''

    name = sgqlc.types.Field(String, graphql_name='name')
    '''dbt model name'''

    alias = sgqlc.types.Field(String, graphql_name='alias')
    '''dbt model alias'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''dbt model description'''

    path = sgqlc.types.Field(String, graphql_name='path')
    '''dbt model path'''

    resource_type = sgqlc.types.Field(String, graphql_name='resourceType')
    '''dbt model resource type'''

    raw_sql = sgqlc.types.Field(String, graphql_name='rawSql')
    '''dbt model definition'''

    raw_node_json = sgqlc.types.Field(String, graphql_name='rawNodeJson')
    '''dbt model raw manifest json'''

    dbt_project = sgqlc.types.Field(sgqlc.types.non_null('DbtProject'), graphql_name='dbtProject')
    '''Associated dbt project'''

    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    '''Associated table'''

    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')

    dbt_run_steps = sgqlc.types.Field(DbtRunStepConnection, graphql_name='dbtRunSteps', args=sgqlc.types.ArgDict((
        ('run_start_time', sgqlc.types.Arg(DateTime, graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(DateTime, graphql_name='runEndTime', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Run steps associated with node

    Arguments:

    * `run_start_time` (`DateTime`): Filter by start time of dbt run
    * `run_end_time` (`DateTime`): Filter by end time of dbt run
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    test_dbt_run_steps = sgqlc.types.Field(DbtRunStepConnection, graphql_name='testDbtRunSteps', args=sgqlc.types.ArgDict((
        ('run_start_time', sgqlc.types.Arg(DateTime, graphql_name='runStartTime', default=None)),
        ('run_end_time', sgqlc.types.Arg(DateTime, graphql_name='runEndTime', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Test run steps associated with node

    Arguments:

    * `run_start_time` (`DateTime`): Filter by start time of dbt run
    * `run_end_time` (`DateTime`): Filter by end time of dbt run
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class DbtProject(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'connection', 'project_id', 'project_name', 'source', 'remote_url', 'subdirectory', 'generates_incidents', 'last_model_import', 'last_test_import', 'dbt_jobs', 'dbt_nodes', 'dbt_edges', 'dbt_runs')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of dbt project'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    connection = sgqlc.types.Field(Connection, graphql_name='connection')
    '''dbt connection'''

    project_id = sgqlc.types.Field(String, graphql_name='projectId')
    '''External project identifier (e.g. dbt Cloud)'''

    project_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='projectName')
    '''dbt project name'''

    source = sgqlc.types.Field(sgqlc.types.non_null(DbtProjectModelSource), graphql_name='source')
    '''Source of data'''

    remote_url = sgqlc.types.Field(String, graphql_name='remoteUrl')
    '''Remote location of the project sources'''

    subdirectory = sgqlc.types.Field(String, graphql_name='subdirectory')
    '''Location of the project subdirectory'''

    generates_incidents = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='generatesIncidents')
    '''Generate incidents for errors'''

    last_model_import = sgqlc.types.Field(DateTime, graphql_name='lastModelImport')
    '''The date of the last model import we know about'''

    last_test_import = sgqlc.types.Field(DateTime, graphql_name='lastTestImport')
    '''The date of the last test import we know about'''

    dbt_jobs = sgqlc.types.Field(sgqlc.types.non_null(DbtJobConnection), graphql_name='dbtJobs', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated dbt project

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    dbt_nodes = sgqlc.types.Field(sgqlc.types.non_null(DbtNodeConnection), graphql_name='dbtNodes', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated dbt project

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    dbt_edges = sgqlc.types.Field(sgqlc.types.non_null(DbtEdgeConnection), graphql_name='dbtEdges', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated dbt project

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    dbt_runs = sgqlc.types.Field(sgqlc.types.non_null(DbtRunConnection), graphql_name='dbtRuns', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated dbt project

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class DbtRun(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'dbt_project', 'job', 'dbt_run_id', 'run_logs', 'generated_at', 'started_at', 'command', 'branch', 'dbt_run_steps')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of dbt project'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    dbt_project = sgqlc.types.Field(sgqlc.types.non_null(DbtProject), graphql_name='dbtProject')
    '''Associated dbt project'''

    job = sgqlc.types.Field(DbtJob, graphql_name='job')
    '''Associated dbt job'''

    dbt_run_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dbtRunId')
    '''dbt run ID'''

    run_logs = sgqlc.types.Field(String, graphql_name='runLogs')
    '''dbt run logs'''

    generated_at = sgqlc.types.Field(DateTime, graphql_name='generatedAt')
    '''Time run_results.json was generated'''

    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    '''Time run started'''

    command = sgqlc.types.Field(String, graphql_name='command')
    '''dbt command that was executed.'''

    branch = sgqlc.types.Field(String, graphql_name='branch')
    '''Code branch dbt command was executed against'''

    dbt_run_steps = sgqlc.types.Field(sgqlc.types.non_null(DbtRunStepConnection), graphql_name='dbtRunSteps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated dbt run

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class DbtRunStep(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'status', 'started_at', 'completed_at', 'thread_id', 'execution_time', 'message', 'raw_json', 'dbt_run', 'node_unique_id', 'table', 'failed_records_count')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of dbt project'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    status = sgqlc.types.Field(String, graphql_name='status')
    '''Status, usually either success or failed'''

    started_at = sgqlc.types.Field(DateTime, graphql_name='startedAt')
    '''Execution start time'''

    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    '''Execution end time'''

    thread_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='threadId')
    '''Thread ID'''

    execution_time = sgqlc.types.Field(Float, graphql_name='executionTime')
    '''Execution time elapsed'''

    message = sgqlc.types.Field(String, graphql_name='message')
    '''Output message, e.g. SUCCESS'''

    raw_json = sgqlc.types.Field(String, graphql_name='rawJson')
    '''dbt raw run result json'''

    dbt_run = sgqlc.types.Field(sgqlc.types.non_null(DbtRun), graphql_name='dbtRun')
    '''Associated dbt run'''

    node_unique_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeUniqueId')
    '''dbt unique ID for node'''

    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    '''Associated table'''

    failed_records_count = sgqlc.types.Field(Int, graphql_name='failedRecordsCount')



class DimensionTrackingSuggestions(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('account_uuid', 'mcon', 'resource_id', 'full_table_id', 'project_name', 'dataset_name', 'table_name', 'table_type', 'field', 'type', 'table_importance_score', 'field_score', 'analytics_export_ts')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')

    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    '''project_name:dataset_name.table_name'''

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    dataset_name = sgqlc.types.Field(String, graphql_name='datasetName')

    table_name = sgqlc.types.Field(String, graphql_name='tableName')

    table_type = sgqlc.types.Field(String, graphql_name='tableType')

    field = sgqlc.types.Field(String, graphql_name='field')

    type = sgqlc.types.Field(String, graphql_name='type')

    table_importance_score = sgqlc.types.Field(Float, graphql_name='tableImportanceScore')

    field_score = sgqlc.types.Field(String, graphql_name='fieldScore')

    analytics_export_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='analyticsExportTs')



class DomainRestriction(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'name', 'description', 'created_by')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Domain UUID'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''Domain name'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''Domain description'''

    created_by = sgqlc.types.Field('User', graphql_name='createdBy')



class Event(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('event_type', 'created_time', 'anomaly', 'data', 'ack_by', 'ack_timestamp', 'event_state', 'notified_users', 'total_comments', 'importance_score', 'is_important', 'is_child', 'uuid', 'warehouse', 'table', 'monitor_id', 'custom_rule_entities', 'custom_rule_projects', 'custom_rule_datasets', 'incident', 'event_generated_time', 'event_comments', 'rca_jobs', 'rca_status', 'has_live_freshness', 'has_reproduction_queries', 'has_sampling', 'table_stats')
    event_type = sgqlc.types.Field(sgqlc.types.non_null(EventModelEventType), graphql_name='eventType')

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    anomaly = sgqlc.types.Field('TableAnomaly', graphql_name='anomaly')

    data = sgqlc.types.Field(JSONString, graphql_name='data')

    ack_by = sgqlc.types.Field('User', graphql_name='ackBy')

    ack_timestamp = sgqlc.types.Field(DateTime, graphql_name='ackTimestamp')

    event_state = sgqlc.types.Field(sgqlc.types.non_null(EventModelEventState), graphql_name='eventState')

    notified_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='notifiedUsers')

    total_comments = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalComments')

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')

    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')

    is_child = sgqlc.types.Field(Boolean, graphql_name='isChild')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')

    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')

    monitor_id = sgqlc.types.Field(UUID, graphql_name='monitorId')

    custom_rule_entities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='customRuleEntities')
    '''Tables referenced if has a custom rule'''

    custom_rule_projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='customRuleProjects')
    '''Projects referenced if has a custom rule'''

    custom_rule_datasets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='customRuleDatasets')
    '''Datasets referenced if has a custom rule'''

    incident = sgqlc.types.Field('Incident', graphql_name='incident')

    event_generated_time = sgqlc.types.Field(DateTime, graphql_name='eventGeneratedTime')

    event_comments = sgqlc.types.Field(sgqlc.types.non_null(EventCommentConnection), graphql_name='eventComments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    rca_jobs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RcaJob))), graphql_name='rcaJobs')

    rca_status = sgqlc.types.Field(sgqlc.types.list_of(EventRcaStatus), graphql_name='rcaStatus')
    '''RCA status associated with the event'''

    has_live_freshness = sgqlc.types.Field(Boolean, graphql_name='hasLiveFreshness')

    has_reproduction_queries = sgqlc.types.Field(Boolean, graphql_name='hasReproductionQueries')

    has_sampling = sgqlc.types.Field(Boolean, graphql_name='hasSampling')

    table_stats = sgqlc.types.Field('TableStats', graphql_name='tableStats')
    '''Stats for the table connected to the event'''



class EventComment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('event', 'user', 'uuid', 'text', 'created_on', 'updated_on', 'is_deleted')
    event = sgqlc.types.Field(sgqlc.types.non_null(Event), graphql_name='event')

    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    updated_on = sgqlc.types.Field(DateTime, graphql_name='updatedOn')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')



class FieldHealthSuggestions(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('account_uuid', 'mcon', 'resource_id', 'full_table_id', 'project_name', 'dataset_name', 'table_name', 'table_type', 'importance_score', 'has_time_field', 'has_txt_field', 'has_num_field', 'has_bool_field', 'analytics_export_ts')
    account_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountUuid')

    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')
    '''project_name:dataset_name.table_name'''

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    dataset_name = sgqlc.types.Field(String, graphql_name='datasetName')

    table_name = sgqlc.types.Field(String, graphql_name='tableName')

    table_type = sgqlc.types.Field(String, graphql_name='tableType')

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')

    has_time_field = sgqlc.types.Field(Boolean, graphql_name='hasTimeField')

    has_txt_field = sgqlc.types.Field(Boolean, graphql_name='hasTxtField')

    has_num_field = sgqlc.types.Field(Boolean, graphql_name='hasNumField')

    has_bool_field = sgqlc.types.Field(Boolean, graphql_name='hasBoolField')

    analytics_export_ts = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='analyticsExportTs')



class FivetranConnector(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'mcon', 'account_id', 'fivetran_destination', 'fivetran_id', 'service', 'schema', 'source_sync_details', 'created_at', 'succeeded_at', 'failed_at', 'sync_frequency', 'setup_state', 'sync_state', 'update_state', 'tables', 'tasks', 'warnings', 'fivetran_status', 'fivetran_url')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Internal surrogate ID of Fivetran Connector'''

    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    fivetran_destination = sgqlc.types.Field(sgqlc.types.non_null('FivetranDestination'), graphql_name='fivetranDestination')

    fivetran_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fivetranId')

    service = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='service')

    schema = sgqlc.types.Field(String, graphql_name='schema')
    '''The schema of a Fivetran Connector'''

    source_sync_details = sgqlc.types.Field(JSONString, graphql_name='sourceSyncDetails')
    '''Information about the synced source accounts'''

    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    '''Timestamp of when a connector is created'''

    succeeded_at = sgqlc.types.Field(DateTime, graphql_name='succeededAt')
    '''Timestamp of a connector's last successful sync'''

    failed_at = sgqlc.types.Field(DateTime, graphql_name='failedAt')
    '''Timestamp of a connector's last failed sync'''

    sync_frequency = sgqlc.types.Field(Int, graphql_name='syncFrequency')
    '''The sync frequency of a connector in minutes'''

    setup_state = sgqlc.types.Field(FivetranConnectorSetupStates, graphql_name='setupState')

    sync_state = sgqlc.types.Field(FivetranConnectorSyncStates, graphql_name='syncState')

    update_state = sgqlc.types.Field(FivetranConnectorUpdateStates, graphql_name='updateState')

    tables = sgqlc.types.Field(WarehouseTableConnection, graphql_name='tables', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('full_table_id', sgqlc.types.Arg(String, graphql_name='fullTableId', default=None)),
))
    )
    '''The warehouse tables that the connector is associated with. Note
    that the list of tables here is subjected to the `tableMcons`
    filter variable provided by users.

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `full_table_id` (`String`)None
    '''

    tasks = sgqlc.types.Field(JSONString, graphql_name='tasks')
    '''Tasks needed to fix the connector status'''

    warnings = sgqlc.types.Field(JSONString, graphql_name='warnings')
    '''Warnings related to the connector status'''

    fivetran_status = sgqlc.types.Field(FivetranConnectorStatuses, graphql_name='fivetranStatus')

    fivetran_url = sgqlc.types.Field(String, graphql_name='fivetranUrl')
    '''The URL to the connector page in Fivetran'''



class FivetranDestination(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('created_time', 'updated_time', 'uuid', 'account_id', 'fivetran_id', 'group_id', 'service', 'config', 'warehouse', 'fivetran_connectors')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Internal surrogate ID of Fivetran Destination'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    fivetran_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fivetranId')
    '''Fivetran internal ID'''

    group_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='groupId')
    '''Associated Fivetran Group ID'''

    service = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='service')
    '''Kind of destination'''

    config = sgqlc.types.Field(JSONString, graphql_name='config')
    '''Service-specific config payload'''

    warehouse = sgqlc.types.Field(Warehouse, graphql_name='warehouse')

    fivetran_connectors = sgqlc.types.Field(sgqlc.types.non_null(FivetranConnectorConnection), graphql_name='fivetranConnectors', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class Incident(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'warehouse', 'created_time', 'updated_time', 'owner', 'severity', 'system_set_severity', 'feedback', 'feedback_time', 'last_update_user', 'project', 'dataset', 'schema', 'incident_type', 'incident_sub_types', 'incident_time', 'lock_incident', 'can_roll_up', 'events', 'incident_reaction', 'slack_msg_details', 'jira_tickets', 'reaction_type', 'summary', 'suggested_owner', 'topology')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''Effective ID of an incident'''

    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')
    '''Warehouse an incident belongs to'''

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    '''Time an incident was created on (i.e. first event)'''

    updated_time = sgqlc.types.Field(DateTime, graphql_name='updatedTime')
    '''Time an incident was last updated'''

    owner = sgqlc.types.Field(String, graphql_name='owner')
    '''Owner assigned to the incident'''

    severity = sgqlc.types.Field(String, graphql_name='severity')
    '''Incident severity'''

    system_set_severity = sgqlc.types.Field(String, graphql_name='systemSetSeverity')
    '''Severity set by the system on incident creation'''

    feedback = sgqlc.types.Field(IncidentModelFeedback, graphql_name='feedback')
    '''Any user feedback for an incident'''

    feedback_time = sgqlc.types.Field(DateTime, graphql_name='feedbackTime')
    '''Time when user provided feedback'''

    last_update_user = sgqlc.types.Field(JSONString, graphql_name='lastUpdateUser')
    '''Who last updated the incident'''

    project = sgqlc.types.Field(String, graphql_name='project')
    '''Project (or database/catalog) tables in an incident belong to. If
    any
    '''

    dataset = sgqlc.types.Field(String, graphql_name='dataset')
    '''Dataset (or schema) tables in an incident belong to. If any'''

    schema = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schema')
    '''project:dataset pairs'''

    incident_type = sgqlc.types.Field(IncidentModelIncidentType, graphql_name='incidentType')
    '''Type of incident'''

    incident_sub_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='incidentSubTypes')
    '''All the incident sub-types that this incident matches, based on
    the type of the events that this incident includes.
    '''

    incident_time = sgqlc.types.Field(DateTime, graphql_name='incidentTime')
    '''Time which serves as the base of the grouping window'''

    lock_incident = sgqlc.types.Field(Boolean, graphql_name='lockIncident')
    '''True if events should not be added to this incident'''

    can_roll_up = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canRollUp')
    '''Used for noise reduction of notifications for custom rules. If
    True, events can still be rolled up into this incident
    '''

    events = sgqlc.types.Field(EventConnection, graphql_name='events', args=sgqlc.types.ArgDict((
        ('event_type', sgqlc.types.Arg(String, graphql_name='eventType', default=None)),
        ('event_state', sgqlc.types.Arg(String, graphql_name='eventState', default=None)),
        ('include_timeline_events', sgqlc.types.Arg(Boolean, graphql_name='includeTimelineEvents', default=None)),
        ('include_anomaly_events', sgqlc.types.Arg(Boolean, graphql_name='includeAnomalyEvents', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `event_type` (`String`)None
    * `event_state` (`String`)None
    * `include_timeline_events` (`Boolean`): Flag indicates whether
      include timeline events or not. If event_type specified, this
      flag will be ignored
    * `include_anomaly_events` (`Boolean`): Flag indicates whether
      include anomaly events or not. If event_type specified, this
      flag will be ignored
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    incident_reaction = sgqlc.types.Field('IncidentReaction', graphql_name='incidentReaction')

    slack_msg_details = sgqlc.types.Field(sgqlc.types.non_null(SlackMessageDetailsConnection), graphql_name='slackMsgDetails', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    jira_tickets = sgqlc.types.Field(sgqlc.types.list_of(JiraTicketOutput), graphql_name='jiraTickets')
    '''Jira tickets associated with the incident'''

    reaction_type = sgqlc.types.Field(IncidentReactionType, graphql_name='reactionType')

    summary = sgqlc.types.Field(IncidentSummary, graphql_name='summary')
    '''Get summary info for incident'''

    suggested_owner = sgqlc.types.Field(String, graphql_name='suggestedOwner')
    '''E-mail of a suggested incident owner'''

    topology = sgqlc.types.Field(IncidentTopology, graphql_name='topology')
    '''Extra information about relation between events in the incident'''



class IncidentReaction(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'incident', 'type', 'reasons', 'notes', 'adapt_model', 'created_by', 'last_updated_by', 'created_time', 'updated_time')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    incident = sgqlc.types.Field(sgqlc.types.non_null(Incident), graphql_name='incident')

    type = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionType), graphql_name='type')

    reasons = sgqlc.types.Field(sgqlc.types.list_of(IncidentReactionReason), graphql_name='reasons')

    notes = sgqlc.types.Field(String, graphql_name='notes')

    adapt_model = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='adaptModel')

    created_by = sgqlc.types.Field('User', graphql_name='createdBy')

    last_updated_by = sgqlc.types.Field('User', graphql_name='lastUpdatedBy')

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')



class MetricMonitoring(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'account_uuid', 'projects', 'datasets', 'description', 'notes', 'labels', 'is_template_managed', 'namespace', 'severity', 'type', 'fields', 'entities', 'created_by', 'time_axis_field_name', 'time_axis_field_type', 'unnest_fields', 'agg_time_interval', 'history_days', 'agg_select_expression', 'where_condition', 'use_partition_clause', 'schedule', 'created_time', 'monitor_name', 'is_paused', 'notify_rule_run_failure', 'disable_look_back_bootstrap', 'segmented_expressions', 'last_update_user', 'last_update_time', 'table', 'select_expressions', 'mcon', 'full_table_id', 'monitor_type', 'schedule_config', 'notification_settings')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    account_uuid = sgqlc.types.Field(UUID, graphql_name='accountUuid')
    '''Customer account id'''

    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='projects')
    '''Projects associated with the monitor'''

    datasets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='datasets')
    '''Datasets associated with the monitor'''

    description = sgqlc.types.Field(String, graphql_name='description')

    notes = sgqlc.types.Field(String, graphql_name='notes')

    labels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MonitorLabelObject))), graphql_name='labels')

    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')
    '''Is this monitor managed by a configuration template (monitors-as-
    code)?
    '''

    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    '''Namespace of rule, used for monitors-as-code'''

    severity = sgqlc.types.Field(String, graphql_name='severity')
    '''Default severity for incidents involving this monitor'''

    type = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringModelType), graphql_name='type')

    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields')

    entities = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entities')
    '''Entities (e.g. tables) associated with monitor'''

    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    '''Who added the monitor'''

    time_axis_field_name = sgqlc.types.Field(String, graphql_name='timeAxisFieldName')

    time_axis_field_type = sgqlc.types.Field(String, graphql_name='timeAxisFieldType')

    unnest_fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='unnestFields')

    agg_time_interval = sgqlc.types.Field(String, graphql_name='aggTimeInterval')

    history_days = sgqlc.types.Field(Int, graphql_name='historyDays')

    agg_select_expression = sgqlc.types.Field(String, graphql_name='aggSelectExpression')

    where_condition = sgqlc.types.Field(String, graphql_name='whereCondition')

    use_partition_clause = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='usePartitionClause')
    '''Whether to use automatic partition filter in query'''

    schedule = sgqlc.types.Field(sgqlc.types.non_null(DataCollectorSchedule), graphql_name='schedule')

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the monitor was first created'''

    monitor_name = sgqlc.types.Field(String, graphql_name='monitorName')
    '''Name of monitor, must be unique per account, used for rule
    identityresolution for monitors-as-code, just a random UUID by
    default
    '''

    is_paused = sgqlc.types.Field(Boolean, graphql_name='isPaused')
    '''Is this monitor paused?'''

    notify_rule_run_failure = sgqlc.types.Field(Boolean, graphql_name='notifyRuleRunFailure')
    '''Flag to indicate whether or not to send a notification if the rule
    fails to run
    '''

    disable_look_back_bootstrap = sgqlc.types.Field(Boolean, graphql_name='disableLookBackBootstrap')
    '''Flag to indicates whether to disable the look back bootstrap for a
    monitor
    '''

    segmented_expressions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='segmentedExpressions')
    '''Fields or expressions to segment by'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who was the last user to update the monitor'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the monitor was last updated'''

    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')
    '''Table related to monitor'''

    select_expressions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MetricMonitorSelectExpression))), graphql_name='selectExpressions')

    mcon = sgqlc.types.Field(String, graphql_name='mcon')

    full_table_id = sgqlc.types.Field(String, graphql_name='fullTableId')

    monitor_type = sgqlc.types.Field(String, graphql_name='monitorType')

    schedule_config = sgqlc.types.Field(ScheduleConfigOutput, graphql_name='scheduleConfig')

    notification_settings = sgqlc.types.Field(sgqlc.types.list_of(AccountNotificationSetting), graphql_name='notificationSettings')



class Monitor(sgqlc.types.Type, IMonitor, IMetricsMonitor, ICustomRulesMonitor, IMonitorStatus):
    __schema__ = schema
    __field_names__ = ()


class MonteCarloConfigTemplate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('namespace', 'template', 'resolved_template', 'created_time', 'last_update_user', 'last_update_time')
    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    '''Namespace of rule, used for monitors-as-code'''

    template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='template')
    '''Input config template, as JSON'''

    resolved_template = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resolvedTemplate')
    '''Config template with resolved object UUIDs, as JSON'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')



class ObjectProperty(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('mcon_id', 'property_name', 'property_value', 'property_source_type', 'property_source')
    mcon_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mconId')
    '''Unique asset identifier'''

    property_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='propertyName')
    '''The name (key) of the property'''

    property_value = sgqlc.types.Field(String, graphql_name='propertyValue')
    '''The value for the property'''

    property_source_type = sgqlc.types.Field(sgqlc.types.non_null(ObjectPropertyModelPropertySourceType), graphql_name='propertySourceType')
    '''The type of source property (i.e. how it was supplied)'''

    property_source = sgqlc.types.Field(String, graphql_name='propertySource')
    '''The origin of the property (e.g. snowflake, bigquery, etc.)'''



class Resource(sgqlc.types.Type, Node):
    '''A resource which contains assets, e.g., a data warehouse, a report
    engine, etc
    '''
    __schema__ = schema
    __field_names__ = ('uuid', 'account', 'name', 'type', 'is_user_provided', 'is_default', 'created_time', 'last_update_user', 'last_update_time', 'collection_preferences')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''The resource id'''

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    '''Customer account'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The name of the resource'''

    type = sgqlc.types.Field(String, graphql_name='type')
    '''The type of the resource'''

    is_user_provided = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUserProvided')
    '''If the resource was created / updated by Monte Carlo or a user'''

    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    '''If the resource is the account's default resource'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the resource was first created'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who last updated the resource'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the resource was last updated'''

    collection_preferences = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferences', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class SlackChannelV2(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('account', 'name', 'channel_id', 'topic', 'purpose', 'created_time')
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')
    '''The account associated with the slack channel.'''

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    '''The name of the slack channel'''

    channel_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='channelId')
    '''The id for the slack channel'''

    topic = sgqlc.types.Field(String, graphql_name='topic')
    '''The slack channel topic'''

    purpose = sgqlc.types.Field(String, graphql_name='purpose')
    '''The slack channel purpose'''

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    '''The time this record was created.'''



class SlackEngagement(sgqlc.types.Type, Node):
    '''Slack Engagement Information'''
    __schema__ = schema
    __field_names__ = ('message', 'uuid', 'event_type', 'event_ts', 'data', 'created_time', 'updated_time')
    message = sgqlc.types.Field(sgqlc.types.non_null('SlackMessageDetails'), graphql_name='message')

    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    event_type = sgqlc.types.Field(SlackEngagementEventType, graphql_name='eventType')

    event_ts = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='eventTs')

    data = sgqlc.types.Field(JSONString, graphql_name='data')

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')



class SlackMessageDetails(sgqlc.types.Type, Node):
    '''Slack Message Information'''
    __schema__ = schema
    __field_names__ = ('incident', 'notification_setting', 'account', 'permalink', 'msg_ts', 'engagements')
    incident = sgqlc.types.Field(sgqlc.types.non_null(Incident), graphql_name='incident')

    notification_setting = sgqlc.types.Field(sgqlc.types.non_null(AccountNotificationSetting), graphql_name='notificationSetting')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    permalink = sgqlc.types.Field(String, graphql_name='permalink')

    msg_ts = sgqlc.types.Field(String, graphql_name='msgTs')

    engagements = sgqlc.types.Field(sgqlc.types.non_null(SlackEngagementConnection), graphql_name='engagements', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class TableAnomaly(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'unique_key', 'warehouse_uuid', 'table', 'rule_uuid', 'anomaly_id', 'detected_on', 'start_time', 'end_time', 'is_active', 'is_false_positive', 'reason', 'data', 'eventmodel_set')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    unique_key = sgqlc.types.Field(String, graphql_name='uniqueKey')

    warehouse_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='warehouseUuid')

    table = sgqlc.types.Field('WarehouseTable', graphql_name='table')

    rule_uuid = sgqlc.types.Field(UUID, graphql_name='ruleUuid')

    anomaly_id = sgqlc.types.Field(String, graphql_name='anomalyId')

    detected_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='detectedOn')

    start_time = sgqlc.types.Field(DateTime, graphql_name='startTime')

    end_time = sgqlc.types.Field(DateTime, graphql_name='endTime')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')

    is_false_positive = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFalsePositive')

    reason = sgqlc.types.Field(sgqlc.types.non_null(TableAnomalyModelReason), graphql_name='reason')

    data = sgqlc.types.Field(JSONString, graphql_name='data')

    eventmodel_set = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='eventmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class TableField(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('version', 'name', 'field_type', 'mode', 'description', 'original_name', 'data_metric_time_field', 'downstream_bi', 'is_time_field', 'is_text_field', 'is_numeric_field', 'is_boolean_field', 'most_recent_use_in_same_table', 'most_recent_use_in_another_table', 'field_mcon', 'object_properties', 'object_metadata')
    version = sgqlc.types.Field(sgqlc.types.non_null('TableSchemaVersion'), graphql_name='version')

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')

    field_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fieldType')

    mode = sgqlc.types.Field(String, graphql_name='mode')

    description = sgqlc.types.Field(String, graphql_name='description')

    original_name = sgqlc.types.Field(String, graphql_name='originalName')

    data_metric_time_field = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dataMetricTimeField')

    downstream_bi = sgqlc.types.Field(sgqlc.types.non_null(TableFieldToBiConnection), graphql_name='downstreamBi', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    is_time_field = sgqlc.types.Field(Boolean, graphql_name='isTimeField')

    is_text_field = sgqlc.types.Field(Boolean, graphql_name='isTextField')

    is_numeric_field = sgqlc.types.Field(Boolean, graphql_name='isNumericField')

    is_boolean_field = sgqlc.types.Field(Boolean, graphql_name='isBooleanField')

    most_recent_use_in_same_table = sgqlc.types.Field(DateTime, graphql_name='mostRecentUseInSameTable')

    most_recent_use_in_another_table = sgqlc.types.Field(DateTime, graphql_name='mostRecentUseInAnotherTable')

    field_mcon = sgqlc.types.Field(String, graphql_name='fieldMcon')

    object_properties = sgqlc.types.Field(sgqlc.types.list_of(ObjectProperty), graphql_name='objectProperties')

    object_metadata = sgqlc.types.Field(CatalogObjectMetadata, graphql_name='objectMetadata')



class TableFieldToBi(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('field', 'bi_account_id', 'bi_identifier', 'bi_name', 'bi_type', 'bi_node_id', 'created_on', 'last_seen')
    field = sgqlc.types.Field(sgqlc.types.non_null(TableField), graphql_name='field')

    bi_account_id = sgqlc.types.Field(UUID, graphql_name='biAccountId')

    bi_identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='biIdentifier')

    bi_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='biName')

    bi_type = sgqlc.types.Field(sgqlc.types.non_null(TableFieldToBiModelBiType), graphql_name='biType')

    bi_node_id = sgqlc.types.Field(String, graphql_name='biNodeId')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    last_seen = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastSeen')



class TablePartitionKeys(sgqlc.types.Type, Node):
    '''Information about the partition keys for a table'''
    __schema__ = schema
    __field_names__ = ('mcon', 'keys', 'template', 'template_keys', 'checksum', 'created_time', 'updated_time')
    mcon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mcon')

    keys = sgqlc.types.Field(JSONString, graphql_name='keys')
    '''List of partition keys metadata'''

    template = sgqlc.types.Field(String, graphql_name='template')
    '''Auto-generated predicate template'''

    template_keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='templateKeys')
    '''List of partition keys used in the template'''

    checksum = sgqlc.types.Field(String, graphql_name='checksum')
    '''MD5 checksum used for incremental loading'''

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    '''When the property was first created'''

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    '''When the property was last updated'''



class TableSchemaVersion(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('table', 'version_id', 'timestamp', 'fields')
    table = sgqlc.types.Field(sgqlc.types.non_null('WarehouseTable'), graphql_name='table')

    version_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versionId')

    timestamp = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='timestamp')

    fields = sgqlc.types.Field(TableFieldConnection, graphql_name='fields', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('search_fields', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='searchFields', default=None)),
        ('is_time_field', sgqlc.types.Arg(Boolean, graphql_name='isTimeField', default=None)),
        ('is_text_field', sgqlc.types.Arg(Boolean, graphql_name='isTextField', default=None)),
        ('is_numeric_field', sgqlc.types.Arg(Boolean, graphql_name='isNumericField', default=None)),
        ('is_boolean_field', sgqlc.types.Arg(Boolean, graphql_name='isBooleanField', default=None)),
        ('suggest_time_axis', sgqlc.types.Arg(Boolean, graphql_name='suggestTimeAxis', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('version', sgqlc.types.Arg(ID, graphql_name='version', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('field_type', sgqlc.types.Arg(String, graphql_name='fieldType', default=None)),
        ('mode', sgqlc.types.Arg(String, graphql_name='mode', default=None)),
        ('description', sgqlc.types.Arg(String, graphql_name='description', default=None)),
        ('original_name', sgqlc.types.Arg(String, graphql_name='originalName', default=None)),
        ('data_metric_time_field', sgqlc.types.Arg(Boolean, graphql_name='dataMetricTimeField', default=None)),
))
    )
    '''Arguments:

    * `search` (`String`)None
    * `search_fields` (`[String]`)None
    * `is_time_field` (`Boolean`)None
    * `is_text_field` (`Boolean`)None
    * `is_numeric_field` (`Boolean`)None
    * `is_boolean_field` (`Boolean`)None
    * `suggest_time_axis` (`Boolean`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `version` (`ID`)None
    * `name` (`String`)None
    * `field_type` (`String`)None
    * `mode` (`String`)None
    * `description` (`String`)None
    * `original_name` (`String`)None
    * `data_metric_time_field` (`Boolean`)None
    '''



class TableStats(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('resource_uuid', 'full_table_id', 'project_name', 'dataset_name', 'table_name', 'is_important', 'importance_score', 'avg_reads_per_active_day', 'total_users', 'degree_out', 'avg_writes_per_active_day')
    resource_uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceUuid')

    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    dataset_name = sgqlc.types.Field(String, graphql_name='datasetName')

    table_name = sgqlc.types.Field(String, graphql_name='tableName')

    is_important = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImportant')

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')

    avg_reads_per_active_day = sgqlc.types.Field(Float, graphql_name='avgReadsPerActiveDay')

    total_users = sgqlc.types.Field(Float, graphql_name='totalUsers')

    degree_out = sgqlc.types.Field(Float, graphql_name='degreeOut')

    avg_writes_per_active_day = sgqlc.types.Field(Float, graphql_name='avgWritesPerActiveDay')



class TableTag(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('table', 'tag', 'is_active')
    table = sgqlc.types.Field(sgqlc.types.non_null('WarehouseTable'), graphql_name='table')

    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')

    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')



class UnifiedUser(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'account_id', 'display_name', 'created_time', 'mc_user', 'custom_user', 'last_update_user', 'last_update_time', 'is_deleted', 'unified_user_assignments')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')
    '''UUID of unified user'''

    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''User-facing display name of user'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the object was first created'''

    mc_user = sgqlc.types.Field('User', graphql_name='mcUser')
    '''Associated MC user'''

    custom_user = sgqlc.types.Field(CustomUser, graphql_name='customUser')
    '''Associated custom user'''

    last_update_user = sgqlc.types.Field('User', graphql_name='lastUpdateUser')
    '''Who last updated the object'''

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')
    '''When the object was last updated'''

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    unified_user_assignments = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserAssignmentConnection), graphql_name='unifiedUserAssignments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated MC user

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''



class UnifiedUserAssignment(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('account_id', 'unified_user', 'relationship_type', 'created_time', 'is_deleted', 'object_mcon')
    account_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='accountId')
    '''Customer account id'''

    unified_user = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUser), graphql_name='unifiedUser')
    '''Associated MC user'''

    relationship_type = sgqlc.types.Field(UnifiedUserAssignmentModelRelationshipType, graphql_name='relationshipType')
    '''Type of relationship'''

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')
    '''When the object was first created'''

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')
    '''Is row deleted?'''

    object_mcon = sgqlc.types.Field(String, graphql_name='objectMcon')



class User(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('cognito_user_id', 'email', 'first_name', 'last_name', 'display_name', 'state', 'created_on', 'is_sso', 'sso_groups', 'sso_groups_updated_at', 'token_id', 'is_deleted', 'notification_settings_added', 'notification_settings_modified', 'user_settings', 'invitees', 'warehouse_deleted_by', 'monitor_labels_created', 'eventmodel_set', 'incident_reactions_created', 'incident_reactions_modified', 'user_comments', 'creator', 'metricmonitoringmodel_set', 'combinedtablestatsmodel_set', 'object_properties', 'catalog_object_metadata', 'resources', 'lineage_block_patterns', 'lineage_repl_rules', 'monte_carlo_config_templates', 'domain_created_by', 'slack_credentials_v2', 'custom_users', 'unified_users', 'last_updated_unified_users', 'collection_preference_created_by', 'collection_preference_last_updated_by', 'collection_preference_deleted_by', 'gh_installations', 'account', 'role', 'auth')
    cognito_user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cognitoUserId')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    first_name = sgqlc.types.Field(String, graphql_name='firstName')

    last_name = sgqlc.types.Field(String, graphql_name='lastName')

    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    '''Text to use when displaying the user.'''

    state = sgqlc.types.Field(sgqlc.types.non_null(UserModelState), graphql_name='state')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    is_sso = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSso')

    sso_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ssoGroups')
    '''Groups provided by the IdP in the last login'''

    sso_groups_updated_at = sgqlc.types.Field(DateTime, graphql_name='ssoGroupsUpdatedAt')
    '''Last time the SSO groups where updated'''

    token_id = sgqlc.types.Field(String, graphql_name='tokenId')
    '''For role=service accounts, the associated API token ID'''

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    notification_settings_added = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsAdded')
    '''Creator of the notification'''

    notification_settings_modified = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountNotificationSetting))), graphql_name='notificationSettingsModified')
    '''User who last updated this notification'''

    user_settings = sgqlc.types.Field(sgqlc.types.non_null(UserSettingsConnection), graphql_name='userSettings', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated user

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    invitees = sgqlc.types.Field(sgqlc.types.non_null(UserInviteConnection), graphql_name='invitees', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `state` (`String`)None
    '''

    warehouse_deleted_by = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Warehouse))), graphql_name='warehouseDeletedBy')

    monitor_labels_created = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MonitorLabelObject))), graphql_name='monitorLabelsCreated')
    '''Monitor label creator'''

    eventmodel_set = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='eventmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    incident_reactions_created = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsCreated', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    incident_reactions_modified = sgqlc.types.Field(sgqlc.types.non_null(IncidentReactionConnection), graphql_name='incidentReactionsModified', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    user_comments = sgqlc.types.Field(sgqlc.types.non_null(EventCommentConnection), graphql_name='userComments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    creator = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='creator', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Who added the monitor

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    metricmonitoringmodel_set = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='metricmonitoringmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Who was the last user to update the monitor

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    combinedtablestatsmodel_set = sgqlc.types.Field(sgqlc.types.non_null(TableStatsConnection), graphql_name='combinedtablestatsmodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    object_properties = sgqlc.types.Field(sgqlc.types.non_null(ObjectPropertyConnection), graphql_name='objectProperties', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon_id', sgqlc.types.Arg(String, graphql_name='mconId', default=None)),
))
    )
    '''Who last updated the property

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `mcon_id` (`String`)None
    '''

    catalog_object_metadata = sgqlc.types.Field(sgqlc.types.non_null(CatalogObjectMetadataConnection), graphql_name='catalogObjectMetadata', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('mcon', sgqlc.types.Arg(String, graphql_name='mcon', default=None)),
))
    )
    '''Who last updated the object

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `mcon` (`String`)None
    '''

    resources = sgqlc.types.Field(sgqlc.types.non_null(ResourceConnection), graphql_name='resources', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Who last updated the resource

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    lineage_block_patterns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNodeBlockPattern))), graphql_name='lineageBlockPatterns')
    '''Who last updated the regexp'''

    lineage_repl_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LineageNodeReplacementRule))), graphql_name='lineageReplRules')
    '''Who last updated the replacement rule'''

    monte_carlo_config_templates = sgqlc.types.Field(sgqlc.types.non_null(MonteCarloConfigTemplateConnection), graphql_name='monteCarloConfigTemplates', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `namespace` (`String`)None
    '''

    domain_created_by = sgqlc.types.Field(sgqlc.types.non_null(DomainRestrictionConnection), graphql_name='domainCreatedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    slack_credentials_v2 = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SlackCredentialsV2))), graphql_name='slackCredentialsV2')
    '''User that installed the Slack app'''

    custom_users = sgqlc.types.Field(sgqlc.types.non_null(CustomUserConnection), graphql_name='customUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Who last updated the object

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='unifiedUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated MC user

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    last_updated_unified_users = sgqlc.types.Field(sgqlc.types.non_null(UnifiedUserConnection), graphql_name='lastUpdatedUnifiedUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Who last updated the object

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    collection_preference_created_by = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferenceCreatedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    collection_preference_last_updated_by = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferenceLastUpdatedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    collection_preference_deleted_by = sgqlc.types.Field(sgqlc.types.non_null(CollectionBlockConnection), graphql_name='collectionPreferenceDeletedBy', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    gh_installations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GithubAppInstallation))), graphql_name='ghInstallations')
    '''User that installed the Github app'''

    account = sgqlc.types.Field(Account, graphql_name='account')

    role = sgqlc.types.Field(String, graphql_name='role')
    '''User internal role. One of:  user, service, system. Check the
    user's groups for their authorization roles
    '''

    auth = sgqlc.types.Field(UserAuthorizationOutput, graphql_name='auth')
    '''User's aggregate authorization policy.'''



class UserDefinedMonitorV2(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'udm_type', 'resource_id', 'creator_id', 'updater_id', 'entities', 'projects', 'datasets', 'rule_comparisons', 'rule_description', 'rule_variables', 'monitor_type', 'monitor_fields', 'monitor_time_axis_field_name', 'monitor_time_axis_field_type', 'created_time', 'last_update_time', 'schedule_type', 'last_run', 'notify_rule_run_failure', 'interval_in_seconds', 'prev_execution_time', 'next_execution_time', 'is_deleted', 'is_template_managed', 'is_snoozeable', 'is_snoozed', 'conditional_snooze', 'snooze_until_time', 'is_paused', 'where_condition', 'use_partition_clause', 'namespace', 'name', 'rule_name', 'rule_notes', 'history_days', 'segmented_expressions', 'interval_minutes', 'agg_time_interval', 'severity', 'entity_mcons', 'has_custom_rule_name', 'is_transitioning_data_provider')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    udm_type = sgqlc.types.Field(sgqlc.types.non_null(UserDefinedMonitorModelUdmType), graphql_name='udmType')

    resource_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='resourceId')

    creator_id = sgqlc.types.Field(String, graphql_name='creatorId')
    '''The email of the user that created the monitor'''

    updater_id = sgqlc.types.Field(String, graphql_name='updaterId')
    '''The email of the user that last updated the monitor'''

    entities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='entities')
    '''Tables associated with monitor'''

    projects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='projects')
    '''Projects associated with monitor'''

    datasets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='datasets')
    '''Datasets associated with monitor'''

    rule_comparisons = sgqlc.types.Field(sgqlc.types.list_of(CustomRuleComparison), graphql_name='ruleComparisons')

    rule_description = sgqlc.types.Field(String, graphql_name='ruleDescription')

    rule_variables = sgqlc.types.Field(JSONString, graphql_name='ruleVariables')

    monitor_type = sgqlc.types.Field(sgqlc.types.non_null(UserDefinedMonitorModelMonitorType), graphql_name='monitorType')

    monitor_fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='monitorFields')

    monitor_time_axis_field_name = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldName')

    monitor_time_axis_field_type = sgqlc.types.Field(String, graphql_name='monitorTimeAxisFieldType')

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')

    last_update_time = sgqlc.types.Field(DateTime, graphql_name='lastUpdateTime')

    schedule_type = sgqlc.types.Field(UserDefinedMonitorModelScheduleType, graphql_name='scheduleType')

    last_run = sgqlc.types.Field(DateTime, graphql_name='lastRun')

    notify_rule_run_failure = sgqlc.types.Field(Boolean, graphql_name='notifyRuleRunFailure')

    interval_in_seconds = sgqlc.types.Field(Int, graphql_name='intervalInSeconds')

    prev_execution_time = sgqlc.types.Field(DateTime, graphql_name='prevExecutionTime')

    next_execution_time = sgqlc.types.Field(DateTime, graphql_name='nextExecutionTime')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    is_template_managed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplateManaged')

    is_snoozeable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozeable')

    is_snoozed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSnoozed')

    conditional_snooze = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='conditionalSnooze')

    snooze_until_time = sgqlc.types.Field(DateTime, graphql_name='snoozeUntilTime')

    is_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaused')

    where_condition = sgqlc.types.Field(String, graphql_name='whereCondition')

    use_partition_clause = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='usePartitionClause')

    namespace = sgqlc.types.Field(String, graphql_name='namespace')

    name = sgqlc.types.Field(String, graphql_name='name')

    rule_name = sgqlc.types.Field(String, graphql_name='ruleName')
    '''Deprecated in favor of name which also provides names for monitors'''

    rule_notes = sgqlc.types.Field(String, graphql_name='ruleNotes')

    history_days = sgqlc.types.Field(Int, graphql_name='historyDays')

    segmented_expressions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='segmentedExpressions')
    '''Fields or expressions to segment by'''

    interval_minutes = sgqlc.types.Field(Int, graphql_name='intervalMinutes')

    agg_time_interval = sgqlc.types.Field(String, graphql_name='aggTimeInterval')

    severity = sgqlc.types.Field(String, graphql_name='severity')

    entity_mcons = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='entityMcons')
    '''MCONs for monitored tables/views'''

    has_custom_rule_name = sgqlc.types.Field(Boolean, graphql_name='hasCustomRuleName')

    is_transitioning_data_provider = sgqlc.types.Field(Boolean, graphql_name='isTransitioningDataProvider')



class UserInvite(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('uuid', 'email', 'state', 'account', 'created_by', 'created_on', 'accepted_on', 'role', 'auth_groups', 'invite_type', 'last_sent_time', 'attempts', 'user_previous_account', 'expires_at')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='uuid')

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')

    state = sgqlc.types.Field(sgqlc.types.non_null(UserInviteModelState), graphql_name='state')

    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')

    created_by = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='createdBy')

    created_on = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdOn')

    accepted_on = sgqlc.types.Field(DateTime, graphql_name='acceptedOn')

    role = sgqlc.types.Field(String, graphql_name='role')
    '''Deprecated. Use auth groups going forward. Will remove after
    migration.
    '''

    auth_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='authGroups')
    '''List of auth group names to put user in on invite acceptance'''

    invite_type = sgqlc.types.Field(UserInviteModelInviteType, graphql_name='inviteType')
    '''Type of invitation.'''

    last_sent_time = sgqlc.types.Field(DateTime, graphql_name='lastSentTime')
    '''Last time this invite was sent'''

    attempts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attempts')
    '''Number of times invite verification has been attempted with the
    current token
    '''

    user_previous_account = sgqlc.types.Field(Account, graphql_name='userPreviousAccount')

    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    '''Expiration of this invite'''



class UserSettings(sgqlc.types.Type, Node):
    '''User settings stored associated with the key.'''
    __schema__ = schema
    __field_names__ = ('user', 'key', 'value', 'created_time', 'updated_time', 'description')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')
    '''Associated user'''

    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')

    value = sgqlc.types.Field(JSONString, graphql_name='value')

    created_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdTime')
    '''When the user-specific setting was first created'''

    updated_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedTime')
    '''When the user-specific setting was last updated'''

    description = sgqlc.types.Field(String, graphql_name='description')
    '''A brief description of the user settings.'''



class WarehouseTable(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('table_id', 'full_table_id', 'warehouse', 'discovered_time', 'friendly_name', 'location', 'project_name', 'dataset', 'description', 'table_type', 'is_encrypted', 'created_time', 'last_modified', 'view_query', 'labels', 'path', 'priority', 'tracked', 'status', 'freshness_anomaly', 'size_anomaly', 'freshness_size_anomaly', 'metric_anomaly', 'dynamic_table', 'is_deleted', 'deleted_at', 'last_observed', 'is_excluded', 'data_provider', 'mcon', 'anomalies', 'tags', 'versions', 'events', 'monitors', 'dbt_nodes', 'dbt_run_steps', 'fivetranconnectormodel_set', 'usage_stats', 'thresholds', 'get_thresholds', 'schema_change_count', 'status_scalar', 'node_id', 'is_partial_date_range', 'last_updates', 'last_updates_v2', 'total_row_counts', 'total_byte_counts', 'write_throughput', 'objects_deleted', 'maintenance_windows', 'check_table_metrics_existence', 'is_muted', 'muted_event_types', 'table_stats', 'object_properties', 'is_transitioning_data_provider', 'table_capabilities', 'partition_keys')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')

    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')

    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')

    discovered_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='discoveredTime')

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')

    location = sgqlc.types.Field(String, graphql_name='location')

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    dataset = sgqlc.types.Field(String, graphql_name='dataset')

    description = sgqlc.types.Field(String, graphql_name='description')
    '''(Deprecated) Use `description` from `CatalogObjectMetadataModel`'''

    table_type = sgqlc.types.Field(String, graphql_name='tableType')

    is_encrypted = sgqlc.types.Field(Boolean, graphql_name='isEncrypted')

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')

    last_modified = sgqlc.types.Field(DateTime, graphql_name='lastModified')

    view_query = sgqlc.types.Field(String, graphql_name='viewQuery')

    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')

    path = sgqlc.types.Field(String, graphql_name='path')

    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')

    tracked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tracked')

    status = sgqlc.types.Field(WarehouseTableModelStatus, graphql_name='status')

    freshness_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='freshnessAnomaly')

    size_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sizeAnomaly')

    freshness_size_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='freshnessSizeAnomaly')

    metric_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='metricAnomaly')

    dynamic_table = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dynamicTable')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    deleted_at = sgqlc.types.Field(DateTime, graphql_name='deletedAt')

    last_observed = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastObserved')

    is_excluded = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExcluded')

    data_provider = sgqlc.types.Field(String, graphql_name='dataProvider')

    mcon = sgqlc.types.Field(String, graphql_name='mcon')
    '''The table's MCON (MC Object Name)'''

    anomalies = sgqlc.types.Field(TableAnomalyConnection, graphql_name='anomalies', args=sgqlc.types.ArgDict((
        ('reasons', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='reasons', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('uuid', sgqlc.types.Arg(UUID, graphql_name='uuid', default=None)),
        ('unique_key', sgqlc.types.Arg(String, graphql_name='uniqueKey', default=None)),
        ('warehouse_uuid', sgqlc.types.Arg(UUID, graphql_name='warehouseUuid', default=None)),
        ('table', sgqlc.types.Arg(ID, graphql_name='table', default=None)),
        ('rule_uuid', sgqlc.types.Arg(UUID, graphql_name='ruleUuid', default=None)),
        ('anomaly_id', sgqlc.types.Arg(String, graphql_name='anomalyId', default=None)),
        ('detected_on', sgqlc.types.Arg(DateTime, graphql_name='detectedOn', default=None)),
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('is_active', sgqlc.types.Arg(Boolean, graphql_name='isActive', default=None)),
        ('is_false_positive', sgqlc.types.Arg(Boolean, graphql_name='isFalsePositive', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    '''Arguments:

    * `reasons` (`[String]`)None
    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `uuid` (`UUID`)None
    * `unique_key` (`String`)None
    * `warehouse_uuid` (`UUID`)None
    * `table` (`ID`)None
    * `rule_uuid` (`UUID`)None
    * `anomaly_id` (`String`)None
    * `detected_on` (`DateTime`)None
    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    * `is_active` (`Boolean`)None
    * `is_false_positive` (`Boolean`)None
    * `reason` (`String`)None
    * `order_by` (`String`): Ordering
    '''

    tags = sgqlc.types.Field(sgqlc.types.non_null(TableTagConnection), graphql_name='tags', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    versions = sgqlc.types.Field(TableSchemaVersionConnection, graphql_name='versions', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('table', sgqlc.types.Arg(ID, graphql_name='table', default=None)),
        ('version_id', sgqlc.types.Arg(String, graphql_name='versionId', default=None)),
        ('timestamp', sgqlc.types.Arg(DateTime, graphql_name='timestamp', default=None)),
        ('order_by', sgqlc.types.Arg(String, graphql_name='orderBy', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `table` (`ID`)None
    * `version_id` (`String`)None
    * `timestamp` (`DateTime`)None
    * `order_by` (`String`): Ordering
    '''

    events = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='events', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    monitors = sgqlc.types.Field(sgqlc.types.non_null(MetricMonitoringConnection), graphql_name='monitors', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('type', sgqlc.types.Arg(String, graphql_name='type', default=None)),
))
    )
    '''Table related to monitor

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    * `type` (`String`)None
    '''

    dbt_nodes = sgqlc.types.Field(sgqlc.types.non_null(DbtNodeConnection), graphql_name='dbtNodes', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated table

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    dbt_run_steps = sgqlc.types.Field(sgqlc.types.non_null(DbtRunStepConnection), graphql_name='dbtRunSteps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Associated table

    Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    fivetranconnectormodel_set = sgqlc.types.Field(sgqlc.types.non_null(FivetranConnectorConnection), graphql_name='fivetranconnectormodelSet', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    '''Arguments:

    * `offset` (`Int`)None
    * `before` (`String`)None
    * `after` (`String`)None
    * `first` (`Int`)None
    * `last` (`Int`)None
    '''

    usage_stats = sgqlc.types.Field(TableUsageStatsData, graphql_name='usageStats')
    '''Section describing various table usage stats'''

    thresholds = sgqlc.types.Field(ThresholdsData, graphql_name='thresholds')
    '''Section describing various anomaly thresholds for the table'''

    get_thresholds = sgqlc.types.Field(ThresholdsData, graphql_name='getThresholds')
    '''Section describing various anomaly thresholds for the table'''

    schema_change_count = sgqlc.types.Field(Int, graphql_name='schemaChangeCount')

    status_scalar = sgqlc.types.Field(Int, graphql_name='statusScalar')

    node_id = sgqlc.types.Field(String, graphql_name='nodeId')

    is_partial_date_range = sgqlc.types.Field(Boolean, graphql_name='isPartialDateRange', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''Arguments:

    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    '''

    last_updates = sgqlc.types.Field(sgqlc.types.list_of(TableUpdateTime), graphql_name='lastUpdates', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''List of table updates

    Arguments:

    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    '''

    last_updates_v2 = sgqlc.types.Field(LastUpdates, graphql_name='lastUpdatesV2', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
))
    )
    '''List of table updates

    Arguments:

    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    '''

    total_row_counts = sgqlc.types.Field(sgqlc.types.list_of(TableTotalRowCount), graphql_name='totalRowCounts', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('eliminate_gaps', sgqlc.types.Arg(Boolean, graphql_name='eliminateGaps', default=None)),
))
    )
    '''List of total row count values for the table

    Arguments:

    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    * `eliminate_gaps` (`Boolean`)None
    '''

    total_byte_counts = sgqlc.types.Field(sgqlc.types.list_of(TableTotalByteCount), graphql_name='totalByteCounts', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(DateTime, graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('eliminate_gaps', sgqlc.types.Arg(Boolean, graphql_name='eliminateGaps', default=None)),
))
    )
    '''List of total byte count values for the table

    Arguments:

    * `start_time` (`DateTime`)None
    * `end_time` (`DateTime`)None
    * `eliminate_gaps` (`Boolean`)None
    '''

    write_throughput = sgqlc.types.Field(sgqlc.types.list_of(TableWriteThroughputInBytes), graphql_name='writeThroughput', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('granularity', sgqlc.types.Arg(String, graphql_name='granularity', default=None)),
))
    )
    '''List of latest write throughput in bytes, at most 10000 data
    points.

    Arguments:

    * `start_time` (`DateTime!`): start time point of the metric.
    * `end_time` (`DateTime`): end time point of the metric, if not
      specified, current timestamp will be used.
    * `granularity` (`String`): Indicates the time interval to
      aggregate the result. By default it is 1h. We support xm(x
      minutes), xh(x hours), xd(x days)
    '''

    objects_deleted = sgqlc.types.Field(sgqlc.types.list_of(TableObjectsDeleted), graphql_name='objectsDeleted', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('granularity', sgqlc.types.Arg(String, graphql_name='granularity', default=None)),
))
    )
    '''List of latest objects deleted events, at most 10000 data points.

    Arguments:

    * `start_time` (`DateTime!`): start time point of the metric.
    * `end_time` (`DateTime`): end time point of the metric, if not
      specified, current timestamp will be used.
    * `granularity` (`String`): Indicates the time interval to
      aggregate the result. By default it is 1h. We support xm(x
      minutes), xh(x hours), xd(x days)
    '''

    maintenance_windows = sgqlc.types.Field(sgqlc.types.list_of(MaintenanceWindow), graphql_name='maintenanceWindows', args=sgqlc.types.ArgDict((
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='endTime', default=None)),
        ('mcon', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='mcon', default=None)),
        ('metric_type', sgqlc.types.Arg(sgqlc.types.non_null(DataMaintenanceMetric), graphql_name='metricType', default=None)),
))
    )
    '''List of windows in which the training is ignored

    Arguments:

    * `start_time` (`DateTime!`): start time point of the metric.
    * `end_time` (`DateTime!`): End time of maintenance period
    * `mcon` (`String!`): MC object identifier
    * `metric_type` (`DataMaintenanceMetric!`)None
    '''

    check_table_metrics_existence = sgqlc.types.Field(sgqlc.types.list_of(TableMetricExistence), graphql_name='checkTableMetricsExistence', args=sgqlc.types.ArgDict((
        ('metric_names', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='metricNames', default=None)),
))
    )
    '''List of metric name and whether they exist or not on a table

    Arguments:

    * `metric_names` (`[String]`): list of metric names to check
      whether they exist or not. If not specified, we will check
      total_byte_count, total_row_count, write_throughput and
      objects_deleted for now.
    '''

    is_muted = sgqlc.types.Field(Boolean, graphql_name='isMuted')
    '''No incidents will be created for this table if muted.'''

    muted_event_types = sgqlc.types.Field(sgqlc.types.list_of(MutedEventType), graphql_name='mutedEventTypes')
    '''Muting is active for the specified event types.'''

    table_stats = sgqlc.types.Field(TableStats, graphql_name='tableStats')
    '''Stats for the table'''

    object_properties = sgqlc.types.Field(sgqlc.types.list_of(ObjectProperty), graphql_name='objectProperties')

    is_transitioning_data_provider = sgqlc.types.Field(Boolean, graphql_name='isTransitioningDataProvider')

    table_capabilities = sgqlc.types.Field(TableCapabilitiesResponse, graphql_name='tableCapabilities')
    '''Capabilities for the table'''

    partition_keys = sgqlc.types.Field(TablePartitionKeys, graphql_name='partitionKeys')
    '''Partition key information'''



class WarehouseTableHealth(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('table_id', 'full_table_id', 'warehouse', 'discovered_time', 'friendly_name', 'location', 'project_name', 'dataset', 'description', 'table_type', 'is_encrypted', 'created_time', 'last_modified', 'view_query', 'labels', 'path', 'priority', 'tracked', 'status', 'freshness_anomaly', 'size_anomaly', 'freshness_size_anomaly', 'metric_anomaly', 'dynamic_table', 'is_deleted', 'deleted_at', 'last_observed', 'is_excluded', 'data_provider', 'mcon', 'is_important', 'importance_score', 'tags', 'categories_with_monitors', 'incidents', 'table_capabilities')
    table_id = sgqlc.types.Field(String, graphql_name='tableId')

    full_table_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullTableId')

    warehouse = sgqlc.types.Field(sgqlc.types.non_null(Warehouse), graphql_name='warehouse')

    discovered_time = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='discoveredTime')

    friendly_name = sgqlc.types.Field(String, graphql_name='friendlyName')

    location = sgqlc.types.Field(String, graphql_name='location')

    project_name = sgqlc.types.Field(String, graphql_name='projectName')

    dataset = sgqlc.types.Field(String, graphql_name='dataset')

    description = sgqlc.types.Field(String, graphql_name='description')
    '''(Deprecated) Use `description` from `CatalogObjectMetadataModel`'''

    table_type = sgqlc.types.Field(String, graphql_name='tableType')

    is_encrypted = sgqlc.types.Field(Boolean, graphql_name='isEncrypted')

    created_time = sgqlc.types.Field(DateTime, graphql_name='createdTime')

    last_modified = sgqlc.types.Field(DateTime, graphql_name='lastModified')

    view_query = sgqlc.types.Field(String, graphql_name='viewQuery')

    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')

    path = sgqlc.types.Field(String, graphql_name='path')

    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')

    tracked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tracked')

    status = sgqlc.types.Field(WarehouseTableModelStatus, graphql_name='status')

    freshness_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='freshnessAnomaly')

    size_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sizeAnomaly')

    freshness_size_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='freshnessSizeAnomaly')

    metric_anomaly = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='metricAnomaly')

    dynamic_table = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dynamicTable')

    is_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeleted')

    deleted_at = sgqlc.types.Field(DateTime, graphql_name='deletedAt')

    last_observed = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='lastObserved')

    is_excluded = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExcluded')

    data_provider = sgqlc.types.Field(String, graphql_name='dataProvider')

    mcon = sgqlc.types.Field(String, graphql_name='mcon')

    is_important = sgqlc.types.Field(Boolean, graphql_name='isImportant')
    '''Indicates if it is a Key Asset'''

    importance_score = sgqlc.types.Field(Float, graphql_name='importanceScore')
    '''Importance score'''

    tags = sgqlc.types.Field(sgqlc.types.list_of(ObjectProperty), graphql_name='tags')
    '''Tags associated with the table'''

    categories_with_monitors = sgqlc.types.Field(sgqlc.types.list_of(IncidentCategory), graphql_name='categoriesWithMonitors')
    '''Categories that have at least one monitor set up'''

    incidents = sgqlc.types.Field(sgqlc.types.list_of(WarehouseTableIncident), graphql_name='incidents', args=sgqlc.types.ArgDict((
        ('limit_per_category', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limitPerCategory', default=None)),
        ('start_time', sgqlc.types.Arg(sgqlc.types.non_null(DateTime), graphql_name='startTime', default=None)),
        ('end_time', sgqlc.types.Arg(DateTime, graphql_name='endTime', default=None)),
        ('include_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='includeFeedback', default=None)),
        ('exclude_feedback', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='excludeFeedback', default=None)),
        ('include_normalized', sgqlc.types.Arg(Boolean, graphql_name='includeNormalized', default=None)),
        ('severities', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='severities', default=None)),
        ('categories', sgqlc.types.Arg(sgqlc.types.list_of(IncidentCategory), graphql_name='categories', default=None)),
))
    )
    '''Incidents associated with the table

    Arguments:

    * `limit_per_category` (`Int!`): Maximum number of incidents per
      category
    * `start_time` (`DateTime!`): Filter incidents newer than this
    * `end_time` (`DateTime`): Filter incidents older than this
    * `include_feedback` (`[String]`): Filter incidents by user
      feedback
    * `exclude_feedback` (`[String]`): Exclude incidents by user
      feedback
    * `include_normalized` (`Boolean`): If false, filter out
      normalized incidents.
    * `severities` (`[String]`): Filter for specific severities
    * `categories` (`[IncidentCategory]`): Include only selected
      incident categories. Or all categories if not specified.
    '''

    table_capabilities = sgqlc.types.Field(TableCapabilitiesResponse, graphql_name='tableCapabilities')
    '''Capabilities for the table'''




########################################################################
# Unions
########################################################################
class RcaData(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (FieldDistRcaResult, DataProfileResult, MetricCorrelationResult, SQLQueryResult)


class UserDefinedMonitor(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (MetricMonitoring, CustomRule)



########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None

