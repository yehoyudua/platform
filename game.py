from my_libery.imports.Gserver import game_server
from my_libery.imports.job import job

class mygame(job):
    def __init__(self):
        self.name = ''
        self.password = ''
        self.my_server = None
        
    def new_server(self, name, password):
        self.name = name
        self.password = password
        self.my_server = game_server(name, password)
        return '^server created.'

    def run_server(self, password):
        if self.my_server:
            self.my_server.new(password)
        else:
            return '*create server first.'
        self.cmd.threads.new('game_server', self.my_server.run, self.stop_server)
        self.cmd.threads.start('game_server')
        return '^runing server...'

    def stop_server(self):
        if self.my_server:
            self.my_server.stop_s()
            return '^server stoped.'
        else:
            return '*create server first.'

    def hack(self, ip):
        self.my_server.hack(ip)
        return '?back'

    def help(self):
        h = '''
            new_server(<name>, <password>) connect to big server

            run_server(<password>) create game server

            stop_server() stop server

            hack(<ip>) hack to server by ip
            '''
        return h

    def start(self, cmd):
        self.cmd = cmd
        return '^for help enter help()'
game = mygame()
        
    
