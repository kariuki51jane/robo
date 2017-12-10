import drive
import encoders

speed = 30


encoder=encoders.wheels(26,24)
drive.SetSpeed(speed, 0)

while(encoder.get()[0]<10):
    pass

encoder.reset_encoder()


drive.SetSpeed(speed, speed);

while(encoder.get()[0]<10):
    pass

encoder.reset_encoder()

drive.SetSpeed(-speed, speed);
while(encoder.get()[0]<10):
    pass

#drive.stop()
#print(encoder.get())
