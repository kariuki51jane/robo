# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import math
from intersect import *
from math import atan2, degrees, pi
from shapely.geometry import LineString
from array import *
from motor import *

 
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
        
        thresh = cv2.threshold(blurred, 110, 255, cv2.THRESH_BINARY)[1]
        edges = cv2.Canny(thresh,100,200,apertureSize = 3)
        cv2.line(image,(0,0),(140,140),(255,77,0),3,cv2.CV_AA)
        cv2.line(image,(140,140),(280,0),(255,77,0),3,cv2.CV_AA)
        cv2.line(image,(140,140),(140,0),(255,255,0),1,cv2.CV_AA)
        cv2.circle(image,(280,0), 20, (100,120,255), 2)
        cv2.circle(image,(280,140), 20, (100,120,255), 2)
        cv2.circle(image,(0,0), 20, (100,120,255), 2)
        cv2.circle(image,(0,140), 20, (100,120,255), 2)
        
        
        
        '''if True:
           lines = cv2.HoughLinesP(edges, 1, math.pi/180.0, 10, np.array([]), 20, 10)[0]
           #a,b,c = lines.shape
           #for i in range(a):
            #   cv2.line(image, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.CV_AA)
           for x1,y1,x2,y2 in lines:
                   cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3,cv2.CV_AA)
                   dx = x2 - x1
                   dy = y2 - y1
                   rads = atan2(-dy,dx)
                   rads %= 2*pi
                   angle = int(degrees(rads))
                   print angle'''
        


        if True:
                
            lines = cv2.HoughLines(edges, 1, math.pi/180.0, 20, np.array([]), 0, 0)
            #a,b,c = lines.shape
            #for i in range(a):
            
            
            a,b,c = lines.shape
            for i in range(a):
                
                a,b,c = lines.shape
                print a
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0, y0 = a*rho, b*rho
                x1=int(x0+1000*(-b))
                y1 =int(y0+1000*(a))
                x2=int(x0-1000*(-b))
                y2=int(y0-1000*(a))
                pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
                pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
                cv2.line(image,pt1,pt2,(0,255,0),3,cv2.CV_AA)
               
                
                dx = x2 - x1
                dy = y2 - y1
                rads = atan2(-dy,dx)
                rads %= 2*pi
                angle = int(degrees(rads))
                #print angle
                #time.sleep(1)
                line1= LineString([(x1,y1),(x2,y2)])
                line2= LineString([(0,0),(140,140)])
                #print(line1.intersection(line2))
                
                intersect = (line1.intersection(line2))
                #map(int , intersect)
                
                x12 = x1 - x2
                x34 = 0 - 140
                x34r =140-280
                y12 = y1 - y2
                y34 = 0 - 140
                y34r =140-0
                c = x12 * y34 - y12 * x34
                c1 = x12 * y34r - y12 * x34r

                a = x1 * y2 - y1 * x2
                b = 0* 140 - 0* 140
                br =140*140-0*280
                if c or c1 >0.1:
                        x1 = (a * x34 - b * x12) / c;
                        y1 = (a * y34 - b * y12) / c;
                        x1r = (a * x34r - br * x12) / c1;
                        y1r = (a * y34r - br * y12) / c1;
                        #print x1
                        
                      
                        cv2.circle(image,(x1,y1), 20, (0,120,255), 2)

                        if((40<=x1<=60)or(400<=x1<=550)):
                                print ("forward")
                                clockwise()
                        elif(551<=x1<=1800):
                                print("left")
                                left()
                        elif(61<=x1<=80):
                                print("right")
                                right()

                '''if ((295<=angle<=300) or (65<=angle<=70)):
                        print "forward"
                elif((285<=angle<=291) or (55<=angle<=64)):
                        print "right"
                elif((300<=angle<=330) or (71<=angle<=85)):
                        print "left"
                else:
                        print "error"  '''
            '''
            for rho,theta in lines:
                
                    
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                cv2.line(image, (x1,y1), (x2,y2), (0, 255, 255), 3, cv2.CV_AA)
                dx = x2 - x1
                dy = y2 - y1
                rads = atan2(-dy,dx)
                rads %= 2*pi
                degs = degrees(rads)
                print degs'''

               
                
        #cv2.imshow("source", edges)
        #cv2.imshow("detected lines", image)
        key = cv2.waitKey(1) & 0xFF
                 
       # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
                 
       # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

