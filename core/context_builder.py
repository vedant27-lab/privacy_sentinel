import psutil
import os
from network_monitor import get_connections_by_process_name

def build_context(process_name, pid, mic=False, cam=False, screen=False):
    cpu = None
    exe_path = None
    connections = []

    try: 
        proc = psutil.Process(pid)
        cpu = proc.cpu_percent(interval=0.1)
        exe_path = proc.exe()

        connections = get_connections_by_process_name(process_name)

    except:
        pass

    return {
        "process_name": process_name,
        "pid": pid,
        "cpu": cpu,
        "exe_path": exe_path,
        "network": len(connections),
        "connections": connections,
        "mic": mic,
        "cam": cam,
        "screen": screen
    }
