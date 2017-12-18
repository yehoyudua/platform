from my_libery.DBY import DBY_obj
from my_libery.imports.job import job
import os
#globals
types = eval(open(r'my_libery\settings\types.plt', 'r').read())
#globals

###my prosses
class myprosses(job):
    def __init__(self):
        self.fileType = '.proj'
        self.cods = {}
        self.progrem = {'name':'', 'password':'', 'type':''}
        self.compil = False
    
    #prosses scripts
    def account(self):
        if self.progrem['name']:
            return '->' + self.progrem['name']
        return ''
        
    def save(self):
        self.db = DBY_obj(self.progrem['password'])
        if self.progrem['name']:
            try:
                self.db.save(self.progrem['name'] + self.fileType, str(self.progrem))
                return('^the file is lock by password')
            except:
                return('*<Error location>')
            return '^Ok save.'

    def load(self, name, password = ''):
        self.db = DBY_obj(password)
        try:
            progrem = self.db.load(name + self.fileType)
        except:
            return('*<Error location>')
        try:
            self.progrem = eval(progrem)
        except:
            if password:
                return('*<password worng!>')
        
        for a, b in self.progrem.items():
            if a[0] == "_":
                self.cods[a] = code_node(a, b[0], open(b[0], 'r').read(), b[1])
        return('^' + name + ' is loaded...')

    def new(self, name, password = ''):
        self.progrem = {}
        self.cods = {}
        self.set('name', name)
        self.set('password', password)
        return '^create project.'

    def run(self):
        res = ''
        if not self.compil:
            res = self.compail()
        print(self.progrem['name'], 'is runing...')
        os.system(r'python my_libery\finish_projects\%s.py'%self.progrem['name'])
        res += '\nproject runing...'
        return res
        
    def compail(self):
        for a, b in self.cods.items():
            try:
                self.cods[a].connect_obj = self.cods[self.cods[a].connect]
            except:
                pass
        file = open(r'my_libery\types\%s\_compail.py'%self.progrem['type'], 'r').read()
        #try:
        exec(file)
        #except:
            #return '*Compail error'
        
        self.compil = True
        return('^' + self.progrem['name'] + ' is cmpail...')

    def add(self, code, name, loc):
        self.cods[name] = code_node(name, loc, code)

    def show(self, typ):
        all_st = ''
        try:
            return typ.show()
        except:
            pass
        if typ == 'types':
            folders = os.listdir(r'my_libery\types')
            for i in folders:
                all_st += i+'\n'
        elif typ == 'scripts':
            files = os.listdir(r'my_libery\types\%s'%self.progrem['type'])
            for i in files:
                all_st += i+'\n'
        elif typ == 'status':
            for a, b in self.progrem.items():
                all_st += str(a) + ' : ' + str(b) + '\n'
        elif typ == "my_cods":
            all_st += 'name, file, connect to\n'
            for a,b in self.progrem.items():
                if a[0] == "_":
                    all_st += a + ' ' + b[0] + ' ' + b[1] + '\n'
        elif typ == 'proj':
            return(str(self.progrem))
        else:
            all_st = ['types', 'scripts', 'status', "my_cods", 'proj']
        return '^' + str(all_st)

    def connect(self, a, b):
        if self.progrem[a] and self.progrem[b]:
            self.progrem[a][1] = b
            self.cods[a].connect = b
        return '^'+a+' ---> '+b

    def set(self, name, value):
        if name[0] == '_' and self.progrem['type']:
            value = r'my_libery\types\%s\%s.py'%(self.progrem['type'], value)
            file = open(value, 'r')
            if not file:
                return('*the part is not exsist!')
            self.cods[name] = code_node(name, value, file.read())
            file.close()
            self.progrem[name] = [value, '']
        else:
            self.progrem[name] = value
        return '^'+name + ' ---> ' + value

    def get(self, name):
        try:
            return ('?' + getattr(self, name))
        except:
            pass
        try:
            return ('?' + self.cods[name])
        except:
            pass
        try:
            return ('?' + self.progrem[name])
        except:
            pass
    #prosses script
    
    #help
    def help(self):
        h = '''^
            new(<name>, *<password>)
            Exampel: new('proj', '1234'), new('proj')

            save()
            run()
            compail()

            load(<name>, *<password>)
            Exampel: load('proj', '1234'), load('proj')

            show(data)
            Exampel: show('types'), show('help')

            set(<name>, <value>)
            Exampel: set('type', 'client'), set('password', 'qwer')
            set('_connect', 'http_server')

            get(<name>)
            Exampel: get('name'), get('type')

            connect(<code_name>, <code_name>)
            Exampel: connect('_server', '_protocol')

            end()
            exit()
            '''
        return(h)
    #help

    def start(self, cmd):
        return '^for help enter help()'
proj = myprosses()
###my prosses

class code_node(object):
    def __init__(self, name, loc, code, connect = "None"):
        self.name = name
        self.loc = loc
        self.code = code
        self.connect = connect
        self.connect_obj = None
        self.is_main = False
    def show(self):
        print('\nname: ', self.name)
        print('loction: ', self.loc)
        print(self.code)
