from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from decimal import Decimal
import cv2
import numpy as np
import imutils
import math
#import RPi.GPIO as GPIO

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
 
# allow the camera to warmup
time.sleep(0.5)

 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image1 = frame.array

        hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(image1,image1, mask= mask)
        cv2.imshow('frame',image1)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                
                break
                
