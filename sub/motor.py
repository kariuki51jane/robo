import RPi.GPIO as GPIO
import time
import drive


GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(13, GPIO.IN)    #SO2
GPIO.setup(15, GPIO.IN)    #S03
GPIO.setup(19, GPIO.IN)    #SO4
GPIO.setup(21, GPIO.IN)    #SO5



drive.SetSpeed(50,0)
time.sleep(0.8)
drive.SetSpeed(50,50)
time.sleep(0.05)
drive.SetSpeed(0,50)
time.sleep(1)
drive.SetSpeed(50,50)
time.sleep(0.25)

    
    




