#!/usr/bin/python
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

Relay = [5, 6, 13, 16, 19, 20, 21, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(0,8):
    GPIO.setup(Relay[i], GPIO.OUT)
    GPIO.output(Relay[i], GPIO.HIGH)

try:
    while True:
        for i in range(6):
            if i == 0:
                GPIO.output(Relay[0], GPIO.LOW)
                GPIO.output(Relay[1], GPIO.LOW)
            else:
                GPIO.output(Relay[0], GPIO.HIGH)
                GPIO.output(Relay[1], GPIO.HIGH)
            if i == 2:
                GPIO.output(Relay[0], GPIO.LOW)
            else:
                GPIO.output(Relay[0], GPIO.HIGH)
            if i == 3:
                GPIO.output(Relay[1], GPIO.LOW)
            else:
                GPIO.output(Relay[1], GPIO.HIGH)
            if i == 4:
                GPIO.output(Relay[0], GPIO.LOW)
            else:
                GPIO.output(Relay[0], GPIO.HIGH)
            time.sleep(0.2)
except:
    GPIO.cleanup()


