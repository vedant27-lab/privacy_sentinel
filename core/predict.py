import joblib

# Load trained model once
model = joblib.load("model.pkl")


def predict_anomaly(features):
    """
    features = [cpu_percent, hour, path_risk]

    Returns:
        "ANOMALY" or "NORMAL"
    """

    try:
        result = model.predict([features])  # model expects 2D array

        return "ANOMALY 🚨" if result[0] == -1 else "NORMAL"

    except Exception as e:
        print(f"[AI ERROR] {e}")
        return "UNKNOWN"