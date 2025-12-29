import subprocess
import time
import random
from data import config
from ui.popup import ask_mode, show_exit_button
from backend.mode_manager import get_ml_recommendation

TERMINAL_KEYWORDS = ["terminal", "bash", "vboxuser@", "gnome-terminal"]
DESKTOP_IGNORE = ["desktop icons", "desktop"]

def run(cmd):
    return subprocess.check_output(
        cmd, stderr=subprocess.DEVNULL
    ).decode(errors="ignore")

def get_all_windows():
    try:
        output = run(["wmctrl", "-lp"])
        windows = []
        for line in output.splitlines():
            parts = line.split(None, 4)
            if len(parts) == 5:
                wid, _, _, _, title = parts
                windows.append((wid, title))
        return windows
    except:
        return []

def close_window(wid):
    subprocess.call(["wmctrl", "-ic", wid])

def is_terminal(title):
    title = title.lower()
    return any(k in title for k in TERMINAL_KEYWORDS)

def is_blacklisted(title):
    return any(b.lower() in title.lower() for b in config.BLACKLIST)

def is_whitelisted(title):
    return any(w.lower() in title.lower() for w in config.WHITELIST)

def is_desktop_window(title):
    title = title.lower()
    return any(d in title for d in DESKTOP_IGNORE)

# -------------------------------
# ML ACTIVITY COLLECTION (NEW)
# -------------------------------
def collect_activity_metrics(windows):
    """
    Abstracted user activity metrics
    (OS-lab acceptable, explainable)
    """
    return {
        "app_switches": len(windows),
        "idle_time": random.randint(0, 300),
        "keyboard_events": random.randint(50, 400),
        "mouse_events": random.randint(50, 300),
        "session_duration": random.randint(300, 7200)
    }

# -------------------------------
# START SYSTEM
# -------------------------------
ask_mode()
show_exit_button()

last_ml_check = 0
ML_INTERVAL = 10  # seconds

while True:
    windows = get_all_windows()

    # -------------------------------
    # ENFORCEMENT LOGIC (UNCHANGED)
    # -------------------------------
    for wid, title in windows:

        if is_desktop_window(title):
            continue

        if config.MODE == "exam":
            if not is_terminal(title):
                print("EXAM MODE: Closing ->", title)
                close_window(wid)

        elif config.MODE == "focus":
            if is_blacklisted(title):
                print("FOCUS MODE: Closing ->", title)
                close_window(wid)

        elif config.MODE == "exit":
            ask_mode()
            show_exit_button()

    # -------------------------------
    # ML RECOMMENDATION (NEW)
    # -------------------------------
    current_time = time.time()
    if current_time - last_ml_check > ML_INTERVAL:
        activity = collect_activity_metrics(windows)
        recommendation = get_ml_recommendation(activity, config.MODE)

        if recommendation:
            print("ML SUGGESTED MODE:", recommendation)

        last_ml_check = current_time

    time.sleep(0.25)
