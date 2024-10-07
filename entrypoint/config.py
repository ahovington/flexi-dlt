from __future__ import annotations

import os
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(".env"))

SECRETS_PATH = Path(".dlt") / "secrets.toml"
if SECRETS_PATH.exists():
    # Flush secrets if they exists
    os.remove(SECRETS_PATH)


class LoadType(StrEnum):
    Full = "Full Load"
    Incremental = "Incremental"


def _create_secrets(
    secret_type: str, database_type: str, connection_params: dict[str, str]
) -> None:
    """Create the secrets toml file for the source and destination databases.

    Args:
        secret_type (str): The type of the secret, either sources or destination.
        database_type (str): The type of the database, example mysql, Bigquery.
        connection_params (dict[str, str]): A dictionary of the connection parameters.
    """
    SECRETS_PATH.parent.mkdir(parents=True, exist_ok=True)
    secrets = [f"[{secret_type}.{database_type}.credentials]\n"]
    for key, secret in connection_params.items():
        if key != "port":
            secrets += [f'{key} = "{secret}"\n']
            continue
        secrets += [f"{key} = {secret}\n"]
    secrets += [""]
    open_mode = "w"
    if SECRETS_PATH.exists():
        open_mode = "a"
    with SECRETS_PATH.open(open_mode, encoding="utf-8") as f:
        f.writelines(secrets)


@dataclass
class Source:
    name: str
    database_type: str
    connection_params: dict[str, str]
    generate_secrets: bool = True

    def create_secrets(self):
        if not self.generate_secrets:
            return
        _create_secrets(
            "sources",
            self.database_type,
            self.connection_params,
        )


@dataclass
class Destination:
    name: str
    database_type: str
    connection_params: dict[str, str]
    schema: str
    table_prefix: str = "src_"
    generate_secrets: bool = True

    def create_secrets(self):
        if not self.generate_secrets:
            return
        _create_secrets(
            "destination",
            self.database_type,
            self.connection_params,
        )


@dataclass
class Table:
    name: str
    schema: str
    load_type: LoadType
    historical_years: int
    update_ts: str | None = None
    include_cols: list[str] | None = None
    exclude_cols: list[str] | None = None
