from socket import *
import sys
import time

# 基本文件操作功能


class FtpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')  # 發送請求
        # 等待回覆
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完畢\n")

        else:
            # 由服務器發送失敗原因
            print(data)

    def do_get(self, filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open('filename', 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
            print("%s下載完畢\n" % filename)
        else:
            print(data)

    def do_put(self, filename):
        try:
            f = open(filename, 'rb')
        except:
            print("没有找到文件")
            return

        self.sockfd.send(('P ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
            print("%s 上傳完成" % filename)
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')


# 網路連接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)  # 文件服務器地址

    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except:
        print("連接服務器失敗")
        return

    ftp = FtpClient(sockfd)  # 功能類對象
    while True:
        print("=============命令選項==============")
        print("============  list  ==============")
        print("============get file==============")
        print("============put file==============")
        print("============  quit  ==============")
        print("==================================")

        cmd = input("請輸入命令。。")

        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd[:3] == 'get':  # 　前三個字母
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        elif cmd.strip() == "quit":
            ftp.do_quit()
            sockfd.close()
            sys.exit("謝謝使用")
        else:
            print("請輸入正確命令!!!")
            continue


if __name__ == "__main__":
    main()
