# 🖥️ Adaptive OS

Adaptive OS is a dynamic window management and distraction control system designed to enhance productivity and enforce focused work environments. By monitoring active windows and categorizing them into different operating modes, it helps users stay on task or ensures integrity during sensitive tasks like exams.

---

## 🚀 Key Features

*   **🎯 Mode-Based Control**: Easily switch between operating modes via a sleek, dark-themed UI.
*   **🛠️ Real-Time Monitoring**: Automatically detects and manages windows using `wmctrl`.
*   **⚖️ Balanced Productivity**:
    *   **Normal Mode**: Standard operation with no restrictions.
    *   **Focus Mode**: Automatically closes blacklisted distractions (e.g., Settings, App Center, Files).
    *   **Exam Mode**: High-security mode allowing only Terminals and Text Editors.
*   **🧩 Simple Integration**: Easy-to-configure whitelist and blacklist for personalized focus.

---

## 📽️ Demo Video

Experience Adaptive OS in action:

[![Adaptive OS Demo](https://img.shields.io/badge/Watch-Demo_Video-red?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/1XCu9v4UgnHoGUtYClahF3t8pd4cWlxM0/view?usp=sharing)

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x
- `wmctrl` (for window management)
- `tkinter` (for the UI)

```bash
# Install wmctrl on Linux
sudo apt-get install wmctrl
```

### Running the Application
Simply execute the main entry point:
```bash
python main.py
```

---

## 📁 Project Structure

- `main.py`: The entry point for the application.
- `backend/monitor.py`: The core engine that tracks and closes windows.
- `ui/popup.py`: A modern Tkinter interface for mode selection.
- `data/config.py`: Configuration file for whitelists and blacklists.

---

## 👥 Authors

*   **Surabhi M**
*   **Tanisha Bhide**

---

*Adaptive OS - Adapting your environment to your goals.*
