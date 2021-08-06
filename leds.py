import threading
import time
import math

DEF_VELOCITY = 20
MIN_CHANGE = 1

class LED:
    def __init__(self, conf):
        print('LED conf:', conf)
        self.init = float(conf["init"])
        self.current = self.init
        self.target = self.init
        self.velocity = float(conf.get("vel", DEF_VELOCITY))
        self.min = float(conf["min"])
        self.max = float(conf["max"])

        # do something interesting with RGB, not just brightness

    def set(self, state):
        if type(state) is bool:
            if state:
                self.target = self.max
            else:
                self.target = self.init
        else:
            self.target = state

    def update(self, delta):
        d = delta * self.velocity

        if abs(self.target - self.current) < MIN_CHANGE:
            self.current = self.target
            return

        if self.target < self.current:
            self.current -= d
        elif self.target > self.current:
            self.current += d

        if self.current < self.min:
            self.current = self.min
        elif self.current > self.max:
            self.current = self.max

        # XXX draw led state

lastlog = 0
def throtlog(msg):
    global lastlog
    now = time.time()
    if now - lastlog > 0.2:
        print(msg)
        lastlog = now

class LEDs:
    def __init__(self, conf, verbose=False):
        self.leds = [LED(c) for c in conf]
        self.last = time.time()
        self.mtx = threading.Lock()
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.verbose = verbose

    def start(self):
        self.thread.start()

    def on_change(self, i, val):
        print("Setting",i,val)
        self.leds[i].set(val)
    
    def run(self):
        while True:
            now = time.time()

            for i,led in enumerate(self.leds):
                led.update(now - self.last)
                if self.verbose:
                    print("{:.2f} -> {:.2f}".format(led.current, led.target), end="\t| ")

            if self.verbose:
                print("")
                
            self.last = now
            time.sleep(0.01)
