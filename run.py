from random import randint
import os
import socket

from my_libery.imports.EDY import EDY
from my_libery.imports.threads import threads
from my_libery.imports.connections import connections

###global code
__import__ = {}

__folders__ = open(r'my_libery\settings\load_folders.plt', 'r').read().split(',')

for j in __folders__:
    __mylibery__ = os.listdir(j)
    for i in __mylibery__:
        if '.py' in i:
            i = i.replace('.py', '')
            exec('from %s.%s import %s'%(j, i, i))
            __import__[i] = eval(i).__class__
###global code

class cmd(object):
    def __init__(self):
        self.job = 'main_plt'
        self.threads = threads()
        self.my_con = connections()
        self.exit = False
        self.back_job = ''
        self.job_obj = eval(self.job)
        self.functions = [packeg.update]
        self.imports = __import__

    def is_connect(self):
        return self.my_con.is_connect()

    def run(self):
        while not self.exit:
            user_input = input('%s >>> '%(self.job + self.job_obj.account()))

            self.inp_control(user_input)
            if self.exit:
                break
            
            if self.is_connect():
                re = self.my_con.send(self.job, user_input)
                print('\n### '+user_input+' ###')
                self.smart_print(re)
                print('### '+user_input+' ###\n')

            else:
                re = self.inp(user_input)
                print('\n### '+user_input+' ###')
                self.smart_print(re)
                print('### '+user_input+' ###\n')

            for i in self.functions:
                i(user_input, re)
        exit()

    def smart_print(self, data):
        hade = ''
        try:
            if data[0] == '*':
                hade = '[-] '
            elif data[0] == '^':
                hade = '[+] '
            elif data[0] == '?':
                hade = '[?] '
            for i in data[1:].split('\n'):
                print(hade + i)
        except:
            print(data)
                
    def inp(self, user_input):
        if user_input == 'help':
            return '*For help enter help()'
        try:
            return eval(('%s.'%self.job) + user_input)
        except:
            pass
        try:
            re = eval('self.' + user_input)
            if re:
                return re
        except:
            return('*<Error input> for help enter help()')

    def inp_control(self, user_input):
        if user_input == 'end()' or user_input == 'exit()':
            self.exit = True
            self.threads.close()
            self.my_con.close()
        elif user_input == 'back()':
            if self.is_connect():
                self.my_con.sockets[self.job]['s'].close()
                self.my_con.sockets[self.job]['con'] = False
                
        

    def inp_test(self, user_input):
        try:
            return eval(self.job + '.' + user_input)
        except AttributeError:
            return eval('self.' + user_input)
        except SyntaxError:
            return '*Syntax error try help()'

    def back(self):
        self.back_job, self.job = self.job, self.back_job
        return '?back'

    def set_job(self, name):
        try:
            eval(name).help()
            res = eval(name).start(self)
            self.back_job = self.job
            self.job = name
            self.job_obj = eval(self.job)
            return res
        except:
            return('*' + name + ' is not a job')

    def make_list(self, lis):
        st = '^'
        for i in lis:
            st += '             ' + i + '\n'
        return st

    def cls(self):
        os.system('cls')
        return '^your windowe is empty.'

my_cmd = cmd()

def wellcom():
    num = randint(1, len(os.listdir('my_libery\settings\wellcom')))
    print(open(r'my_libery\settings\wellcom\wellcom%s.plt'%str(num), 'r').read())

def info():
    print('')
    my_cmd.smart_print(open(r'my_libery\settings\start_info.plt', 'r').read())
    print('')

def main():
    wellcom()
    info()
    main_plt.start(my_cmd)
    my_cmd.run()
main()
