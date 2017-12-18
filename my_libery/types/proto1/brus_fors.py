
chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
class my_brus_fors(object):
    def __init__(self):
        self.inp = self.my_inp()
    def my_inp(self):
        for i in chars:
            for j in chars:
                for k in chars:
                    yield i + j + k
data = my_brus_fors()

