import time
import socketserver
import threading

class handler(socketserver.StreamRequestHandler):
    def __init__(self, *args, **kw):
        socketserver.StreamRequestHandler.__init__(self, *args, **kw)
        self.pending = []

    def handle(self):
        self.server.register(self)
        print("Someone connected...")
        while True:
            try:
                # self.request is the TCP socket connected to the client
                data = self.rfile.readline()
                if len(data):
                    print("{} wrote: {}".format(self.client_address[0], data))
                    self.parse_exec(data)
                else:
                    time.sleep(0.01)
            except ConnectionResetError as e:
                print("Connection reset:", self.client_address[0])
                self.server.unregister(self)
                return

    def send(self, idx, val):
        v1,v2,v3,v4,v5 = val
        msg = f"{idx},{v1},{v2},{v3},{v4},{v5}|"
        self.wfile.write(bytes(msg, 'utf-8'))
        
    def parse_exec(self, cmd):
        if cmd == b"hello\n":
            print("Sending", self.server.state.items())
            for k,v in self.server.state.items():
                print(k,  v)
                self.send(k, v)
                  
    def __del__(self):
        self.server.unregister(self)

class Server(socketserver.ThreadingTCPServer):
    def __init__(self, host, conf):
        host,port = host.split(":")

        socketserver.ThreadingTCPServer.allow_reuse_address = True
        socketserver.ThreadingTCPServer.__init__(self, (host, int(port)), handler)
        self.sens = conf
        self.conns = {}
        self.mtx = threading.Lock()
        self.state = {}

    def serve(self):
        self.serve_forever()

    def on_change(self, idx, state):
        print("Server on_change:", idx, state)

        closed = []

        with self.mtx:
            self.state[idx] = state
            for c,_ in self.conns.items():
                try:
                    c.send(idx, state)
                except ConnectionResetError:
                    closed += [c]
                except Exception as e:
                    print("Failed to write to {}: {}".format(c.client_address[0], e))
                    closed += [c]

            for _,c in enumerate(closed):
                del self.conns[c]

    def register(self, o):
        with self.mtx:
            self.conns[o] = True

    def unregister(self, o):
        with self.mtx:
            try:
                del self.conns[o]
            except KeyError:
                return
