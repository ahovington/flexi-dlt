from .config import Destination, Source, Table
from .destinations import dest_duckdb, dest_snowflake
from .pipeline import extract_load
from .sources import srcPostgresHockey
from .src_hockey import tablesHockey

CONFIGURED_DESTINATION = "DUCKDB"
CONFIGURED_SOURCE = "HOCKEY"
CONFIGURED_TABLES = "HOCKEY"


destination: dict[str, Destination] = {
    "SNOWFLAKE": dest_snowflake(),
    "DUCKDB": dest_duckdb(),
}.get(CONFIGURED_DESTINATION)
source: dict[str, Source] = {"HOCKEY": srcPostgresHockey}.get(CONFIGURED_SOURCE)
tables: list[Table] = {"HOCKEY": tablesHockey}.get(CONFIGURED_TABLES)

extract_load(destination, source, tables)
