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
pwmL = GPIO.PWM(Enable_Lpin,0)
pwmL.start(0)

#Setting Right Motor
GPIO.setup(Enable_Rpin, GPIO.OUT)
GPIO.setup(In1_Rpin, GPIO.OUT)
GPIO.setup(In2_Rpin, GPIO.OUT)
pwmR = GPIO.PWM(Enable_Rpin,0)
pwmR.start(0)



GPIO.output(In1_Lpin, True)
GPIO.output(In2_Lpin, False)
pwm1.ChangeDutyCycle(50)

GPIO.output(In1_Rpin, True)
GPIO.output(In2_Rpin, False)
pwm2.ChangeDutyCycle(50)

sleep(1)



