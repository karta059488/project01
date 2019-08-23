from socketserver import *

# 創建服務器類


# class Server(ForkingMixIn, TCPServer):
class Server(ForkingTCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        # self.request ==> accept 返回的套接字
        print("Connect from",
              self.request.getpeername())
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'Receive')


if __name__ == "__main__":
    server_addr = ("0.0.0.0", 8888)

    # 創建服務器對象
    server = Server(server_addr, Handler)
    # 啟動服務器
    server.serve_forever()
