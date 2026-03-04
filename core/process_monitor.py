import psutil as ps
import time

def get_running_processes():
    processes = []

    for process in ps.process_iter(['pid', 'name', 'cpu_percent','memory_percent']):
        try:
            processes.append(process.info)
        except (ps.NoSuchProcess, ps.AccessDenied):
            pass

    return processes

def monitor_processes():
    while True:
        process_list = get_running_processes()

        print("\nRunning Processes:")
        print("-"*40)
        for proc in process_list[:10]:
            print(
                f"PID: {proc['pid']} | "
                f"Name: {proc['name']} | "
                f"CPU: {proc['cpu_percent']}% | "
                f"Memory: {proc['memory_percent']:.2f}%"
            )

        time.sleep(5)