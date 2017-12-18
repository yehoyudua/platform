class job(object):
    def __init__(self):
        self.theards = {}
        self.connections = {}
        self.cmd = None

    def start(self, cmd):
        self.cmd = cmd
        return 'OK'

    def account(self):
        return ''

    def help(self):
        h = '''
            *no help for this module
            '''
        return h
