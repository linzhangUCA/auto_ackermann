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
        self.MAX_THROTTLE = 0.25
        assert self.MAX_THROTTLE <= 1
        self.STEER_CENTER = 100
        self.MAX_STEER = 50
        self.rudder.angle = self.STEER_CENTER

    def halt(self):
        self.engine.stop()
        self.engine.close()


# test
bot = Vehicle()
