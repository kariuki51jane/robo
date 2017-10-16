import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)
i=0
while(i<=9):
    ser.write('3')
    i=i+1
