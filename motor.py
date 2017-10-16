import RPi.GPIO as GPIO
from time import sleep

enable_Lpin =38
in1_Lpin = 33
in2_Lpin =31

enable_Rpin =40
in1_Rpin = 37
in2_Rpin =35

GPIO.setmode(GPIO.BOARD)

GPIO.setup(enable_Lpin, GPIO.OUT)
GPIO.setup(in1_Lpin, GPIO.OUT)
GPIO.setup(in2_Lpin, GPIO.OUT)

GPIO.setup(enable_Rpin, GPIO.OUT)
GPIO.setup(in1_Rpin, GPIO.OUT)
GPIO.setup(in2_Rpin, GPIO.OUT)

pwm1 = GPIO.PWM(enable_Lpin, 500)
pwm1.start(0)

pwm2 = GPIO.PWM(enable_Rpin, 500)
pwm2.start(0)

GPIO.output(in1_Lpin, True)
GPIO.output(in2_Lpin, False)
pwm1.ChangeDutyCycle(50)

GPIO.output(in1_Rpin, True)
GPIO.output(in2_Rpin, False)
pwm2.ChangeDutyCycle(50)

sleep(0.5)


GPIO.output(in1_Lpin, True)
GPIO.output(in2_Lpin, False)
pwm1.ChangeDutyCycle(50)

GPIO.output(in1_Rpin, False)
GPIO.output(in2_Rpin, True)
pwm2.ChangeDutyCycle(50)

sleep(0.5)

GPIO.output(in1_Lpin, False)
GPIO.output(in2_Lpin, True)
pwm1.ChangeDutyCycle(50)

GPIO.output(in1_Rpin, True)
GPIO.output(in2_Rpin, False)
pwm2.ChangeDutyCycle(50)

sleep(0.5)

GPIO.output(in1_Lpin, False)
GPIO.output(in2_Lpin, False)
pwm1.ChangeDutyCycle(0)

GPIO.output(in1_Rpin, False)
GPIO.output(in2_Rpin, False)
pwm2.ChangeDutyCycle(0)

