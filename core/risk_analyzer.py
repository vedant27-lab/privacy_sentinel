import os

SUSPICIOUS_DIRECTORIES = [
    "AppData\\Temp",
    "AppData\\Roaming",
    "Downloads",
    "Temp"
]

SAFE_DIRECTORIES = [
    "Program Files",
    "Windows\\System32"
]


def calculate_path_risk(exe_path):

    if exe_path is None:
        return "UNKNOWN"

    path = exe_path.lower()

    for safe in SAFE_DIRECTORIES:
        if safe.lower() in path:
            return "LOW"

    for suspicious in SUSPICIOUS_DIRECTORIES:
        if suspicious.lower() in path:
            return "HIGH"

    return "MEDIUM"