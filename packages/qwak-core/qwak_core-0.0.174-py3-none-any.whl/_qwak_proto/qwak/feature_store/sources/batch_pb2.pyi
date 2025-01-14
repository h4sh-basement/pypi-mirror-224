"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BatchSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DATE_CREATED_COLUMN_FIELD_NUMBER: builtins.int
    ATHENASOURCE_FIELD_NUMBER: builtins.int
    MONGOSOURCE_FIELD_NUMBER: builtins.int
    CSVSOURCE_FIELD_NUMBER: builtins.int
    SNOWFLAKESOURCE_FIELD_NUMBER: builtins.int
    PARQUETSOURCE_FIELD_NUMBER: builtins.int
    JDBCSOURCE_FIELD_NUMBER: builtins.int
    VERTICASOURCE_FIELD_NUMBER: builtins.int
    BIGQUERYSOURCE_FIELD_NUMBER: builtins.int
    ELASTICSEARCHSOURCE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Source given name (by the user)"""
    description: builtins.str
    """Source description"""
    date_created_column: builtins.str
    """Date column of the database, used slicing the data already processed by the feature store engine"""
    @property
    def athenaSource(self) -> global___AthenaSource: ...
    @property
    def mongoSource(self) -> global___MongoSource: ...
    @property
    def csvSource(self) -> global___CsvSource: ...
    @property
    def snowflakeSource(self) -> global___SnowflakeSource: ...
    @property
    def parquetSource(self) -> global___ParquetSource: ...
    @property
    def jdbcSource(self) -> global___JdbcSource: ...
    @property
    def verticaSource(self) -> global___VerticaSource: ...
    @property
    def bigquerySource(self) -> global___BigquerySource: ...
    @property
    def elasticsearchSource(self) -> global___ElasticsearchSource: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        description: builtins.str = ...,
        date_created_column: builtins.str = ...,
        athenaSource: global___AthenaSource | None = ...,
        mongoSource: global___MongoSource | None = ...,
        csvSource: global___CsvSource | None = ...,
        snowflakeSource: global___SnowflakeSource | None = ...,
        parquetSource: global___ParquetSource | None = ...,
        jdbcSource: global___JdbcSource | None = ...,
        verticaSource: global___VerticaSource | None = ...,
        bigquerySource: global___BigquerySource | None = ...,
        elasticsearchSource: global___ElasticsearchSource | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["athenaSource", b"athenaSource", "bigquerySource", b"bigquerySource", "csvSource", b"csvSource", "elasticsearchSource", b"elasticsearchSource", "jdbcSource", b"jdbcSource", "mongoSource", b"mongoSource", "parquetSource", b"parquetSource", "snowflakeSource", b"snowflakeSource", "type", b"type", "verticaSource", b"verticaSource"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["athenaSource", b"athenaSource", "bigquerySource", b"bigquerySource", "csvSource", b"csvSource", "date_created_column", b"date_created_column", "description", b"description", "elasticsearchSource", b"elasticsearchSource", "jdbcSource", b"jdbcSource", "mongoSource", b"mongoSource", "name", b"name", "parquetSource", b"parquetSource", "snowflakeSource", b"snowflakeSource", "type", b"type", "verticaSource", b"verticaSource"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["athenaSource", "mongoSource", "csvSource", "snowflakeSource", "parquetSource", "jdbcSource", "verticaSource", "bigquerySource", "elasticsearchSource"] | None: ...

global___BatchSource = BatchSource

class FileSystemConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AWS_S3_CONFIGURATION_FIELD_NUMBER: builtins.int
    AWS_S3_ANONYMOUS_FIELD_NUMBER: builtins.int
    AWS_S3_ASSUME_ROLE_CONFIGURATION_FIELD_NUMBER: builtins.int
    @property
    def aws_s3_configuration(self) -> global___AwsS3FileSystemConfiguration: ...
    @property
    def aws_s3_anonymous(self) -> global___AnonymousS3Configuration: ...
    @property
    def aws_s3_assume_role_configuration(self) -> global___AwsS3AssumeRole: ...
    def __init__(
        self,
        *,
        aws_s3_configuration: global___AwsS3FileSystemConfiguration | None = ...,
        aws_s3_anonymous: global___AnonymousS3Configuration | None = ...,
        aws_s3_assume_role_configuration: global___AwsS3AssumeRole | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aws_s3_anonymous", b"aws_s3_anonymous", "aws_s3_assume_role_configuration", b"aws_s3_assume_role_configuration", "aws_s3_configuration", b"aws_s3_configuration", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aws_s3_anonymous", b"aws_s3_anonymous", "aws_s3_assume_role_configuration", b"aws_s3_assume_role_configuration", "aws_s3_configuration", b"aws_s3_configuration", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["aws_s3_configuration", "aws_s3_anonymous", "aws_s3_assume_role_configuration"] | None: ...

global___FileSystemConfiguration = FileSystemConfiguration

class AwsS3AssumeRole(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_ARN_FIELD_NUMBER: builtins.int
    role_arn: builtins.str
    """Role to assume"""
    def __init__(
        self,
        *,
        role_arn: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["role_arn", b"role_arn"]) -> None: ...

global___AwsS3AssumeRole = AwsS3AssumeRole

class AwsS3FileSystemConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCESS_KEY_SECRET_NAME_FIELD_NUMBER: builtins.int
    SECRET_KEY_SECRET_NAME_FIELD_NUMBER: builtins.int
    SESSION_TOKEN_SECRET_NAME_FIELD_NUMBER: builtins.int
    BUCKET_FIELD_NUMBER: builtins.int
    access_key_secret_name: builtins.str
    """AWS s3 access key"""
    secret_key_secret_name: builtins.str
    """AWS s3 secret key"""
    session_token_secret_name: builtins.str
    """AWS s3 session token"""
    bucket: builtins.str
    """AWS s3 bucket"""
    def __init__(
        self,
        *,
        access_key_secret_name: builtins.str = ...,
        secret_key_secret_name: builtins.str = ...,
        session_token_secret_name: builtins.str = ...,
        bucket: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_key_secret_name", b"access_key_secret_name", "bucket", b"bucket", "secret_key_secret_name", b"secret_key_secret_name", "session_token_secret_name", b"session_token_secret_name"]) -> None: ...

global___AwsS3FileSystemConfiguration = AwsS3FileSystemConfiguration

class AnonymousS3Configuration(google.protobuf.message.Message):
    """Anonymous S3 access"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AnonymousS3Configuration = AnonymousS3Configuration

class JdbcSource(google.protobuf.message.Message):
    """Jdbc Batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    USERNAME_SECRET_NAME_FIELD_NUMBER: builtins.int
    PASSWORD_SECRET_NAME_FIELD_NUMBER: builtins.int
    DB_TABLE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    MYSQLSOURCE_FIELD_NUMBER: builtins.int
    POSTGRESQLSOURCE_FIELD_NUMBER: builtins.int
    REDSHIFTSOURCE_FIELD_NUMBER: builtins.int
    url: builtins.str
    """Connection url i.e. some_address:optional_port"""
    username_secret_name: builtins.str
    """Jdbc username secret service secret name"""
    password_secret_name: builtins.str
    """Jdbc password secret service secret name"""
    db_table: builtins.str
    """The database and table i.e. database1.some_table"""
    query: builtins.str
    """Query to run before a casual select runs"""
    @property
    def mysqlSource(self) -> global___MysqlSource: ...
    @property
    def postgresqlSource(self) -> global___PostgresqlSource: ...
    @property
    def redshiftSource(self) -> global___RedshiftSource: ...
    def __init__(
        self,
        *,
        url: builtins.str = ...,
        username_secret_name: builtins.str = ...,
        password_secret_name: builtins.str = ...,
        db_table: builtins.str = ...,
        query: builtins.str = ...,
        mysqlSource: global___MysqlSource | None = ...,
        postgresqlSource: global___PostgresqlSource | None = ...,
        redshiftSource: global___RedshiftSource | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["mysqlSource", b"mysqlSource", "postgresqlSource", b"postgresqlSource", "redshiftSource", b"redshiftSource", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["db_table", b"db_table", "mysqlSource", b"mysqlSource", "password_secret_name", b"password_secret_name", "postgresqlSource", b"postgresqlSource", "query", b"query", "redshiftSource", b"redshiftSource", "type", b"type", "url", b"url", "username_secret_name", b"username_secret_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["mysqlSource", "postgresqlSource", "redshiftSource"] | None: ...

global___JdbcSource = JdbcSource

class MysqlSource(google.protobuf.message.Message):
    """MySQL source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MysqlSource = MysqlSource

class PostgresqlSource(google.protobuf.message.Message):
    """PostgreSQL source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___PostgresqlSource = PostgresqlSource

class RedshiftSource(google.protobuf.message.Message):
    """Redshift batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_USER_FIELD_NUMBER: builtins.int
    IAM_ROLE_ARN_FIELD_NUMBER: builtins.int
    ACCESS_KEY_ID_FIELD_NUMBER: builtins.int
    SECRET_ACCESS_KEY_FIELD_NUMBER: builtins.int
    db_user: builtins.str
    """The user that will connect to the db"""
    iam_role_arn: builtins.str
    """IAM Role ARN to create STS with"""
    access_key_id: builtins.str
    """Aws access key id"""
    secret_access_key: builtins.str
    """Aws secret access key"""
    def __init__(
        self,
        *,
        db_user: builtins.str = ...,
        iam_role_arn: builtins.str = ...,
        access_key_id: builtins.str = ...,
        secret_access_key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_key_id", b"access_key_id", "db_user", b"db_user", "iam_role_arn", b"iam_role_arn", "secret_access_key", b"secret_access_key"]) -> None: ...

global___RedshiftSource = RedshiftSource

class AthenaSource(google.protobuf.message.Message):
    """Athena batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATABASE_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    database: builtins.str
    """Athena DB name"""
    table: builtins.str
    """Athena DB table"""
    def __init__(
        self,
        *,
        database: builtins.str = ...,
        table: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "table", b"table"]) -> None: ...

global___AthenaSource = AthenaSource

class BigquerySource(google.protobuf.message.Message):
    """Bigquery batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREDENTIALS_SECRET_NAME_FIELD_NUMBER: builtins.int
    DATASET_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    PARENT_PROJECT_FIELD_NUMBER: builtins.int
    SQL_FIELD_NUMBER: builtins.int
    VIEWS_ENABLED_FIELD_NUMBER: builtins.int
    MATERIALIZATION_DATASET_FIELD_NUMBER: builtins.int
    MATERIALIZATION_PROJECT_FIELD_NUMBER: builtins.int
    MATERIALIZATION_EXPIRATION_TIME_IN_MINUTES_FIELD_NUMBER: builtins.int
    credentials_secret_name: builtins.str
    """Qwak secret name of the credentials json used to authenticate with big query"""
    dataset: builtins.str
    """dataset [optional] - not needed in case sql flow is given"""
    table: builtins.str
    """table [optional] - not needed in case sql flow is given"""
    project: builtins.str
    """project where the table sits [optional] (defaults to the project of the credentials)"""
    parent_project: builtins.str
    """parent project - project used for billing [optional] (defaults to the project of the credentials)"""
    sql: builtins.str
    """sql [optional] - run an sql on top of the data source, if set:
    views_enabled must be true
    materialization_dataset must be set to a dataset where the GCP user has table creation permission
    """
    views_enabled: builtins.bool
    """views enabled - enable reading views [optional] (default to false)"""
    materialization_dataset: builtins.str
    """materialization params became deprecated due to using big query python client instead of the spark connector for sql flow
    materialization dataset - dataset to materialize views in [optional] (defaults the the dataset of the source)
    """
    materialization_project: builtins.str
    """materialization project - project to materialize views in [optional] (defaults the the project of the source)"""
    materialization_expiration_time_in_minutes: builtins.str
    """materialization expiration time in minutes - for how long to keep the view [optional] defaults to 24h"""
    def __init__(
        self,
        *,
        credentials_secret_name: builtins.str = ...,
        dataset: builtins.str = ...,
        table: builtins.str = ...,
        project: builtins.str = ...,
        parent_project: builtins.str = ...,
        sql: builtins.str = ...,
        views_enabled: builtins.bool = ...,
        materialization_dataset: builtins.str = ...,
        materialization_project: builtins.str = ...,
        materialization_expiration_time_in_minutes: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["credentials_secret_name", b"credentials_secret_name", "dataset", b"dataset", "materialization_dataset", b"materialization_dataset", "materialization_expiration_time_in_minutes", b"materialization_expiration_time_in_minutes", "materialization_project", b"materialization_project", "parent_project", b"parent_project", "project", b"project", "sql", b"sql", "table", b"table", "views_enabled", b"views_enabled"]) -> None: ...

global___BigquerySource = BigquerySource

class CsvSource(google.protobuf.message.Message):
    """Csv batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    QUOTE_CHARACTER_FIELD_NUMBER: builtins.int
    ESCAPE_CHARACTER_FIELD_NUMBER: builtins.int
    FILESYSTEM_CONFIGURATION_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Csv path"""
    quote_character: builtins.str
    """Quote character for csv parsing (defaults to "). meaning string enclosed by "I am some, string" will be read as 1 object even if there are , inside"""
    escape_character: builtins.str
    """Escape character to the quote character (defaults to "). meaning that a preceding " to the quote character i.e "" the quoting will be ignored"""
    @property
    def filesystem_configuration(self) -> global___FileSystemConfiguration:
        """File system configuration"""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        quote_character: builtins.str = ...,
        escape_character: builtins.str = ...,
        filesystem_configuration: global___FileSystemConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filesystem_configuration", b"filesystem_configuration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["escape_character", b"escape_character", "filesystem_configuration", b"filesystem_configuration", "path", b"path", "quote_character", b"quote_character"]) -> None: ...

global___CsvSource = CsvSource

class MongoSource(google.protobuf.message.Message):
    """Mongo batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOSTS_FIELD_NUMBER: builtins.int
    USERNAME_SECRET_NAME_FIELD_NUMBER: builtins.int
    PASSWORD_SECRET_NAME_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    COLLECTION_FIELD_NUMBER: builtins.int
    CONNECTION_PARAMS_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    hosts: builtins.str
    """Mongo host address"""
    username_secret_name: builtins.str
    """Mongo username"""
    password_secret_name: builtins.str
    """Mongo password kubernetes secret name"""
    database: builtins.str
    """Mongo data base name"""
    collection: builtins.str
    """Mongo collection name"""
    connection_params: builtins.str
    """Mongo connection parameters"""
    protocol: builtins.str
    """Mongo protocol, defaults to mongodb"""
    def __init__(
        self,
        *,
        hosts: builtins.str = ...,
        username_secret_name: builtins.str = ...,
        password_secret_name: builtins.str = ...,
        database: builtins.str = ...,
        collection: builtins.str = ...,
        connection_params: builtins.str = ...,
        protocol: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["collection", b"collection", "connection_params", b"connection_params", "database", b"database", "hosts", b"hosts", "password_secret_name", b"password_secret_name", "protocol", b"protocol", "username_secret_name", b"username_secret_name"]) -> None: ...

global___MongoSource = MongoSource

class SnowflakeSource(google.protobuf.message.Message):
    """Snowflake batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    USERNAME_SECRET_NAME_FIELD_NUMBER: builtins.int
    PASSWORD_SECRET_NAME_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    WAREHOUSE_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    host: builtins.str
    """SF host address <account_identifier>.snowflakecomputing.com]"""
    username_secret_name: builtins.str
    """SF username kubernetes secret name"""
    password_secret_name: builtins.str
    """SF password kubernetes secret name"""
    database: builtins.str
    """SF database name"""
    schema: builtins.str
    """SF schema name"""
    warehouse: builtins.str
    """SF warehouse name"""
    table: builtins.str
    """SF table name, can not be set together with query"""
    query: builtins.str
    """SF query, can not be set together with table"""
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        username_secret_name: builtins.str = ...,
        password_secret_name: builtins.str = ...,
        database: builtins.str = ...,
        schema: builtins.str = ...,
        warehouse: builtins.str = ...,
        table: builtins.str = ...,
        query: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "host", b"host", "password_secret_name", b"password_secret_name", "query", b"query", "schema", b"schema", "table", b"table", "username_secret_name", b"username_secret_name", "warehouse", b"warehouse"]) -> None: ...

global___SnowflakeSource = SnowflakeSource

class ParquetSource(google.protobuf.message.Message):
    """Parquet batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    FILESYSTEM_CONFIGURATION_FIELD_NUMBER: builtins.int
    path: builtins.str
    """Path to parquet file"""
    @property
    def filesystem_configuration(self) -> global___FileSystemConfiguration:
        """File system configuration"""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        filesystem_configuration: global___FileSystemConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filesystem_configuration", b"filesystem_configuration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filesystem_configuration", b"filesystem_configuration", "path", b"path"]) -> None: ...

global___ParquetSource = ParquetSource

class VerticaSource(google.protobuf.message.Message):
    """Vertica batch source"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    TABLE_FIELD_NUMBER: builtins.int
    USERNAME_SECRET_NAME_FIELD_NUMBER: builtins.int
    PASSWORD_SECRET_NAME_FIELD_NUMBER: builtins.int
    host: builtins.str
    """Vertica host address, without port"""
    port: builtins.int
    """Vertica port number"""
    database: builtins.str
    """Vertica database name"""
    schema: builtins.str
    """Vertica schema name"""
    table: builtins.str
    """Vertica table name"""
    username_secret_name: builtins.str
    """Vertica username qwak secret name"""
    password_secret_name: builtins.str
    """Vertica password qwak secret name"""
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        port: builtins.int = ...,
        database: builtins.str = ...,
        schema: builtins.str = ...,
        table: builtins.str = ...,
        username_secret_name: builtins.str = ...,
        password_secret_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["database", b"database", "host", b"host", "password_secret_name", b"password_secret_name", "port", b"port", "schema", b"schema", "table", b"table", "username_secret_name", b"username_secret_name"]) -> None: ...

global___VerticaSource = VerticaSource

class ElasticsearchSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODES_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    EXCLUDE_FIELDS_FIELD_NUMBER: builtins.int
    PARSE_DATES_FIELD_NUMBER: builtins.int
    USERNAME_SECRET_NAME_FIELD_NUMBER: builtins.int
    PASSWORD_SECRET_NAME_FIELD_NUMBER: builtins.int
    nodes: builtins.str
    """List of node addresses, port can be specified per node here e.g. 1.1.1.1:9200 - takes precedence over `port`"""
    port: builtins.int
    """Port"""
    resource: builtins.str
    """Resource to query for, i.e. index name"""
    query: builtins.str
    """Elasticsearch query to run on top of the data source"""
    exclude_fields: builtins.str
    """List of fields to exclude"""
    parse_dates: builtins.bool
    """Flag determining if date fields should be parsed as dates [defaults to True]"""
    username_secret_name: builtins.str
    """Elasticsearch username qwak secret name"""
    password_secret_name: builtins.str
    """Elasticsearch password qwak secret name"""
    def __init__(
        self,
        *,
        nodes: builtins.str = ...,
        port: builtins.int = ...,
        resource: builtins.str = ...,
        query: builtins.str = ...,
        exclude_fields: builtins.str = ...,
        parse_dates: builtins.bool = ...,
        username_secret_name: builtins.str = ...,
        password_secret_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exclude_fields", b"exclude_fields", "nodes", b"nodes", "parse_dates", b"parse_dates", "password_secret_name", b"password_secret_name", "port", b"port", "query", b"query", "resource", b"resource", "username_secret_name", b"username_secret_name"]) -> None: ...

global___ElasticsearchSource = ElasticsearchSource
