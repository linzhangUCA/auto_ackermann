import sys
import time
import numpy as np
import pygame
from pygame.locals import *
from pygame import event, display, joystick
from adafruit_servokit import ServoKit
from gpiozero import PhaseEnableMotor


class Vehicle:

    def __init__(self, servo_address=0x40, servo_channel=0, motor_phase=24, motor_enable=18):
        # instantiate motor and servo
        self.engine = PhaseEnableMotor(phase=motor_phase, enable=motor_enable)
        self.servo_kit = ServoKit(channels=16, address=servo_address)
        self.steer = servo_kit.servo[servo_channel]
        # set limit for motor and servo
        self.MAX_THROTTLE = 0.25
        assert MAX_THROTTLE <= 1
        self.STEER_CENTER = 100
        self.MAX_STEER = 50
        self.steer.angle = self.STEER_CENTER
        display.init()
        joystick.init()
        print(f"{self.get_numControllers()} joystick connected")
        self.controller = joystick.Joystick(0)

    def get_numControllers():
        return joystick.get_count()


