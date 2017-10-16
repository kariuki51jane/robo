# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO        # calling for header file for GPIO’s of PI
import time
#from sonar import *
#from sonar1 import *# calling for time to provide delays in program
GPIO.setwarnings(False)          # do not show any warnings
GPIO.setmode (GPIO.BOARD)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)     # initialize GPIO19 as an output
R = GPIO.PWM(12,50)              # GPIO19 as PWM output, with 50Hz frequency
R.start(2.5)
L = GPIO.PWM(26,50)              # GPIO19 as PWM output, with 50Hz frequency
L.start(13.5)                   # generate PWM signal with 7.5% duty cycle
while True:                                                       # execute loop forever                                    
        L.ChangeDutyCycle(13.5)
        R.ChangeDutyCycle(2.5)   # change duty cycle for getting the servo position to 90º
        time.sleep(1)                                      # sleep for 1 second
        L.ChangeDutyCycle(10.5)
        R.ChangeDutyCycle(4.5)
        #sonar()                                                 
        #sonarR()
        time.sleep(1)
        L.ChangeDutyCycle(9.5)
        R.ChangeDutyCycle(5.5)   # change duty cycle for getting the servo position to 180º
        #sonar()                                                 
        #sonarR()
        time.sleep(1)# sleep for 1 second
        L.ChangeDutyCycle(8.5)
        R.ChangeDutyCycle(6.5)   # change duty cycle for getting the servo position to 180º
        #sonar()                                                 
        #sonarR()
        time.sleep(1)
        L.ChangeDutyCycle(7.5)
        R.ChangeDutyCycle(7.5)   # change duty cycle for getting the servo position to 180º
        #sonar()                                                 
        #sonarR()
        time.sleep(1)
        L.ChangeDutyCycle(6.5)
        R.ChangeDutyCycle(8.5)  # change duty cycle for getting the servo position to 0º
        #sonar()                                                 
        #sonarR()
        time.sleep(1)                  # sleep for 1 second
        
       
