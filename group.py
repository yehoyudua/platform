from my_libery.server import server
from my_libery.imports.EDY import EDY
from my_libery.imports.job import job
import threading
import socket

class mygroup(job):
    def __init__(self):
        self.name = ''
        self.password = ''
        self.admin = None
        self.my_server = None
        self.s = None
        self.user_name = ''
        self.cmd = None
        
    def new_group(self, name, password = '', prog = 'proj'):
        self.name = name
        self.password = password
        if name:
            self.my_server = server(name, password, self.cmd.imports[prog])
        else:
            return '*the name cant be empty.'
        self.ed = EDY(password)
        return '^group created.'
    
    def join(self, ip, name, password = ''):
        self.cmd.my_con.new_socket(name, password)
        self.cmd.my_con.connect(name, (ip, 28))
        self.cmd.my_con.sockets[name]['s'].send((name+':'+password+':'+self.user_name).encode())
        ans = self.cmd.my_con.sockets[name]['s'].recv(1024).decode()
        if ans == 'ok':
            self.cmd.back_job = self.cmd.job
            self.cmd.job = name
            return '?ok you connected.'
        else:
            return ans
        
    def run(self):
        self.activ = True
        if self.my_server:
            self.cmd.threads.new('server_group', self.my_server.run, self.stop)
            self.cmd.threads.start('server_group')
            return('^runing server...')
        else:
            return('*<create new_group() first>')
    def send(self, st):
        self.s.send(str(self.ed.en(str(st))).encode())
        return self.ed.de(eval(self.s.recv(2048).decode()))
    
    def stop(self):
        self.my_server.activ = False
        return '?group stoped.'
        
    def show(self, name):
        try:
            return self.my_server.proj.show(name)
        except:
            return '*server is not activ.'
    
    def help(self):
        h = '''^
            new_group(<name>, *<password>)

            join(<ip>, <name>, *<password>)

            run()
            stop()

            show(<obj>)
            
            help()
            '''
        return h

    def admin(self, act, how = ''):
        if act == 'show':
            if how == 'all':
                return self.my_server.control
            else:
                return self.my_server.control[how]
        elif act == 'help':
            h = '''
                admin('show', 'all')
                admin('show', <user name>)
                '''
        

    def start(self, cmd):
        self.cmd = cmd
        self.user_name = input('Enter your name: ')
        return '^for help enter help()'

group = mygroup()
