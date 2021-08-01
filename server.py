from config.config import load

class Server:
    def __init__(self):
        self.sens = load()

    def on_change(self, idx, state):
        print(idx, state)

        #if listener
        # send update
