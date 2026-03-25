import subprocess

def is_suspicious_path(path):
    if not path:
        return True
    
    path = path.lower()

    return any(x in path for x in ["temp", "downloads", "appdata"])

def get_signature_status(path):
    try:
        cmd = f'powershell Get-AuthenticodeSignature "{path}"'
        out = subprocess.check_output(cmd, shell=True).decode()

        if "Valid" in out:
            return "VALID"
        return "INVALID"
    except:
        return "UNKNOWN"
    
    