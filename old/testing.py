
import RPi.GPIO as GPIO
import time

enable_LFpin =38
in1_LFpin = 33
in2_LFpin =31

enable_LRpin =40
in1_LRpin = 37
in2_LRpin =35

enable_RRpin =32
in1_RRpin = 16
in2_RRpin =15

enable_RFpin =36
in1_RFpin = 29
in2_RFpin =18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(enable_LFpin, GPIO.OUT)
GPIO.setup(enable_LRpin, GPIO.OUT)
GPIO.setup(enable_RRpin, GPIO.OUT)
GPIO.setup(enable_RFpin, GPIO.OUT)

GPIO.setup(in1_LFpin, GPIO.OUT)
GPIO.setup(in2_LFpin, GPIO.OUT)
pwm1 = GPIO.PWM(enable_LFpin, 500)
pwm1.start(0)

GPIO.setup(in1_LRpin, GPIO.OUT)
GPIO.setup(in2_LRpin, GPIO.OUT)
pwm2 = GPIO.PWM(enable_LRpin, 500)
pwm2.start(0)

GPIO.setup(in1_RFpin, GPIO.OUT)
GPIO.setup(in2_RFpin, GPIO.OUT)
pwm3 = GPIO.PWM(enable_RFpin, 500)
pwm3.start(0)

GPIO.setup(in1_RRpin, GPIO.OUT)
GPIO.setup(in2_RRpin, GPIO.OUT)
pwm4 = GPIO.PWM(enable_RRpin, 500)
pwm4.start(0)

def clockwise():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(20) 
    pwm2.ChangeDutyCycle(20)    
    pwm3.ChangeDutyCycle(20) 
    pwm4.ChangeDutyCycle(20)

def counter_clockwise():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    pwm1.ChangeDutyCycle(30)        #LR
    pwm2.ChangeDutyCycle(30)        #LF
    pwm3.ChangeDutyCycle(30)        #RR
    pwm4.ChangeDutyCycle(30)        #RF

def right():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(60) 
    pwm2.ChangeDutyCycle(60)    
    pwm3.ChangeDutyCycle(0) 
    pwm4.ChangeDutyCycle(0)
    
def left():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    pwm1.ChangeDutyCycle(0) 
    pwm2.ChangeDutyCycle(0)    
    pwm3.ChangeDutyCycle(55) 
    pwm4.ChangeDutyCycle(60)

def Hright():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(50) 
    pwm2.ChangeDutyCycle(50)    
    pwm3.ChangeDutyCycle(40) 
    pwm4.ChangeDutyCycle(50)
    
def Hleft():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    pwm1.ChangeDutyCycle(50) 
    pwm2.ChangeDutyCycle(50)    
    pwm3.ChangeDutyCycle(40) 
    pwm4.ChangeDutyCycle(50)

def hault():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(0) 
    pwm2.ChangeDutyCycle(0)    
    pwm3.ChangeDutyCycle(0) 
    pwm4.ChangeDutyCycle(0)




while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "w":
        clockwise()
    elif direction == "d":
        right()
    elif direction == "a":
        left()
    elif direction == "e":
        Hright()
    elif direction == "q":
        Hleft()
    elif direction == "s":
        counter_clockwise()
    else:
        hault()
    
