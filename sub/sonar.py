import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)



class sonar1:
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

    try:
      pulse_duration = pulse_end - pulse_start
    except:
      print("Error happened\n")
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance


  



