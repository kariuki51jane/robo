# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
#import imutils
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

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #Define the threshold for finding a blue object with hsv
        lower_blue = np.array([110,100,100])
        upper_blue = np.array([130,255,255])

        #Create a binary image, where anything blue appears white and everything else is black
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        #Get rid of background noise using erosion and fill in the holes using dilation and erode the final image on last time
        element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        mask = cv2.erode(mask,element, iterations=2)
        mask = cv2.dilate(mask,element,iterations=2)
        mask = cv2.erode(mask,element)
        
        #Create Contours for all blue objects
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        maximumArea = 0
        bestContour = None
        for contour in contours:
            currentArea = cv2.contourArea(contour)
            if currentArea > maximumArea:
                bestContour = contour
                maximumArea = currentArea
         #Create a bounding box around the biggest blue object
        if bestContour is not None:
            x,y,w,h = cv2.boundingRect(bestContour)
            cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 3)

        #Show the original camera feed with a bounding box overlayed 
        cv2.imshow('frame',frame)
        #Show the contours in a seperate window
        cv2.imshow('mask',mask)





	         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
