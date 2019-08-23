from socketserver import *

# 創建服務器類


class Server(ThreadingMixIn, UDPServer):
    pass


class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline()
            print(self.client_address)
            if not data:
                break
            print(data)
            self.wfile.write(b'Receive from')


if __name__ == "__main__":
    server_addr = ("0.0.0.0", 8888)

    # 創建服務器對象
    server = Server(server_addr, Handler)
    # 啟動服務器
    server.serve_forever()
