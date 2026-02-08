import os
import subprocess
import time
from data import config
from ui.popup import ask_mode, show_exit_button, show_ml_suggestion

# ---------------- STATE ----------------
exam_started = False

TERMINAL_KEYWORDS = ["terminal", "bash", "vboxuser@", "gnome-terminal"]
DESKTOP_IGNORE = ["desktop", "desktop icons"]
EXIT_POPUP_ALLOW = ["exit mode", "mode recommendation"]
EXAM_WINDOW_KEYWORDS = ["exam mode"]

# --- Normal-mode behavior state ---
last_window_title = None
same_window_start = None
switch_count = 0
ml_suggested = False

FOCUS_TIME_THRESHOLD = 10      # seconds (demo-friendly)
SWITCH_THRESHOLD = 6           # frequent switching
CHECK_INTERVAL = 0.3


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


def is_exit_popup(title):
    return any(k in title.lower() for k in EXIT_POPUP_ALLOW)


def is_exam_window(title):
    return any(k in title.lower() for k in EXAM_WINDOW_KEYWORDS)


def is_whitelisted(title):
    return any(w.lower() in title.lower() for w in config.WHITELIST)


# 🔑 FILE-BASED IPC CHECK
def exam_finished():
    return os.path.exists("exam/exam_done.flag")


# ---------------- START ----------------
ask_mode()
show_exit_button()

while True:
    wid, title = get_active_window()
    windows = get_all_windows()

    # 🔴 SHUTDOWN MODE — EXIT PROGRAM COMPLETELY
    if config.MODE == "shutdown":
        print("AdaptiveOS shutting down...")
        os._exit(0)

    # 🔴 EXIT MODE (return to mode selection)
    if config.MODE == "exit":
        ml_suggested = False
        switch_count = 0
        last_window_title = None
        same_window_start = None
        exam_started = False

        ask_mode()
        show_exit_button()
        time.sleep(CHECK_INTERVAL)
        continue

    # 🔴 EXAM MODE — STRICT LOCKDOWN
    if config.MODE == "exam":

        # 🚀 Launch exam app only once
        if not exam_started:
            print("EXAM MODE: Launching exam application")
            os.system("python3 exam/exam_app.py &")
            exam_started = True

        # ✅ Check if exam finished
        if exam_finished():
            os.remove("exam/exam_done.flag")
            config.MODE = "exit"
            continue

        for w_id, w_title in windows:

            # ✅ Allowed windows
            if is_desktop_window(w_title):
                continue
            if is_terminal(w_title):
                continue
            if is_exam_window(w_title):
                continue
            if is_whitelisted(w_title):
                continue

            print("EXAM MODE: Closing ->", w_title)
            close_window(w_id)

        time.sleep(CHECK_INTERVAL)
        continue

    # 🟡 FOCUS MODE — AUTO CLOSE BLACKLISTED
    if config.MODE == "focus":
        for w_id, w_title in windows:
            if is_desktop_window(w_title):
                continue
            if is_blacklisted(w_title):
                print("FOCUS MODE: Closing ->", w_title)
                close_window(w_id)

        time.sleep(CHECK_INTERVAL)
        continue

    # 🔵 NORMAL MODE (BEHAVIOR-BASED SUGGESTION)
    if title and not is_desktop_window(title):

        if title != last_window_title:
            switch_count += 1
            last_window_title = title
            same_window_start = time.time()

        # 🔴 Case-1: Distracted
        if not ml_suggested and switch_count >= SWITCH_THRESHOLD:
            reason = (
                "You have been switching between applications frequently.\n\n"
                "This behavior indicates possible distraction.\n\n"
                "Focus Mode can help limit distractions."
            )
            show_ml_suggestion(reason)
            ml_suggested = True

        # 🔵 Case-2: Focused
        elif not ml_suggested and same_window_start:
            elapsed = time.time() - same_window_start
            if elapsed >= FOCUS_TIME_THRESHOLD:
                reason = (
                    "You have been working continuously on the same application.\n\n"
                    "To maintain this focus and avoid distractions,\n"
                    "Focus Mode is recommended."
                )
                show_ml_suggestion(reason)
                ml_suggested = True

    time.sleep(CHECK_INTERVAL)

