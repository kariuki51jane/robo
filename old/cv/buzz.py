import RPi.GPIO as GPIO
import time
 
#initialisiere GPIO
pin=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def buzz1():
    for x in range(0,1) :
        GPIO.output(pin,True)
        time.sleep(0.1)
        GPIO.output(pin,False)
        time.sleep(0.1)
        #GPIO.cleanup()
        x=x+1

def buzz2():
    for x in range(0,1) :
        GPIO.output(pin,True)
        time.sleep(0.4)
        GPIO.output(pin,False)
        time.sleep(0.1)
        #GPIO.cleanup()
        x=x+1
    
