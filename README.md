# Mullvad VPN Alert Script

This Python script monitors the connection status of **Mullvad VPN** and alerts you with a sound when it disconnects.

## Features
- Monitors Mullvad VPN connection status
- Plays a sound alert when the VPN disconnects
- Customizable alert sound

## Prerequisites
Before running the script, ensure that you have the following installed:
- **Python 3.x** (preferably Python 3.6 or later)
- **pygame** (for playing sound)

### Installation

1. **Install Python (if not already installed)**:
   - On **Linux** (Ubuntu/Debian-based):
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

   - On **macOS** (if Python 3 isn't installed):
     ```bash
     brew install python3
     ```

   - On **Windows**, you can download Python from [here](https://www.python.org/downloads/).

2. **Install pygame**:
   Pygame is used for playing sound alerts. Install it via pip:
   ```bash
   pip3 install pygame
   ```
   
## Setting Up the Alert Sound

The script uses an MP3 file to play an alert when Mullvad VPN disconnects. By default, the script points to `/home/samsep10l/loud.mp3` for the alert sound.

### To replace the sound with your own:

1. **Prepare your MP3 file:**  
   - Place your custom MP3 file somewhere accessible on your computer.  
   - For example, you can store it in your Music folder or any other directory.

2. **Edit the script:**  
   - Open the `alert_mullvad.py` file and update the `alert_sound` variable with the path to your own MP3 file:

     ```python
     alert_sound = "/path/to/your/alert-sound.mp3"
     ```

   - Make sure the file path points to your new MP3 file.

## Running the Script

1. Open a terminal and navigate to the directory where the script is saved:

   ```bash
   cd /path/to/your/script
   ```

   ```bash
   python3 alert_mullvad.py
   ```

   - The script will check if Mullvad VPN is connected every 5 seconds. If it disconnects, it will play the alert sound you configured.


## Proof of Concept


https://github.com/user-attachments/assets/d1c536a2-5290-4d5c-a63c-22d910472a8e


   


   
