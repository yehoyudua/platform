class my_proto(object):
    def inp(self, data):
        if data.decode() == '11p':
            return b'currect'
        return data
proto = my_proto()
