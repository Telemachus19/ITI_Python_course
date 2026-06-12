import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'employees.db')

def init_db():
    """Initializes the database schema if it doesn't already exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL,
            is_manager INTEGER DEFAULT 0,
            managed_department TEXT
        )
    ''')
    conn.commit()
    conn.close()
