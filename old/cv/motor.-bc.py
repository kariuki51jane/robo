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
    pwm1.ChangeDutyCycle(15) 
    pwm2.ChangeDutyCycle(15)    
    pwm3.ChangeDutyCycle(15) 
    pwm4.ChangeDutyCycle(15)
def fast():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(40) 
    pwm2.ChangeDutyCycle(40)    
    pwm3.ChangeDutyCycle(40) 
    pwm4.ChangeDutyCycle(40)
def slow():
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
    pwm1.ChangeDutyCycle(20)        #LR
    pwm2.ChangeDutyCycle(20)        #LF
    pwm3.ChangeDutyCycle(15)        #RR
    pwm4.ChangeDutyCycle(20)        #RF

def brake():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    pwm1.ChangeDutyCycle(10)        #LR
    pwm2.ChangeDutyCycle(10)        #LF
    pwm3.ChangeDutyCycle(10)        #RR
    pwm4.ChangeDutyCycle(10)        #RF

def brakeF():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(10) 
    pwm2.ChangeDutyCycle(10)    
    pwm3.ChangeDutyCycle(10) 
    pwm4.ChangeDutyCycle(10)
def right():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(30) 
    pwm2.ChangeDutyCycle(30)    
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
    pwm1.ChangeDutyCycle(20) 
    pwm2.ChangeDutyCycle(0)    
    pwm3.ChangeDutyCycle(25) 
    pwm4.ChangeDutyCycle(30)

def Hright():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(70) 
    pwm2.ChangeDutyCycle(70)    
    pwm3.ChangeDutyCycle(0) 
    pwm4.ChangeDutyCycle(0)


def Hardright():
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
    pwm3.ChangeDutyCycle(20) 
    pwm4.ChangeDutyCycle(20)
def Hardleft():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    pwm1.ChangeDutyCycle(30) 
    pwm2.ChangeDutyCycle(30)    
    pwm3.ChangeDutyCycle(60) 
    pwm4.ChangeDutyCycle(60)
def Hleft():
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
    pwm3.ChangeDutyCycle(70) 
    pwm4.ChangeDutyCycle(70)

def turn1HL():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    pwm1.ChangeDutyCycle(3) 
    pwm2.ChangeDutyCycle(3)    
    pwm3.ChangeDutyCycle(60) 
    pwm4.ChangeDutyCycle(60)
def hault():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, True)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, True)
    pwm1.ChangeDutyCycle(0) 
    pwm2.ChangeDutyCycle(0)    
    pwm3.ChangeDutyCycle(0) 
    pwm4.ChangeDutyCycle(0)

def obsright():
    GPIO.output(in1_RRpin, False)
    GPIO.output(in2_RRpin, True)
    GPIO.output(in1_RFpin, False)
    GPIO.output(in2_RFpin, True)
    GPIO.output(in1_LRpin, True)
    GPIO.output(in2_LRpin, False)
    GPIO.output(in1_LFpin, True)
    GPIO.output(in2_LFpin, False)
    pwm1.ChangeDutyCycle(40) 
    pwm2.ChangeDutyCycle(40)    
    pwm3.ChangeDutyCycle(45) 
    pwm4.ChangeDutyCycle(45)
def obsleft():
    GPIO.output(in1_RRpin, True)
    GPIO.output(in2_RRpin, False)
    GPIO.output(in1_RFpin, True)
    GPIO.output(in2_RFpin, False)
    GPIO.output(in1_LRpin, False)
    GPIO.output(in2_LRpin, True)
    GPIO.output(in1_LFpin, False)
    GPIO.output(in2_LFpin, True)
    pwm1.ChangeDutyCycle(40) 
    pwm2.ChangeDutyCycle(40)    
    pwm3.ChangeDutyCycle(40) 
    pwm4.ChangeDutyCycle(40)

def right_nin():
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
    pwm3.ChangeDutyCycle(50) 
    pwm4.ChangeDutyCycle(50)

def left_nin():
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
    pwm3.ChangeDutyCycle(50) 
    pwm4.ChangeDutyCycle(50)

def turn_nin():
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
    pwm3.ChangeDutyCycle(50) 
    pwm4.ChangeDutyCycle(50)    
