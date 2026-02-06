import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
import json
from data import config
from ui.popup import ask_mode


class ExamApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Exam Mode")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)

        QUESTIONS_PATH = os.path.join(os.path.dirname(__file__), "questions.json")
        with open(QUESTIONS_PATH) as f:
            self.questions = json.load(f)

        self.index = 0
        self.answers = [tk.IntVar(value=-1) for _ in self.questions]

        # ========== NEW: UI STATE VARIABLES ==========
        self.username = ""  # Stored in memory only
        self.usn = ""       # USN stored in memory only
        self.logged_in = False
        # ============================================

        # ========== NEW: MAIN CONTAINER FRAME ==========
        self.main_container = tk.Frame(self.root, bg="#1e1e2e")
        self.main_container.pack(expand=True, fill="both")
        # ===============================================

        # ========== NEW: LOGIN FRAME (INITIAL VIEW) ==========
        self.login_frame = None
        # =====================================================

        # ========== NEW: NAVBAR FRAME (PERSISTENT) ==========
        self.navbar_frame = None
        self.username_label = None
        self.score_label = None
        # ====================================================

        # ========== EXISTING: CONTENT FRAME (QUESTIONS) ==========
        self.frame = None
        # =========================================================

        # ========== NEW: SHOW LOGIN FIRST ==========
        self.render_login()
        # ===========================================

        self.root.mainloop()

    # ========== NEW: LOGIN SCREEN ==========
    def render_login(self):
        """Display login screen before exam starts"""
        self.login_frame = tk.Frame(self.main_container, bg="#1e1e2e")
        self.login_frame.pack(expand=True, fill="both")

        # Title
        tk.Label(
            self.login_frame,
            text="Exam Login",
            font=("Segoe UI", 32, "bold"),
            fg="#f8f8f2",
            bg="#1e1e2e"
        ).pack(pady=50)

        # ========== NEW: USERNAME INPUT ==========
        # Username label
        tk.Label(
            self.login_frame,
            text="Enter Username:",
            font=("Segoe UI", 16),
            fg="#f8f8f2",
            bg="#1e1e2e"
        ).pack(pady=(30, 5))

        # Username entry
        self.username_entry = tk.Entry(
            self.login_frame,
            font=("Segoe UI", 14),
            bg="#313244",
            fg="#f8f8f2",
            insertbackground="#f8f8f2",
            width=35,
            justify="center",
            relief="flat",
            bd=2
        )
        self.username_entry.pack(pady=5, ipady=8)
        self.username_entry.focus()
        # =========================================

        # ========== NEW: USN INPUT ==========
        # USN label
        tk.Label(
            self.login_frame,
            text="Enter USN:",
            font=("Segoe UI", 16),
            fg="#f8f8f2",
            bg="#1e1e2e"
        ).pack(pady=(20, 5))

        # USN entry
        self.usn_entry = tk.Entry(
            self.login_frame,
            font=("Segoe UI", 14),
            bg="#313244",
            fg="#f8f8f2",
            insertbackground="#f8f8f2",
            width=35,
            justify="center",
            relief="flat",
            bd=2
        )
        self.usn_entry.pack(pady=5, ipady=8)
        # ====================================

        # Bind Enter key to start exam
        self.username_entry.bind("<Return>", lambda e: self.usn_entry.focus())
        self.usn_entry.bind("<Return>", lambda e: self.start_exam())

        # Start exam button
        tk.Button(
            self.login_frame,
            text="Start Exam",
            font=("Segoe UI", 16, "bold"),
            bg="#a6e3a1",
            fg="#000000",
            height=2,
            width=20,
            cursor="hand2",
            relief="flat",
            command=self.start_exam
        ).pack(pady=50)

    def start_exam(self):
        """Validate login and transition to exam view"""
        username_input = self.username_entry.get().strip()
        usn_input = self.usn_entry.get().strip()
        
        # ========== NEW: VALIDATE BOTH FIELDS ==========
        if not username_input or not usn_input:
            return  # Require both username and USN before starting
        # ===============================================
        
        # Store credentials in memory
        self.username = username_input
        self.usn = usn_input
        self.logged_in = True
        
        # Destroy login frame
        self.login_frame.destroy()
        
        # Setup exam UI
        self.setup_exam_ui()
    # ========================================

    # ========== NEW: SETUP EXAM UI WITH NAVBAR ==========
    def setup_exam_ui(self):
        """Initialize navbar and content frames for exam"""
        
        # Create persistent navbar
        self.navbar_frame = tk.Frame(self.main_container, bg="#313244", height=70)
        self.navbar_frame.pack(side="top", fill="x")
        self.navbar_frame.pack_propagate(False)

        # ========== NEW: USERNAME + USN DISPLAY (LEFT) ==========
        user_info_frame = tk.Frame(self.navbar_frame, bg="#313244")
        user_info_frame.pack(side="left", padx=25, pady=10)

        tk.Label(
            user_info_frame,
            text=f"Student: {self.username}",
            font=("Segoe UI", 13, "bold"),
            fg="#f8f8f2",
            bg="#313244"
        ).pack(anchor="w")

        tk.Label(
            user_info_frame,
            text=f"USN: {self.usn}",
            font=("Segoe UI", 11),
            fg="#cdd6f4",
            bg="#313244"
        ).pack(anchor="w")
        # ========================================================

        # Score display (right side)
        self.score_label = tk.Label(
            self.navbar_frame,
            text=f"Score: 0/{len(self.questions)}",
            font=("Segoe UI", 16, "bold"),
            fg="#a6e3a1",
            bg="#313244"
        )
        self.score_label.pack(side="right", padx=25, pady=15)

        # Create content frame for questions
        self.frame = tk.Frame(self.main_container, bg="#1e1e2e")
        self.frame.pack(expand=True, fill="both")

        # Render first question
        self.render_question()
    # ====================================================

    # ========== NEW: CALCULATE LIVE SCORE ==========
    def calculate_score(self):
        """Calculate current score based on correct answers"""
        score = 0
        for i, question in enumerate(self.questions):
            selected = self.answers[i].get()
            # Check if answer is selected and matches correct answer
            if selected != -1 and "correct" in question:
                if selected == question["correct"]:
                    score += 1
        return score

    def update_score_display(self):
        """Update score in navbar (UI only)"""
        if self.score_label:
            current_score = self.calculate_score()
            self.score_label.config(text=f"Score: {current_score}/{len(self.questions)}")
    # ===============================================

    def clear(self):
        """Clear content frame only (navbar persists)"""
        if self.frame:
            for w in self.frame.winfo_children():
                w.destroy()

    def render_question(self):
        """Render current question (existing logic with improved UI)"""
        self.clear()
        q = self.questions[self.index]

        # Question header with number
        question_header = tk.Frame(self.frame, bg="#1e1e2e")
        question_header.pack(pady=20)

        tk.Label(
            question_header,
            text=f"Question {self.index + 1} of {len(self.questions)}",
            font=("Segoe UI", 12),
            fg="#7f849c",
            bg="#1e1e2e"
        ).pack()

        # Question text
        tk.Label(
            self.frame,
            text=q['question'],
            font=("Segoe UI", 20, "bold"),
            fg="#f8f8f2",
            bg="#1e1e2e",
            wraplength=1000,
            justify="left"
        ).pack(pady=(10, 40), padx=100)

        # ========== NEW: IMPROVED OPTIONS UI ==========
        options_frame = tk.Frame(self.frame, bg="#1e1e2e")
        options_frame.pack(pady=10)

        # Option labels (A, B, C, D)
        option_labels = ["A", "B", "C", "D"]

        for i, opt in enumerate(q["options"]):
            # Create container for each option
            option_container = tk.Frame(
                options_frame,
                bg="#313244",
                relief="flat",
                bd=0
            )
            option_container.pack(fill="x", padx=150, pady=8)

            # Radiobutton with improved styling
            rb = tk.Radiobutton(
                option_container,
                text=f"  {option_labels[i]}.  {opt}",
                variable=self.answers[self.index],
                value=i,
                font=("Segoe UI", 15),
                fg="#f8f8f2",
                bg="#313244",
                activebackground="#45475a",
                selectcolor="#45475a",
                anchor="w",
                padx=20,
                pady=15,
                indicatoron=True,
                cursor="hand2",
                command=self.update_score_display  # Update score when answer selected
            )
            rb.pack(fill="x", expand=True)
        # ==============================================

        # Navigation button
        btn_text = "Submit" if self.index == len(self.questions) - 1 else "Next"

        tk.Button(
            self.frame,
            text=btn_text,
            font=("Segoe UI", 15, "bold"),
            bg="#a6e3a1",
            fg="#000000",
            height=2,
            width=15,
            cursor="hand2",
            relief="flat",
            command=self.next
        ).pack(pady=50)

    def next(self):
        """Handle next/submit button (existing logic unchanged)"""
        if self.answers[self.index].get() == -1:
            return

        if self.index < len(self.questions) - 1:
            self.index += 1
            self.render_question()
        else:
            self.finish_exam()

    def finish_exam(self):
        """Complete exam and signal monitor (existing logic unchanged)"""
        # Create signal file
        with open("exam/exam_done.flag", "w") as f:
            f.write("done")

        self.root.destroy()


if __name__ == "__main__":
    ExamApp()
