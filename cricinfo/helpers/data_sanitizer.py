import pandas as pd


def clean_nan_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Remove trailing unnamed columns with all null values.

    ESPN Cricinfo tables often include an extra unnamed column filled with NaN.
    """
    if dataframe.columns[-1].startswith("Unnamed") and dataframe[dataframe.columns[-1]].isna().all():
        return dataframe.iloc[:, :-1]
    return dataframe
