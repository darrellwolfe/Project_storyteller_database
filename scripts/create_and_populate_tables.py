import sqlite3
import pandas as pd

# Function to create and populate tables
def create_and_populate_tables(excel_path):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()

    # Load the workbook to get sheet names
    xls = pd.ExcelFile(excel_path)
    
    # Iterate through each sheet in the workbook
    for sheet_name in xls.sheet_names:
        # Drop the table if it exists
        cursor.execute(f'DROP TABLE IF EXISTS "{sheet_name}"')
        
        # Read the sheet into a DataFrame
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # Create table schema based on DataFrame columns
        columns = df.columns
        column_definitions = ', '.join([f'"{col}" TEXT' for col in columns])
        cursor.execute(f'CREATE TABLE IF NOT EXISTS "{sheet_name}" ({column_definitions})')

        # Insert DataFrame data into the table
        df.to_sql(sheet_name, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    excel_path = 'data/StorytellerDatabase_Tables.xlsm'  # Updated path to the new workbook
    create_and_populate_tables(excel_path)
    print("Tables created and populated successfully.")
