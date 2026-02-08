import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "mode_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

def suggest_mode(activity):
    """
    Returns:
        {
            "mode": "FOCUS" | "NORMAL",
            "confidence": int,
            "reason": str
        }
    """

    features = pd.DataFrame([activity])

    # Predict probabilities
    probs = model.predict_proba(features)[0]
    pred_idx = probs.argmax()

    mode = encoder.inverse_transform([pred_idx])[0]
    confidence = int(probs[pred_idx] * 100)

    if mode == "FOCUS":
        reason = (
            "High sustained interaction, long session duration, "
            "and minimal application switching indicate focused behavior."
        )
    else:
        reason = (
            "Frequent application switching and lower engagement "
            "suggest distracted or casual usage."
        )

    return {
        "mode": mode,
        "confidence": confidence,
        "reason": reason
    }
