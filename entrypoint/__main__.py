import os

from .config import Destination
from .pipeline import extract_load
from .src_hockey import hockey_source

destination = Destination(
    name="SnowflakeLoader",
    database_type="snowflake",
    connection_params={
        "host": os.getenv("SNOWFLAKE_HOST"),
        "database": "WEST_HOCKEY",
        "schema": "RAW",
        "warehouse": "LOAD",
        "role": "LOADER",
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "username": os.getenv("SNOWFLAKE_USER"),
    },
    schema="RAW",
)

destination.create_secrets()

extract_load(destination, hockey_source)
