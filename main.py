from core.process_monitor import monitor_processes_changes
from database.db import initialize_database
from core.network_monitor import monitor_network
from core.device_monitor import monitor_devices

if __name__ == "__main__":
    initialize_database()
   #monitor_processes_changes()

    #monitor_network()
    monitor_devices()