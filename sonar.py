import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


TRIG_RIGHT = 23
ECHO_RIGHT = 29


TRIG_LEFT = 32
ECHO_LEFT = 36

#print "Distance Measurement In Progress"

GPIO.setup(TRIG_LEFT,GPIO.OUT)
GPIO.setup(ECHO_LEFT,GPIO.IN)

GPIO.setup(TRIG_RIGHT,GPIO.OUT)
GPIO.setup(ECHO_RIGHT,GPIO.IN)

GPIO.output(TRIG_LEFT, False)
GPIO.output(TRIG_RIGHT, False)

class sonar:
  def __init__(self,TRIG,ECHO):
    self.TRIG_Pin=TRIG
    self.ECHO_Pin=ECHO
    GPIO.setup(self.TRIG_Pin,GPIO.OUT)
    GPIO.setup(self.ECHO_Pin,GPIO.IN)
    GPIO.output(self.TRIG_Pin, False)

  def read(self):
    GPIO.output(self.TRIG_Pin, True)
    time.sleep(0.1)
    GPIO.output(self.TRIG_Pin, False)

    while GPIO.input(self.ECHO_Pin)==0:
      pulse_start = time.time()

    while GPIO.input(self.ECHO_Pin)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance
    
