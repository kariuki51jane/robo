import compass 
from motor import *
import time



s = compass.hmc5883l()
def deg():
          degrees =s.degrees(s.heading())
          deg=degrees+90
          if deg>360:
            deg=deg-360
            return deg
          else:
            return deg

def turn():    
    degrees =s.degrees(s.heading())
        
    x=deg()
    print degrees
    print x
           
    if degrees>=270:
        while(270<=degrees<=359):   #set turning direction
            obsright()
            degrees =s.degrees(s.heading()) #update degrees
            print degrees
        while(0<=degrees<=x-10):
            obsright()
            degrees =s.degrees(s.heading())
            print degrees
        while(x+10<=degrees<=100):
            obsleft()
            degrees =s.degrees(s.heading())
            print degrees
              
    else:
        while(0<=degrees<=x-10):
            obsright()
            degrees =s.degrees(s.heading())
            print degrees
        while(x+10<=degrees<=359):
            obsleft()
            degrees =s.degrees(s.heading())
            print degrees


def deg1():
          degrees =s.degrees(s.heading())
          deg=degrees-90
          if deg<0:
            deg=deg+360
            return deg
          else:
            return deg

def turn1():    
    degrees =s.degrees(s.heading())
        
    x=deg1()
    print degrees
    print x
           
    if degrees<=90:
        while(0<=degrees<=90):   #set turning direction
            obsleft()
            degrees =s.degrees(s.heading()) #update degrees
            print degrees
        while(x-10<=degrees<=359):
            obsleft()
            degrees =s.degrees(s.heading())
            print degrees
        while(270<=degrees<=x+10):
            obsright()
            degrees =s.degrees(s.heading())
            print degrees
              
    else:
        while(359<=degrees<=x+10):
            obsleft()
            degrees =s.degrees(s.heading())
            print degrees
        while(0<=degrees<=x-10):
            obsright()
            degrees =s.degrees(s.heading())
            print degrees
