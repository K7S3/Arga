"""
This module contains unit tests for data preprocessing steps in the project.
It tests the loading, cleaning, and transformation of data. This includes steps
both before and after prediction.
"""
import unittest
import sys
import pandas as pd

sys.path.insert(0, '.')


class TestDataPreprocessing(unittest.TestCase):
    """
    Test the data preprocessing steps.
    """

    def setUp(self):
        self.df = pd.read_csv("./data/raw/AI Test-1.csv", header=None).T
        self.df.columns = ["time", "revenue"]
        self.df["time"] = self.df["time"].str.replace(".1", "")
        self.df["time"] = pd.to_datetime(self.df["time"])
        self.df["revenue"] = pd.to_numeric(self.df["revenue"])
        self.predicted_df = pd.read_csv("./data/predicted/AI Test-1.csv")

    def test_df_not_empty(self):
        """
        Test if the DataFrame is not empty.
        """
        self.assertNotEqual(self.df.shape[0], 0)

    def test_df_columns(self):
        """
        Test if the DataFrame has the correct columns.
        """
        self.assertEqual(list(self.df.columns), ["time", "revenue"])

    def test_time_column_type(self):
        """
        Test if the time column is of type datetime64.
        """
        self.assertEqual(self.df["time"].dtype, "datetime64[ns]")

    def test_revenue_column_type(self):
        """
        Test if the revenue column is of type float64.
        """
        self.assertEqual(self.df["revenue"].dtype, "float64")

    def test_no_null_values(self):
        """ "
        Test if there are no null values in the DataFrame.
        """
        self.assertEqual(self.predicted_df.isnull().sum().sum(), 0)


if __name__ == "__main__":
    unittest.main()
