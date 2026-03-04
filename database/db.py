import sqlite3

DB_NAME = "privacy_sentinel.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS process_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            event_type TEXT,
            process_name TEXT,
            pid INTEGER,
            cpu_percent REAL,
            memory_percent REAL,
            exe_path TEXT,
            parent_process TEXT,
            username TEXT
        )
    """)

    conn.commit()
    conn.close()