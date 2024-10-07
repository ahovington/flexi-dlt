# Flexi Data Load Tool

## Overview

This project uses the open source [dlt](https://dlthub.com/docs/intro) tools to extract data from various sources and load it into a target system. The primary goal is to streamline the data integration process, ensuring that data is readily available for analysis and reporting.

## Features

**Sources**, **Destinations** and **Tables** are all defined separately, this provides flexibilty in how the extract load pipe line is constructed.

For instance, this flexiblity allows you to:
- Load tables from one source to multiple destinations.
- Load tables from multiple sources to one destination.

Sources and Destinations currently used:
- Sources: Postgres
- Destinations: Snowflake, DuckDB. Coming BigQuery, DeltaLake.

Table extract load features:
- Exclude columns.
- Set a start date for extraction.
- Load data incrementally.

## Requirements

- Python 3.11 or higher
- Required libraries listed in `pyproject.toml`

## Installation

1. Install the dependencies using uv:

```bash
make requirements-test
```

Usage
To run the data extraction and loading process, use the following command:

```bash
make run
```

License
This project is licensed under the MIT License. See the LICENSE file for details.
