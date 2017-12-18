import socket

class my_client(object):
    def run_client(self):
        ip = input('Enter ip:')
        port = int(input("Enter port:"))
        s = socket.socket()
        s.connect((ip, port))
        while 1:
            s.send(next(data.inp).encode())
            print(s.recv(1024).decode())
        
def main():
    client = my_client()
    client.run_client()

main()
