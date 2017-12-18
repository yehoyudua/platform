import socket, time, select
from my_libery.proj import myprosses
from my_libery.imports.EDY import EDY
from my_libery.imports.job import job

class server(job):
    def __init__(self, name, password, script):
        self.name = name
        self.password = password
        self.activ = True
        self.users = {}
        self.proj = script()
        try:
            self.proj.load(name, password)
        except:
            self.proj.new(name, password)
        self.s = socket.socket()
        self.s.bind(('0.0.0.0', 28))
        self.s.listen(5)

        self.control = {}
        self.names = {}
        
    def run(self):
        self.ed = EDY(self.password)
        ocs = []
        bay = b'goodBay'
        while self.activ:
            time.sleep(0.1)
            rlist, wlist, xlist = select.select([self.s] + ocs, ocs, [])
            for current_socket in rlist:
                if current_socket is self.s:
                    (new_socket, address) = self.s.accept()
                    name_and_pass = new_socket.recv(1024).decode().split(':')
                    ocs = self.connect(name_and_pass, new_socket, ocs)
                else:
                    try:
                        data = current_socket.recv(1024).decode()
                        self.users[current_socket] = self.ed.de(eval(data))
                        self.control[self.names[new_socket]].append(data)
                    except:
                        ocs = self.disconnect(current_socket, ocs)
            self.send_waiting_messages(wlist)
    
    def send_waiting_messages(self, wlist):
        for sock in wlist:
            if sock in self.users.keys() and self.users[sock]:
                data = self.users[sock]
                try:
                    out = eval('self.proj.' + data)
                except:
                    out = '<Error try help()>'
                if out == None:
                    out = 'None'
                sock.send(str(self.ed.en(str(out))).encode())
                self.users[sock] = ''

    def connect(self, name_and_pass, new_socket, ocs):
        wellcom = b'ok'

        if name_and_pass[0] == self.name and name_and_pass[1] == self.password:
            if not name_and_pass[2] in self.names.keys():
                ocs.append(new_socket)
                new_socket.send(wellcom)
                self.users[new_socket] = ''
                self.names[new_socket] = name_and_pass[2]
                self.control[self.names[new_socket]] = []
            else:
                new_socket.send(b'user name all ready exsist.')
                new_socket.close()
        else:
            new_socket.send(b'name or password worng')
            new_socket.close()
        return ocs

    def disconnect(self, current_socket, ocs):
        ocs.remove(current_socket)
        self.users.pop(current_socket)
        self.control.pop(self.names[current_socket])
        self.names.pop(current_socket)
        return ocs

    def close(self):
        self.s.close()
