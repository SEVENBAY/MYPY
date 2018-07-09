import socket


ip_port = ('127.0.0.1',9999)
s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind(ip_port)
s.listen(1)
print("waiting for connect...")
conn, address = s.accept()
print('connect from',address)
while True:
    data = conn.recv(1024).decode("utf8")
    if data == 'q':
        break
    print("消息>",data)
    info = "发送成功..."
    conn.sendall(bytes((info).encode()))

s.close()
