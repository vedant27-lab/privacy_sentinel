import psutil
import time

from datetime import datetime

from core.network_monitor import get_connections_by_process_name
from database.db import log_device_event, log_process_event

from core.context_builder import build_context
from core.brain import evaluate


CPU_THRESHOLD = 10
CHECK_INTERVAL = 3

SYSTEM_PROCESS = [
    "system idle process",
    "system",
    "svchost.exe",
    "lsass.exe",
    "searchindexer.exe"
]

active_screen_processes = {}

def is_screenshot_tool(name):
    name = name.lower()
    return any(tool in name for tool in {
        "snippingtool",
        "snip",
        "screenclip",
        "screenshot"
    })

def detect_screen_behaviour():
    current_active = {}

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']

            if name.lower() in SYSTEM_PROCESS:
                continue

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

    print("Advanced Screen Monitoring Started... \n")
    while True:
        detected = detect_screen_behaviour()

        for pid, info in detected.items():
            if pid not in active_screen_processes:
                ctx = build_context(
                    process_name=info['name'],
                    pid=pid,
                    screen=True
                )

                level, reasons = evaluate(ctx)

                print(f"[START] {info['type']} detected")
                print(f"Process: {info['name']} (PID {pid})")
                print(f"[RISK] {level}")

                for r in reasons:
                    print(f" - {r}")

                print(f"CPU: {info['cpu']:.2f}%")

                if info["connections"]:
                    for conn in info["connections"]:
                        print(f"[DATA] -> {conn['ip']}:{conn['port']}")
                print(f"Time: {datetime.now()}\n")

                log_device_event("SCREEN_START", info['name'], pid)

                log_process_event(
                    "SCREEN_START",
                    ctx["process_name"],
                    ctx["pid"],
                    ctx["cpu"],
                    None,
                    ctx["exe_path"],
                    None,
                    None,
                    level,
                    ", ".join(reasons)
                )

        for pid in list(active_screen_processes.keys()):
            if pid not in detected:
                info = active_screen_processes[pid]
                print(f"[STOP] Screen activity stopped")
                print(f"Process: {info['name']} (PID {pid})")
                print(f"Time: {datetime.now()}\n")

                log_device_event("SCREEN_STOP", info['name'], pid)
        active_screen_processes = detected

        time.sleep(CHECK_INTERVAL)