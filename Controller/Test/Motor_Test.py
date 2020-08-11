#!/usr/bin/env python3

import time
import Adafruit_PCA9685

# Initalise pwm
pwm = Adafruit_PCA9685.PCA9685(0x70)
pwm.set_pwm_freq(60)

def test_all_pwm():
    """ Test all pwm through the full range """
    
    print("Running test for all channel")
    time.sleep(2)
    for x in range(10):
        x= x*50
        x+=150
        pwm.set_all_pwm(0,x)
        print('Current value: (0,{})'.format(x))
        time.sleep(2)
    pwm.set_all_pwm(0,0)
    print("Test for all channel finished")
    

def test_pwm(channel):
    """ 
    Test pwm on specified channel through the full range

    :channel: Specified channel to test
    """
    
    assert type(channel) is IntType, "Parameter channel needs to be an integer"
    print("Running test for {}".format(channel))
    time.sleep(2)
    for x in range(10):
        x= x*50
        x+=150
        pwm.set_all_pwm(0,x)
        print('Current value: (0,{})'.format(x))
        time.sleep(2)
    pwm.set_pwm(channel,0,0)
    print("Test for {} finished".format(channel))

def test_speed(channel=None, on=None, off=None):
    """
    Test specified speed on specified channel.
    If no channel is selected, all pwm channels will be selected.

    :on: on pulse
    :off: off pulse
    :channel: Specified channel to test
    """
    
    assert type(channel) is IntType, "Parameter channel needs to be an integer"
    assert on != None, "Please input integer for on tick"
    assert off != None, "Please input integer for off tick"
    assert type(on) is IntType, "Parameter 'on' needs to be an integer"
    assert type(off) is IntType, "Parameter 'off' needs to be an interger"
    if channel == None:
        pwm.set_all_pwm(on, off)
    else:
        pwm.set_pwm(channel, on, off)
    print("Running at ({},{}) for channel {}".format(on,off,channel))

def stop():
    pwm.set_all_pwm(0,0)
    print("All motors stopped")

def instructions():
    all_pwm = "Test every channel through the full range"

    pwm = "Test specified channel through the full range"

    speed = """ Test specified speed on specified channel.
If no channel is specified, all channel will be tested """

    stop = "Stops motors on every channel"

    print("Test Address set to 0x70, Test Freq set to 60")
    print("Commands in this test:")
    print("test_all_pwm() : {}".format(all_pwm))
    print("test_pwm(channel) : {}".format(pwm))
    print("test_speed(channel, on, off) : {}".format(speed))
    print("stop(): {}".format(stop))

if __name__ == "__main__": instructions()
