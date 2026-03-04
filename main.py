from core.process_monitor import monitor_processes_changes
from database.db import initialize_database
from core.network_monitor import monitor_network

if __name__ == "__main__":
    initialize_database()
   #monitor_processes_changes()

    monitor_network()