import sqlite3

def create_tables():
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    
    # Create character_class_list table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS character_class_list (
            id INTEGER PRIMARY KEY,
            character_category TEXT,
            character_class TEXT,
            character_name_this_series TEXT,
            lawful_chaotic_grid TEXT,
            race_species TEXT,
            character_class_description TEXT
        )
    ''')
    
    # Create assets table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY,
            asset_name TEXT,
            asset_type TEXT,
            asset_description TEXT
        )
    ''')
    
    # Create locations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            location_name TEXT,
            location_description TEXT,
            coordinates TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")
