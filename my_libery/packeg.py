from my_libery.imports.job import job
from my_libery.DBY import DBY_obj

class mypackeg(job):
    def __init__(self):
        self.fileType = '.pack'
        self.new_packeg = ''
        self.db = DBY_obj()
        self.cmd = None

    def help(self):
        h = '''^
        show()
        
        save(<name>)

        load(<name>)
        '''
        return h

    def start(self, cmd):
        self.cmd = cmd
        self.cmd.functions.append(self.update)
        return '^packeg loaded.'

    def update(self, inp, out):
        if not '[-]' in out and not 'packeg' in inp:
            self.new_packeg += inp + '#$#'

    def save(self, name):
        self.db.save(name + self.fileType, self.new_packeg)
        return '^packeg saved.'

    def load(self, name):
        try:
            data = self.db.load(name + self.fileType)
        except:
            return '*packeg not fuond.'
        for i in data.split('#$#'):
            print('[->]'+ i + ':')
            try:
                self.cmd.smart_print(self.cmd.inp(i))
            except:
                pass
        return '^loaded sucssful.'

    def show(self):
        return '^' + ''.join(i+'\n' for i in self.new_packeg.split('#$#')[:-1])

packeg = mypackeg()
