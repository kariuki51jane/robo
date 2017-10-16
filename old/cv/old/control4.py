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
import serial
from motor import *
import finput
from final import *


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
	image = image1[100:240,30:310]
	

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        thresh = cv2.threshold(blurred, 75, 255, cv2.THRESH_BINARY)[1]
        
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
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
                                cv2.drawContours(image,contours, -1, (0,255,0), 3)
                                cv2.circle(image,(cx,cy), 5, (0,0,255), -1)
                                cv2.circle(image,(140,70), 6, (255,120,255), -1)
                                cv2.line(image,(cx,cy),(140,70),(255,0,0),5)
                                a=(140-cy)
                                b=(70-cx)
                                A = math.pow(a,2)/100
                                B = math.pow(b,2)/100
                                x=float(A+B)
                                xf=float(math.sqrt(x))
                                print(xf)
                                if(11.1<=xf<=14.5):
                        
                                        Hleft()
                                if(5.5<=xf<=6.5):
                                        
                                        Hright()
                                if (9<= xf <= 11):
                                        
                                        Hleft()
                                if(6.6<=xf<=8.9):
                                        
                                        Hright()
                                        #cv2.imshow('road',image)
        elif len(contours)<=2 :
                cnt1=contours[0]
                cnt2=contours[1]
                M1=cv2.moments(cnt1)
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        
                        rows,cols = image.shape[:2]
                        [vx1,vy1,x1,y1]=cv2.fitLine(cnt1,cv2.cv.CV_DIST_L2,0,0.01,0.01)
                        [vx2,vy2,x2,y2]=cv2.fitLine(cnt2,cv2.cv.CV_DIST_L2,0,0.01,0.01)
                        lefty1 = int((-x1*vy1/vx1) + y1)
                        righty1 =int(((cols-x1)*vy1/vx1)+y1)
                        lefty2 = int((-x2*vy2/vx2) + y2)
                        righty2 =int(((cols-x2)*vy2/vx2)+y2)
                        
                        
                        #print cols-1 , righty ,rows ,lefty
                        cv2.line(image,(cols-1,righty1),(0,lefty1),(255,0,0),2)
                        
                        cv2.line(image,(cols-1,righty2),(0,lefty2),(255,255,0),2)
                        angle1 = int(math.atan((righty1-lefty1)/((cols-1)-0))*180/math.pi)
                        angle2 = int(math.atan((righty2-lefty2)/((cols-1)-0))*180/math.pi)
                        #print("right")
                        if angle1<0:
                                #print (-angle1)
                                angle1 = -angle1
                        
                        #print("left")
                        if angle2<0:
                                #print (-angle2)
                                angle2 = -angle2
                        print angle1
                        print angle2
                        if 60<=angle1<=75 and 60<=angle2<=75 :
                                print "foarward"
                                clockwise()
                        elif 60<=angle1<=75 and 40<=angle2<=50 :
                                print "foarward"
                                clockwise()
                        elif 40<=angle1<=50 and 80<=angle2<=90 :
                                print "foarward"
                                clockwise()
                        elif angle1>=81 and 40<=angle2<=65 :
                                print "left"
                                left()
                        elif angle1>=76:
                                print "right"
                                right()
                        
                                
                        elif angle2>=76:
                                print "left"
                                left()
                        else:
                                print "error"
                        #cv2.ellipse(image,ellipse,(0,0,255),2)
                        cv2.drawContours(image,contours, -1, (0,255,0), 2)
                        #cv2.circle(image,(cx,cy), 5, (0,0,255), -1)
                        
                        #cv2.line(image,(cx,cy),(160,140),(255,0,0),5)
                        
                        #cv2.imshow('DrawR',thresh)
                        #cv2.imshow('road',image)

                                
        else :
                cv2.drawContours(image,contours, -1, (0,255,0), 2)
                #cv2.imshow('Free',image)



	         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                
                break
                


