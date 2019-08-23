from socket import *
import sys

if len(sys.argv) < 3:
    print('''
		argv is error!
		run as
		python3 udp_clinet.py 127.0.0.1 8888
		''')
    raise

# 命令行輸入ip,端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

# 創建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 消息收發
while True:
    data = input("消息")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    data, addr = sockfd.recvfrom(1024)
    print("服務器接收到:", data.decode())
sockfd.close()
