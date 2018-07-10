import socket


host = ('127.0.0.1', 9999)
s = socket.socket()
s.connect(host)
while True:
    info = input("please input(q for disconnect):")
    if len(info) == 0:
        continue
    if info == 'q':
        s.sendall(bytes(info.encode()))
        break
    s.sendall(bytes(info.encode()))
    data = s.recv(1024)
    print("send-->", data.decode())
s.close()
