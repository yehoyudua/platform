import socket

class SSY(socket.socket):
    def __init__(self, fileno=None):
        #self.fileno = fileno
        super(SSY).__init__()
s = SSY()
