import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
SERVO= 12

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(SERVO, GPIO.OUT)

p = GPIO.PWM(SERVO, 50)
p.start(4.5)
GPIO.output(TRIG, False)


enable_Lpin =38
in1_Lpin = 33
in2_Lpin =31

enable_Rpin =40
in1_Rpin = 37
in2_Rpin =35


GPIO.setup(enable_Lpin, GPIO.OUT)
GPIO.setup(in1_Lpin, GPIO.OUT)
GPIO.setup(in2_Lpin, GPIO.OUT)

GPIO.setup(enable_Rpin, GPIO.OUT)
GPIO.setup(in1_Rpin, GPIO.OUT)
GPIO.setup(in2_Rpin, GPIO.OUT)

pwm1 = GPIO.PWM(enable_Lpin, 500)
pwm1.start(0)

pwm2 = GPIO.PWM(enable_Rpin, 500)
pwm2.start(0)


class obstacle_avoidance:
	#initial distance
	distance_m30=100
	distance_0=100
	distance_30=100	
	distance_m45=100
	distance_45=100

	def suppress():
		return True 	
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
	
	def readsonar(self):
				
        	p.ChangeDutyCycle(4.5)
                self.distance_m30=self.sonar()
                print "Distance at -30 "+str(self.distance_m30)+"cm"
                time.sleep(0.5) # sleep 1 second

                p.ChangeDutyCycle(2.5)  # turn towards 0 degree
                self.distance_0=self.sonar()
                print "Distance at 0 "+str(self.distance_0)+"cm"
                time.sleep(0.5) # sleep 1 second
		
		p.ChangeDutyCycle(6.5) # turn towards 30 degree - right
                self.distance_30=self.sonar()
                print "Distance at 30 "+str(self.distance_30)+"cm"
                time.sleep(0.5) # sleep 1 second

	def takeControl(self):
                self.readsonar()
                if(self.distance_m30<30 or self.distance_0<30 or self.distance_30<30):
                        print "Obstacle Ovoidance Taking Control"
                        return True

	def action(self):
                print "Obstacle avoidance processing"
		
		p.ChangeDutyCycle(7.5)
                self.distance_m45=self.sonar()
                print "Distance at -45 "+str(self.distance_m45)+"cm"
              

       		if(self.distance_m45>50):
			#turn left
			GPIO.output(in1_Lpin, True)
			GPIO.output(in2_Lpin, False)
			pwm1.ChangeDutyCycle(100)

			GPIO.output(in1_Rpin, False)
			GPIO.output(in2_Rpin, True)
			pwm2.ChangeDutyCycle(100)

			time.sleep(2)

			GPIO.output(in1_Lpin, False)
                        GPIO.output(in2_Lpin, False)
                        pwm1.ChangeDutyCycle(0)

                        GPIO.output(in1_Rpin, False)
                        GPIO.output(in2_Rpin, False)
                        pwm2.ChangeDutyCycle(0)



		else:
			p.ChangeDutyCycle(12.5) # turn towards 45 degree - right
	               	self.distance_45=self.sonar()
	               	print "Distance at 45 "+str(self.distance_45)+"cm"
                	
			if(self.distance_45>50):
				#turn right
				GPIO.output(in1_Lpin, False)
				GPIO.output(in2_Lpin, True)
				pwm1.ChangeDutyCycle(100)

				GPIO.output(in1_Rpin, True)
				GPIO.output(in2_Rpin, False)
				pwm2.ChangeDutyCycle(100)
				
				time.sleep(2)
				
				GPIO.output(in1_Lpin, False)
                                GPIO.output(in2_Lpin, False)
 				pwm1.ChangeDutyCycle(0)

                                GPIO.output(in1_Rpin, False)
                                GPIO.output(in2_Rpin, False)
  				pwm2.ChangeDutyCycle(0)

			

			else:
				#turn backward
				GPIO.output(in1_Lpin, True)
				GPIO.output(in2_Lpin, False)
				pwm1.ChangeDutyCycle(100)

				GPIO.output(in1_Rpin, False)
				GPIO.output(in2_Rpin, True)
				pwm2.ChangeDutyCycle(100)

				time.sleep(4)

				GPIO.output(in1_Lpin, False)
                                GPIO.output(in2_Lpin, False)
                                pwm1.ChangeDutyCycle(0)

                                GPIO.output(in1_Rpin, False)
                                GPIO.output(in2_Rpin, False)
                                pwm2.ChangeDutyCycle(0)




                return True


class wandering:
	def takeControl(self):
		return True
	def action(self):
		GPIO.output(in1_Lpin, True)
                GPIO.output(in2_Lpin, False)
                pwm1.ChangeDutyCycle(100)

                GPIO.output(in1_Rpin, True)
                GPIO.output(in2_Rpin, False)
                pwm2.ChangeDutyCycle(100)

                time.sleep(1.75)                               
		GPIO.output(in1_Lpin, False)
                GPIO.output(in2_Lpin, False)
                pwm1.ChangeDutyCycle(0)

                GPIO.output(in1_Rpin, False)
                GPIO.output(in2_Rpin, False)
                pwm2.ChangeDutyCycle(0)
		
	def suppress(self):
                return True
       

B1=obstacle_avoidance()
B2=wandering()


while True:
	if(B1.takeControl()==True):
		B1.action()
	elif(B2.takeControl()==True):
		B2.action()
GPIO.cleanup()
