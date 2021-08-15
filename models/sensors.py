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
SENS_PER_ARD = 5

class Arduino:
    def __init__(self, addr):
        self.addr = addr
        self.probe()

    def probe(self):
        return cmds.parse(i2c, self.addr)

class Sensors:
    def __init__(self, conf, cb):
        self.raw_conf = conf
        self.on_update = cb
        self.ards = []
        self.thread = threading.Thread(target=self.run, daemon=True)
        #self.mtx = threading.Lock()

    def add(self, addr):
        self.ards += [Arduino(addr)]

    def probe(self):
        last = []
        for a in self.ards:
            last += [a.probe()]
        return last

    def start(self):
        self.thread.start()

    def run(self):
        global i2c
        dvcs = i2c.scan()

        print("I2C devices found: ", [hex(i) for i in dvcs])
        time.sleep(0.5)

        if not len(dvcs):
            return

        if I2C_ARD1 in dvcs:
            self.ards += [Arduino(I2C_ARD1)]
        if I2C_ARD2 in dvcs:
            self.ards += [Arduino(I2C_ARD2)]

        # XXX Revisit
        last = [[] for _ in range(len(self.ards))]

        while True:
            try:
                latest = self.probe()

                # print(latest)
                for i,_ in enumerate(latest):
                    for j,v in enumerate(latest[i]):
                        # linearized offset
                        loff = i*SENS_PER_ARD + j

                        if len(last) <= loff:
                            last += [-1 for _ in range(loff - len(last) + 1)]

                        if v != last[loff]:
                            if self.on_update:
                                self.on_update(loff, v)
                            last[loff] = v

            except Exception as e:
                print("Exception in sensor loop:", e)
                time.sleep(0.25)
                # Reinit i2c
                i2c.deinit() 
                i2c = busio.I2C(board.SCL, board.SDA)

            time.sleep(0.01)

if __name__ == "__main__":
    sens_main()
