import logging
from pathlib import Path

import dlt
import duckdb
from dlt.common import pendulum
from dlt.sources.sql_database import sql_table

from .config import Destination, LoadType, Source, Table


def extract_load(source: Source, destination: Destination, tables: list[Table]) -> None:
    """Extract and load data from source to destination.

    Args:
        source (Source): The config for the source database.
        destination (Destination): The config for the destination database.
        tables (list[Table]): A list of tables to load from the source to the destination.
    """
    logging.info("Starting extract load")
    # Credentials for the source and target database.
    source.create_secrets()
    destination.create_secrets()
    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name=destination.name,
        destination=destination.database_type,
        dataset_name=destination.schema,
        progress="log",
    )

    incremental_load = []
    full_load = []
    for table in tables:
        if source.database_type.lower() == "duckdb":
            conn = duckdb.connect(Path("./src_duckdb.duckdb"))
            pipeline.run(
                conn.sql(f"""select * from {table.name}""").df(),
                table_name=table.name,
            )
            continue
        if table.load_type == LoadType.Incremental:
            start_date = pendulum.now().subtract(years=table.historical_years)
            end_date = pendulum.now()
            incremental_load += [
                sql_table(
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
                    table=table.name,
                    chunk_size=10,
                    reflection_level="full_with_precision",
                    defer_table_reflect=True,
                    included_columns=table.include_cols,
                )
            ]
    full_load = incremental_load + full_load
    if full_load:
        # The merge write disposition merges existing rows in the destination by primary key
        info = pipeline.run(full_load, write_disposition="merge")
        print(info)
