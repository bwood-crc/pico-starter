# Import necessary modules
from machine import I2C, Pin
from ds3231 import *
import time

# Define the pins for I2C communication
sda_pin=Pin(4)
scl_pin=Pin(5)

# Initialize the I2C interface with the specified pins
i2c = I2C(0, scl=scl_pin, sda=sda_pin)
time.sleep(0.5)

# Create an instance of the DS3231 class for interfacing with the DS3231 RTC
ds = DS3231(i2c)

# Set the DS3231 RTC to current system time
ds.set_time()
