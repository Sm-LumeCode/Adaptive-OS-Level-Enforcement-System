import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "mode_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

FEATURE_ORDER = [
    "session_duration",
    "app_switches",
    "idle_time",
    "keyboard_events",
    "mouse_events"
]

def suggest_mode(activity):
    """
    Returns:
        (suggested_mode, reason)
    """

    # 🔴 Read exact feature order from trained model
    feature_names = model.feature_names_in_

    # Build data strictly in that order
    data = [[activity[name] for name in feature_names]]

    features = pd.DataFrame(data, columns=feature_names)

    prediction = model.predict(features)[0]

    if prediction == "focus":
        reason = (
            "Sustained session activity with minimal application switching "
            "and consistent user interaction indicates focused behavior."
        )
        return "focus", reason

    return "normal", "No strong focus pattern detected."
