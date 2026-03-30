from sklearn.ensemble import IsolationForest
try:
    from core.feature_engine import get_features
except ModuleNotFoundError:
    from feature_engine import get_features
import joblib

def train():
    X = get_features()

    if len(X) == 0:
        print("No data available to train model. Please collect some events first.")
        return

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(X)

    joblib.dump(model, "model.pkl")
    print("Model trained and saved!")

if __name__ == "__main__":
    train()