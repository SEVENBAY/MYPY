import socket, sys
import re
import time

re_str = "^put .+\..{3}$"
patten = re.compile(re_str)
# str = "put aaasdf.aaa"
# result = patten.match(str)
# print(result)
host = ('127.0.0.1', 9999)
s = socket.socket()
s.connect(host)
while True:
    info = input("please input('put filename'):")
    if len(info) == 0:
        continue
    if info == 'q':
        s.sendall(info.encode())
        break
    if "put" in info:
        if "put" in info and not patten.match(info):
            print("command error...")
            continue
        else:
            filename = info.split()[1]
            try:
                f = open(filename,"rb")
                f_total_count = 0
                for count, each_line in enumerate(f):
                    # 文件总行数
                    f_total_count += 1
                with open(filename, "rb") as f:
                    s.sendall(info.encode())
                    print(">>>发送中...")
                    # 已发送行数
                    send_line = 0
                    for line in f:
                        s.sendall(line)
                        send_line += 1
                        sys.stdout.write("\r")
                        sys.stdout.write("%s |%s%%" % (round(send_line*100/f_total_count)//2*'#', round(send_line*100/f_total_count)))
                        sys.stdout.flush()
                    else:
                        print(">>>发送完成...")
                        time.sleep(0.5)
                        s.sendall("done".encode())
            except FileNotFoundError:
                print("file not found...")
                s.sendall("send file fail...".encode())
    else:
        s.sendall(info.encode())
        data = s.recv(4096)
        print("send-->", data.decode())
s.close()
