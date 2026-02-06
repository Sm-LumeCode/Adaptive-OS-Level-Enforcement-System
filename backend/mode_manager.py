CURRENT_MODE = None
PREVIOUS_MODE = None

def set_mode(mode):
    global CURRENT_MODE, PREVIOUS_MODE
    PREVIOUS_MODE = CURRENT_MODE
    CURRENT_MODE = mode
    print(f"[MODE] → {mode}")

def restore_previous_mode():
    global CURRENT_MODE
    CURRENT_MODE = None
    print("[MODE] → NONE")

def get_mode():
    return CURRENT_MODE

