import compass 

comread = compass.hmc5883l()
degrees =comread.degrees(comread.heading())

while True:
    degrees =comread.degrees(comread.heading())
    print degrees
