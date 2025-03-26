import os
import time
import subprocess
import pygame

# Initialize pygame mixer with no welcome message
pygame.init()
pygame.mixer.init()
alert_sound = "/home/samsep10l/loud.mp3"  # Your alert sound file

def is_mullvad_connected():
    """Check Mullvad VPN status."""
    try:
        result = subprocess.run(["mullvad", "status"], capture_output=True, text=True)
        return "Connected" in result.stdout
    except Exception as e:
        print(f"[ERROR] Failed to check Mullvad status: {e}")
        return False

def play_alert():
    """Play the alert sound when VPN disconnects."""
    pygame.mixer.music.load(alert_sound)
    pygame.mixer.music.play()

# Check initial status
status = is_mullvad_connected()
if status:
    print("[INFO] Mullvad VPN is currently CONNECTED.")
else:
    print("[WARNING] Mullvad VPN is currently DISCONNECTED!")

previous_status = status

# Monitor VPN status
while True:
    current_status = is_mullvad_connected()
    
    if previous_status and not current_status:
        print("[ALERT] Mullvad VPN Disconnected! Playing alert sound.")
        play_alert()
    
    previous_status = current_status
    time.sleep(5)  # Check every 5 seconds

