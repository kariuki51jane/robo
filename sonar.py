import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# working
#TRIG_LEFT = 23
#ECHO_LEFT = 29
# end working



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

def sonar():
  counter=0
  while True:
    GPIO.output(TRIG_LEFT, True)
    time.sleep(0.1)
    GPIO.output(TRIG_LEFT, False)

    while GPIO.input(ECHO_LEFT)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO_LEFT)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "Distance L:",distance,"cm"

sonar()
