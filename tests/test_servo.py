import time
from adafruit_servokit import ServoKit


kit = ServoKit(channels=8, address=0x40)
print("180")
kit.servo[0].angle = 180  # left bound
time.sleep(1)
print("50")
kit.servo[0].angle = 50  # right bound
time.sleep(1)
print("90")
kit.servo[0].angle = 115
time.sleep(1)
