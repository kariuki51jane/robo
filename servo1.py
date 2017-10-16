import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(22,GPIO.OUT) 
frequencyHertz = 50 
pwm = GPIO.PWM(22,frequencyHertz)
leftPosition=7.5 
r1=2.2 
rightPosition=2.5 
middlePosition=(rightPosition-leftPosition)/ 2 + leftPosition 
msPerCycle = 1000/ frequencyHertz

def servo():
	left=leftPosition * 100 / msPerCycle
	r1p=r1 * 100 / msPerCycle
  	right=rightPosition * 100 / msPerCycle
  	pwm.start(left)
  	time.sleep(0.12)
  	pwm.start(r1p)
  	time.sleep(0.12)
	pwm.start(right)
  	time.sleep(0.12)
  	pwm.start(r1p)
  	time.sleep(0.12) pwm.stop()

servo()
GPIO.cleanup()
