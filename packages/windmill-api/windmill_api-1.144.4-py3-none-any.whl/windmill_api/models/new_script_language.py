from enum import Enum


class NewScriptLanguage(str, Enum):
    PYTHON3 = "python3"
    DENO = "deno"
    GO = "go"
    BASH = "bash"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    BIGQUERY = "bigquery"
    SNOWFLAKE = "snowflake"
    GRAPHQL = "graphql"
    NATIVETS = "nativets"
    BUN = "bun"

    def __str__(self) -> str:
        return str(self.value)
