import sys
import time
import pygame
from pygame.locals import *
from pygame import event, display, joystick
from adafruit_servokit import ServoKit


def get_numControllers():
    return joystick.get_count()


# SETUP
kit = ServoKit(channels=8, address=0x77)
steer = kit.servo[6]
display.init()
joystick.init()
print(f"{get_numControllers()} joystick connected")
js = joystick.Joystick(0)


# MAIN
while True:
    for e in event.get():
        if e.type == QUIT:
            print("QUIT detected, terminating...")
            pygame.quit()
            sys.exit()
        if e.type == JOYAXISMOTION:
            v_0 = js.get_axis(0)
            print(f"steering joystick value: {v_0}")
