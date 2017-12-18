from hashlib import shake_256

class EDY_lego(object):
    def __init__(self):
        password = input('Enter encrypt password: ')
        k1, k2 = self.new_keys(password)
        self.strong = 5
        self.range_of_chars = 255
        self.k1 = k1
        self.k2 = k2
        self.k3 = self.my_hash(self.k1, self.k2)

    def inp(self, string):
        string = string[0]
        if type(string) == str:
            return self.en(string)
        elif type(string) == list:
            return self.de(string)

    def new_keys(self, password):
        num = 100
        has = shake_256()
        has.update(password.encode())
        k1 = self.get_num(has.hexdigest(num))
        k2 = self.get_num(has.hexdigest(num*2)[num:])
        return k1, k2

    def get_num(self, st):
        num = 0
        for i in st:
            num += ord(i)
        return num

    def my_hash(self, num, num_of_digest):
        hk3 = shake_256()
        hk3.update(str(num).encode())
        k3 = self.get_num(hk3.hexdigest(num_of_digest))
        return k3

    def g(self, n):
        e = (n**self.k1) % self.k3
        return e, self.my_hash(e+self.k1, 30)

    def en_hard(self, st):
        ans = []
        for i in st:
            i = ord(i)
            ans.append(self.g(i))
        return(ans)

    def dg(self, e, he):
        for i in range(0, self.range_of_chars):
            if (i**self.k1) % self.k3 == e:
                if self.my_hash(e+self.k1, 30) == he:
                    return(i)

    def de_hard(self, data):
        st = 0
        for e, he in data:
            st += self.dg(e, he)
        return st

    def en(self, st):
        ans = []
        password = 0
        hard_points = 0
        for i in st:
            if hard_points < self.strong:
                password += ord(i)
                ans.append(self.en_hard(i))
                hard_points += 1
            else:
                i = ord(i)
                ans.append((i + password) % 255)
                password = i
        return ans

    def de(self, data):
        st = ""
        password = 0
        for i in data:
            if type(i) == list:
                ans = self.de_hard(i)
                password += ans
                st += chr(ans)
            else:
                ans = (i - password) % 255
                st += chr(ans)
                password = ans
        return st
                
EDY = EDY_lego()
'''def test():
    ed = EDY("<password>")
    data = ed.en('hello it is working!.')
    print("encrypt:", data)
    print("decrypt:", ed.de(data))
'''

