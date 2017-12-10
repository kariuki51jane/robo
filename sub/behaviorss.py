import RPi.GPIO as GPIO
import time
import drive
import servo

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(13, GPIO.IN)    #SO2
GPIO.setup(15, GPIO.IN)    #S03
GPIO.setup(19, GPIO.IN)    #SO4
GPIO.setup(21, GPIO.IN)    #SO5


TRIG = 23
ECHO = 29


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)




class obstacle_avoidance:
	#initial distance
	distance_m30=100
	distance_0=100
	distance_30=100	
	distance_m45=100
	distance_45=100

	def suppress():
		return True

	
	def takeControl(self):
                
                self.distance_m30=self.sonar()
                print "Distance at -30 "+str(self.distance_m30)+"cm"

                        
##                        print("read sonar")
##              GPIO.output(TRIG, True)
##		time.sleep(0.1)
##		GPIO.output(TRIG, False)
##
##  		while GPIO.input(ECHO)==0:
##        		pulse_start = time.time()
##
##  		while GPIO.input(ECHO)==1:
##        		pulse_end = time.time()
##
##  		pulse_duration = pulse_end - pulse_start
##  		distanceL = pulse_duration * 17150
##  		distanceL = round(distanceL,2)
##  		print(distanceL)
                
		
                servo.pRightServo.ChangeDutyCycle(2.5)
                servo.pLeftServo.ChangeDutyCycle(2.5)
                time.sleep(0.2)
##                distanceL=servo.sonarL.read()
##                
##                print("\nrequired : ",distanceL)
##                
##                if(distanceL<=30):
##                        print("Obstacle detected left middle")
##                        return True
##                
##                #left middle
##        
##                
                servo.pRightServo.ChangeDutyCycle(5)
                servo.pLeftServo.ChangeDutyCycle(5)
                time.sleep(0.2)
##                print("left front ",servo.sonarL.read())
##
##                #left front
##                
                servo.pRightServo.ChangeDutyCycle(7.5)
                servo.pLeftServo.ChangeDutyCycle(7.5)
                time.sleep(0.2)
##   
##
                servo.pRightServo.ChangeDutyCycle(10)
                servo.pLeftServo.ChangeDutyCycle(10)
                time.sleep(0.2)
##                print("right font ",servo.sonarR.read())
##
##                #right font
##
##                
                servo.pRightServo.ChangeDutyCycle(12.5)
                servo.pLeftServo.ChangeDutyCycle(12.5)
                time.sleep(0.2)
                print("right middle ",servo.sonarR.read())
##
##                #right middle
##
                servo.pRightServo.ChangeDutyCycle(10)
                servo.pLeftServo.ChangeDutyCycle(10)
                time.sleep(0.2)
##
##
                servo.pRightServo.ChangeDutyCycle(7.5)
                servo.pLeftServo.ChangeDutyCycle(7.5)
                time.sleep(0.2)
##
##
                servo.pRightServo.ChangeDutyCycle(5)
                servo.pLeftServo.ChangeDutyCycle(5)
                time.sleep(0.2)

	def action(self):
                print "Obstacle avoidance processing"
                #drive.SetSpeed(0,50)
                #time.sleep(0.2)
                #drive.SetSpeed(50,0)
                #time.sleep(0.2)
                #drive.SetSpeed(50,50)
                #time.sleep(0.2)
                #drive.SetSpeed(50,0)
                #time.sleep(0.2)
                #drive.SetSpeed(0,50)
                #time.sleep(0.2)
                
        def sonar(self):
                GPIO.output(TRIG, True)
		time.sleep(0.1)
		GPIO.output(TRIG, False)

  		while GPIO.input(ECHO)==0:
        		pulse_start = time.time()

  		while GPIO.input(ECHO)==1:
        		pulse_end = time.time()

  		pulse_duration = pulse_end - pulse_start
  		distance = pulse_duration * 17150
  		distance = round(distance,2)

  		return distance
                


class lineFollowing:
        
        def takeControl(self):
		print "Line following Taking Control"
		return True
	def action(self):
                s1=GPIO.input(11)
                s2=GPIO.input(13)
                s3=GPIO.input(15)
                s4=GPIO.input(19)
                s5=GPIO.input(21)
    
                if(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
                        print "Line finding behaviour"
                        self.halt_here()
                elif(s1==0)and(s2==0)and(s3==1)and(s4==0)and(s5==0):
                        self.forward()
                elif(s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
                        self.forward()
                elif(s1==0)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
                        self.forward()
                elif(s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
                        self.forward()
                elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==0):
                        self.forward()
                elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==1):
                        self.sharp_turn_right()
                elif(s1==0)and(s2==1)and(s3==1)and(s4==1)and(s5==1):
                        self.sharp_turn_right()
                elif(s1==0)and(s2==0)and(s3==0)and(s4==1)and(s5==0):
                        self.sharp_turn_right()
                elif(s1==0)and(s2==0)and(s3==0)and(s4==0)and(s5==1):
                        self.sharp_turn_right()
                elif(s1==0)and(s2==0)and(s3==1)and(s4==1)and(s5==1):
                        self.sharp_turn_right()
                elif(s1==1)and(s2==0)and(s3==0)and(s4==0)and(s5==0):
                        self.sharp_turn_left()
                elif(s1==0)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
                        self.sharp_turn_left()
                elif(s1==1)and(s2==1)and(s3==0)and(s4==0)and(s5==0):
                        self.sharp_turn_left()
                elif(s1==1)and(s2==1)and(s3==1)and(s4==0)and(s5==0):
                        self.sharp_turn_left()
                elif(s1==1)and(s2==1)and(s3==1)and(s4==1)and(s5==0):
                        self.sharp_turn_left()
                else:
                        self.halt_here()
                        
	def suppress(self):
                print("Here suprresed")
                self.halt_here()
                return True
        
        def forward(self):
                drive.SetSpeed(50,50)

        def halt_here(self):
                drive.SetSpeed(0,0)
    
        def slight_turn_right(self):
                drive.SetSpeed(50,0)
    
        def sharp_turn_right(self):
                drive.SetSpeed(50,-50)

        def sharp_turn_left(self):
                drive.SetSpeed(-50,50)

        def slight_turn_left(self):
                drive.SetSpeed(0,50)
        
      
