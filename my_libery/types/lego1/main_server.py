import socket, time

class serverTCP(object):
    def __init__(self):
        self.s = socket.socket()
        self.s.bind(("0.0.0.0", 28))
        self.s.listen(1)
        try:
            self.call = eval("@function@")
        except:
            pass
    def run(self):
        new_s, addr = self.s.accept()
        while 1:
            time.sleep(0.1)
            try:
                ans = self.call([new_s.recv(1024).decode()])
                new_s.send(ans.encode())
            except:
                new_s.close()
server = serverTCP()

def main():
    server.run()
main()
