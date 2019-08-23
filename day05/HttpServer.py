# coding=utf-8
'''
http server v2.0
1.多現成併發
2.可以請求簡單數據
3.能進行簡單請求解析
4.結構使用類進行封裝
'''

from socket import *
from threading import Thread
import sys
import traceback
import time

# httpserver類封裝具體的服務器功能


class HTTPServer(object):
    def __init__(self, server_addr, static_dir):
        # 增加服務器對象屬性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        # 創建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(self.server_address)

        # 設置監聽等待客戶端連接
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port%d" % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服務器退出")
            except Exception:
                traceback.print_exc()
                continue
            # 創建新的現成處理請求
            clientThread = Thread(
                target=self.handleRequest, args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    # 具體的客戶端請求函數
    def handleRequest(self, connfd):
        # 接收客戶端請求
        request = connfd.recv(4096)
        # 解析請求內容
        requestHeaders = request.splitlines()
        print(connfd.getpeername(), ":", requestHeaders[0])

        # 獲取具體請求內容b'GET / HTTP/1.1'
        getRequest = str(requestHeaders[0]).split(' ')[1]   # 獲取道地一向請求內容( HTTP)

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd, getRequest)
        else:
            # pass
            self.get_data(connfd, getRequest)
        connfd.close()

    def get_html(self, connfd, getRequest):
        if getRequest == '/':
            filename = self.static_dir + "/index.html"  # 表示要獲取到主頁面
        else:
            filename = self.static_dir + getRequest
        try:
            f = open(filename)
        except Exception:
            # 没有找到页面
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += '\r\n'
            responseBody = "Sorry,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self, connfd, getRequest):
        urls = ['/time', '/tedu', '/python']

        if getRequest in urls:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            if getRequest == '/time':
                responseBody = time.ctime()
            elif getRequest == '/tedu':
                responseBody = "Welcome to tedu"
            elif getRequest == '/python':
                responseBody = "開心用python"

        else:
            responseHeaders = "HTTP/1.1 404 NOT FOUND\r\n"
            responseHeaders += '\r\n'
            responseBody = "Sorry,not found the data"

        response = responseHeaders + responseBody
        connfd.send(response.encode())


if __name__ == "__main__":
            # 服務器ip
    server_addr = ('0.0.0.0', 8000)
    # 我的靜態頁面存處目錄
    static_dir = './static'

    # 生成對象
    httpd = HTTPServer(server_addr, static_dir)

    # 啟動服務器
    httpd.server_forever()
