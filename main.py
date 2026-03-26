from core.process_monitor import monitor_processes_changes
from core.network_monitor import monitor_network
from core.device_monitor import monitor_devices
from core.screen_monitor import monitor_screen
from database.db import initialize_database
import threading


if __name__ == "__main__":
    initialize_database()

    t1 = threading.Thread(target=monitor_processes_changes)
    t2 = threading.Thread(target=monitor_network)
    t3 = threading.Thread(target=monitor_devices)
    t4 = threading.Thread(target=monitor_screen)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()