import threading
import time
import mido

m = mido.open_output('abletree', virtual=True)

cc_numbers = [
    1,  # knob 0, mod wheel
    2,  # knob 1, breath control
    7,  # knob 2, volume
    10,  # knob 3 pan
    11,  # knob 4, expression
    53,  # knob 5
    54,  # knob 6
    74,  # knob 7
    74,  # knob 8, Filter frequency cutoff
    71,  # knob 9, Filter resonance
    58,  # knob 10
    59,  # knob 11
    60,  # knob 12
    61,  # knob 13
    62,  # knob 14
    63  # knob 15
]

class KnobState:
    def __init__(self):
        self.triggered = False
        self.last_ts = time.time()

        self.attack = 100
        self.decay = 200
        self.min = 1
        self.max = 127

        self.val = self.min

    def poke(self):
        now = time.time() 
        delt = now - self.last_ts
        last = self.val

        if self.triggered:
            self.val += delt * self.attack
        else:
            self.val -= delt * self.decay

        if self.val > self.max:
            self.val = self.max
        elif self.val < self.min:
            self.val = self.min

        self.last_ts = now
        if int(self.val) != int(last):
            return True

        return False

class MidiState:
    def __init__(self):
        self.last = {}
        self.mtx = threading.Lock()
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def on_update(self, ard, state):
        with self.mtx:
            if ard not in self.last:
                self.last[ard] = [KnobState() for _ in state]

            for i,v in enumerate(state):
                if v:
                    self.last[ard][i].triggered = True
                else:
                    self.last[ard][i].triggered = False

        if len(self.last) > 16:
            raise Exception("Too many sensor inputs")

    def run(self):
        while True:
            self._run()
            time.sleep(0.005)

    def _run(self):
        pending = []

        with self.mtx:
            for i,knobs in self.last.items():
                for j,k in enumerate(knobs):
                    if k.poke():
                        pending += [(j,k.val)]

        for (i,v) in pending:
            msg = mido.Message('control_change', 
                control=0x35,
                channel=i,
                value=int(v))

            m.send(msg)

