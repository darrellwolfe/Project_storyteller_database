import PySimpleGUI as sg
import sqlite3

# Function to ensure necessary tables exist
def ensure_tables_exist():
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    
    # Fetch all existing table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = cursor.fetchall()
    tables = [table[0] for table in existing_tables]  # Fetch all existing table names

    for table in tables:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS "{table}" ("id" INTEGER PRIMARY KEY)')
    
    conn.commit()
    conn.close()

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
    columns = fetch_columns(table)
    placeholders = ', '.join(['?'] * len(columns))
    cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})", values)
    conn.commit()
    conn.close()

# Function to update an existing entry in the selected table
def update_entry(table, id, values):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    columns = fetch_columns(table)
    assignments = ', '.join([f'{col} = ?' for col in columns])
    cursor.execute(f'''
        UPDATE {table}
        SET {assignments}
        WHERE id = ?
    ''', values + (id,))
    conn.commit()
    conn.close()

# Function to fetch columns from the table
def fetch_columns(table):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [info[1] for info in cursor.fetchall()]
    conn.close()
    return columns[1:]  # Exclude the id column

# Function to reset specific columns for all rows in the selected table
def reset_columns(table):
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    columns = fetch_columns(table)
    assignments = ', '.join([f'{col} = "None"' for col in columns])
    cursor.execute(f'UPDATE {table} SET {assignments}')
    conn.commit()
    conn.close()

# Function to calculate column widths
def calculate_column_widths(data, headers):
    col_widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
            else:
                # If there are more cells than headers, expand the list
                col_widths.append(len(str(cell)))
    return [width + 2 for width in col_widths]  # Add some padding

# Ensure necessary tables exist
ensure_tables_exist()

# Define the table column headers (fetched dynamically later)
table_headers = {
    'StoryStructure_StoryArchs': [],
    'StoryStructure_CharacterArchs': [],
    'Character_Class_List': [],
    'LitRPG_Definitions_Tropes': [],
    'LitRPG_Progress_Blank': [],
    'LitRPG_Progress_Ex1': [],
    'LitRPG_Progress_Ex2': [],
    'Storyteller_Resources': [],
    'Lawful-Chaotic_Good-Evil_Matrix': []
}

# Function to update table headers dynamically
def update_table_headers():
    for table in table_headers:
        table_headers[table] = fetch_columns(table)

# Define the window layout
layout = [
    [sg.Text('Storyteller Database Application')],
    [sg.Combo(list(table_headers.keys()), default_value="StoryStructure_StoryArchs", key='-TABLE_SELECT-', enable_events=True)],
    [sg.Button('Refresh'), sg.Button('Add Entry'), sg.Button('Select Row for Editing'), sg.Button('Update Selected Row'), sg.Button('Reset Columns'), sg.Button('Exit')],
    [sg.Text('ID', size=(15, 1)), sg.InputText(key='-ID-', readonly=True)]
]

# Create input fields based on the maximum number of columns
max_columns = 20
for i in range(1, max_columns + 1):
    layout.append([sg.Text(f'Field {i}', size=(15, 1), key=f'-LABEL{i}-', visible=False), sg.InputText(key=f'-FIELD{i}-', visible=False)])

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
    for i in range(1, max_columns + 1):
        window[f'-FIELD{i}-'].update(visible=False)
        window[f'-LABEL{i}-'].update(visible=False)
    for i, header in enumerate(headers):
        window[f'-LABEL{i+1}-'].update(value=header, visible=True)
        window[f'-FIELD{i+1}-'].update(visible=True)

# Initial table headers update
update_table_headers()

# Initial table display update
update_table_display('StoryStructure_StoryArchs')  # Update to the correct initial table name

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
        entry_values = tuple(values[f'-FIELD{i}-'] for i in range(1, max_columns + 1) if window[f'-FIELD{i}-'].visible)
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
        entry_values = tuple(values[f'-FIELD{i}-'] for i in range(1, max_columns + 1) if window[f'-FIELD{i}-'].visible)
        update_entry(table, id, entry_values)
        sg.popup_no_wait('Entry Updated!', keep_on_top=True)
        update_table_display(table)
    elif event == 'Reset Columns':
        confirm = sg.popup_yes_no("Are you sure you want to reset? All data will be lost!", keep_on_top=True)
        if confirm == 'Yes':
            reset_columns(values['-TABLE_SELECT-'])
            sg.popup_no_wait('Columns Reset!', keep_on_top=True)
            update_table_display(table)

window.close()
