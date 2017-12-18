import socket
from time import sleep
from my_libery.imports.job import job

class myshop(job):
    def __init__(self):
        self.server_addr = ('127.0.0.1', 80)
        self.s = socket.socket()
        self.connect = False
    
    def start(self, cmd):
        ##
        try:
            if not self.connect:
                name = input('Enter a name: ')
                password = input('Enter a password: ')
                self.s.connect(self.server_addr)
                self.s.recv(1024).decode()
                self.send('sing_in$$$'+name+'$$$'+password)
                self.connect = True
        except:
            return '*your computer cant connect to serever.'
        #
        self.get('all')
        return('^' + name + ' your connected.')
        ##

    def help(self):
        return('^help.')
    
    def send(self, st):
        self.s.send(st.encode())
        return self.s.recv(4096).decode()

    def show(self, dic, sp = ''):
        sp += '   '
        for a, b in dic.items():
            if type(b) == dict:
                print(sp + '##' + a + '##')
                self.show(b, sp)
            else:
                 print(sp + a + ': ' + str(b))
        return '^ok'

    def get(self, st):
        my_get = eval(self.send('shop$$$%s$$$get'%st))
        if type(my_get) == dict:
            self.show(my_get)
        else:
            return('^    ' + st + ': ' + str(my_get))
        
shop = myshop()
