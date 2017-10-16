# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
        lower_red = np.array([0,0,255])
        upper_red = np.array([120,10,220])
        
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(image,image, mask= mask)

        cv2.imshow('frame',image)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
