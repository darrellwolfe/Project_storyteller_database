import PySimpleGUI as sg
import sqlite3

# Function to fetch data from the database
def fetch_data(table):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to add a new entry to the selected table
def add_entry(table, values):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    if table == "character_class_list":
        cursor.execute("INSERT INTO character_class_list (character_category, character_class, character_name_this_series, lawful_chaotic_grid, race_species, character_class_description) VALUES (?, ?, ?, ?, ?, ?)", values)
    elif table == "assets":
        cursor.execute("INSERT INTO assets (asset_name, asset_type, asset_description) VALUES (?, ?, ?)", values)
    elif table == "locations":
        cursor.execute("INSERT INTO locations (location_name, location_description, coordinates) VALUES (?, ?, ?)", values)
    conn.commit()
    conn.close()

# Function to update an existing entry in the selected table
def update_entry(table, id, values):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    if table == "character_class_list":
        cursor.execute('''
            UPDATE character_class_list
            SET character_category = ?, character_class = ?, character_name_this_series = ?, lawful_chaotic_grid = ?, race_species = ?, character_class_description = ?
            WHERE id = ?
        ''', values + (id,))
    elif table == "assets":
        cursor.execute('''
            UPDATE assets
            SET asset_name = ?, asset_type = ?, asset_description = ?
            WHERE id = ?
        ''', values + (id,))
    elif table == "locations":
        cursor.execute('''
            UPDATE locations
            SET location_name = ?, location_description = ?, coordinates = ?
            WHERE id = ?
        ''', values + (id,))
    conn.commit()
    conn.close()

# Function to reset specific columns for all rows in the selected table
def reset_columns(table):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    if table == "character_class_list":
        cursor.execute('''
            UPDATE character_class_list
            SET character_name_this_series = 'None', lawful_chaotic_grid = 'None', race_species = 'None'
        ''')
    elif table == "assets":
        cursor.execute('''
            UPDATE assets
            SET asset_name = 'None', asset_type = 'None', asset_description = 'None'
        ''')
    elif table == "locations":
        cursor.execute('''
            UPDATE locations
            SET location_name = 'None', location_description = 'None', coordinates = 'None'
        ''')
    conn.commit()
    conn.close()

# Function to calculate column widths
def calculate_column_widths(data, headers):
    col_widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    return [width + 2 for width in col_widths]  # Add some padding

# Define the table column headers
table_headers = {
    "character_class_list": ["ID", "Category", "Class", "Name", "Lawful/Chaotic", "Race/Species", "Description"],
    "assets": ["ID", "Asset Name", "Asset Type", "Asset Description"],
    "locations": ["ID", "Location Name", "Location Description", "Coordinates"]
}

# Define the window layout
layout = [
    [sg.Text('Storyteller Database Application')],
    [sg.Combo(list(table_headers.keys()), default_value="character_class_list", key='-TABLE_SELECT-', enable_events=True)],
    [sg.Button('Refresh'), sg.Button('Add Entry'), sg.Button('Select Row for Editing'), sg.Button('Update Selected Row'), sg.Button('Reset Columns'), sg.Button('Exit')],
    [sg.Text('ID', size=(15, 1)), sg.InputText(key='-ID-', readonly=True)],
    [sg.Text('Field 1', size=(15, 1)), sg.InputText(key='-FIELD1-')],
    [sg.Text('Field 2', size=(15, 1)), sg.InputText(key='-FIELD2-')],
    [sg.Text('Field 3', size=(15, 1)), sg.InputText(key='-FIELD3-')],
    [sg.Text('Field 4', size=(15, 1)), sg.InputText(key='-FIELD4-', visible=False)],
    [sg.Text('Field 5', size=(15, 1)), sg.InputText(key='-FIELD5-', visible=False)],
    [sg.Text('Field 6', size=(15, 1)), sg.InputText(key='-FIELD6-', visible=False)]
]

# Create the window
window = sg.Window('Storyteller Database Application', layout, resizable=True, size=(800, 600), finalize=True)

# Function to update the table display based on the selected table
def update_table_display(table):
    data = fetch_data(table)
    headers = table_headers[table]
    column_widths = calculate_column_widths(data, headers)
    table_element = sg.Table(values=data, headings=headers, display_row_numbers=False, auto_size_columns=False, col_widths=column_widths, num_rows=20, key='-TABLE-', vertical_scroll_only=False, justification='left', enable_events=True)
    window.extend_layout(window, [[table_element]])
    window['-TABLE-'].update(values=data)
    for i in range(1, 7):
        window[f'-FIELD{i}-'].update(visible=False)
    for i, header in enumerate(headers[1:], start=1):  # Skip ID column
        window[f'-FIELD{i}-'].update(visible=True)
        window[f'-FIELD{i}-'].update(value='')

# Initial table display update
update_table_display('character_class_list')

# Event loop to process events and get values of inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '-TABLE_SELECT-':
        update_table_display(values['-TABLE_SELECT-'])
    elif event == 'Refresh':
        update_table_display(values['-TABLE_SELECT-'])
    elif event == 'Add Entry':
        table = values['-TABLE_SELECT-']
        entry_values = tuple(values[f'-FIELD{i}-'] for i in range(1, 7) if window[f'-FIELD{i}-'].visible)
        add_entry(table, entry_values)
        sg.popup('Entry Added!', keep_on_top=True)
        update_table_display(table)
    elif event == 'Select Row for Editing':
        selected_rows = values['-TABLE-']
        if selected_rows:
            selected_row = selected_rows[0]
            row_data = fetch_data(values['-TABLE_SELECT-'])[selected_row]
            window['-ID-'].update(row_data[0])
            for i, data in enumerate(row_data[1:], start=1):
                window[f'-FIELD{i}-'].update(data)
    elif event == 'Update Selected Row':
        table = values['-TABLE_SELECT-']
        id = values['-ID-']
        entry_values = tuple(values[f'-FIELD{i}-'] for i in range(1, 7) if window[f'-FIELD{i}-'].visible)
        update_entry(table, id, entry_values)
        sg.popup_no_wait('Entry Updated!', keep_on_top=True)
        update_table_display(table)
    elif event == 'Reset Columns':
        confirm = sg.popup_yes_no("Are you sure you want to reset? All data will be lost!", keep_on_top=True)
        if confirm == 'Yes':
            reset_columns(values['-TABLE_SELECT-'])
            sg.popup_no_wait('Columns Reset!', keep_on_top=True)
            update_table_display(values['-TABLE_SELECT-'])

window.close()
