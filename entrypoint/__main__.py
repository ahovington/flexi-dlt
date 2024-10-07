import os

from .config import Destination, Source, Table
from .destinations import dest_duckdb, dest_snowflake
from .pipeline import extract_load
from .sources import srcPostgresHockey
from .src_hockey import tablesHockey

CONFIGURED_DESTINATION = "DUCKDB"
CONFIGURED_SOURCE = "HOCKEY"
CONFIGURED_TABLES = "HOCKEY"


source: dict[str, Source] = {"POSTGRES": srcPostgresHockey}[
    os.getenv("SOURCE_DATABASE")
]
destination: dict[str, Destination] = {
    "SNOWFLAKE": dest_snowflake(),
    "DUCKDB": dest_duckdb(),
}[os.getenv("TARGET_DATABASE")]
tables: list[Table] = {"HOCKEY": tablesHockey}[os.getenv("TABLES")]

extract_load(destination, source, tables)
