# - Reads sensors
# - Converts to MIDI
# - Controls LEDs

import time
import socket
import argparse

DEFAULT_HOST="192.168.0.30:9999"
TIMEOUT=10
NUM_SENS_PER_ARD = 5

def test_mode(host, conf):
    from testing import generator
    from server import Server

    s = Server(host, conf["sensors"])
    #l = LEDs(conf["leds"])
    #l.start()

    def on_change(i, v):
        #l.on_change(i, v)
        s.on_change(i, v)

    generator.run(on_change)

    s.serve()

def test_client():
    # connect locally
    # read values
    # send cmd/conf/led updates?
    from client import Client

    c = Client('localhost:9090')

    while True:
        pass

def client(host, on_change):
    host, port = host.split(":")

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, int(port)))
                sock.settimeout(TIMEOUT)
                sock.sendall(bytes("hello\n", 'ascii'))

                while True:
                    if not _client(sock, on_change):
                        break

        except socket.timeout:
            print("Timed out, reconnecting...")

def _client(sock, on_change):
    print("Waiting...")
    data = str(sock.recv(1024), 'ascii')
    if len(data) == 0:
        print("Server returned 0 bytes")
        time.sleep(0.1)
        return False

    print("Received: {}".format(data))
    updates = data.split('|')

    if len(updates) <= 1:
        # Missing a |
        # discard
        return True

    for u in updates:
        toks = u.split(",")
        if len(toks) != NUM_SENS_PER_ARD + 1:
            break

        idx = int(toks[0])
        state = [int(t) for t in toks[1:]]
    
        #if val == "0":
        #    val = False
        #if val == "1":
        #    val = True

        on_change(int(idx), state)
    
    return True

def midi_client(host, conf):
    # connect to server and receive midi signals
    from midi import MidiState
    client(host, MidiState().on_update)

def led_client(host, conf):
    from leds import LEDs
    l = LEDs(conf["leds"], verbose=False)
    l.start()
    client(host, l.on_change)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--host', type=str, default=DEFAULT_HOST)
    ap.add_argument('--mode', 
        type=str, 
        default="server", 
        help="options: server, led_client, midi_client, test")
    args = ap.parse_args()

    if args.mode == "midi_client":
        midi_client(args.host, None)
        return

    from config.config import load_sql
    conf = load_sql()

    if args.mode == "server":
        from models.sensors import Sensors
        from server import Server
        srv = Server(args.host, conf["sensors"])
        Sensors(conf["sensors"], srv.on_change).start()
        srv.serve()
    elif args.mode == "led_client":
        led_client(args.host, conf)
    elif args.mode == "test":
        test_mode(args.host, conf)
    else:
        print("Unrecognized mode:", args.mode)

if __name__ == "__main__":
    main()
