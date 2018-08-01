import socketserver


class MySocketServer(socketserver.BaseRequestHandler):

    def handle(self):

        print("connected with", self.client_address)
        while True:
            data = self.request.recv(4096).decode()
            data_list = data.split()
            if data == 'q':
                break
            if data_list[0] == 'put':
                print("from", self.client_address)
                print("file %s receiving..." % data_list[1])
                f = open(r"C:\Users\Administrator\Desktop\jb51.net\%s" % data_list[1],"wb")
                while True:
                    line = self.request.recv(409600)
                    if line == "done".encode():
                        f.close()
                        break
                    f.write(line)
                print("file received done...")
                self.request.sendall(bytes("ok".encode()))
            else:
                print("from", self.client_address, "-->", data)
                self.request.sendall(bytes("ok".encode()))
        print("disconnect from", self.client_address)


if __name__ == "__main__":
    ip_port = ("127.0.0.1", 9999)
    server = socketserver.ThreadingTCPServer(ip_port, MySocketServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("exit!")
