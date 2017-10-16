import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

enable_Lpin =38
in1_Lpin = 33
in2_Lpin =31

enable_Rpin =40
in1_Rpin = 37
in2_Rpin =35

GPIO.setup(enable_Lpin, GPIO.OUT)
GPIO.setup(in1_Lpin, GPIO.OUT)
GPIO.setup(in2_Lpin, GPIO.OUT)

GPIO.setup(enable_Rpin, GPIO.OUT)
GPIO.setup(in1_Rpin, GPIO.OUT)
GPIO.setup(in2_Rpin, GPIO.OUT)


GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(13, GPIO.IN)    #SO2
GPIO.setup(15, GPIO.IN)    #S03
GPIO.setup(19, GPIO.IN)    #SO4
GPIO.setup(21, GPIO.IN)    #SO5
sleep(1)
pwm1 = GPIO.PWM(enable_Lpin, 400)
pwm1.start(0)

pwm2 = GPIO.PWM(enable_Rpin, 400)
pwm2.start(0)


def forward():
    GPIO.output(in1_Lpin, True)
    GPIO.output(in2_Lpin, False)
    pwm1.ChangeDutyCycle(60)
    
    GPIO.output(in1_Rpin, True)
    GPIO.output(in2_Rpin, False)
    pwm2.ChangeDutyCycle(60)

def halt_here():
    print "halt"
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    
def slight_turn_right():
    GPIO.output(in1_Lpin, True)
    GPIO.output(in2_Lpin, False)
    pwm1.ChangeDutyCycle(60)
    
    GPIO.output(in1_Rpin, True)
    GPIO.output(in2_Rpin, False)
    pwm2.ChangeDutyCycle(0)
    
def sharp_turn_right():
    GPIO.output(in1_Lpin, True)
    GPIO.output(in2_Lpin, False)
    pwm1.ChangeDutyCycle(60)
    
    GPIO.output(in1_Rpin, False)
    GPIO.output(in2_Rpin, True)
    pwm2.ChangeDutyCycle(60)
    
def sharp_turn_left():
    GPIO.output(in1_Lpin, False)
    GPIO.output(in2_Lpin, True)
    pwm1.ChangeDutyCycle(60)
    
    GPIO.output(in1_Rpin, True)
    GPIO.output(in2_Rpin, False)
    pwm2.ChangeDutyCycle(60)
    
def slight_turn_left():
    GPIO.output(in1_Lpin, False)
    GPIO.output(in2_Lpin, True)
    pwm1.ChangeDutyCycle(0)
    
    GPIO.output(in1_Rpin, True)
    GPIO.output(in2_Rpin, False)
    pwm2.ChangeDutyCycle(60)
    

try:
  while True:
    s1=GPIO.input(11)
    s2=GPIO.input(13)
    s3=GPIO.input(15)
    s4=GPIO.input(19)
    s5=GPIO.input(21)
    print(s1,s2,s3,s4,s5)
    
    if(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
        print "Line finding behaviour"
        
    elif(s1==0)and(s2==0)and(s3==1)and(s4==0)and(s5==0):
        print "forward"
        forward()
        
    elif(s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
        print "forward"
        forward()
      
        
    elif(s1==0)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
        print "forward"
        forward()
       
        
    elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==0):
        print "forward"
        forward()
        
    elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==1):
        print "Slight turn right"
        sharp_turn_right()
    
    elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==0):
        print "Slight turn right"
        sharp_turn_right()
        
    elif(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==1):
        print "Slight turn right"
        sharp_turn_right()
    elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==1):
        print "Slight turn right"
        sharp_turn_right()
        
    elif(s1==1)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
        print "Sharp turn left"
        sharp_turn_left()
        
    elif(s1==0)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
        print "Slight turn left"
        sharp_turn_left()
    
        
    elif(s1==1)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
        print "Slight turn left"
        sharp_turn_left()
    elif(s1==1)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
        print "Sharp turn left"
        sharp_turn_left()
    
    
    else:
        halt_here()
    
       
except:
    pwm1.start(0)
    pwm2.start(0)