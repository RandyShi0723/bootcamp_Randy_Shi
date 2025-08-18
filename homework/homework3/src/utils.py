import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return numeric summary stats, transposed for readability."""
    return df.describe().T

def pick_category_column(df: pd.DataFrame) -> str:
    """Pick a likely categorical column name."""
    candidates = ['category', 'Category', 'cat', 'group', 'Group']
    for c in candidates:
        if c in df.columns:
            return c
    obj_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(obj_cols) > 0:
        return obj_cols[0]
    return df.columns[0]