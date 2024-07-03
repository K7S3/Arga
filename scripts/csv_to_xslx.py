"""
This script converts a CSV file to an Excel file.
"""

import pandas as pd


def convert_csv_to_xlsx(csv_file_path: str, xlsx_file_path: str) -> None:
    """
    Converts a CSV file to an Excel file.

    Args:
        csv_file_path (str): The path to the CSV file.
        xlsx_file_path (str): The path to the Excel file.

    Returns:
        None
    """

    # Read the CSV file
    data_csv = pd.read_csv(csv_file_path)

    # Convert the CSV file to an Excel file
    data_csv.to_excel(xlsx_file_path, index=False)


if __name__ == "__main__":
    convert_csv_to_xlsx(
        "../data/predicted/AI Test-1.csv", "../data/predicted/AI Test-1.xlsx"
    )
