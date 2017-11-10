import RPi.GPIO as GPIO
import time

Right_servo=10
Left_servo =12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Right_servo, GPIO.OUT)
GPIO.setup(Left_servo, GPIO.OUT)

pLeftServo = GPIO.PWM(Left_servo, 50)
pRightServo = GPIO.PWM(Right_servo, 50)

pLeftServo.start(7.5)
pRightServo.start(7.5)

try:
        while True:
		pLeftServo.ChangeDutyCycle(7.5)  # turn towards 90 degree
		pRightServo.ChangeDutyCycle(7.5)  # turn towards 90 degree
		time.sleep(0.25) # sleep 

		pLeftServo.ChangeDutyCycle(2.5)  # turn towards 0 degree
		pRightServo.ChangeDutyCycle(2.5)  # turn towards 90 degree
		time.sleep(0.25) # sleep

		pLeftServo.ChangeDutyCycle(12.5) # turn towards 180 degree
		pRightServo.ChangeDutyCycle(12.5)  # turn towards 90 degree
                time.sleep(0.25) # sleep


except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()
