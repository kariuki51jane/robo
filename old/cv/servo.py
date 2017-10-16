import RPi.GPIO as GPIO
import time
from sonar import *
from sonar1 import *



GPIO.setmode(GPIO.BOARD)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
frequencyHertz = 50
pwm = GPIO.PWM(26,frequencyHertz)
pwm1 = GPIO.PWM(12,frequencyHertz)

leftPosition=7.5
r1=2.2
#r2=2.2
rightPosition=2.5

leftPosition1=1.8
r11=1.3
#r21=1.3
rightPosition1=1

middlePosition=(rightPosition-leftPosition)/ 2 + leftPosition


msPerCycle = 1000/ frequencyHertz
def servo():
  
  left=leftPosition * 100 / msPerCycle
  left1=leftPosition1 * 100 / msPerCycle
  r1p=r1 * 100 / msPerCycle
  #r2p=r2 * 100 / msPerCycle
  r11p=r11 * 100 / msPerCycle
  #r21p=r21 * 100 / msPerCycle
  right=rightPosition * 100 / msPerCycle
  right1=rightPosition1 * 100 / msPerCycle
  sonar()
  sonarR()
  pwm.start(left)
  pwm1.start(left1)
  time.sleep(0.12)
  sonar()
  sonarR()
  pwm.start(r1p)
  pwm1.start(r11p)
  time.sleep(0.12)
  #sonar()
  #sonarR()
  #pwm.start(r2p)
  #pwm1.start(r21p)
  #time.sleep(0.15)

  sonar()
  sonarR()
  pwm.start(right)
  pwm1.start(right1)
  time.sleep(0.12)
  #sonar()
  #sonarR()
  #pwm.start(r2p)
  #pwm1.start(r21p)
  #time.sleep(0.15)
  sonar()
  sonarR()
  pwm.start(r1p)
  pwm1.start(r11p)
  time.sleep(0.12)

pwm.stop()
pwm1.stop()

GPIO.cleanup()
