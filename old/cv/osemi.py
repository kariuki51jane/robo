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
from motor import *
from buzz import *
from ardres import *
#from ardisend import *
import finput
from final import *
from sonarR import *


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
MIFAREReader = finput.MFRC522()

# allow the camera to warmup
time.sleep(0.5)

 
# capture frames from the camera
        #sonar()
while True:
    sonarR()
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

            
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image1 = frame.array
            #image = image1[100:240,20:300]
            imageL =image1[170:200,0:140]
            imageR =image1[170:200,140:280]

            gray = cv2.cvtColor(imageL, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)[1]
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

            grayR = cv2.cvtColor(imageR, cv2.COLOR_BGR2GRAY)
            blurredR = cv2.GaussianBlur(grayR, (5, 5), 0)
            threshR = cv2.threshold(blurredR, 100, 255, cv2.THRESH_BINARY)[1]
            contoursR, hierarchyR = cv2.findContours(threshR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                   
            #obs()
          
     

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
                            #cv2.drawContours(imageL,contours, -1, (0,255,0), 3)
                            #cv2.circle(imageL,(cx,cy), 5, (0,0,255), -1)
                            #cv2.circle(image,(140,70), 6, (255,120,255), -1)
                            #cv2.line(imageL,(cx,cy+15),(cx,cy-15),(255,255,0),2)
                            #cv2.line(imageL,(0,15),(120,15),(0,255,0),2)

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
                            if(24<=x<=44):
                                    print ("forward")
                                    clockwise()
                                    #fast()
                            if(45<=x<=55):
                                    print("right")
                                    right()
                                            
                            if (13<=x<=23):
                                    print ("left")
                                    left()
                            if(x>=56):
                                    print("hard right")
                                    Hright()
                            if(x<=12):
                                    print("hard left")
                                    Hleft()
                                   
                   
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
                                    #cv2.drawContours(imageR,contoursR, -1, (0,255,0), 3)
                                    #cv2.circle(imageR,(cx,cy), 5, (0,0,255), -1)
                                    
                                    #cv2.line(imageR,(cx,cy+15),(cx,cy-15),(255,255,0),2)
                                    #cv2.line(imageR,(0,15),(140,15),(0,255,0),2)

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
                                    
                            if(106<=x<=124):
                                    print ("forward")
                                    clockwise()
                            if(90<=x<=106):
                                    print("left")
                                    left()
                                            
                            if (125<=x<=140):
                                    print ("right")
                                    right()
                            if(69<=x<=89):
                                    print("hard left")
                                    Hleft()
                            if(x<=69):
                                    print("hard hard left")
                                    Hardleft()
                            if(x>=141):
                                    print("hard right")
                                    Hright()
                                   
                                            
                                    #cv2.imshow('DrawR',threshR)
                                    #cv2.imshow('mask1R',imageR)
                    
            else :
                            #time.sleep(0.2)
             
                    print "out"
                    hault()

                            
                            #MIFAREReader = finput.MFRC522()
                    time.sleep(0.1)
                    slow()
                    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                    if status == MIFAREReader.MI_OK:
                            buzz1()
                            time.sleep(0.1)
                            hault()
                            counter_clockwise()
                            time.sleep(0.3)
                            hault()
                            readRFID()
                            buzz2()
                            #v2.imshow('mask1',image1)
                            #cv2.imshow('thresh',thresh)
                            '''ser = serial.Serial('/dev/ttyACM0',9600)
                            ser.write('7')'''
                           
                    
          
                    

                             #cv2.imshow("hough", )
            key = cv2.waitKey(1) & 0xFF
                     
                            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
                     
                            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                            
                    break
            break
                            


