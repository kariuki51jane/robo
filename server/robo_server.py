import socket
import random
import sys
from time import sleep
import json

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
		print >>sys.stderr, 'received "%s"' % data
		sleep(1)

finally:
	print >>sys.stderr, 'closing socket'
	sock.close()
