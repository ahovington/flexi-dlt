from .config import LoadType, Table

tablesHockey = [
    Table(
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
    Table(
        name="registrations",
        schema="public",
        load_type=LoadType.Incremental,
        historical_years=2,
        update_ts="update_ts",
    ),
]
