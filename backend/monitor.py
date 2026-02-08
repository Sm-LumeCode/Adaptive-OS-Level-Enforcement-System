import os
import subprocess
import time
from ML.predictor import suggest_mode
from data import config
from ui.popup import ask_mode, show_exit_button, show_ml_suggestion
import sys

# ---------------- STATE ----------------
exam_started = False

TERMINAL_KEYWORDS = ["terminal", "bash", "vboxuser@", "gnome-terminal"]
DESKTOP_IGNORE = ["desktop", "desktop icons"]
EXIT_POPUP_ALLOW = ["exit mode", "mode recommendation"]
EXAM_WINDOW_KEYWORDS = ["exam mode"]

# Normal-mode ML logic state
last_window_title = None
same_window_start = None
ml_suggested = False

FOCUS_TIME_THRESHOLD = 10      # seconds
CHECK_INTERVAL = 0.3

# Activity metrics
app_switches = 0
idle_time = 0
keyboard_events = 0
mouse_events = 0

session_start = time.time()


# ---------------- HELPERS ----------------
def run(cmd):
    return subprocess.check_output(
        cmd, stderr=subprocess.DEVNULL
    ).decode(errors="ignore")


def get_active_window():
    try:
        wid = run(["xdotool", "getwindowfocus"]).strip()
        title = run(["xdotool", "getwindowname", wid]).strip()
        return wid, title
    except:
        return None, ""


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
    return any(k in title.lower() for k in TERMINAL_KEYWORDS)


def is_blacklisted(title):
    return any(b.lower() in title.lower() for b in config.BLACKLIST)


def is_desktop_window(title):
    return any(d in title.lower() for d in DESKTOP_IGNORE)


def is_exam_window(title):
    return any(k in title.lower() for k in EXAM_WINDOW_KEYWORDS)


def is_whitelisted(title):
    return any(w.lower() in title.lower() for w in config.WHITELIST)


def exam_finished():
    return os.path.exists("exam/exam_done.flag")


# ---------------- START ----------------
ask_mode()
show_exit_button()


# Exit program function (if user chooses EXIT in popup)
def exit_program():
    sys.exit(0)


# ---------------- MAIN LOOP ----------------
while True:
    wid, title = get_active_window()
    windows = get_all_windows()
    now = time.time()

    # ---------------- EXIT MODE ----------------
    if config.MODE == "exit":
        ml_suggested = False
        last_window_title = None
        same_window_start = None
        session_start = now
        exam_started = False

        ask_mode()
        show_exit_button()
        time.sleep(CHECK_INTERVAL)
        continue

    # ---------------- EXAM MODE ----------------
    if config.MODE == "exam":
        if not exam_started:
            os.system("python3 exam/exam_app.py &")
            exam_started = True

        if exam_finished():
            os.remove("exam/exam_done.flag")
            config.MODE = "exit"
            continue

        for w_id, w_title in windows:
            if (
                is_desktop_window(w_title)
                or is_terminal(w_title)
                or is_exam_window(w_title)
                or is_whitelisted(w_title)
            ):
                continue
            close_window(w_id)

        time.sleep(CHECK_INTERVAL)
        continue

    # ---------------- FOCUS MODE ----------------
    if config.MODE == "focus":
        for w_id, w_title in windows:
            if is_desktop_window(w_title):
                continue
            if is_blacklisted(w_title):
                close_window(w_id)
        time.sleep(CHECK_INTERVAL)
        continue

    # ---------------- NORMAL MODE (ML LOGIC) ----------------
    if not title or is_desktop_window(title):
        time.sleep(CHECK_INTERVAL)
        continue

    # Track window focus
    if title != last_window_title:
        app_switches += 1
        last_window_title = title
        same_window_start = now
        ml_suggested = False  # reset on window change

    focused_duration = now - same_window_start
    session_duration = now - session_start

    # ⛔ Skip suggestions before focus threshold
    if focused_duration < FOCUS_TIME_THRESHOLD:
        time.sleep(CHECK_INTERVAL)
        continue

    # ⛔ Prevent repeated suggestions
    if ml_suggested:
        time.sleep(CHECK_INTERVAL)
        continue

    # ---------------- COLLECT ACTIVITY FOR ML ----------------
    activity = {
        "app_switches": app_switches,
        "idle_time": idle_time,
        "keyboard_events": keyboard_events,
        "mouse_events": mouse_events,
        "session_duration": session_duration
    }

    # Get ML suggestion
    result = suggest_mode(activity)
    mode = result.get("mode", "focus")
    confidence = result.get("confidence", 60)
    reason = result.get("reason", "Focused on same app")

    # Show suggestion if confidence ≥ 60
    if confidence >= 60:
        message = (
            f"🔮 Recommended Mode: {mode}\n"
            f"Confidence: {confidence}%\n\n"
            f"{reason}"
        )
        show_ml_suggestion(message)
        ml_suggested = True

    time.sleep(CHECK_INTERVAL)
