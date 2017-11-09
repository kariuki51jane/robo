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

speed = 300;







# drive from A to B
#kSetSpeed(h, speed, speed);
#pause(3.0);

# turn towards C
#kSetSpeed(h, -speed,speed);
#pause(1.2);

#drive from B to C
#kSetSpeed(h, speed, speed);
#pause(8.0);

# turn towards D
#kSetSpeed(h, speed,-speed);
#pause(1.2);

# drive from C to D
#kSetSpeed(h, speed, speed);
#pause(3.5);

# stop at the target
#kStop(h);
