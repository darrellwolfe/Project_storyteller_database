import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('data/storytelling.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM character_class_list")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to display data in the message box
def show_data():
    rows = fetch_data()
    message = ""
    for row in rows:
        message += f"ID: {row[0]}, Category: {row[1]}, Class: {row[2]}, Name: {row[3]}\n"
    messagebox.showinfo("Character Class List", message)

# Create the main application window
root = tk.Tk()
root.title("Storyteller Database Application")

# Create a button to fetch and display data
fetch_button = tk.Button(root, text="Fetch Data", command=show_data)
fetch_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
