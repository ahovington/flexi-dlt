import os

from .config import LoadType, Source

hockey_source = Source(
    name="Hockey",
    database_type="postgres",
    connection_params={
        "database": os.getenv("POSTGRES_DATABASE_NAME"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "username": os.getenv("POSTGRES_USER"),
        "host": os.getenv("POSTGRES_HOST"),
    },
    tables=[
        Source.Table(
            name="players",
            schema="public",
            load_type=LoadType.Full,
            historical_years=2,
            update_ts="update_ts",
            exclude_cols=[
                "first_name",
                "last_name",
                "full_name",
                "email_address",
                "mobile_number",
            ],
        ),
        Source.Table(
            name="registrations",
            schema="public",
            load_type=LoadType.Incremental,
            historical_years=2,
            update_ts="update_ts",
        ),
    ],
)
