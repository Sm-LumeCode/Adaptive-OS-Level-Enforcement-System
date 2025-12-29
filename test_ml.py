from ML.predictor import suggest_mode

activity = {
    'app_switches': 20,
    'idle_time': 60,
    'keyboard_events': 220,
    'mouse_events': 200,
    'session_duration': 3600
}

print("Suggested mode:", suggest_mode(activity))
