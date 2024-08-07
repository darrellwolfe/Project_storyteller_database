import pandas as pd
import sqlite3

def populate_character_class_list(db_path, df):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    for index, row in df.iterrows():
        c.execute('''
            INSERT INTO character_class_list (
                character_category,
                character_class,
                character_name_this_series,
                lawful_chaotic_grid,
                race_species,
                character_class_description
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            row['Character_Category'],
            row['Character_Class'],
            row['Character_Name_ThisSeries'],
            row['Lawful/Chaotic Grid'],
            row['Race/Species'],
            row['Character_Class_Description']
        ))
    
    conn.commit()
    conn.close()

def main():
    # Load the Excel file
    file_path = 'path/to/your/excel/file.xlsm'
    xls = pd.ExcelFile(file_path)

    # Load the 'Character Class List' sheet to inspect its content
    character_class_list_df = pd.read_excel(xls, sheet_name='Character Class List')

    # Populate character_class_list table
    populate_character_class_list('data/storytelling.db', character_class_list_df)

if __name__ == "__main__":
    main()
