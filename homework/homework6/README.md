## Data Cleaning Strategy

Applied a systematic cleaning process

1. **Fill Missing Values**
   - Used the `fill_missing_median` function to replace misiing values with the median of each numeric column.

2. **Drop Missing Values**
   - Used the `drop_missing` function:
     - Dropped rows with missing values in specific columns.
     - Dropped rows exceeding a missing-value threshold.
     - By default, dropped any row with at least one missing value.

3. **Normalization**
   - Used the `normalize_data` function:
     - Default method: Min-Max scaling to [0,1].
     - Alternative method: Standard scaling.
