class proto(object):
    def __init__(self):
        try:
            self.call = eval("@function@")
        except:
            pass
    def inp(self, data):
        return str(self.call(data))
protocol = proto()
