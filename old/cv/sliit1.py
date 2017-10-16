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
	imageL =image1[210:240,0:140]
	imageR =image1[210:240,180:320]
	path= image1[40:200,0:340]
        #cv2.imshow('left',imageL)
        #cv2.imshow('right',imageR)
        gray = cv2.cvtColor(imageL, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        grayR = cv2.cvtColor(imageR, cv2.COLOR_BGR2GRAY)
        blurredR = cv2.GaussianBlur(grayR, (5, 5), 0)
        threshR = cv2.threshold(blurredR, 220, 255, cv2.THRESH_BINARY)[1]
        contoursR, hierarchyR = cv2.findContours(threshR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        
        if len(contours)==1 :
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
                        if(48<=x<=68):
                                print ("forward")
                        if(69<=x<=96):
                                print("right")
                                
                        if (20<=x<=47):
                                print ("left")
                        if(x>=97):
                                print("hard right")
                        if(x<=19):
                                print("hard left")
                       
                                
                        cv2.imshow('LEFT Threshold',thresh)
                        cv2.imshow('ROI LEFT',imageL)
                        #cv2.imshow('Video',image1)

        
        elif len(contoursR)==1 :
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
                        
                        if(66<=x<=86):
                                print ("forward")
                        if(38<=x<=65):
                                print("left")
                                
                        if (87<=x<=114):
                                print ("right")
                        if(x<=37):
                                print("hard left")
                        if(x>=114):
                                print("hard right")
                       
                                
                        cv2.imshow('Right Threshold',threshR)
                        cv2.imshow('ROI Right',imageR)

        elif len(contours)==2 and len(contoursR)==0:
                
                print "RFID activated"
                #cv2.imshow('Video',image1)
                
        elif len(contoursR)==2 and len(contours)==0:
                
                print "RFID activated"
                #cv2.imshow('Video',image1)
        #elif len(contours)==2 or len(contoursR)==2:
        #       print "speed mark detect"
                
         #       cv2.imshow('Video',image1)
        elif len(contoursR)>2 or len(contours)>2:
                cv2.imshow('ROI Right',image1)
                print "woooow"
        else :
                print "out"
                cv2.imshow('mask1',image1)
                cv2.imshow('thresh',imageR)
                
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
                


