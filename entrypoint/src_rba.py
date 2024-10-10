import duckdb

from .config import LoadType, Table

conn = duckdb.connect("./src_duckdb.duckdb")

conn.sql(
    """
    CREATE OR REPLACE TABLE housing_lending_rates as (
        SELECT *
        FROM read_csv(
            'https://www.rba.gov.au/statistics/tables/csv/f6-data.csv',
            header = True,
            SKIP = 10
        )
    )
    """
)

conn.sql(
    """
    CREATE OR REPLACE TABLE business_lending_rates as (
        SELECT *
        FROM read_csv(
            'https://www.rba.gov.au/statistics/tables/csv/f7-data.csv',
            header = True,
            SKIP = 10
        )
    )
    """
)


tablesRBA = [
    Table(
        name="housing_lending_rates",
        schema="main",
        load_type=LoadType.Full,
        historical_years=100,  # not required for rba data
    ),
    Table(
        name="business_lending_rates",
        schema="main",
        load_type=LoadType.Full,
        historical_years=100,  # not required for rba data
    ),
]
