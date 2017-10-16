import RPi.GPIO as GPIO
import time
from sonarR import *
from sonarL import *

while True:
    sonarR()
    sonarL()
