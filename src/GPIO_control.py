from PCA9685 import PWM
import time
from smbus2 import SMBus

fPWM = 50
i2c_address = 0x40      #connect to the I2C address of the motor
channel = 0             # control board address connected to the motor
a = 8.5
b = 2

def setup():
    global pwm
    bus = SMBus(1)
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)


def setup():
    global pwm
    bus = SMBus(1)  # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)


def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print
    "direction =", direction, "-> duty =", duty
    time.sleep(1)




