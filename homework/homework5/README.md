Data Storage
  Folders
    data/raw/: stores original CSV outputs
    data/processed/: stores Parquet outputs

  Environment Variables
    DATA_DIR_RAW: where CSV files are written/read
    DATA_DIR_PROCESSED: where Parquet files are written/read

  Formats
    CSV: text-based, easy to share
    Parquet: binary, preserves dtypes efficiently

Validation Summary
  Checks performed on reload
    shape_equal: dataframe shape matches original
    date_is_datetime: date column parsed as datetime
    price_is_numeric: price column loaded as numeric

  Assumptions
    CSV date column parsed with parse_dates=['date'] if present
    Parquet requires pyarrow or fastparquet
    Parent directories auto-created, clear error raised if parquet engine missing
