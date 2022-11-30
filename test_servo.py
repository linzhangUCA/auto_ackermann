import time
from adafruit_servokit import ServoKit


kit = ServoKit(channels=8, address=0x77)
print("180")
kit.servo[6].angle = 180
time.sleep(1)
print("60")
kit.servo[6].angle = 60
time.sleep(1)
print("90")
kit.servo[6].angle = 90
time.sleep(1)
