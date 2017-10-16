# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from decimal import Decimal
import cv2
import numpy as np
import imutils
import math
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
	image = image1[100:240,20:320]

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)>= 2:
                cnt1=contours[0]
                M1=cv2.moments(cnt1)

                cnt2=contours[1]
                M2=cv2.moments(cnt2)

                '''cnt3=contours[3]
                M3=cv2.moments(cnt3)'''
                '''rows,cols = image.shape[:2]
                [vx,vy,x,y] = cv2.fitLine(cnt, cv2.cv,0,0.01,0.01)
                lefty = int((-x*vy/vx) + y)
                righty = int(((cols-x)*vy/vx)+y)
                cv2.line(image,(cols-1,righty),(0,lefty),(0,255,0),2)'''
                M1x1 = int(M1['m10'])
                M1x2 = int(M1['m00'])
                M1y1 = int(M1['m01'])
                M1y2 = int(M1['m00'])

                M2x1 = int(M2['m10'])
                M2x2 = int(M2['m00'])
                M2y1 = int(M2['m01'])
                M2y2 = int(M2['m00'])
                if ((M1x1 and M1x2 and M1y1 and M1y2 and M2x1 and M2x2 and M2y1 and M2y2) != 0): 
                        #print M
                        cx = M1x1/M1x2
                        cy = M1y1/M1y2
                        #print cx , cy
                        cx1 = M2x1/M2x2
                        cy1 = M2y1/M2y2

                        #cx2 = int(M3['m10']/M3['m00'])
                        #cy2 = int(M3['m01']/M3['m00'])'''
                        
                        #area = cv2.contourArea(cnt)
                        #print area
                        cv2.drawContours(image,contours, -1, (0,255,0), 3)
                        cv2.circle(image,(cx,cy), 5, (0,0,255), -1)
                        cv2.circle(image,(cx1,cy1), 5, (0,0,255), -1)
                        cv2.circle(image,(cx,cy), 20, (0,120,255), 2)
                        cv2.circle(image,(cx1,cy1), 20, (0,120,255), 2)
                        cv2.circle(image,(160,240), 20, (255,120,255), -1)
                        cv2.line(image,(cx,cy),(160,240),(255,0,0),5)
                        cv2.line(image,(cx1,cy1),(160,240),(255,255,0),5)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        a=(240-cy)
                        b=(160-cx)
                        c=(cx1-160)
                        d=(240-cy1)

                        #x=float(((240-cy)** (2))+((160-cx)** (2)))
                        #y=float((cx1-160)** (2))+((240-cy1)** (2)))
                        A = math.pow(a,2)/100
                        B = math.pow(b,2)/100
                        C = math.pow(c,2)/100
                        D = math.pow(d,2)/100
                        #right=math.pow(y,2)/100
                        x=float(A+B)
                        y=float(C+D)

                        #ellipse = cv2.fitEllipse(cnt1)
                        #im = cv2.ellipse(image,ellipse,(50,100,200),2)

                        '''rows,cols = image.shape[:2]
                        [vx,vy,x,y] = cv2.fitLine(cnt1,cv2.cv.CV_DIST_L2,0,0.01,0.01)
                        lefty = int((-x*vy/vx) + y)
                        righty = int(((cols-x)*vy/vx)+y)
                        img = cv2.line(image,(cols-1,righty),(0,lefty),(255,0,0),2)'''
                        #angle1 = int(math.atan((240-cy)/(160-cx))*180/math.pi)
                        #angle2 = int(math.atan((240-cy1)/(160-cx1))*180/math.pi)
                        #print angle1 , angle2

                                                #cv2.norm(left, right,normType=CV_L2, mask=CV_8UC1)
                
                        xf=float(math.sqrt(x))
                        yf=float(math.sqrt(y))
                        print xf , yf
                        #cv2.putText(image,'xf',(100,100), font, 0.4,(255,255,255),1)
                        #cv2.putText(image,'yf',(100,120), font, 0.4,(255,255,255),1)
                        #cv2.circle(image,(cx2,cy2), 5, (0,0,255), -1)
                        #px= thresh[100,100]
                        #print px
                        #print image.shape
                        #p = 160-cx1
                        #print p
                        cv2.imshow('Draw',thresh)
                        cv2.imshow('mask1',image)
        
        else :
                cv2.imshow('mask1',image1)
                




	         #cv2.imshow("hough", )
        key = cv2.waitKey(1) & 0xFF
         
                # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
         
                # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break


