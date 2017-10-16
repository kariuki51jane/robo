# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from decimal import Decimal
import cv2
import numpy as np
import imutils
import math
import RPi.GPIO as GPIO
import socket
import serial
#from motor import *

# initialize the camera and grab a reference to the raw camera capture
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

	#image = image1[100:240,20:300]
	imageL =image1[170:200,0:140]
	imageR =image1[170:200,140:280]
	path= image1[40:200,0:340]
        #cv2.imshow('left',imageL)
        #cv2.imshow('right',imageR)
        gray = cv2.cvtColor(imageL, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 20, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        grayR = cv2.cvtColor(imageR, cv2.COLOR_BGR2GRAY)
        blurredR = cv2.GaussianBlur(grayR, (5, 5), 0)
        threshR = cv2.threshold(blurredR, 20, 255, cv2.THRESH_BINARY)[1]
        contoursR, hierarchyR = cv2.findContours(threshR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	         #cv2.imshow("hough", )
        cv2.drawContours(imageL,contours, -1, (0,255,0), 3)
        cv2.drawContours(imageR,contoursR, -1, (0,255,0), 3)
        cv2.circle(imageR,(cx,cy), 5, (0,0,255), -1)
        cv2.circle(imageL,(cx,cy), 5, (0,0,255), -1)
                        #cv2.circle(image,(140,70), 6, (255,120,255), -1)
        cv2.line(imageL,(cx,cy+15),(cx,cy-15),(255,255,0),2)
        cv2.line(imageL,(0,15),(120,15),(0,255,0),2)
                        #cv2.circle(image,(140,70), 6, (255,120,255), -1)
        cv2.line(imageR,(cx,cy+15),(cx,cy-15),(255,255,0),2)
        cv2.line(imageR,(0,15),(140,15),(0,255,0),2)
        cv2.imshow('LROI',imageL)
        cv2.imshow('RROI',imageR)
        

        
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                
                break
                        
