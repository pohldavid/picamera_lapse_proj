#! /usr/bin/python3

import os
import datetime
import time
from pathlib import Path
import fakepicamera as picamera


def lapse(lapse_interval, total_frames, target_folder):
    """specify lapse interval in seconds, total number of frames to be captured
        target folder """

    with picamera.PiCamera() as camera:
        
        # camera.led = False
        camera.rotation = 90
        camera.vflip=False
        camera.hflip=False
        camera.start_preview()  # I suppose it settles the sensor ?
        time.sleep(2)
    
        counter = 0
        
        for filename in camera.capture_continuous(target_folder + "/img{counter:05d}.jpg"):
            print("Captured %s" % filename)
            print("counter", counter)
            counter += 1
            if counter == total_frames:
                break
            time.sleep(lapse_interval)


lapse(3,100,"./")