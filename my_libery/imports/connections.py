import socket
from my_libery.imports.EDY import EDY

class connections(object):
    def __init__(self):
        self.s = socket.socket()
        self.sockets = {'main':{'s':self.s, 'con':False}}
        
    def connect(self, name, server_addr):
        try:
            self.sockets[name]['s'].connect(server_addr)
        except:
            return '*cant connect name error.'
        self.sockets[name]['con'] = True
        return '?socket connected.'

    def disconnect(self, name):
        try:
            self.sockets[name]['s'] = socket.socket()
            self.sockets[name]['con'] = False
        except:
            return '*cant connect name error.'
        return '?socket disconnected.'
            

    def send(self, name, st):
        self.sockets[name]['s'].send(str(self.sockets[name]['ed'].en(str(st))).encode())
        return self.sockets[name]['ed'].de(eval(self.recv(name).decode()))

    def recv(self, name):
        return self.sockets[name]['s'].recv(4096)

    def is_connect(self):
        for a, b in self.sockets.items():
            if b['con']:
                return True
        return False

    def new_socket(self, name, password):
        self.sockets[name] = {'s':socket.socket(), 'con':False, 'ed':EDY(password)}

    def close(self):
        for a, b in self.sockets.items():
            try:
                b['s'].close()
            except:
                pass

    
