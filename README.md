# AdaptiveOS  
An OS-Level Intelligent Focus and Exam Supervision System

## Overview

AdaptiveOS is a Linux-based operating system–level supervision system designed to provide intelligent focus assistance and secure exam supervision without compromising user privacy. The system introduces multiple operating modes that regulate application usage and window behavior based on context, enabling productivity and integrity in focus-critical and examination environments.

Unlike traditional solutions that rely on invasive techniques such as webcam monitoring or screen recording, AdaptiveOS operates strictly at the window and process control level, ensuring ethical and privacy-preserving supervision.

## Key Features

- Multiple operating modes: Normal, Focus, Exam and Exit
- OS-level application and window enforcement
- Intelligent behavior-based focus suggestions
- Secure full-screen exam supervision
- Privacy-first design with no intrusive monitoring
- Lightweight implementation suitable for continuous execution

## Operating Modes

### Normal Mode
- Default operating mode with unrestricted system usage
- User behavior such as application switching and session duration is observed
- Intelligent recommendations are generated to suggest switching to Focus Mode when distraction patterns are detected

### Focus Mode
- Enforces a distraction-free environment
- Automatically closes blacklisted applications
- Allows only essential productivity applications
- Designed to enhance concentration without blocking user control completely

### Exam Mode
- Strict supervision mode intended for examinations
- Launches a full-screen exam application
- Automatically closes all unauthorized windows
- Prevents window switching and multitasking
- Exam session ends only after submission

### Exit Mode
- Restores system to normal operation
- Clears enforcement state
- Allows re-selection of operating modes

## System Architecture

AdaptiveOS operates entirely in user space and consists of the following components:

- **Monitoring Engine:** Continuously observes active windows and system state
- **Enforcement Layer:** Applies application restrictions based on the selected mode
- **User Interface Layer:** Provides mode selection, exit controls and suggestions
- **Exam Application Module:** Handles full-screen exam delivery and submission
- **Machine Learning Module:** Generates focus recommendations based on user behavior

## Machine Learning-Based Focus Recommendation

AdaptiveOS uses a lightweight machine learning model to analyze behavioral indicators such as:

- Session duration
- Application switching frequency
- User interaction patterns

Based on these parameters, the system recommends switching to Focus Mode when sustained focus or distraction is detected. The ML component is advisory and does not enforce mode changes automatically.

## Technologies Used

- **Programming Language:** Python  
- **Platform:** Linux (Ubuntu)  
- **UI Framework:** Tkinter  
- **Window Control:** wmctrl, xdotool  
- **Machine Learning:** Scikit-learn  
- **Data Handling:** Pandas  
- **Model Persistence:** Joblib  
- **Version Control:** Git  

## Required Dependencies

- Python 3.x  
- wmctrl  
- xdotool  
- tkinter  
- pandas  
- scikit-learn  
- joblib  

Install system tools using:
```bash
sudo apt install wmctrl xdotool

Install Python dependencies using:

```bash
pip install pandas scikit-learn joblib
```

---

## Privacy and Ethics

AdaptiveOS is designed with privacy as a core principle.

- No webcam access  
- No microphone usage  
- No screen recording  
- No keystroke logging  
- No content-level inspection  

All enforcement is performed strictly at the operating system level using window and process control mechanisms.

---

## Limitations

- Website-level blocking inside browsers is not supported  
- Machine learning recommendations depend on training data quality  
- Currently supports Linux desktop environments using X11 window managers  

---

## Future Scope

- Personalized focus thresholds per user  
- Multiple focus levels such as Focus-Light and Focus-Strict  
- Wayland window manager support  
- Enhanced machine learning models for adaptive behavior analysis  
- Integration with institutional examination platforms  
- Administrative dashboards and analytics  

---

## Conclusion

AdaptiveOS demonstrates how operating system concepts such as window management and access control can be combined with lightweight machine learning to provide intelligent focus assistance and secure exam supervision. The system offers an ethical, privacy-respecting alternative to conventional proctoring and productivity tools.

---

## Authors

- **Surabhi M**  
- **Tanisha Bhide**
