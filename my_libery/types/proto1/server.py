import socket

class my_server(object):
    def __init__(self):
        self.s = socket.socket()
        self.s.bind(('0.0.0.0', 80))
        self.s.listen(5)
    def run_server(self):
        new_s, addr = self.s.accept()
        while 1:
            try:
                new_s.send(proto.inp(new_s.recv(1024)))
            except:
                new_s.close()
    def close():
        self.s.close()
def main():
    server = my_server()
    server.run_server()
main()
