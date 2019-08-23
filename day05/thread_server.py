from socket import *
import os
import sys
from threading import *
import traceback

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 客戶端處理函數


def handler(connfd):
    print("Connect from", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'Receive requst')
    connfd.close()


# 創建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 等待客戶端請求
while True:
    try:
        connfd, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服務器退出")
    except Exception:
        traceback.print_exc()
        continue

    t = Thread(target=handler, args=(connfd,))
    t.setDaemon(True)    # 則分支線程隨主線程退出
    t.start()
