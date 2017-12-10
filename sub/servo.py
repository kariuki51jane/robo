import RPi.GPIO as GPIO
import sonar
import time

Right_servo=10
Left_servo =12

TRIG_RIGHT = 32
ECHO_RIGHT = 36

TRIG_LEFT = 23
ECHO_LEFT = 29

GPIO.setmode(GPIO.BOARD)

GPIO.setup(TRIG_LEFT,GPIO.OUT)
GPIO.setup(ECHO_LEFT,GPIO.IN)

GPIO.setup(TRIG_RIGHT,GPIO.OUT)
GPIO.setup(ECHO_RIGHT,GPIO.IN)

GPIO.output(TRIG_LEFT, False)
GPIO.output(TRIG_RIGHT, False)

GPIO.setup(Right_servo, GPIO.OUT)
GPIO.setup(Left_servo, GPIO.OUT)

pLeftServo = GPIO.PWM(Left_servo, 50)
pRightServo = GPIO.PWM(Right_servo, 50)

pLeftServo.start(2.5)
pRightServo.start(2.5)

sonarR=sonar.sonar1(TRIG_RIGHT,ECHO_RIGHT)
sonarL=sonar.sonar1(TRIG_LEFT,ECHO_LEFT)



