import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)


class wheels:
    def __init__(self,lpin,rpin):
        self.lpin=lpin
        self.rpin=rpin
        self.lpincount=0
        self.rpincount=0
        GPIO.setup(self.lpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.rpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.lpin, GPIO.FALLING, callback=self.LeftWheel)
        GPIO.add_event_detect(self.rpin, GPIO.FALLING, callback=self.RightWheel)

    def reset_encoder(self):
        self.lpincount=0
        self.rpincount=0
    def LeftWheel(self,channel):
        self.lpincount+=1
    def RightWheel(self,channel):
        self.rpincount+=1
    def get(self):
        return self.lpincount,self.rpincount
     

  



