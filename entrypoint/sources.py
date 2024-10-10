import os

from .config import Source

srcPostgresHockey = Source(
    name="Hockey",
    database_type="sql_database",
    connection_params={
        "drivername": "postgresql",
        "database": os.getenv("POSTGRES_DATABASE_NAME"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "username": os.getenv("POSTGRES_USER"),
        "host": os.getenv("POSTGRES_HOST"),
        "port": 5432,
    },
)


srcDuckdb = Source(
    name="DuckDB",
    database_type="duckdb",
    connection_params={},
    generate_secrets=False,
)
