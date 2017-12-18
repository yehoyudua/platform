from threading import Thread

class threads(object):
    def __init__(self):
        self.threads = {}

    def new(self, name, fun, stop_fun):
        new_thread = Thread(target = fun)
        self.threads[name] = (new_thread, stop_fun)

    def stop(self, name):
        exsist = self.not_exsist(name)
        if exsist:
            return exsist

        try:
            self.threads[name][1]()
        except:
            pass
        return '^thread remove.'

    def start(self, name):
        exsist = self.not_exsist(name)
        if exsist:
            return exsist

        try:
            self.threads[name][0].start()
        except:
            return '*thread is all raedy started.'

    def close(self):
        for i in self.threads.keys():
            self.stop(i)
        return '?threads closed.'

    def not_exsist(self, name):
        if not name in self.threads.keys():
            return "*thread name doas not exsist."
        return 
        

