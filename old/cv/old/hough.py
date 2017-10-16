# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
 
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
        
        thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)[1]
        edges = cv2.Canny(thresh,100,200,apertureSize = 3)
        #laplacian = cv2.Laplacian(gray,cv2.CV_64F)
                
        minLineLength = 200
        maxLineGap = 10
        lines = cv2.HoughLinesP(edges,1,np.pi/180,2,minLineLength,maxLineGap)[0]
        for x1,y1,x2,y2 in lines:
                print x1 ,y1
                cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)



        
                # show the frame
                cv2.imshow("canny", edges)
                        
                cv2.imshow("hough", image)
                key = cv2.waitKey(1) & 0xFF
                 
                 # clear the stream in preparation for the next frame
                rawCapture.truncate(0)
                 
                 # if the `q` key was pressed, break from the loop
                if key == ord("q"):
                            break
