from cricinfo.helpers.data_sanitizer import clean_nan_column
import pandas as pd
import numpy as np


class TestCleanNanColumn:

    def test_removes_unnamed_nan_column(self):
        df = pd.DataFrame({"number": [1, 2, 3]})
        df["Unnamed"] = np.nan
        cleaned = clean_nan_column(df)
        assert cleaned is not None
        assert list(cleaned.columns) == ["number"]

    def test_preserves_dataframe_without_unnamed_column(self):
        df = pd.DataFrame({"number": [1, 2, 3], "name": ["a", "b", "c"]})
        cleaned = clean_nan_column(df)
        assert list(cleaned.columns) == ["number", "name"]
