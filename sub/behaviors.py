import RPi.GPIO as GPIO
import time
import drive

GPIO.setmode(GPIO.BOARD)

TRIG = 23
ECHO = 29
SERVO= 12

TRIG_RIGHT = 32
ECHO_RIGHT = 36
Right_servo=10

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(SERVO, GPIO.OUT)

GPIO.setup(TRIG_RIGHT,GPIO.OUT)
GPIO.setup(ECHO_RIGHT,GPIO.IN)
GPIO.setup(Right_servo, GPIO.OUT)

GPIO.setup(11, GPIO.IN)    #SO1
GPIO.setup(13, GPIO.IN)    #SO2
GPIO.setup(15, GPIO.IN)    #S03
GPIO.setup(19, GPIO.IN)    #SO4
GPIO.setup(21, GPIO.IN)    #SO5

p = GPIO.PWM(SERVO, 50)
p.start(4.5)

pR = GPIO.PWM(Right_servo, 50)
pR.start(4.5)

GPIO.output(TRIG, False)

GPIO.output(TRIG_RIGHT, False)




class obstacle_avoidance:
	#initial distance
	distance_m30=100
	distance_0=100
	distance_30=100

	distance_m30_R=100
	distance_0_R=100
	distance_30_R=100	


	def suppress():
		return True 	
	def sonarL(self):
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
  	
  	def sonarR(self):
		GPIO.output(TRIG_RIGHT, True)
		time.sleep(0.1)
		GPIO.output(TRIG_RIGHT, False)

  		while GPIO.input(ECHO_RIGHT)==0:
        		pulse_start = time.time()

  		while GPIO.input(ECHO_RIGHT)==1:
        		pulse_end = time.time()

  		pulse_duration = pulse_end - pulse_start
  		distance = pulse_duration * 17150
  		distance = round(distance,2)

  		return distance
	
	def readsonar(self):
				
        	p.ChangeDutyCycle(4.5)
        	pR.ChangeDutyCycle(4.5)
                self.distance_m30=self.sonarL()
                self.distance_m30_R=self.sonarR()

                time.sleep(0.05) # sleep 1 second

                p.ChangeDutyCycle(2.5)  # turn towards 0 degree
                pR.ChangeDutyCycle(2.5)
                self.distance_0=self.sonarL()
                self.distance_0_R=self.sonarR()
                
        
                time.sleep(0.05) # sleep 1 second
		
		p.ChangeDutyCycle(6.5) # turn towards 30 degree - right
		pR.ChangeDutyCycle(6.5)
                self.distance_30=self.sonarL()
                self.distance_30_R=self.sonarR()


	def takeControl(self):
                self.readsonar()
                if(self.distance_m30<30 or self.distance_0<30 or self.distance_30<30 or self.distance_m30_R<30 or self.distance_0_R<30 or self.distance_30_R<30):
                        print "Obstacle Ovoidance Taking Control"
                        return True

	def action(self):
                print "Obstacle avoidance processing"
                drive.SetSpeed(0,0)
                time.sleep(10)
		
class wandering:
	def takeControl(self):
		print "wandering taking control"
		return True
	def action(self):
		print "wandering action"
		GPIO.output(in1_Lpin, True)
                GPIO.output(in2_Lpin, False)
                pwm1.ChangeDutyCycle(50)

                GPIO.output(in1_Rpin, True)
                GPIO.output(in2_Rpin, False)
                pwm2.ChangeDutyCycle(50)

		
	def suppress(self):
		GPIO.output(in1_Lpin, False)
                GPIO.output(in2_Lpin, False)
                pwm1.ChangeDutyCycle(0)

                GPIO.output(in1_Rpin, False)
                GPIO.output(in2_Rpin, False)
                pwm2.ChangeDutyCycle(0)

                return True

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
      
