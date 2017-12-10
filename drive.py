import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

#Left Motor
Enable_Lpin =38
In1_Lpin = 33
In2_Lpin =31

#Right Motor
Enable_Rpin =40
In1_Rpin = 37
In2_Rpin =35

#Setting Left Motor
GPIO.setup(Enable_Lpin, GPIO.OUT)
GPIO.setup(In1_Lpin, GPIO.OUT)
GPIO.setup(In2_Lpin, GPIO.OUT)
pwmL = GPIO.PWM(Enable_Lpin,500)
pwmL.start(0)

#Setting Right Motor
GPIO.setup(Enable_Rpin, GPIO.OUT)
GPIO.setup(In1_Rpin, GPIO.OUT)
GPIO.setup(In2_Rpin, GPIO.OUT)
pwmR = GPIO.PWM(Enable_Rpin,500)
pwmR.start(0)


def SetSpeed(SpeedL,SpeedR):
    SpeedR=SpeedR-8
    
    if SpeedR>=0 and SpeedL>=0:
        GPIO.output(In1_Lpin, True)
        GPIO.output(In2_Lpin, False)
        pwmL.ChangeDutyCycle(SpeedL)

        GPIO.output(In1_Rpin, True)
        GPIO.output(In2_Rpin, False)
        pwmR.ChangeDutyCycle(SpeedR)
         
        
    elif SpeedR>=0 and SpeedL<=0:
        GPIO.output(In1_Lpin, False)
        GPIO.output(In2_Lpin, True)
        pwmL.ChangeDutyCycle(-SpeedL)

        GPIO.output(In1_Rpin, True)
        GPIO.output(In2_Rpin, False)
        pwmR.ChangeDutyCycle(SpeedR)
    
    elif SpeedR<=0 and SpeedL<=0:
        
        GPIO.output(In1_Lpin, False)
        GPIO.output(In2_Lpin, True)
        pwmL.ChangeDutyCycle(-SpeedL)

        GPIO.output(In1_Rpin, False)
        GPIO.output(In2_Rpin, True)
        pwmR.ChangeDutyCycle(-SpeedR)
        
    elif SpeedR<=0 and SpeedL>=0:
        GPIO.output(In1_Lpin, True)
        GPIO.output(In2_Lpin, False)
        pwmL.ChangeDutyCycle(SpeedL)

        GPIO.output(In1_Rpin, False)
        GPIO.output(In2_Rpin, True)
        pwmR.ChangeDutyCycle(-SpeedR)
    
def stop():
        GPIO.output(In1_Lpin, False)
        GPIO.output(In2_Lpin, False)
        pwmL.ChangeDutyCycle(0)

        GPIO.output(In1_Rpin, False)
        GPIO.output(In2_Rpin, False)
        pwmR.ChangeDutyCycle(0)
    
def gpioCleanUP():
    GPIO.cleanup()




