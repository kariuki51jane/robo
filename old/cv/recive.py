#from path import *

import socket, time
def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return
   
def Tcp_Write(D):
   s.send(D + '\r')
   return 
   
def Tcp_Read( ):
        
	a = ' '
	b = ''
	while a != '\r':
		a = s.recv(1)
		b = b + a
	return b

def Tcp_Close( ):
   s.close()
   return

'''    
def recive():
    data=MFRC522.path()
        
    if (len(data)>=1):
        if data[0]=='a' :
            data1=1
            return data1
            #print data[0]
        elif data[0]=='b' :
            data1=2
            return data1
        elif data[0]=='c' :
            data1=3
            return data1
            #print data[0]
        elif data[0]=='d' :
            data1=4
            return data1
        elif data[0]=='e' :
            data1=5
            return data1
            #print data[0]
        elif data[0]=='f' :
            data1=6
            return data1


def recive1():
    data=MFRC522.path()
    
    if (len(data)>=2):
        if data[1]=='a' :
            data1=1
            return data1
        elif data[1]=='b' :
            data1=2
            return data1
        elif data[1]=='c' :
            data1=3
            return data1
            #print data[0]
        elif data[1]=='d' :
            data1=4
            return data1
        elif data[1]=='e' :
            data1=5
            return data1
            #print data[0]
        elif data[1]=='f' :
            data1=6
            return data1
def recive2():
    
    data=MFRC522.path()
    if (len(data)>=3):
        if data[2]=='a' :
            data1=1
            return data1
        elif data[2]=='b' :
            data1=2
            return data1
        elif data[2]=='c' :
            data1=3
            return data1
            #print data[0]
        elif data[2]=='d' :
            data1=4
            return data1
        elif data[2]=='e' :
            data1=5
            return data1
            #print data[0]
        elif data[2]=='f' :
            data1=6
            return data1
def recive3():
    
    data=MFRC522.path()
    if (len(data)>=4):
        if data[1]=='a' :
            data1=1
            return data1
        elif data[1]=='b' :
            data1=2
            return data1
        elif data[1]=='c' :
            data1=3
            return data1
            #print data[0]
        elif data[1]=='d' :
            data1=4
            return data1
        elif data[1]=='e' :
            data1=5
            return data1
            #print data[0]
        elif data[1]=='f' :
            data1=6
            return data1 '''


#Tcp_Close()
#s.close()

