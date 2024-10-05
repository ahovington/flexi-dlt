# Flexi Data Load Tool

## Overview

This project is designed to extract data from various sources and load it into a designated target system. The primary goal is to streamline the data integration process, ensuring that data is readily available for analysis and reporting.

## Features

- **Source**: Extract data from multiple source databases (Postgres, MySQL).
- **Target**: Load data into multiple destination databases (Snowflake, BigQuery, DeltaLake).
- **Configuration**: Easy source table configuration with support to exclude columns, select a start date and load incrementally.

## Requirements

- Python 3.11 or higher
- Required libraries (listed in `requirements.txt`)

## Installation

1. Install the dependencies using uv:

```bash
uv install
```

2. Configure your data sources.
- Create a new file per source in the entrypoint. Prefix the source with `src_`
- Import the `Source` dataclass from the config.
- Add the source database configurations.
- Add the source table configurations.
- Import the new source into  `__main__`
- Create a new `Destination` in the `__main__` file using the `Destination` dataclass from the config.
- Generate the secrets for both the destination and the source.
- Add the new source and destination to a new `extract_load` function.

Usage
To run the data extraction and loading process, use the following command:

```bash
uv run -m entrypoint
```

License
This project is licensed under the MIT License. See the LICENSE file for details.
