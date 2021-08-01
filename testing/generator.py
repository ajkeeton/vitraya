from config.config import *
import time
import random

class TesterState:
    def __init__(self, num):
        self.n = num
        self.state = [False for _ in range(num)]

    def pick(self):
        i = random.randint(0, len(self.state)-1)
        self.state[i] = not self.state[i]
        return i, self.state[i]

def run(on_change):
    sens = load()
    state = TesterState(len(sens))

    while True:
        time.sleep(0.25)
        if random.random() > 0.5:
            i,s = state.pick()
            on_change(i,s)