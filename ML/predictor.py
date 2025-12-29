import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "mode_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

def suggest_mode(activity):
    """
    activity = {
        'app_switches': int,
        'idle_time': int,
        'keyboard_events': int,
        'mouse_events': int,
        'session_duration': int
    }
    """

    features = [[
        activity['app_switches'],
        activity['idle_time'],
        activity['keyboard_events'],
        activity['mouse_events'],
        activity['session_duration']
    ]]

    prediction = model.predict(features)
    return encoder.inverse_transform(prediction)[0]