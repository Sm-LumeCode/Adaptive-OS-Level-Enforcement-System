# Adaptive OS-Level Enforcement System

## Project Overview
The Adaptive OS-Level Enforcement System is a Linux-based desktop control system designed to regulate application access based on user-selected operational modes. The system enforces access policies in real time at the operating system level without relying on invasive monitoring techniques such as cameras, microphones, or screen recording.

The project introduces three operational modes—Normal, Focus, and Exam—to support distraction-free work environments and controlled examination scenarios while preserving user privacy. All enforcement is performed in user space using OS utilities, ensuring transparency and minimal system overhead.

---

## Key Features
- Mode-based application enforcement (Normal, Focus, Exam)
- Real-time monitoring of desktop windows and processes
- Automatic restriction of unauthorized or distracting applications
- Enhanced Exam Mode with single-window full-screen enforcement
- Persistent exit control for safe and seamless mode switching
- Lightweight Logistic Regression model for intelligent mode recommendation
- User-space implementation without administrative privileges
- Privacy-preserving design
- Modular and extensible architecture

---

## Operational Modes

### Normal Mode
- Observes system usage without enforcing restrictions
- Collects non-invasive usage patterns for intelligent recommendations

### Focus Mode
- Automatically blocks predefined distracting applications
- Uses blacklist-based enforcement for productivity enhancement

### Exam Mode
- Launches a single full-screen examination window
- Prevents opening of any other application or window
- User cannot exit until the exam is completed or explicitly quit
- Enforcement is entirely OS-level with no browser dependency
- Designed to eliminate multitasking and malpractice

---

## Intelligent Mode Recommendation
The system integrates a lightweight Logistic Regression model to recommend suitable operational modes based on historical application usage patterns. The model analyzes non-sensitive behavioral metrics such as application switching frequency and usage duration to suggest transitions between Normal, Focus, and Exam modes. This approach ensures adaptability while preserving user privacy and system performance.

---

## Project Structure
```text
AdaptiveOS/
├── backend/
│   └── monitor.py        # Core enforcement logic and window monitoring
├── ui/
│   └── popup.py          # Tkinter-based UI for mode selection and exit control
├── data/
│   └── config.py         # Mode rules, whitelist, blacklist, ML parameters
├── requirements.txt      # Python dependencies
├── main.py               # Entry point of the system
└── README.md             # Project documentation
```
## Tools and Technologies Used
<li>
Python 3
<li>
Tkinter
<li>
wmctrl
<li>
xdotool
<li>
Logistic Regression
<li>
Git & GitHub
</li>

### Installation and Setup
Prerequisites:
<li>
Linux operating system (X11 session required)
<li>
Python 3 installed

Install required system utilities:
```text
sudo apt install wmctrl xdotool
```

Install Python dependencies:
```text
pip install -r requirements.txt
```
How to Run ?
```text
python main.py
```
### Future Enhancements
<li>
Advanced ML-based behavior analysis
<li>
Exam activity logging and analytics
<li>
System tray integration
<li>
Support for additional desktop environments
<li>
Secure browser integration for web-based exams
</li>

### Authors
<b>Surabhi M and Tanisha Bhide</b>