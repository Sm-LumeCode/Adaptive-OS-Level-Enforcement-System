MODE = "normal"

# Terminal ONLY allowed in exam
WHITELIST = ["terminal","text editor"]

# Block these in focus
BLACKLIST = ["app center", "settings", "help", "files", "trash", "youtube", "instagram"]

# ---------------- ACTIVITY TRACKING (FOR ML) ----------------
# These values are updated by monitor logic

ACTIVE_WINDOW_TIME = 0        # seconds user stays on same window
WINDOW_SWITCH_COUNT = 0       # number of app switches
IDLE_TIME = 0                 # idle duration
KEYBOARD_EVENTS = 80           # keyboard activity count
MOUSE_EVENTS = 50              # mouse activity count
SESSION_DURATION = 300          # total session time in seconds


def get_activity_snapshot():
    """
    Returns activity features exactly as required by the ML model.
    This is an interface layer, not enforcement logic.
    """
    return {
        "active_time": ACTIVE_WINDOW_TIME,
        "app_switches": WINDOW_SWITCH_COUNT,
        "idle_time": IDLE_TIME,
        "keyboard_events": KEYBOARD_EVENTS,
        "mouse_events": MOUSE_EVENTS,
        "session_duration": SESSION_DURATION
    }
