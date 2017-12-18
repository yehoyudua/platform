import socket, select, time
from my_libery.imports.sec import sec

class game_server(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.server_password = ''
        self.stop = False
    
    def register(self):
        name = self.name
        password = self.password
        server_addr = (input('Enter ip: '), 80)
        s1 = socket.socket()
        s1.connect(server_addr)
        s1.recv(1024)
        s1.send(("sing_in$$$" + name + "$$$" + password).encode())
        if not "wellcom" in s1.recv(1024).decode():
            raise
        s1.send(("new_server$$$" + self.server_password).encode())
        s1.recv(1024)
        s1.send(b"sing_out")
        s1.recv(1024)
    
    def new(self, password):
        self.server_password = password
        return '^ok server create'

    def stop_s(self):
        self.stop = True

    def run(self):
        if not self.server_password:
            return '^create server first password'
        s = socket.socket()
        s.bind(('0.0.0.0', 28))
        s.listen(5)
        ocs = []
        password = self.server_password
        if password != "<password>":
            try:
                self.register()
            except:
                pass
                #return("*register faild")

        while not self.stop:
            time.sleep(0.5)
            rlist, wlist, xlist = select.select([s] + ocs, ocs, [])
            for current_socket in rlist: 
                if current_socket is s:
                    (new_socket, address) = s.accept()
                    try:
                        new_socket.send(b"Connected!")
                        d = new_socket.recv(1024).decode()
                        if d == "OK":
                            new_socket.send(password.encode())
                        else:
                            new_socket.send(b"Logged In!")
                        ocs.append(new_socket)
                    except:
                        new_socket.close()
                else:
                    try:
                        data = current_socket.recv(1024).decode()
                    except:
                        ocs.remove(current_socket)
                        continue
                    if not sec.sec(data):
                        try:
                            try:
                                run = eval(data)
                                current_socket.send(str(run).encode())
                            except:
                                exec(data)
                                current_socket.send(b"None")
                        except:
                            current_socket.send(b"Error")
                    else:
                        current_socket.send(b"Stop Hacking!")

    def hack(self, ip):
        s = socket.socket()
        s.connect((ip, 28))
        print(s.recv(1024).decode())
        s.send(b"0")
        print(s.recv(1024).decode())
        print('enter back() to stop.')
        while 1:
            msg = input('hack(%s)>>> '%ip)
            if msg == 'back()':
                break
            s.send(msg.encode())
            out = s.recv(1024).decode()
            print(out)
        s.close()
    
if __name__ == "__main__":
    ser = game_server('a', 'a')
    print(ser.new('wweee'))
    print(ser.run())
