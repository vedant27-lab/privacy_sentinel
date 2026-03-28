def evaluate_process_risk(process_name, cpu, exe_path, device_used):
    alerts = []
    if cpu and cpu > 80:
        alerts.append("High CPU usage")
    
    if exe_path:
        path = exe_path.lower()
        if "temp" in path or "downloads" in path:
            alerts.append("Suspicious execution path")
    if device_used:
        safe_apps = ["chrome", "zoom", "teams", "discord", "WindowsCamera"]

        if not any(app in process_name.lower() for app in safe_apps):
            alerts.append("Unknown app using sensitive device")
    return alerts
    