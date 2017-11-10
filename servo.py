import RPi.GPIO as GPIO
import time

Right_servo=10
Left_servo =12

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Right_servo, GPIO.OUT)
GPIO.setup(Left_servo, GPIO.OUT)

pLeftServo = GPIO.PWM(Left_servo, 50)
pRightServo = GPIO.PWM(Right_servo, 50)

pLeftServo.start(2.5)
pRightServo.start(2.5)




try:
        while True:
                pRightServo.ChangeDutyCycle(2.5)
                pLeftServo.ChangeDutyCycle(2.5)
                time.sleep(0.2)
                pRightServo.ChangeDutyCycle(5)
                pLeftServo.ChangeDutyCycle(5)
                time.sleep(0.2)
                pRightServo.ChangeDutyCycle(7.5)
                pLeftServo.ChangeDutyCycle(7.5)
                time.sleep(0.2) 
                pRightServo.ChangeDutyCycle(10)
                pLeftServo.ChangeDutyCycle(10)
                time.sleep(0.2)
                pRightServo.ChangeDutyCycle(12.5)
                pLeftServo.ChangeDutyCycle(12.5)
                time.sleep(0.2)
                pRightServo.ChangeDutyCycle(10)
                pLeftServo.ChangeDutyCycle(10)
                time.sleep(0.2)
                pRightServo.ChangeDutyCycle(7.5)
                pLeftServo.ChangeDutyCycle(7.5)
                time.sleep(0.2)
                pRightServo.ChangeDutyCycle(5)
                pLeftServo.ChangeDutyCycle(5)
                time.sleep(0.2)
                
except KeyboardInterrupt:
        pLeftServo.stop()
        pRightServo.stop()
        GPIO.cleanup()


