# Adaptive OS-Level Enforcement System

## Project Overview
The Adaptive OS-Level Enforcement System is a Linux-based desktop control system designed to regulate application access based on user-selected operational modes. The system enforces access policies in real time at the operating system level without relying on invasive monitoring techniques such as cameras or microphones.

The project introduces three operational modes—Normal, Focus, and Exam—to support distraction-free work environments and controlled examination scenarios while preserving user privacy.

## Key Features
- Mode-based application enforcement (Normal, Focus, Exam)
- Real-time monitoring of desktop windows
- Automatic restriction of unauthorized or distracting applications
- Persistent exit control for seamless mode switching
- User-space implementation without administrative privileges
- Privacy-preserving design
- Modular and extensible architecture

## Operational Modes
- Normal Mode: Observes system usage without enforcing restrictions.
- Focus Mode: Automatically blocks predefined distracting applications using blacklist-based enforcement.
- Exam Mode: Restricts all applications except essential tools such as the terminal, ensuring a controlled environment.

## Project Structure
AdaptiveOS/
├── backend/
│   └── monitor.py          # Core enforcement logic and window monitoring
├── ui/
│   └── popup.py            # Tkinter-based UI for mode selection and exit control
├── data/
│   └── config.py           # Configuration for modes, whitelist, and blacklist
├── requirements.txt        # Python dependencies
├── main.py                 # Entry point of the system
└── README.md               # Project documentation

## Tools and Technologies Used
- Python 3
- Tkinter
- wmctrl
- xdotool
- Git & GitHub

## Installation and Setup
Prerequisites:
- Linux operating system (X11 session required)
- Python 3 installed

Install required system utilities:
sudo apt install wmctrl xdotool

Install Python dependencies:
pip install -r requirements.txt

## How to Run
python main.py

Steps:
1. A mode selection popup appears.
2. Select Normal, Focus, or Exam mode.
3. Application access is enforced based on the selected mode.
4. Use the Exit Mode button to safely switch modes.

## Testing
The system was tested by launching various applications under different modes to validate enforcement behavior. Restricted applications were consistently blocked while permitted applications continued to function normally. Mode switching and exit functionality were verified for stability.

## Future Enhancements
- Machine learning–based mode recommendation
- Intelligent behavior analysis for adaptive enforcement
- Logging and analytics for usage monitoring
- System tray integration
- Support for additional desktop environments

## Limitations
- Designed specifically for Linux systems running X11
- User-space enforcement only (no kernel-level lockdown)
- Wayland-based desktops are not supported

## Academic Relevance
This project demonstrates core operating system concepts including access control, user-space enforcement, process monitoring, and modular system design. It serves as a foundation for further research in intelligent and secure computing environments.

## Authors
Surabhi M  
Tanisha Bhide
