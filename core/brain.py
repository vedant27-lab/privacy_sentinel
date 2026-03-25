from core.identity import is_suspicious_path, get_signature_status
from core.behavior import get_behavior_flags

def evaluate(ctx):
    reasons = []

    flags = get_behavior_flags(ctx)

    suspicious_path = is_suspicious_path(ctx["exe_path"])
    signature = get_signature_status(ctx["exe_path"])

    if ("MIC" in flags or "CAM" in flags or "SCREEN" in flags):
        if "NETWORK" in flags:
            if suspicious_path or signature != "VALID":
                return "CRITICAL", [
                    "Sensitive device access",
                    "Network transimission",
                    "Untrusted identity"
                ]
            
        if "SCREEN" in flags and "NETWORK" in flags:
            return "HIGH", ["Screen capture + network"]
        
        if "MIC" in flags and "NETWORK" in flags:
            return "HIGH", ["Mic + network"]
        
        if "MIC" in flags or "CAM" in flags:
            return "MEDIUM", ["Suspicious path"]
        
        return "LOW", ["Normal"]