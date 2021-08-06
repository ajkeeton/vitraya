
# - Reads sensors
# - Converts to MIDI
# - Controls LEDs

# Can be run as a server to only read and forward sensor data to a client
from server import Server
from leds import LEDs
import time
import socket
import argparse

from config.config import load_sql

DEFAULT_HOST="localhost:9999"

def test_mode(host, conf):
    from testing import generator

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
    host,port = host.split(":")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, int(port)))
        sock.sendall(bytes("hello\n", 'ascii'))

        while True:
            data = str(sock.recv(1024), 'ascii')
            if len(data) == 0:
                time.sleep(0.01)
                continue

            print("Received: {}".format(data))
            updates = data.split('|')

            # XXX 
            # need to make sure we have a '|' or this is an incomplete message
            for u in updates:
                toks = u.split(",")
                if len(toks) != 2:
                    break
                idx, val = toks
                if val == "False":
                    val = False
                if val == "True":
                    val = True

                on_change(int(idx), bool(val))

def midi_client(host, conf):
    #m = MIDI(conf["sensors"])
    #client(host, m.on_change)
    return

def led_client(host, conf):
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

    conf = load_sql()

    if args.mode == "server":
        Server(args.host, conf["sensors"]).serve()
    elif args.mode == "led_client":
        led_client(args.host, conf)
    elif args.mode == "midi_client":
        midi_client(args.host, conf)
    elif args.mode == "test":
        test_mode(args.host, conf)
    else:
        print("Unrecognized mode:", args.mode)

if __name__ == "__main__":
    main()