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
def path():
    

    Tcp_connect( '192.168.43.28', 17098)
    Tcp_Write('a')
        #print Tcp_Read()
        #Tcp_Write('hello')
        #print Tcp_Read()
    data=[]

    data=Tcp_Read()
    print data
    return data 
