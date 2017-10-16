import serial

ser = serial.Serial('/dev/ttyUSB0',9600)

while True:
	read_serial=int(ser.readline(),10)
	if read_serial==0:
                print "no"
        elif read_serial==1:
                print "yes"
	else:
                print "yes"
	#s[0] = str(int (ser.readline(),16))
	#print s[0]
	#print read_serial
