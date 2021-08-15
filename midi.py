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
        self.val = 1

    def poke(self):
        if self.triggered:
            self.val += 1
        else:
            self.val -= 2

        if self.val > 127:
            self.val = 127
        elif self.val < 1:
            self.val = 1

class MidiState:
    def __init__(self):
        self.last = {}
        self.mtx = threading.Lock()
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def on_update(self, i, v):
        with self.mtx:
            if i not in self.last:
                self.last[i] = KnobState()
            if v:
                self.last[i].triggered = True
            else:
                self.last[i].triggered = False

        if len(self.last) > 16:
            raise Exception("Too many sensor inputs")

    def run(self):
        while True:
            self._run()
            time.sleep(0.01)

    def _run(self):
        update = False
        with self.mtx:
            for i,l in self.last.items():
                if l.triggered and l.val >= 1 and l.val <= 127:
                    update = True
                l.poke()

        if not update:
            return

        with self.mtx:
            for k,v in self.last.items():
                msg = mido.Message('control_change', 
                    control=0x35,
                    channel=k,
                    value=v.val)

            m.send(msg)

