import time
import sys
import board
import busio
import struct
import binascii
import sys
import threading

sys.path.insert(0, '.')
import cmds
from config.config import *

i2c = busio.I2C(board.SCL, board.SDA)
I2C_ARD1 = 8
I2C_ARD2 = 9
I2C_ARD3 = 10
I2C_ARD4 = 11
SENS_PER_ARD = 5
PACKET_SIZE = 20

def crc16(data: bytes):
    data = bytearray(data)
    poly = 0x8001
    crc = 0
    for b in data:
        crc ^= (0xFF & b) << 8
        for _ in range(0, 8):
            if crc & (1 << 15): 
                crc <<= 1
                crc ^= poly
            else:
                crc <<= 1

    return crc & 0xffff

class Arduino:
    def __init__(self, addr):
        self.addr = addr
        self.probe()

    def probe(self):
        if not i2c.try_lock():
            return []

        buf = bytearray(PACKET_SIZE)
        i2c.readfrom_into(self.addr, buf)
        #print(addr, binascii.hexlify(buf), end='')
        i2c.unlock()

        ts, t, l, a, b, c, d, e, cs = struct.unpack('LHHHHHHHH', buf)

        # Check CRC
        if cs != crc16(buf[0:18]) and t != 0:
            # print(f"{addr}: CRC failed for address: {cs} invalid")
            return []

        if t == 0:
            print(f"{addr}: Hello message, {l} bytes:")
            print(binascii.hexlify(buf))
        elif t == 1:
            # print(ts, "State:", a, b, c, d, e)
            return [a, b, c, d, e]
        else:
            print(f"Invalid type {t} in:", binascii.hexlify(buf))

class Sensors:
    def __init__(self, conf, cb):
        self.raw_conf = conf
        self.on_update = cb
        self.ards = {} 
        self.thread = threading.Thread(target=self.run, daemon=True)

    def add(self, addr):
        self.ards += [Arduino(addr)]

    def probe(self):
        last = {}
        for _,a in self.ards.items():
            last[a.addr] = a.probe()
        return last

    def start(self):
        self.thread.start()

    def run(self):
        global i2c
        dvcs = i2c.scan()

        print("I2C devices found: ", [hex(i) for i in dvcs])
        time.sleep(0.25)

        if not len(dvcs):
            return

        if I2C_ARD1 in dvcs:
            self.ards[I2C_ARD1] = Arduino(I2C_ARD1)
        if I2C_ARD2 in dvcs:
            self.ards[I2C_ARD2] = Arduino(I2C_ARD2)

        last = {} 

        while True:
            try:
                latest = self.probe()

                for ard,state in latest.items():
                    if not state:
                        continue

                    if last.get(ard, []) != state:
                        self.on_update(ard, state)
                        last[ard] = state
           
            except Exception as e:
                print("Exception in sensor loop:", e)
                time.sleep(0.25)
                # Reinit i2c
                i2c.deinit() 
                i2c = busio.I2C(board.SCL, board.SDA)

            time.sleep(0.005)

if __name__ == "__main__":
    sens_main()
