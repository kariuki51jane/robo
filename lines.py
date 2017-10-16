def line_finding():
    GPIO.output(in1_Lpin, True)
    GPIO.output(in2_Lpin, False)
    pwm1.ChangeDutyCycle(90)
    
    GPIO.output(in1_Rpin, False)
    GPIO.output(in2_Rpin, True)
    pwm2.ChangeDutyCycle(60)
    

    GPIO.output(in1_Lpin, False)
    GPIO.output(in2_Lpin, True)
    pwm1.ChangeDutyCycle(60)
    
    GPIO.output(in1_Rpin, True)
    GPIO.output(in2_Rpin, False)
    pwm2.ChangeDutyCycle(90)
    
 