from config.config import *
import time
import random
import threading

class TesterState:
    def __init__(self, num):
        self.n = num
        self.state = [False for _ in range(num)]

    def pick(self):
        i = random.randint(0, len(self.state)-1)
        self.state[i] = not self.state[i]
        return i, self.state[i]

def run(on_change):
    sens = load_sql()
    state = TesterState(len(sens["sensors"]))
    def _run():
        while True:
            time.sleep(0.4)
            if random.random() > 0.5:
                i, s = state.pick()
                on_change(i, s)

    t = threading.Thread(target=_run, daemon=True)
    t.start()