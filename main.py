from core.process_monitor import monitor_processes_changes
from database.db import initialize_database

if __name__ == "__main__":
    initialize_database()
    monitor_processes_changes()