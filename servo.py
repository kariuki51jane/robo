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

sonarR=sonar.sonar(TRIG_RIGHT,ECHO_RIGHT)
sonarL=sonar.sonar(TRIG_LEFT,ECHO_LEFT)



try:
        while True:
                pRightServo.ChangeDutyCycle(2.5)
                pLeftServo.ChangeDutyCycle(2.5)
                time.sleep(0.2)
                
                print("left middle ",sonarL.read())

                #left middle
                
                

                pRightServo.ChangeDutyCycle(5)
                pLeftServo.ChangeDutyCycle(5)
                time.sleep(0.2)
                print("left front ",sonarL.read())

                #left front


                
                pRightServo.ChangeDutyCycle(7.5)
                pLeftServo.ChangeDutyCycle(7.5)
                time.sleep(0.2)
   

                
                pRightServo.ChangeDutyCycle(10)
                pLeftServo.ChangeDutyCycle(10)
                time.sleep(0.2)
                print("right font ",sonarR.read())


                #right font

                
                pRightServo.ChangeDutyCycle(12.5)
                pLeftServo.ChangeDutyCycle(12.5)
                time.sleep(0.2)
                print("right middle ",sonarR.read())

                #right middle

                
                pRightServo.ChangeDutyCycle(10)
                pLeftServo.ChangeDutyCycle(10)
                time.sleep(0.2)
                print(sonarR.read())
                print(sonarL.read())

                pRightServo.ChangeDutyCycle(7.5)
                pLeftServo.ChangeDutyCycle(7.5)
                time.sleep(0.2)
                print(sonarR.read())
                print(sonarL.read())

                pRightServo.ChangeDutyCycle(5)
                pLeftServo.ChangeDutyCycle(5)
                time.sleep(0.2)
                print(sonarR.read())
                print(sonarL.read())

                
except KeyboardInterrupt:
        pLeftServo.stop()
        pRightServo.stop()
        GPIO.cleanup()


