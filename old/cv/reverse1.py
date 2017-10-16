from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import imutils
import RPi.GPIO as GPIO
from motor import *

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
 

time.sleep(0.5)
def reverse():
        count=0
        white=0
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                # grab the raw NumPy array representing the image, then initialize the timestamp
                # and occupied/unoccupied text
                image1 = frame.array
                imageReverse =image1[170:200,20:280]

                grayReverse = cv2.cvtColor(imageReverse, cv2.COLOR_BGR2GRAY)
                blurredReverse = cv2.GaussianBlur(grayReverse, (5, 5), 0)
                threshReverse = cv2.threshold(blurredReverse, 20, 255, cv2.THRESH_BINARY)[1]
                contoursReverse, hierarchy = cv2.findContours(threshReverse,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                cv2.drawContours(image,contours, -1, (0,255,0), 3)
            
                if len(contoursReverse)>0 and white==2:
                        #hault()
                        clockwise()
                        time.sleep(0.1)
                        hault()
                        time.sleep(10)
                        break
                if len(contoursReverse)==0:
                    print "reverse"
                    counter_clockwise()
          
                if len(contoursReverse)>0:
                    print "Wdetect"
                    counter_clockwise()
                    white=1
                if len(contoursReverse)==0 and white==1:
                        print "2nd black"
                        counter_clockwise()
                        white=2


                key = cv2.waitKey(1) & 0xFF
                 
                        # clear the stream in preparation for the next frame
                rawCapture.truncate(0)
                 
                        # if the `q` key was pressed, break from the loop
                if key == ord("q"):
                        
                        break
                        
