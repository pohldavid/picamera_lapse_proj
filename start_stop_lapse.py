#! /usr/bin/python3
"""
 ____   ____ ____    ____   ___ ____  _____        ___ _____       _ _  _   
|  _ \ / ___|  _ \  |___ \ / _ \___ \|___ /       / _ \___ /      / | || |  
| | | | |  _| |_) |   __) | | | |__) | |_ \ _____| | | ||_ \ _____| | || |_ 
| |_| | |_| |  __/   / __/| |_| / __/ ___) |_____| |_| |__) |_____| |__   _|
|____/ \____|_|     |_____|\___/_____|____/       \___/____/      |_|  |_|  

make executable and 
add the following to /etc/rc.local

/path-to-script/reboot_shutdown.py

"""                                                                            
import os
import time
from signal import pause
from gpiozero import Button

button = Button(26) # a momentary button

def reboot():
    os.system("reboot")

def turn_off():
    os.system("shutdown -h now")

def turn_off_or_reboot():
    print("button pressed")
    time.sleep(3)
    if button.is_pressed:
        print("Turn off")
        turn_off()
    else:
        print("reboot")
        reboot()
    
button.when_pressed = turn_off_or_reboot

pause()