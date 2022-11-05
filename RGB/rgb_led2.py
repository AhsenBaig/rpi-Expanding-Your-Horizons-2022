#!/usr/bin/python
import RPi.GPIO as GPIO   
GPIO.setmode(GPIO.BCM)  # choose BCM numbering scheme.  
 
   
GPIO.setup(17, GPIO.OUT)# set GPIO 17 as output for white led  
GPIO.setup(27, GPIO.OUT)# set GPIO 27 as output for red led  
GPIO.setup(22, GPIO.OUT)# set GPIO 22 as output for red led
   
hz = input('Please define the frequency in Herz(recommended:75): ')
reddc = input('Please define the red LED Duty Cycle: ')
greendc = input('Please define the green LED Duty Cycle: ')
bluedc = input('Please define the blue LED Duty Cycle: ')
 
red = GPIO.PWM(17, hz)    # create object red for PWM on port 17  
green = GPIO.PWM(27, hz)      # create object green for PWM on port 27   
blue = GPIO.PWM(22, hz)      # create object blue for PWM on port 22 
 
try:   
    while True:
            red.start((reddc/2.55))   #start red led
        green.start((greendc/2.55)) #start green led
        blue.start((bluedc/2.55))  #start blue led
  
except KeyboardInterrupt:
        red.stop()   #stop red led
        green.stop() #stop green led
        blue.stop()  #stop blue led
   
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit  
