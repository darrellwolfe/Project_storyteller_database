-- Run these SQL commands to create tables if they don't exist
CREATE TABLE IF NOT EXISTS character_class_list (
    id INTEGER PRIMARY KEY,
    character_category TEXT,
    character_class TEXT,
    character_name_this_series TEXT,
    lawful_chaotic_grid TEXT,
    race_species TEXT,
    character_class_description TEXT
);

CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY,
    asset_name TEXT,
    asset_type TEXT,
    asset_description TEXT
);

CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY,
    location_name TEXT,
    location_description TEXT,
    coordinates TEXT
);
