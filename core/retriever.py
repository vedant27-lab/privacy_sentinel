import sqlite3

DB = "privacy_sentinel.db"


def get_recent_events(limit=10):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT process_name, risk_level, reason, timestamp
        FROM process_events
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows


def get_high_risk_events(limit=5):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT process_name, risk_level, reason, timestamp
        FROM process_events
        WHERE risk_level IN ('HIGH', 'CRITICAL')
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows