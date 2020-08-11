#!/usr/bin/env python3

import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address=0x70)
pwm.set_pwm_freq(60)

motor_left = 0 # 150 goes forward
motor_right = 1# 600 goes forward
#swap the values to swap direction

greetings = ['hello', 'hi', 'on,']
farewells = ['bye', 'off']
    
class motor():
    """ Motor Controls """
    def turn_left():
        pwm.set_pwm(motor_left, 0, 0)
        pwm.set_pwm(motor_right, 0, 150)
        
    def turn_right():
        pwm.set_pwm(motor_left, 0, 600)
        pwm.set_pwm(motor_right, 0, 0)
        
    def foward():
        pwm.set_pwm(motor_left, 0, 600)
        pwm.set_pwm(motor_right, 0, 150)
        
    def reverse():
        pwm.set_pwm(motor_left, 0, 150)
        pwm.set_pwm(motor_right, 0, 600)
    
    def stop():
        pwm.set_all_pwm(0, 0)
        

        
            
class speech():  
    def command(cmd):
        if any(x in cmd for x in greetings): 
            print("Hi there!")
            speech.action('greetings')
            
        elif any(x in cmd for x in farewells):  
            print('See you later!')
            speech.action('farewells')
            
        elif ('green light') in cmd:
            print("Let's go!")
            motor.foward()
            
        elif ('left') in cmd:
            print("Turning left")
            motor.turn_left()
            
        elif ('right') in cmd:
            print("Turning right")
            motor.turn_right()
            
        elif ('wait') in cmd:
            print("HALT!!!")
            motor.stop()
            
    def action(event):
        if 'greetings' in event:
            print(':D')
            motor.turn_left()
            time.sleep(3)
            motor.stop()

        if 'farewells' in event:
            print(':<')
            motor.reverse()
            time.sleep(.5)
            motor.stop()
            


