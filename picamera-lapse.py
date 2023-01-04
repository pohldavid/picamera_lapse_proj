#! /usr/bin/python3

import os
import datetime
import time
from pathlib import Path
import picamera

home_folder = os.environ["HOME"]

# for running as root
#home_folder = '/home/pi'

base_folder = "Time_Lapse"

today = datetime.datetime.now().strftime("%Y-%m-%d")  # e.g. 2023-01-01

""" define a folder to hold all time lapse sequences """
lapse_folder = home_folder + "/Pictures/Time_Lapse/" + today

"""Make a folder for today"""
if not Path(lapse_folder).exists():
    Path.mkdir(Path(lapse_folder), parents=True)

time_now = datetime.datetime.now().strftime("%I-%M-%S%p%Z")  # e.g.

now_folder = lapse_folder + "/" + time_now  # e.g. 2023-01-01

"""Make a folder for the current time lapse"""
if not Path(now_folder).exists():
    Path.mkdir(Path(now_folder), parents=True)

with picamera.PiCamera() as camera:
    # camera.led = False
    camera.rotation = 90
    # camera.vflip=True
    # camera.hflip=True
    camera.start_preview()  # I suppose it settles the sensor ?
    time.sleep(2)

    counter = 0
    lapse_interval = 3
    recording_duration = 60 * 60 # minutes * 60
    total_frames = recording_duration / lapse_interval
    print(f"Capturing {total_frames} frames in {recording_duration} seconds using a lapse interval of {lapse_interval} of seconds.")

    for filename in camera.capture_continuous(now_folder + "/img{counter:05d}.jpg"):
        print("Captured %s" % filename)
        print("counter", counter)
        counter += 1
        if counter == total_frames:
            break
        time.sleep(lapse_interval)
