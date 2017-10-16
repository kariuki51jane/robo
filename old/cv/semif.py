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
from obsturn import *
#from ardisend import *
import finput
from final import *
from sonarR import *
from obsgo import *
#from sonarL import *


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
MIFAREReader = finput.MFRC522()
irpin=12

GPIO.setup(irpin,GPIO.IN)

# allow the camera to warmup
time.sleep(0.5)

 
# capture frames from the camera
        #sonar()
detectdoubleS=0
detectdoubleS1=0
brake1=0
brake2=0
brakeRFID=0
scan=1
count=0
white=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        reverse=0
        image1 = frame.array
        ##### OBSATACLE CHECKING#############################
        '''
        if scan==1:
                print "collision avoidance system activated"
                obstacle=0
                brake1=0
                while True:
                        if sonarR1() >=30:
                                brake1=0
                                break
                        else:
                                print "Obstacle detected"
                                if brake1==0:
                                        brake()
                                        time.sleep(0.4)
                                        brake1=1
                                hault()
                                buzz1()
                                obstacle=obstacle+1
                                if obstacle==10:
                                        print "trurn"
                                        #turn()
                                        #obsright()
                                        #time.sleep(2)
                                        turn()
                                        hault()
                                        time.sleep(2)
                                        reverse=1
        if reverse==1:
                print "oyeeeee"
                while True:
                        IR=GPIO.input(irpin)
                        if IR==1:
                                counter_clockwise()
                                brake2=0
                        if IR==0:
                                if brake2==0:
                                        brake()
                                        time.sleep(0.3)
                                        brake2=1
                                counter_clockwise()
                                time.sleep(0.2)
                                brakeF()
                                time.sleep(0.5)
                                hault()
                                obsgo()
                                turn1()
                                break
                        
                
        
        '''
        ######### OBSTACLE CHECKING END ###############################
       
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        
        #image = image1[100:240,20:300]
        imageL =image1[210:240,0:140]
        imageR =image1[210:240,180:320]

        gray = cv2.cvtColor(imageL, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        grayR = cv2.cvtColor(imageR, cv2.COLOR_BGR2GRAY)
        blurredR = cv2.GaussianBlur(grayR, (5, 5), 0)
        threshR = cv2.threshold(blurredR, 120, 255, cv2.THRESH_BINARY)[1]
        contoursR, hierarchyR = cv2.findContours(threshR,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
               
        #obs()
      
 

        if len(contours)==1 :
                brake1=0
                
                if detectdoubleS1==1:
                        detectdoubleS=1
                if detectdoubleS1==2:
                        detectdoubleS=0

                        
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
                        if(48<=x<=68):
                                print ("forward")
                                clockwise()
                                #fast()
                        if(69<=x<=96):
                                print("right")
                                right()
                                        
                        if (20<=x<=47):
                                print ("left")
                                left()
                        if(x>=97):
                                print("hard right")
                                Hright()
                        #if(x>=91):
                         #       print ("HARD RIGHT")
                          #      turn3R()
                        #if(x>=131):
                         #       print("motor stop")
                        if(x<=19):
                                print("hard left")
                                turn1HL()
                               
               
        elif len(contoursR)==1 :
                brake1=0
                
                if detectdoubleS1==1:
                        detectdoubleS=1
                if detectdoubleS1==2:
                        detectdoubleS=0

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
                                
                        if(66<=x<=86):
                                print ("forward")
                                clockwise()
                        if(38<=x<=65):
                                print("left")
                                left()
                                        
                        if (87<=x<=114):
                                print ("right")
                                right()
                        if(x<=37):
                                print("hard left")
                                Hleft()
                        #if(x<=69):
                         #       print("hard hard left")
                                Hardleft()
                        if(x>=114):
                                print("hard right")
                                Hright()
                               
                                        
                                #cv2.imshow('DrawR',threshR)
                                #cv2.imshow('mask1R',imageR)

        elif len(contours)==2 and len(contoursR)==0:
                
                print "RFID activated"
                if brakeRFID==0:
                        brake()
                        time.sleep(0.5)
                        brakeRFID=1
                        
                slow()
                time.sleep(0.1)
                hault()

                        
                        #MIFAREReader = finput.MFRC522()
                time.sleep(0.1)
                #slow()
                (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                if status == MIFAREReader.MI_OK:
                        buzz1()
                        clockwise()
                        time.sleep(0.2)
                        hault()
                        #counter_clockwise()
                        #time.sleep(0.3)
                        #hault()
                        readRFID()
                        buzz2()
                        brakeRFID=0
        
        elif len(contours)==0 and len(contoursR)==2:
                
                print "RFID activated"
                if brakeRFID==0:
                        brake()
                        time.sleep(0.5)
                        brakeRFID=1
                        
                slow()
                time.sleep(0.1)
                hault()

                        
                        #MIFAREReader = finput.MFRC522()
                time.sleep(0.1)
                #slow()
                (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                if status == MIFAREReader.MI_OK:
                        buzz1()
                        time.sleep(0.1)
                        hault()
                        #counter_clockwise()
                        #time.sleep(0.3)
                        #hault()
                        readRFID()
                        buzz2()
                        brakeRFID=0
                
                        

        #elif len(contours)>2 or len(contoursR)>2:
         #       print "det"
                '''
                if detectdoubleS==0:
                        scan=2
                        detectdoubleS1=1
                        print "start slow"
                        
                        if brake1==0:
                                brake()
                                time.sleep(0.5)
                                brake1=1
                        
                        slow()
                        
                        
                        
                if detectdoubleS==1:
                        scan=1
                        detectdoubleS1=2
                        print "boost"
                        slow()
                '''
        elif len(contours)==0 or len(contoursR)==0:
                print "RFID activated"
                if brakeRFID==0:
                        brake()
                        time.sleep(0.5)
                        brakeRFID=1
                        
                slow()
                time.sleep(0.1)
                hault()

                        
                        #MIFAREReader = finput.MFRC522()
                time.sleep(0.1)
                (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
                if status == MIFAREReader.MI_OK:
                        buzz1()
                        clockwise()
                        time.sleep(0.2)
                        hault()
                        #counter_clockwise()
                        #time.sleep(0.3)
                        #hault()
                        readRFID()
                        buzz2()
                        brakeRFID=0
                        #v2.imshow('mask1',image1)
                        #cv2.imshow('thresh',thresh)
                        '''ser = serial.Serial('/dev/ttyACM0',9600)
                        ser.write('7')'''
                       
                
        else:
                print "ERROR... SYSTEM STOPED "
                

                         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
                 
                        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
                 
                        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                        
                break
                        


