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
        thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        grayR = cv2.cvtColor(imageR, cv2.COLOR_BGR2GRAY)
        blurredR = cv2.GaussianBlur(grayR, (5, 5), 0)
        threshR = cv2.threshold(blurredR, 100, 255, cv2.THRESH_BINARY)[1]
        contoursR, hierarchyR = cv2.findContours(threshR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        
        if len(contours)>0 :
                cnt1=contours[0]
                M1=cv2.moments(cnt1)
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        cv2.drawContours(imageL,contours, -1, (0,255,0), 3)
                        cv2.circle(imageL,(cx,cy), 5, (0,0,255), -1)
                        #cv2.circle(image,(140,70), 6, (255,120,255), -1)
                        cv2.line(imageL,(cx,cy+15),(cx,cy-15),(255,255,0),2)
                        cv2.line(imageL,(0,15),(120,15),(0,255,0),2)

                        x12 =cx- cx
                        y12=(cy+15)-(cy-15)
                        x34= 0 - 120
                        y34 =15-15
                        c = x12 * y34 - y12 * x34
                        a=cx*(cy-15)-((cy+15)*cx)
                        b=0*15-15*120

                                        
                        x = (a * x34 - b * x12) / c
                        y = (a * y34 - b * y12) / c
                        
                        print x
                        if(25<=x<=65):
                                print ("forward")
                        if(66<=x<=75):
                                print("right")
                                
                        if (15<=x<=24):
                                print ("left")
                        if(76<=x<=100):
                                print("hard right")
                        if(0<=x<=24):
                                print("hard left")
                       
                                
                        cv2.imshow('LEFT Threshold',thresh)
                        cv2.imshow('ROI LEFT',imageL)
                        #cv2.imshow('Video',image1)
        
       
        elif len(contoursR)>0 :
                cnt1=contoursR[0]
                M1=cv2.moments(cnt1)
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        cv2.drawContours(imageR,contoursR, -1, (0,255,0), 3)
                        cv2.circle(imageR,(cx,cy), 5, (0,0,255), -1)
                        #cv2.circle(image,(140,70), 6, (255,120,255), -1)
                        cv2.line(imageR,(cx,cy+15),(cx,cy-15),(255,255,0),2)
                        cv2.line(imageR,(0,15),(140,15),(0,255,0),2)

                        x12 =cx- cx
                        y12=(cy+15)-(cy-15)
                        x34= 0 - 120
                        y34 =15-15
                        c = x12 * y34 - y12 * x34
                        a=cx*(cy-15)-((cy+15)*cx)
                        b=0*15-15*120

                                        
                        x = (a * x34 - b * x12) / c
                        y = (a * y34 - b * y12) / c

                        print x
                        
                        if(95<=x<=115):
                                print ("forward")
                        if(85<=x<=94):
                                print("left")
                                
                        if (114<=x<=125):
                                print ("right")
                        if(40<=x<=84):
                                print("hard left")
                        if(126<=x<=135):
                                print("hard right")
                       
                                
                        cv2.imshow('Right Threshold',threshR)
                        cv2.imshow('ROI Right',imageR)
        
        else :
                print "out"
                cv2.imshow('mask1',image1)
                cv2.imshow('thresh',thresh)
                '''ser = serial.Serial('/dev/ttyACM0',9600)
                ser.write('7')'''
                

        #cv2.imshow('lane detection',path)

	         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                
                break
                


