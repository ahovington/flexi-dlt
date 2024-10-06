import os

from .config import Destination, Source
from .pipeline import extract_load
from .src_hockey import hockey_source

CONFIGURED_DESTINATION = "SNOWFLAKE"
CONFIGURED_SOURCE = "HOCKEY"


class MissingEnvironemntVariable(Exception):
    def __str__(envar: str):
        return f"Missing environment variable {envar}"


def dest_snowflake():
    password = os.getenv("SNOWFLAKE_PASSWORD")
    username = os.getenv("SNOWFLAKE_USER")
    if not password:
        raise MissingEnvironemntVariable("SNOWFLAKE_PASSWORD")
    if not username:
        raise MissingEnvironemntVariable("SNOWFLAKE_USER")
    destination = Destination(
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
    destination.create_secrets()
    return destination


destination: dict[str, Destination] = {"SNOWFLAKE": dest_snowflake()}.get(
    CONFIGURED_DESTINATION
)
source: dict[str, Source] = {"HOCKEY": hockey_source}.get(CONFIGURED_SOURCE)

extract_load(dest_snowflake(), source)
