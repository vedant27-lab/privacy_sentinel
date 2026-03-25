import sqlite3
import pandas as pd

DB_NAME = "privacy_sentinel.db"

def load_data():
    conn = sqlite3.connect(DB_NAME)
    query = """
    SELECT
        cpu_percent,
        exe_path,
        risk_level,
        timestamp
    FROM process_events
    WHERE event_type LIKE 'SCREEN%
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    return df

def preprocess(df):

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hour"] = df["timestamp"].dt.hour

    def path_risk(path):
        if path is None:
            return 1
        
        path = path.lower()

        if "program files" in path:
            return 0
        elif "temp" in path or "downloads" in path:
            return 2
        else:
            return 1
        
    df["path_risk"] = df["exe_path"].apply(path_risk)

    risk_map = {
        "LOW": 0,
        "MEDIUM": 1,
        "HIGH": 2,
        "CRITICAL": 3
    }

    df["risk_num"] = df["exe_path"].map(risk_map).fillna(0)

    return df

def get_features():
    df = load_data()
    df = preprocess(df)

    features = df[[
        "cpu_percent",
        "hour",
        "path_risk"
    ]]

    return features