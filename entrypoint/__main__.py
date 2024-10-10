import os

from .config import Destination, Source, Table
from .destinations import dest_duckdb, dest_snowflake
from .pipeline import extract_load
from .sources import srcDuckdb, srcPostgresHockey
from .src_hockey import tablesHockey
from .src_rba import tablesRBA

SOURCE: dict[str, Source] = {"POSTGRES": srcPostgresHockey, "DUCKDB": srcDuckdb}[
    os.getenv("SOURCE_DATABASE")
]
DESTINATION: dict[str, Destination] = {
    "SNOWFLAKE": dest_snowflake(),
    "DUCKDB": dest_duckdb(),
}[os.getenv("TARGET_DATABASE")]
TABLES: list[Table] = {"HOCKEY": tablesHockey, "RBA": tablesRBA}[os.getenv("TABLES")]

extract_load(SOURCE, DESTINATION, TABLES)
