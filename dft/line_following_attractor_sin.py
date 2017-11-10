import RPi.GPIO as GPIO
from time import sleep
import drive
import math

#IR Semsors
GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(13, GPIO.IN)    #SO2
GPIO.setup(15, GPIO.IN)    #S03
GPIO.setup(19, GPIO.IN)    #SO4
GPIO.setup(21, GPIO.IN)    #SO5

speed = 50 # constant forward speed
lamda = 0.3 # turning rate factor


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
        angle_difference=0
    elif(s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
        angle_difference=0
    elif(s1==0)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
        angle_difference=-10
    elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==0):
        angle_difference=10
    elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==1):
        angle_difference=30
    elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==0):
        angle_difference=30
    elif(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==1):
        angle_difference=30
    elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==1):
        angle_difference=30
    elif(s1==1)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
        angle_difference=-30
    elif(s1==0)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
        angle_difference=-30
    elif(s1==1)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
        angle_difference=-30
    elif(s1==1)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
        angle_difference=-30

    pi=math.pi
    angle_difference=45
    d_phi = lamda * (-math.sin(pi*(angle_difference)/180))
    v_mm_per_second = d_phi/math.pi * 53
    v_pulses_per_second = v_mm_per_second / 0.13

    print(-v_pulses_per_second + speed, v_pulses_per_second + speed)
    drive.SetSpeed(-v_pulses_per_second + speed, v_pulses_per_second + speed)
 
    
    else:
        drive.stop()
    
       
except:
    drive.stop()





