import psutil
import time
import os
from datetime import datetime

from core.network_monitor import get_connections_by_process_name
from database.db import log_device_event


CPU_THRESHOLD = 10
CHECK_INTERVAL = 3

active_screen_processes = {}


def is_screenshot_tool(name):
    name = name.lower()
    return any(tool in name for tool in [
        "snippingtool",
        "snip",
        "screenclip",
        "screenshot"
    ])


def detect_screen_behavior():

    current_active = {}

    for proc in psutil.process_iter(['pid', 'name']):

        try:
            pid = proc.info['pid']
            name = proc.info['name']

            cpu = proc.cpu_percent(interval=0.1)

            if cpu < CPU_THRESHOLD and not is_screenshot_tool(name):
                continue

            connections = get_connections_by_process_name(name)

            is_streaming = cpu >= CPU_THRESHOLD and len(connections) > 0
            is_recording = cpu >= CPU_THRESHOLD and len(connections) == 0
            is_screenshot = is_screenshot_tool(name)

            if is_streaming or is_recording or is_screenshot:

                current_active[pid] = {
                    "name": name,
                    "cpu": cpu,
                    "connections": connections,
                    "type": (
                        "STREAMING" if is_streaming else
                        "RECORDING" if is_recording else
                        "SCREENSHOT"
                    )
                }

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return current_active


def monitor_screen():

    global active_screen_processes

    print("Advanced Screen Monitoring Started...\n")

    while True:

        detected = detect_screen_behavior()

        for pid, info in detected.items():

            if pid not in active_screen_processes:

                print(f"[START] {info['type']} detected")
                print(f"Process: {info['name']} (PID {pid})")
                print(f"CPU: {info['cpu']:.2f}%")

                if info["connections"]:
                    for conn in info["connections"]:
                        print(f"[DATA] → {conn['ip']}:{conn['port']}")

                print(f"Time: {datetime.now()}\n")

                log_device_event("SCREEN_START", info['name'], pid)

 
        for pid in list(active_screen_processes.keys()):

            if pid not in detected:

                info = active_screen_processes[pid]

                print(f"[STOP] Screen activity stopped")
                print(f"Process: {info['name']} (PID {pid})")
                print(f"Time: {datetime.now()}\n")

                log_device_event("SCREEN_STOP", info['name'], pid)

        active_screen_processes = detected

        time.sleep(CHECK_INTERVAL)