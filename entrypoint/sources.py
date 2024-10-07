import os

from .config import Source

srcPostgresHockey = Source(
    name="Hockey",
    database_type="postgres",
    connection_params={
        "database": os.getenv("POSTGRES_DATABASE_NAME"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "username": os.getenv("POSTGRES_USER"),
        "host": os.getenv("POSTGRES_HOST"),
    },
)
