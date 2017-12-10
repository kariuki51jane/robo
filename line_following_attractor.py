import RPi.GPIO as GPIO
from time import sleep
import drive

#IR Semsors
GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(13, GPIO.IN)    #SO2
GPIO.setup(15, GPIO.IN)    #S03
GPIO.setup(19, GPIO.IN)    #SO4
GPIO.setup(21, GPIO.IN)    #SO5

speed=50

def forward():
    drive.SetSpeed(speed,speed)
def slight_turn_right():
    drive.SetSpeed(speed,-speed/4)

def sharp_turn_right():
     drive.SetSpeed(speed,-speed)
    
def sharp_turn_left():
    drive.SetSpeed(-speed,speed)
    
    
def slight_turn_left():
    drive.SetSpeed(-speed/4,speed)
    

try:

  while True:
    s1=GPIO.input(11)
    s2=GPIO.input(13)
    s3=GPIO.input(15)
    s4=GPIO.input(19)
    s5=GPIO.input(21)
    
    if(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
        pass #line finding 
    elif(s1==0)and(s2==0)and(s3==1)and(s4==0)and(s5==0):
        forward()
    elif(s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
        forward()
    elif(s1==0)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
        forward()
    elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==0):
        forward()
    elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==1):
        sharp_turn_right()
    elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==0):
        sharp_turn_right()
    elif(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==1):
        sharp_turn_right()
    elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==1):
        sharp_turn_right()
    elif(s1==1)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
        sharp_turn_left()
    elif(s1==0)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
        sharp_turn_left()
    elif(s1==1)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
        sharp_turn_left()
    elif(s1==1)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
        sharp_turn_left()
    
    
    else:
        drive.stop()
    
       
except:
    drive.stop()
