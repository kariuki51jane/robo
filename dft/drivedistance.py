import drive
import encoders

speed = 40

encoder=encoders.wheels(26,24)
drive.SetSpeed(speed, speed);

while(encoder.get()[0]<30):
    pass
drive.stop()
print(encoder.get())
