import sys
import time
import numpy as np
import pygame
from pygame.locals import *
from pygame import event, display, joystick
from adafruit_servokit import ServoKit
from gpiozero import PhaseEnableMotor


class Vehicle:
    def __init__(
        self, kit_address=0x40, servo_channel=0, motor_phase=24, motor_enable=18
    ):
        # vehicle has to be under control
        display.init()
        joystick.init()
        print(f"{joystick.get_count()} joystick connected")
        assert joystick.get_count() == 1, f"Vehicle has to be controlled by exact 1 joystick"
        self.controller = joystick.Joystick(0)
        # instantiate motor and servo
        self.kit = ServoKit(channels=16, address=kit_address)
        self.rudder = self.kit.servo[servo_channel]
        self.engine = PhaseEnableMotor(phase=motor_phase, enable=motor_enable)
        # set limit for motor and servo
        self.max_throttle = 0.25
        assert self.max_throttle <= 1
        self.steer_center = 100
        self.max_steer = 50
        self.rudder.angle = self.steer_center

    def halt(self):
        self.engine.stop()
        self.engine.close()
        sys.exit()


# Uncomment following to test
# bot = Vehicle()
# try:
#     while True:
#         for e in event.get():
#             if e.type == QUIT:
#                 print("QUIT detected, terminating...")
#                 pygame.quit()
#                 sys.exit()
#             if e.type == JOYAXISMOTION:
#                 val_0 = bot.controller.get_axis(0)
#                 val_4 = bot.controller.get_axis(4)
#                 print(f"steering joystick value: {val_0}, speed joystick value: {val_4}")
#                 speed = -np.clip(val_4, -bot.max_throttle, bot.max_throttle)
#                 if speed > 0:
#                     bot.engine.forward(speed)
#                 elif speed < 0:
#                     bot.engine.backward(-speed)
#                 else:
#                     bot.engine.stop()
#                 ang = bot.steer_center - bot.max_steer * val_0
#                 bot.rudder.angle = ang
# except KeyboardInterrupt:
#     bot.halt()
