import RPi.GPIO as GPIO 
import threading 
import time 
import behaviors 
import sys 
import select

activated_behavior=0
def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return True
    return False


def Arbitrator():
	print threading.currentThread().getName(), 'Starting'
	print "I am the sheduler"
	#while True:
	#	print "Arbitrator running"
	#	time.sleep(1)

	print threading.currentThread().getName(), 'Exiting'

def Behavior1():
	print threading.currentThread().getName(), 'Starting'
	print "Behavior 1"
	B1=behaviors.obstacle_avoidance()
	global activated_behavior	
	while True:
		if heardEnter()==True:
                	break
        	if(B1.takeControl()==True):
			print "B1 Take control True"
			activated_behavior=1
			print activated_behavior
			B1.action()
			activated_behavior=0
		time.sleep(1)
	
	print threading.currentThread().getName(), 'Exiting'

def Behavior2():
	print threading.currentThread().getName(), 'Starting'
	print "Behavior 2"
	global activated_behavior
	B2=behaviors.wandering()
        while True:
		if heardEnter()==True:
                	break

                if(B2.takeControl()==True and not(activated_behavior==1)):
                        print "B2 Take control True"
			print activated_behavior
			B2.action()
                time.sleep(1)
	print threading.currentThread().getName(), 'Exiting'

arbit = threading.Thread(target=Arbitrator)
beh1  = threading.Thread(target=Behavior1)
beh2  = threading.Thread(target=Behavior2) 

arbit.start()
beh1.start()
beh2.start()
