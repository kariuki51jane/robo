import serial
from buzz import *
from motor import*
ser = serial.Serial('/dev/ttyUSB0', 9600)
#s=[0,1]

def sonar():
        count=0
        while True:
                
                read_serial=ser.readline()
                if int(read_serial)==11:
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
                    count=0
                    break
