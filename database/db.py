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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS network_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        process_name TEXT,
        pid INTEGER,
        remote_ip TEXT,
        remote_port INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS device_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        device_type TEXT,
        process_name TEXT,
        pid INTEGER
    )
    """)



    conn.commit()
    conn.close()

def log_network_event(process_name, pid, ip, port):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO network_events
        (process_name, pid, remote_ip, remote_port)
        VALUES (?, ?, ?, ?)
    """, (process_name, pid, ip, port))

    conn.commit()
    conn.close()

def log_process_event(event_type, process_name, pid, cpu, memory, exe_path, parent, username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO process_events
        (event_type, process_name, pid, cpu_percent, memory_percent, exe_path, parent_process, username)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (event_type, process_name, pid, cpu, memory, exe_path, parent, username))

    conn.commit()
    conn.close()

def log_device_event(device_type, process_name, pid):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO device_events
        (device_type, process_name, pid)
        VALUES (?, ?, ?)
    """, (device_type, process_name, pid))

    conn.commit()
    conn.close()