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
	image = image1[100:240,160:300]
	image2 = image1[100:240,20:160]
	image3 = image1[100:240,20:300]


        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        blurred2 = cv2.GaussianBlur(gray2, (5, 5), 0)
        thresh = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)[1]
        thresh2 = cv2.threshold(blurred2, 50, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)== 1 :
                cnt1=contours[0]
                M1=cv2.moments(cnt1)
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        #ellipse = cv2.fitEllipse(cnt1)
                        rows,cols = image.shape[:2]
                        [vx,vy,x,y]=cv2.fitLine(cnt1,cv2.cv.CV_DIST_L2,0,0.01,0.01)
                        lefty = int((-x*vy/vx) + y)
                        righty =int(((cols-x)*vy/vx)+y)
                        
                        
                        #print cols-1 , righty ,rows ,lefty
                        cv2.line(image,(cols-1,righty),(0,lefty),(255,0,0),2)
                        angle = int(math.atan((righty-lefty)/((cols-1)-0))*180/math.pi)
                        print("right")
                        print angle
                        #cv2.ellipse(image,ellipse,(0,0,255),2)
                        cv2.drawContours(image,contours, -1, (0,255,0), 2)
                        cv2.circle(image,(cx,cy), 5, (0,0,255), -1)
                        
                        #cv2.line(image,(cx,cy),(160,140),(255,0,0),5)
                        
                        #cv2.imshow('DrawR',thresh)
                        cv2.imshow('right',image)
                

                
        if len(contours2)== 1 :
                cnt1=contours2[0]
                M1=cv2.moments(cnt1)
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        #ellipse = cv2.fitEllipse(cnt1)
                        rows,cols = image2.shape[:2]
                        [vx,vy,x,y]=cv2.fitLine(cnt1,cv2.cv.CV_DIST_L2,0,0.01,0.01)
                        lefty = int((-x*vy/vx) + y)
                        righty =int(((cols-x)*vy/vx)+y)
                        
                        
                        #print cols-1 , righty ,rows ,lefty
                        cv2.line(image2,(cols-1,righty),(0,lefty),(255,0,0),2)
                        angle = int(math.atan((righty-lefty)/((cols-1)-0))*180/math.pi)
                        print("left")
                        print angle
                        cv2.drawContours(image2,contours2, -1, (0,255,0), 3)
                        cv2.circle(image2,(cx,cy), 5, (0,0,255), -1)
                        
                        #cv2.line(image2,(cx,cy),(140,70),(255,0,0),5)
                      
                        #cv2.imshow('DrawL',thresh2)
                        cv2.imshow('Left',image2)
        if (len(contours)<=0 or len(contours2)<=0):
                cnt1=contours[0]
                M1=cv2.moments(cnt1)
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        cv2.drawContours(image3,contours, -1, (0,255,0), 3)
                        cv2.circle(image3,(cx,cy), 5, (0,0,255), -1)
                        cv2.circle(image3,(140,70), 6, (255,120,255), -1)
                        cv2.line(image3,(cx,cy),(140,70),(255,0,0),5)
                        a=(140-cy)
                        b=(70-cx)
                        A = math.pow(a,2)/100
                        B = math.pow(b,2)/100
                        x=float(A+B)
                        xf=float(math.sqrt(x))
                        
                        print(xf)
                        cv2.imshow('Full',image3)
                        '''if(11.1<=xf<=14.5):
                
                                Hleft()
                        if(5.5<=xf<=6.5):
                                
                                Hright()
                        if (9<= xf <= 11):
                                
                                Hleft()
                        if(6.6<=xf<=8.9):
                                
                                Hright()'''
                
                
        
        #else :
         #       cv2.imshow('Free1',image1)
                '''ser = serial.Serial('/dev/ttyACM0',9600)
                ser.write('7')'''
                




	         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                
                break
                


