import pandas as pd


def convert_xlsx_to_csv(xlsx_file_path: str, csv_file_path: str) -> None:
    """
    Converts an Excel file to a CSV file.

    Args:
        xlsx_file_path (str): The path to the Excel file.
        csv_file_path (str): The path to the CSV


    Returns
        None
    """

    # Read the Excel file
    data_xls = pd.read_excel(xlsx_file_path, index_col=None)

    # Convert the Excel file to a CSV file
    data_xls.to_csv(csv_file_path, encoding="utf-8", index=False)


convert_xlsx_to_csv("../data/raw/AI Test-1.xlsx", "../data/raw/AI Test-1.csv")
