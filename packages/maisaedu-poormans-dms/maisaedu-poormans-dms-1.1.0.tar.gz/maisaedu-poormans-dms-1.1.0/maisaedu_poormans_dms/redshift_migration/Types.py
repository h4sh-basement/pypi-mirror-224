LOCAL = "local"
DEV = "dev"
PROD = "prod"

FULL = "full"
INCREMENTAL = "incremental"

PREFECT_DMS = "prefect-dms"
PREFECT = "prefect"

SAVED_S3 = "saved-s3"
SAVED_REDSHIFT = "saved-redshift"

S3 = "s3"
REDSHIFT = "redshift"

IAM_ROLE = "arn:aws:iam::977647303146:role/service-role/AmazonRedshift-CommandsAccessRole-20220714T104138"

MAX_VARCHAR_LENGTH = 60000

SUPER = "super"
INT = "int"
BIGINT = "bigint"
VARCHAR = "varchar"
TEXT = "text"
TIMESTAMP = "timestamp"
BOOLEAN = "boolean"
STR = "str"
BOOL = "bool"
DATETIME64 = "datetime64[ns]"
DATETIME64_TZ = "datetime64[ns, UTC]"
NUMERIC = "numeric"
FLOAT = "float"
DOUBLE = "double"
TIMESTAMPTZ = "timestamptz"
JSON = "json"
JSONB = "jsonb"
UUID = "uuid"


def target_type_is_numeric(target_type):
    if (
        target_type == INT
        or target_type == BIGINT
        or target_type == NUMERIC
        or target_type == FLOAT
        or target_type == DOUBLE
    ):
        return True
    else:
        return False


def check_if_env_is_valid(env):
    if env not in [LOCAL, DEV, PROD]:
        raise ValueError("env must be 'local', 'dev' or 'prod'")


def check_if_option_is_valid(option):
    if option not in [FULL, INCREMENTAL, None]:
        raise ValueError("option must be 'full' or 'incremental'")
