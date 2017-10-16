import serial
from buzz import *
from motor import*

def obs():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    count=0
    while True:
        
        read_serial=ser.readline()
        if int(read_serial)==1:
            print "obs"
            hault()
                        
            count=count+1
            if count == 500:
                buzz1()
                buzz1()
                Hardright()
                time.sleep(0.5)
                hault()
                #time.sleep(5)
                                
        else:
            clockwise()
            count=0
            print "no"
            break
