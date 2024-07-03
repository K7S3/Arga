import unittest
import pandas as pd


class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("data/raw/AI Test-1.csv", header=None).T
        self.df.columns = ["time", "revenue"]
        self.df["time"] = self.df["time"].str.replace(".1", "")
        self.df["time"] = pd.to_datetime(self.df["time"])
        self.df["revenue"] = pd.to_numeric(self.df["revenue"])
        self.predicted_df = pd.read_csv("data/predicted/AI Test-1.csv")

    def test_df_not_empty(self):
        self.assertNotEqual(self.df.shape[0], 0)

    def test_df_columns(self):
        self.assertEqual(list(self.df.columns), ["time", "revenue"])

    def test_time_column_type(self):
        self.assertEqual(self.df["time"].dtype, "datetime64[ns]")

    def test_revenue_column_type(self):
        self.assertEqual(self.df["revenue"].dtype, "float64")

    def test_no_null_values(self):
        self.assertEqual(self.predicted_df.isnull().sum().sum(), 0)


if __name__ == "__main__":
    unittest.main()
