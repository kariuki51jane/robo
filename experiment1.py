import drive
import encoders
#here, we have chosen to drive a Z like shape;
# that is:
# 
# C     D
# o-----o
#  \  X
#   \
#    \
#     \
#   X  \
# o-----o
# A     B
# start the robot at A, facing towards B. D is the goal, X are obstacles.
#
# The commands have been determined by hand, i.e., by trial and error.
# Alternatively, we could have chosen to drive in arcs.

speed = 50

encoder=encoders.wheels(26,24)


# drive from A to B
drive.SetSpeed(speed, speed);
print(encoder.get())
drive.sleep(1)

# turn towards C
drive.SetSpeed(-speed,speed);
drive.sleep(0.7)

#drive from B to C
drive.SetSpeed(speed, speed);
drive.sleep(1.5)

# turn towards D
drive.SetSpeed(speed,-speed);
drive.sleep(0.7)

# drive from C to D
drive.SetSpeed(speed, speed);
drive.sleep(1)

# stop
drive.stop();

while 1:
    sleep(10)

drive.gpioCleanUP()
