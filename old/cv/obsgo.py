import time
from sonarL import *
from sonarR import *
from motor import *
from buzz import *
irpin=12

GPIO.setup(irpin,GPIO.IN)


def obsgo():
    
    count1=0
    count2=0
    count3=0
    count4=0
    CIR=0
    CIR1=0
    CIR2=0
    while True:
        IR=GPIO.input(irpin)
        sonarL1()
        sonarR1()
        #print "left :", sonarL1()
        #print "right :", sonarR1()


        if sonarL1()<25:
            count1=1
            
        if sonarR1()<25:
            count2=1
            

            
        if sonarR1()<25 and count1==1:
            count3=1

        if sonarL1()<25 and count2==1:
            count4=1

            
        if sonarL1()>26 and count4==1:
            print "object pass hari"
            #clockwise()
            if IR==1:
                CIR=1
                clockwise()
                print "go B"
            if IR==0 and CIR==1:
                CIR1=1
                clockwise()
                print "go W"
            if IR==1 and CIR1==1:
                CIR2=2
                clockwise()
                print "go M B"
            if CIR2==2 and IR==0:
                print "detect W"
                brake()
                time.sleep(0.3)
                counter_clockwise()
                time.sleep(0.6)
                break
                
                
            #print "object pass"
            #time.sleep(5)
            #clockwise()
            #time.sleep(0.4)
            #break    
        if sonarR1()>26 and count3==1:
            print "object pass"
            #clockwise()
            if IR==1:
                CIR=1
                clockwise()
                print "go B"
            if IR==0 and CIR==1:
                CIR1=1
                clockwise()
                print "go W"
            if IR==1 and CIR1==1:
                CIR2=2
                clockwise()
                print "go M B"
            if CIR2==2 and IR==0:
                print "detect W"
                brake()
                time.sleep(0.3)
                counter_clockwise()
                time.sleep(0.6)
                break
                
