import logging

import dlt
from dlt.common import pendulum
from dlt.sources.credentials import ConnectionStringCredentials
from dlt.sources.sql_database import sql_table

from .config import Destination, LoadType, Source


def extract_load(destination: Destination, source: Source) -> None:
    """Extract and load data from source to destination.

    Args:
        destination (Destination): The config for the destination database.
        source (Source): The config for the source database with table configs.
    """
    logging.info("Starting extract load")
    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name=destination.name,
        destination=destination.database_type,
        dataset_name=destination.schema,
        progress="log",
    )

    # Credentials for the source database.
    credentials = ConnectionStringCredentials(source.db_url)

    incremental_load = []
    full_load = []
    for table in source.tables:
        if table.load_type == LoadType.Incremental:
            start_date = pendulum.now().subtract(years=table.historical_years)
            end_date = pendulum.now()
            incremental_load += [
                sql_table(
                    credentials=credentials,
                    table=table.name,
                    incremental=dlt.sources.incremental(
                        table.update_ts,
                        initial_value=start_date,
                        end_value=end_date,
                        row_order="desc",
                    ),
                    chunk_size=10,
                    reflection_level="full_with_precision",
                    defer_table_reflect=True,
                    included_columns=table.include_cols,
                )
            ]
        if table.load_type == LoadType.Full:
            full_load += [
                sql_table(
                    credentials=credentials,
                    table=table.name,
                    chunk_size=10,
                    reflection_level="full_with_precision",
                    defer_table_reflect=True,
                    included_columns=table.include_cols,
                )
            ]
    # The merge write disposition merges existing rows in the destination by primary key
    info = pipeline.run(incremental_load + full_load, write_disposition="merge")
    print(info)
