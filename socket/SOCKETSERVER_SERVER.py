import socketserver


class MySocketServer(socketserver.BaseRequestHandler):

    def handle(self):

        print("connect with", self.client_address)
        while True:
            data = self.request.recv(1024).decode()
            if data == 'q':
                break
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
