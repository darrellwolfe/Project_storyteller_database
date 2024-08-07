import sqlite3

def create_database(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create character_class_list table
    c.execute('''
    CREATE TABLE IF NOT EXISTS character_class_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_category TEXT,
        character_class TEXT,
        character_name_this_series TEXT,
        lawful_chaotic_grid TEXT,
        race_species TEXT,
        character_class_description TEXT
    )
    ''')

    # Create story_planning_summary table
    c.execute('''
    CREATE TABLE IF NOT EXISTS story_planning_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scenes TEXT,
        avg_words_per_scene INTEGER,
        estimated_word_count INTEGER,
        character_1 TEXT,
        character_2 TEXT,
        character_3 TEXT,
        story_archetypes_1 TEXT,
        story_archetypes_2 TEXT,
        story_archetypes_3 TEXT,
        story_archetypes_4 TEXT,
        story_archetypes_5 TEXT
    )
    ''')

    # Create story_planning_detailed table
    c.execute('''
    CREATE TABLE IF NOT EXISTS story_planning_detailed (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        scene INTEGER,
        percent REAL,
        story_element TEXT,
        character_1 TEXT,
        character_1_abilities TEXT,
        character_2 TEXT,
        character_2_abilities TEXT,
        character_3 TEXT,
        character_3_abilities TEXT,
        story_archetypes_1 TEXT,
        story_archetypes_2 TEXT,
        story_archetypes_3 TEXT,
        story_archetypes_4 TEXT,
        story_archetypes_5 TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database('data/storytelling.db')
