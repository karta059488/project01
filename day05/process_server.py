from socket import *
import os
import sys
from multiprocessing import *
import traceback
import signal

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 客戶端處理函數


def handler():     # 進程方式不用添加變量
    print("Connect from", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'Receive requst')
    connfd.close()
    sys.exit(0)   # 子進程退出


# 創建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 處理防止殭屍,在父進程中忽略子進程狀態改變,子進程退出自動由系統處理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


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

    p = Process(target=handler)   # 因為複製新的使用新的地址
    p.daemon = True
    p.start()
