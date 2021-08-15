import mido
import time
import random

from mido.ports import multi_receive


cc_number = [
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
def generate():
    m = mido.open_output('abletree', virtual=True)

    while True:
        msg = mido.Message('control_change',
                channel=0,
                value=random.randint(1, 0x7f),
                control=0x35,
                #control=0x1f # random.randint(1, 127)
                ) # random.randint(1, 127))
        print(msg.hex())
        m.send(msg)
        time.sleep(0.5)

generate()
