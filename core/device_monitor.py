import winreg
import time
from database.db import log_device_event
from core.rule_engine import evaluate_proess_risk
from core.network_monitor import get_connections_by_process_name
import os
import psutil

KEYS = {
    "WEBCAM": r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam",
    "MICROPHONE": r"SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone",
}

last_seen = set()

def get_active_apps(device_key):
    results = []
    try:
        base = winreg.OpenKey(winreg.HKEY_CURRENT_USER, device_key)
        i = 0
        while True:
            try:
                subkey_name = winreg.EnumKey(base, i)

                if subkey_name == "NonPackaged":
                    i += 1
                    continue
                sub = winreg.OpenKey(base, subkey_name)

                try:
                    last_used, _ = winreg.QueryValueEx(sub, "LastUsedTimeStop")
                    if last_used == 0:
                        results.append({
                            "app": subkey_name,
                            "type": "UWP"
                        })
                except FileNotFoundError:
                    pass
                i += 1
            except OSError:
                break
        
        try:
            nonpkg = winreg.OpenKey(base, "NonPackaged")
            j = 0
            while True:
                try:
                    app = winreg.EnumKey(nonpkg, j)
                    sub = winreg.OpenKey(nonpkg, app)

                    try:
                        last_used, _ = winreg.QueryValueEx(sub, "LastUsedTimeStop")

                        if last_used == 0:
                            results.append({
                                "app":app.replace("#", "\\"),
                                "type": "Win32"
                            })
                    except FileNotFoundError:
                        pass
                    
                    j += 1
                
                except OSError:
                    break
        except FileNotFoundError:
            pass
    except FileNotFoundError:
        pass
    return results

def monitor_devices():
    global last_seen

    print("Device monitoring started...\n")

    while True:
        current_seen = set()

        for device, key in KEYS.items():
            active_apps = get_active_apps(key)

            for app in active_apps:
                identifier = f"{device}:{app['app']}"
                current_seen.add(identifier)

                if identifier not in last_seen:
                    print(f"[ALERT] {device} in use | Type: {app['type']} | App: {app['app']}")
                    log_device_event(device, app['app'], 0)

                    alerts = evaluate_proess_risk(
                        process_name=app['app'],
                        cpu=None,
                        exe_path=app['app'],
                        device_used=True
                    )

                    for alert in alerts:
                        print(f"[Risk] {alert}")
                process_name = os.path.basename(app['app'])
                connections = get_connections_by_process_name(process_name)
                if connections:
                    for conn in connections:
                        print(f"[NETWORK] {process_name} -> {conn['ip']}:{conn['port']}")
                else:
                    print(f"[NETWORK] {process_name} -> No active connections")

        last_seen = current_seen
        time.sleep(1)