import os
from pathlib import Path

import dlt
import duckdb

from .config import Destination
from .errors import MissingEnvironemntVariable


def dest_snowflake():
    password = os.getenv("SNOWFLAKE_PASSWORD")
    username = os.getenv("SNOWFLAKE_USER")
    if not password:
        raise MissingEnvironemntVariable("SNOWFLAKE_PASSWORD")
    if not username:
        raise MissingEnvironemntVariable("SNOWFLAKE_USER")
    return Destination(
        name="SnowflakeLoader",
        database_type="snowflake",
        connection_params={
            "host": os.getenv("SNOWFLAKE_HOST"),
            "database": "WEST_HOCKEY",
            "schema": "RAW",
            "warehouse": "LOAD",
            "role": "LOADER",
            "password": password,
            "username": username,
        },
        schema="RAW",
    )


def dest_duckdb():
    return Destination(
        name="DuckDB",
        database_type=dlt.destinations.duckdb(
            duckdb.connect(Path("./dest_duckdb.duckdb"))
        ),
        connection_params={},
        schema="main",
        generate_secrets=False,
    )
