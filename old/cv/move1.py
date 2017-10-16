# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from motor import *

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
history=10
# allow the camera to warmup
time.sleep(0.5)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
B = cv2.BackgroundSubtractorMOG2() 
# capture frames from the camera

counter=0
counter1=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
        value=0
        if counter1==1:
                counter1==1
        else:
                counter1=0
	image = frame.array
	img=image[60:200,0:320]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        #thresh = cv2.threshold(blurred, 100, 150, cv2.THRESH_BINARY)[1]
        pp = B.apply(gray,learningRate=1.0/history)
        cnts, hierarchy = cv2.findContours(pp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(img,(20,0),(20,200),(0,255,0),2)
        cv2.line(img,(300,0),(300,200),(0,255,0),2)
        
        if len(cnts) > 0:
                

            c = max(cnts, key=cv2.contourArea)
            M1 = cv2.moments(c)
            M1x1 = int(M1['m10'])
            M1x2 = int(M1['m00'])
            M1y1 = int(M1['m01'])
            M1y2 = int(M1['m00'])
            
            if ((M1x1 and M1x2 and M1y1 and M1y2 ) != 0):
                    cx = M1x1/M1x2
                    cy = M1y1/M1y2
                    if 20<=cx<=300:
                            value=1
                            counter1=1

                    if cx>300 and counter1==1:
                            value=2
                    if cx<20 and counter1==1:
                            value=2
                    
            cv2.line(img,(cx+40,cy),(cx-40,cy),(255,255,0),2)
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
            '''
            x12=(cx+40)-(cx-40)
            y12=cy-cy
            x34=20-20
            y34=0-200
            c = x12 * y34 - y12 * x34
            a=((cx-40)*cy)-((cx+40)*cy)
            b=0*20-20*200
            x = (a * x34 - b * x12) / c
            y = (a * y34 - b * y12) / c
            print x,y'''

            #(x,y,w,h) = cv2.boundingRect(c)
        
            #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

        if value==0:
                counter=counter+1
                if counter >=200 :
                        print "go"
                        clockwise()
                        
        elif value==1:
                print "halt"
                hault()
        elif value==2 :
                print "object pass"
                clockwise()
                
        else:
                print "error"

        #cv2.imshow('mask',pp)
        #cv2.imshow('mask1',img)
        

        
       


	         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
