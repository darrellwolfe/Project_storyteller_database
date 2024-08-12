import sqlite3
import pandas as pd

# Function to create and populate tables
def create_and_populate_tables(excel_path):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()

    # Define table schemas and corresponding Excel sheet names
    tables = {
        'Story_Planning_Summary': 'Story_Planning_Summary',
        'Story_Planning_Detailed': 'Story_Planning_Detailed',
        'Story_Structure_Overview': 'Story Structure Overview',
        'Character_Story_Archetype': 'Character_Story_Archetype',
        'Story_Archetype': 'Story_Archetype',
        'Genre_SubGenre': 'Genre_SubGenre'
    }

    for table, sheet_name in tables.items():
        # Drop the table if it exists
        cursor.execute(f'DROP TABLE IF EXISTS {table}')
        
        # Read the Excel sheet into a DataFrame
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # Create table schema based on DataFrame columns
        columns = df.columns
        column_definitions = ', '.join([f'"{col}" TEXT' for col in columns])
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} ({column_definitions})')

        # Insert DataFrame data into the table
        df.to_sql(table, conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    excel_path = 'data/Fantasy_SciFi Novel_Placeholder.xlsm'
    create_and_populate_tables(excel_path)
    print("Tables created and populated successfully.")
