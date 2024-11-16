import pandas as pd

class DataSanatizer:
    """
    For data sanitization utility methods
    """

    @staticmethod
    def _clean_nan_column(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        The last column of the DataFrame is usually an unamed column with all null values. 
        It should be discared.
        """
        if dataframe.columns[-1].startswith("Unnamed") and dataframe[dataframe.columns[-1]].isna().all():
            return dataframe.iloc[:, :-1]