import socket
import random
import sys
from time import sleep
import json
import RPi.GPIO as GPIO
from time import sleep

enable_Lpin =38
in1_Lpin = 33
in2_Lpin =31

enable_Rpin =40
in1_Rpin = 37
in2_Rpin =35

GPIO.setmode(GPIO.BOARD)

GPIO.setup(enable_Lpin, GPIO.OUT)
GPIO.setup(in1_Lpin, GPIO.OUT)
GPIO.setup(in2_Lpin, GPIO.OUT)

GPIO.setup(enable_Rpin, GPIO.OUT)
GPIO.setup(in1_Rpin, GPIO.OUT)
GPIO.setup(in2_Rpin, GPIO.OUT)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5002)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	while True:
		message = {"switch":"ON", "simulate":0,"energy": 70,"speed": 80,"distance" :100,"temp" : 27}		
		message["speed"]=random.randint(50, 100)
		message["temp"]=random.randint(20, 30)
		message["energy"]=random.randint(0, 100)
		message["distance"]=random.randint(0, 300)
		#print >>sys.stderr, 'sending "%s"' % message
		sock.sendall(json.dumps(message))
		data = sock.recv(100)
		dic=json.loads(data)
		if(dic['switch'])==1:
			pwm1 = GPIO.PWM(enable_Lpin, 500)
			pwm1.start(0)

			pwm2 = GPIO.PWM(enable_Rpin, 500)
			pwm2.start(0)

			GPIO.output(in1_Lpin, True)
			GPIO.output(in2_Lpin, False)
			pwm1.ChangeDutyCycle(50)

			GPIO.output(in1_Rpin, True)
			GPIO.output(in2_Rpin, False)
			pwm2.ChangeDutyCycle(50)

			sleep(0.5)
	
			GPIO.output(in1_Lpin, False)
			GPIO.output(in2_Lpin, False)
			pwm1.ChangeDutyCycle(0)

			GPIO.output(in1_Rpin, False)
			GPIO.output(in2_Rpin, False)
			pwm2.ChangeDutyCycle(0)

		sleep(1)
finally:
	print >>sys.stderr, 'closing socket'
	sock.close()
