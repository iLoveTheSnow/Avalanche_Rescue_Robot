#Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
#[GCC 6.3.0 20170516] on linux
#Type "copyright", "credits" or "license()" for more information.
#Traceback (most recent call last):
#File "<pyshell#0>", line 1, in <module>
#ImportError: No module named 'RSi'

import RPi.GPIO as GPIO
import smbus
## ExpanderPi import ADC

##adc = ADC()
##adc.set_adc_refvoltage(5)
##import time


from rrb2 import *
rr = RRB2()
#GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD)
#Traceback (most recent call last):
 # File "<pyshell#3>", line 1, in <module>
  #  GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD)
#AttributeError: module 'RPi.GPIO' has no attribute 'PUD'
##GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
##GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
##GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
##GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.PWM(21, 0)
#Warning (from warnings module):
 # File "__main__", line 1
#RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
while True:

##    print("This is on pin 21 " , GPIO.input(21))
##    print adc.read_adc_voltage(1,0)
##    ##print read_voltage(2)
##    time.sleep(1)
#    while GPIO.wait_for_edge(21, GPIO.RISING):
#        print("Are we here")
#        while GPIO.wait_for_edge(21, GPIO.FALLING) != True:
#            print("Working 2")
            
    #while GPIO.wait_for_edge(21, GPIO.RISING):
     #   while GPIO.wait_for_edge(21, GPIO.FALLING)!= True:
      #      print(GPIO.input(21))
##            print("pin 21 output: ", GPIO.input(21))
####            print(input(21))
####            print("pin 20 output: ", GPIO.input(20))
####            print("pint 3 output: ", GPIO.input(3))
####            print(GPIO.gpio_function(2))
####            print(GPIO.output())
##            ## Car drives here    
##    
####    GPIO.wait_for_edge(21, GPIO.RISING)

    i = 0
    ##for (i=0; i>5; i++)
    while i < 5: 
        rr.forward(2, 1)
        rr.reverse(4, 1)
        rr.forward(2, 1)
        rr.left(.5, 1)
        i = i + 1
    i = 0 
    rr.right(2, 1)
    rr.forward(7, 1)
##    while i < 5: 
##        rr.forward(2, 1)
##        rr.reverse(4, 1)
##        rr.forward(2, 1)
##        rr.left(.5, 1)
##        i = i + 1
####    i =0
##    rr.forward(5.1)
    
    
      
##    rr.left(6.3, 1)
##    rr.reverse(2, 1)
##    rr.right(2, 1)
##    print(GPIO.RISING)

    ##GPIO.wait_for_edge(21, GPIO.FALLING)
    ##print(GPIO.FALLING)
    
    GPIO.cleanup()
    