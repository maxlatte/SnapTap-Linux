# SnapTap
A snaptap script for Linux written in Python.


SnapTap-Linux

A lightweight Python-based SOCD (Simultaneous Opposite Cardinal Direction) cleaner for Linux. This script brings "Snap Tap" functionality to any keyboard (specifically tested on the Razer Huntsman Mini) by intercepting raw input events at the kernel level.
🚀 Features

    Zero-Latency Logic: Intercepts evdev events directly.

    Directional Priority: If A and D are held simultaneously, the last key pressed takes priority.

    Resume Logic: Releasing the priority key automatically resumes the movement of the still-held opposite key.

    Hardware Agnostic: Works on any keyboard by pointing to the correct /dev/input/event* node.

📋 Prerequisites

You will need Python 3 and the evdev library installed on your system.


For Arch / CachyOS:

sudo pacman -S python-evdev


For Debian / Ubuntu:

sudo apt install python3-evdev


🛠️ Setup & Usage
1. Identify your Keyboard

Run the following command to find which eventX node corresponds to your keyboard's main input:

sudo python -m evdev.evtest

Look for the device name (e.g., Razer Razer Huntsman Mini Keyboard) and note the event number (e.g., event6).
2. Configure the Script

Open snaptap.py and update the DEVICE_PATH variable:
Python

DEVICE_PATH = '/dev/input/event6'  # Replace with your event number

3. Run the Script

The script requires root privileges to "grab" the device and create a virtual input.

sudo python snaptap.py

🐧 Autostart (Hyprland / Sway)

To run this automatically on login with a graphical password prompt, add this to your config:

exec-once = pkexec python /path/to/snaptap.py

⚠️ Important Disclaimer

Game Integrity: Using software-based SOCD cleaners may be against the Terms of Service for certain competitive games (e.g., Counter-Strike 2). Use at your own risk. This project is for educational and accessibility purposes.
