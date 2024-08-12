import pandas as pd

# Function to check sheet names in the Excel file
def check_sheet_names(excel_path):
    xls = pd.ExcelFile(excel_path)
    print("Available sheet names:", xls.sheet_names)

if __name__ == "__main__":
    excel_path = 'data/StorytellerDatabase_Tables.xlsm'
    check_sheet_names(excel_path)
