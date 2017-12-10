import RPi.GPIO as GPIO 
import threading 
import time 
import behaviors 
import sys 
import select

activated_behavior=3
B1=behaviors.obstacle_avoidance()
B3=behaviors.lineFollowing()

def Behavior1():
	print "Behavior 1"
	global activated_behavior
	
	while True:
                print("taking control")
        	if(B1.takeControl()==True):
			print "B1 Take control True"
		#	B3.suppress()
		#	activated_behavior=1
		#	B1.action()
			activated_behavior=3
	print threading.currentThread().getName(), 'Exiting'

def Behavior3():
    
	print threading.currentThread().getName(), 'Starting'
	print "Behavior 3"
	global activated_behavior
	
        while True:
                #print("line follower")
                if(activated_behavior==3):
                        B3.action()
                        pass
	print threading.currentThread().getName(), 'Exiting'



beh1  = threading.Thread(target=Behavior1)
beh3  = threading.Thread(target=Behavior3) 

try:
        beh1.start()
        beh3.start()
except:
    print "Caught an exception"


