import psutil as ps
import time
from database.db import log_process_event
from core.risk_analyzer import calculate_path_risk



def get_process_metadata(pid):
    try:
        proc = ps.Process(pid)
        cpu = proc.cpu_percent(interval=0.1)
        memory = proc.memory_percent()
        exe_path = proc.exe()
        parent = proc.parent().name() if proc.parent() else "N/A"
        username = proc.username()

        return cpu, memory, exe_path, parent, username
    except(ps.NoSuchProcess, ps.AccessDenied):
        return None, None, None, None, None



def get_process_snapshot():
    processes = {}
    for proc in ps.process_iter(['pid', 'name']):
        try:
            processes[proc.info['pid']] = proc.info['name']
        except (ps.NoSuchProcess, ps.AccessDenied):
            pass

    return processes

def monitor_processes_changes():
    previous_snapshot = get_process_snapshot()

    while True:
        time.sleep(5)
        current_snapshot = get_process_snapshot()
        previous_pids = set(previous_snapshot.keys())
        current_pid = set(current_snapshot.keys())

        new_processes = current_pid - previous_pids
        terminated_processes = previous_pids - current_pid

        for pid in new_processes:
            name = current_snapshot[pid]
            print(f"[NEW PROCESS] {name} (PID: {pid})")

            cpu, memory, exe_path, parent, username = get_process_metadata(pid)

            risk = calculate_path_risk(exe_path)

            log_process_event(
                "START",
                name,
                pid,
                cpu,
                memory,
                exe_path,
                parent,
                username
            )
        
        for pid in terminated_processes:
            name = previous_snapshot[pid]
            print(f"[TERMINATED] {name} (PID: {pid})")
            log_process_event("TERMINATED", name, pid, None, None, None, None, None)
        previous_snapshot = current_snapshot