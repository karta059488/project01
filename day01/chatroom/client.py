from socket import *
import sys
import os

# 發送消息


def send_msg(s, name, addr):
    while True:
        text = input("發言：")
        # 果輸入quit表示退出
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), addr)
            sys.exit("退出聊天室")

        msg = 'C %s %s' % (name, text)
        s.sendto(msg.encode(), addr)

# 接收消息


def recv_msg(s):
    while True:
        data, addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode() + '\n發言:', end="")

# 創建套接字登錄，創建子進程


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    # 創建套接字

    s = socket(AF_INET, SOCK_DGRAM)

    while True:
        name = input("請輸入姓名")
        msg = "L " + name
        # 發送登錄請求
        s.sendto(msg.encode(), ADDR)
        # 等待服務器回覆
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("你以進入聊天室")
            break
        else:
            # 不成功服務器會回覆不允許登錄原因
            print(data.decode())

    # 創建父子進程
    pid = os.fork()
    if pid < 0:
        sys.exit("創建子進程失敗")
    elif pid == 0:
        send_msg(s, name, ADDR)
    else:
        recv_msg(s)


if __name__ == "__main__":
    main()
