#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Class for determining the type of button click for raspberry pi 2.
# Used to control the device with a single button.
# Different functions can be associated with different types of button clicks.

# D.Plotnikov 2021

import RPi.GPIO as GPIO
from time import sleep
from time import time


class SmartButton:

    def __str__(self):                                              # info
        msg = "The class determines the type of button press: long press, single press, multiple press."
        return msg

    def __init__(self, pin, time_to_wait=1, time_longpush=2):
        self.pin = pin                                              # set GPIO № as input (button)
        self.time_to_wait = time_to_wait                            # waiting time after pressing the button
        self.time_longpush = time_longpush                          # long press time
        GPIO.setmode(GPIO.BCM)                                      # set up BCM GPIO numbering
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def push(self):  # the method returns exactly how the button was clicked: "long_push" or "***_push"
        GPIO.wait_for_edge(self.pin, GPIO.FALLING, bouncetime=200)  # waiting for a click
        print("push")
        count = 1                                                   # click counter
        push_down = time()
        while GPIO.input(self.pin) == 0:                            # polling
            sleep(0.01)
        push_up = time()
        push_time = push_up - push_down                             # how long was the button pressed

        if push_time > self.time_longpush:                          # is  it "long_push"
            return "long_push"

        if push_time < self.time_longpush:                          # timer until a new tap is made
            now = time()
            wtime = now + self.time_to_wait
            while wtime > now:                                      # polling. again
                if GPIO.input(self.pin) == 0:
                    print("push")
                    count += 1
                    wtime = now + self.time_to_wait
                    while GPIO.input(self.pin) == 0:
                        sleep(0.01)
                now = time()
        return count
