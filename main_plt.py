from my_libery.imports.job import job
class mymain(job):
    def __init__(self):
        self.cmd = None

    def start(self, cmd):
        self.cmd = cmd

    def help(self):
        h = '''^
            set_job(<name>)
            Exampel: set_job('proj'), set_job('group')

            back()

            show_all_scripts()
            '''
        return h
    
    def show_all_scripts(self):
        return self.cmd.make_list(self.cmd.imports)

main_plt = mymain()
