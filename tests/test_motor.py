from gpiozero import PhaseEnableMotor
from time import sleep

throttle = PhaseEnableMotor(phase=24, enable=18)
print("Forward")
throttle.forward(0.2)
sleep(4)
print("Stop")
throttle.stop()
sleep(1)
print("Backward")
throttle.backward(0.2)
sleep(4)
