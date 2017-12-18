from my_libery.imports import EDY, job

class DBY_obj(job.job):
    def __init__(self, password = ''):
        self.fileType = '.db'
        self.password = password
        if password:
            self.en_de = EDY.EDY(password)
        else:
            self.en_de = None
        self.path = r'my_libery\DB'
    
    def save(self, file, data, password = ''):
        if not '.' in file:
            file += self.fileType
        if password:
            self.en_de = EDY.EDY(password)
        if self.en_de:
            open(self.path + '\%s'%(file), 'w').write(str(self.en_de.en(data)))
        else:
            open(self.path + '\%s'%(file), 'w').write(data)
        return '?OK saved.'

    def load(self, file, password = ''):
        if not '.' in file:
            file += self.fileType
        if password:
            self.en_de = EDY.EDY(password)
        if self.en_de:
            try:
                data = self.en_de.de(eval(open(self.path + '\%s'%(file), 'r').read()))
            except:
                data = "*file name or password worng!"
        else:
            data = open(self.path + '\%s'%(file), 'r').read()
        return data

    def help(self):
        h = '''^
                save(file, data, *<password>)

                load(file, *<password>)
            '''
        return h
    def start(self, cmd):
        self.cmd = cmd
        return "?wellcome to my data base tool for help enter help()."
DBY = DBY_obj()
