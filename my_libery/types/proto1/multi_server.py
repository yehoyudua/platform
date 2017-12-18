import random, select, time, socket

class my_server(object):
    def run_server(self):
        s = socket.socket()
        port = 80

        try:
            s.bind(('0.0.0.0', port))
        except:
            print('the port is open cheke anzer port!\n')

        s.listen(5)

        def send_waiting_messages(wlist):
            for i in wlist:
                i.send(mas)
                

        ###connect
        ocs = []
        mas = b'hello'
        while True:
            time.sleep(0.1)
            rlist, wlist, xlist = select.select([s] + ocs, ocs, [])
            for current_socket in rlist:
                if current_socket is s:
                    (new_socket, address) = s.accept()    
                    ocs.append(new_socket)
                else:
                    #try:
                    if 1:
                        data = proto.inp(current_socket.recv(1024))
                        print('data ', data)
                        mas = data
                    #except:
                     #   ocs.remove(current_socket)
                      #  print("Connection with client closed.")
            send_waiting_messages(wlist)
        ###end connect

def main():
    server = my_server()
    server.run_server()
main()
