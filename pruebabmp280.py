from machine import I2C, Pin
import time
from bmp280 import *

bus = I2C(0, sda=Pin(0), scl=Pin(1))
bmp = BMP280(bus)

while True:
    print(bmp.temperature)
    print(bmp.pressure)
    time.sleep(5)
    
