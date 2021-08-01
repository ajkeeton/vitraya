
# - Reads sensors
# - Converts to MIDI
# - Controls LEDs

# Can be run as a server to only read and forward sensor data to a client
from server import Server

def test_server():
    from testing import generator

    s = Server()

    generator.run(s.on_change)

def test_client():
    # connect locally
    # read values
    # send led updates
    from client import Client

    c = Client('localhost:9999')

    while True:
        pass

test_server()
test_client()