from socket import *

# 創建客戶端套接
sockfd = socket(AF_INET, SOCK_STREAM)

# 發起連接
server_addr = ('127.0.0.1', 8888)
sockfd.connect(server_addr)


while True:
    # 消息發送接收
    data = input("發送。。")
    sockfd.send(data.encode())
    if not data:
        break
    data = sockfd.recv(1024)
    print("接收到", data.decode())

# 關閉套接字
sockfd.close()
