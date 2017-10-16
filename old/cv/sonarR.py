import RPi.GPIO as GPIO
import time
from motor import *
from buzz import *
from obsturn import *
#from reverse1 import *
GPIO.setmode(GPIO.BOARD)

TRIG = 10
ECHO = 8

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

def sonarR():
  obstacle=0
  brake1=0

  #print "Waiting For Sensor To Settle"
  #time.sleep(2)
  while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()



    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance R:",distance,"cm"
    
  
    if distance >=30:
      brake1=0
      break
    else:
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
      
        #return reverseValue
        #reverse()

  #return distance

def sonarR1():
  counter=0
  #print "Waiting For Sensor To Settle"
  #time.sleep(2)
  while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()



    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    #print "Distance R:",distance,"cm"
    break
  return distance 
  #GPIO.cleanup()
