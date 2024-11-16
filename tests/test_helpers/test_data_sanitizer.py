from cricinfo.helpers.data_sanitizer import DataSanatizer
import pandas as pd
import numpy as np

class TestDataSanitizer:

    def test_clean_nan_column(self):
        df = pd.DataFrame({'number': [1,2,3]})
        df["Unnamed"] = np.nan #create a column with NaN data to mimic cricinfo DF
        cleaned_df = DataSanatizer._clean_nan_column(df)
        assert cleaned_df is not None
        assert not cleaned_df[cleaned_df.columns[-1]].isna().all()