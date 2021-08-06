import time
import sys
import board
import busio
import struct
import binascii
from config.config import load_sql

I2C_ARD1 = 8
I2C_ARD2 = 9

class Arduino:
    def __init__(self, addr):
        self.addr = addr
        self.probe()

    def probe():
        pass

class Sensors:
    def __init__(self, conf):
        self.raw_conf = conf
        self.ards = []

    def add(self, addr):
        self.args += [Arduino(addr)]

def sen_main():
    i2c = busio.I2C(board.SCL, board.SDA)

    dvcs = i2c.scan()
    conf = load_sql()

    print("I2C devices found: ", [hex(i) for i in dvcs])

    sensors = Sensors(conf["sensors"])
    
    if I2C_ARD1 in dcvs:
        sensors.add(I2C_ARD1)
    if I2C_ARD2 in dcvs:
        sensors.add(I2C_ARD2)

if __name__ == "__main__":
    sen_main()