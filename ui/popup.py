import tkinter as tk
import threading
from data import config
import sys

# ------------------ COLORS ------------------
BG_COLOR = "#1e1e2e"
TEXT_COLOR = "#f8f8f2"

BTN_NORMAL = "#89b4fa"
BTN_FOCUS = "#a6e3a1"
BTN_EXAM = "#f38ba8"
BTN_EXIT = "#e64553"
BTN_STAY = "#fab387"

BTN_HOVER_DARKEN = 0.9
BTN_WIDTH = 28   # ✅ fixed width for equal size buttons

# ------------------ HELPERS ------------------
def darken(hex_color, factor=0.9):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"


def styled_button(parent, text, color, command):
    btn = tk.Button(
        parent,
        text=text,
        bg=color,
        fg="#000000",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        height=2,
        width=BTN_WIDTH,     # ✅ key fix
        command=command
    )
    btn.bind("<Enter>", lambda e: btn.config(bg=darken(color, BTN_HOVER_DARKEN)))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    btn.pack(fill="x", pady=6)
    return btn


# ------------------ MODE SELECTION ------------------
def ask_mode():
    root = tk.Tk()
    root.title("AdaptiveOS")
    root.geometry("620x420")
    root.configure(bg=BG_COLOR)
    root.attributes("-topmost", True)

    def set_mode(mode):
        config.MODE = mode
        root.destroy()

    tk.Label(
        root,
        text="Select Operating Mode",
        font=("Segoe UI", 14, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=14)

    def exit_program():
        root.quit()
        root.destroy()
        sys.exit(0)

    styled_button(root, "Normal Mode", BTN_NORMAL, lambda: set_mode("normal"))
    styled_button(root, "Focus Mode", BTN_FOCUS, lambda: set_mode("focus"))
    styled_button(root, "Exam Mode", BTN_EXAM, lambda: set_mode("exam"))
    styled_button(root, "EXIT", BTN_EXIT, exit_program)
    root.mainloop()


# ------------------ EXIT MODE BUTTON ------------------
def show_exit_button():
    def run():
        win = tk.Tk()
        win.title("Exit Mode")
        win.geometry("200x90+20+20")
        win.configure(bg=BG_COLOR)
        win.attributes("-topmost", True)

        def exit_mode():
            config.MODE = "exit"
            win.destroy()

        styled_button(win, "EXIT MODE", BTN_EXIT, exit_mode)
        win.mainloop()

    threading.Thread(target=run, daemon=True).start()


# ------------------ ML SUGGESTION POPUP ------------------
def show_ml_suggestion(reason_text):
    def run():
        win = tk.Tk()
        win.title("Mode Recommendation")
        win.geometry("520x420")
        win.configure(bg=BG_COLOR)
        win.attributes("-topmost", True)

        def switch_to_focus():
            config.MODE = "focus"
            win.destroy()

        def stay_normal():
            win.destroy()

        tk.Label(
            win,
            text="Focus Mode Suggested",
            font=("Segoe UI", 15, "bold"),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=(15, 6))

        tk.Label(
            win,
            text=reason_text,
            wraplength=380,
            justify="center",
            font=("Segoe UI", 10),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=(0, 10))

        btn_frame = tk.Frame(win, bg=BG_COLOR)
        btn_frame.pack(fill="x", padx=20)

        styled_button(
            btn_frame,
            "Switch to Focus Mode",
            BTN_FOCUS,
            switch_to_focus
        )

        styled_button(
            btn_frame,
            "Stay in Normal Mode",
            BTN_STAY,
            stay_normal
        )

        win.mainloop()

    threading.Thread(target=run, daemon=True).start()
