import tkinter as tk
from data import config
import threading

BG_COLOR = "#1e1e2e"
TEXT_COLOR = "#f8f8f2"

BTN_NORMAL = "#89b4fa"
BTN_FOCUS = "#a6e3a1"
BTN_EXAM = "#f38ba8"
BTN_EXIT = "#e64553"

BTN_HOVER_DARKEN = 0.90


def darken(hex_color, factor=0.9):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)

    return f"#{r:02x}{g:02x}{b:02x}"


def styled_button(parent, text, color, command):
    btn = tk.Button(
        parent,
        text=text,
        bg=color,
        fg="#000000",
        font=("Segoe UI", 11, "bold"),
        relief="flat",
        height=2,
        command=command
    )

    btn.bind(
        "<Enter>",
        lambda e: btn.config(bg=darken(color, BTN_HOVER_DARKEN))
    )
    btn.bind(
        "<Leave>",
        lambda e: btn.config(bg=color)
    )

    btn.pack(fill="x", pady=6)
    return btn


def ask_mode():
    root = tk.Tk()
    root.title("AdaptiveOS")
    root.geometry("320x260")
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

    styled_button(root, "Normal Mode", BTN_NORMAL, lambda: set_mode("normal"))
    styled_button(root, "Focus Mode", BTN_FOCUS, lambda: set_mode("focus"))
    styled_button(root, "Exam Mode", BTN_EXAM, lambda: set_mode("exam"))

    root.mainloop()


def show_exit_button():
    def run():
        win = tk.Tk()
        win.title("Exit Mode")
        win.geometry("200x90+20+20")
        win.configure(bg=BG_COLOR)
        win.attributes("-topmost", True)

        def exit_mode():
            config.MODE = "exit"

        styled_button(win, "EXIT MODE", BTN_EXIT, exit_mode)

        win.mainloop()

    threading.Thread(target=run, daemon=True).start()
