import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin=12

GPIO.setup(pin,GPIO.IN)

while True:
    x=GPIO.input(pin)
    print x
