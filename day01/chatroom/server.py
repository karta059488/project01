#!/usr/bin/env python3
# coding=utf-8

'''
name:  Sam
email: karta@tedu.cn
date:  2019-07-29
class: AID1805
introduce: Chatroom server
env:   python3.5
'''
# 第一部創建網路連接
from socket import *
import os
import sys

# 登錄判斷


def do_login(s, user, name, addr):
    if (name in user) or name == "管理員":
        s.sendto("該用戶以存在".encode(), addr)
        return
    s.sendto(b'OK', addr)

    # 通知其他人
    msg = "\n歡迎 %s 進入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])  # 通知便利在字典李的所有人
    # 插入用戶
    user[name] = addr


def do_chat(s, user, name, text):
    msg = "\n%s 說： %s" % (name, text)
    for i in user:
        if i != name:  # 要跳過自己，不是發給自己要發給其他人
            s.sendto(msg.encode(), user[i])

# 退出聊天室


def do_quit(s, user, name):
    msg = '\n'+name + "退出了聊天室"
    for i in user:
        if i == name:
            s.sendto(b'EXIT', user[i])
        else:
            s.sendto(msg.encode(), user[i])

    del user[name]


# 接收客戶端請求
def do_parent(s):
    # 儲存結構 {'zhangsan':('127.0.0.1',9999)}
    user = {}

    while True:
        msg, addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')

    # 區分請求類型
        if msgList[0] == "L":  # 　判斷前面是L代表你要開始傳送訊息聊天開始
            do_login(s, user, msgList[1], addr)
        elif msgList[0] == 'C':
            do_chat(s, user, msgList[1], ' '.join(msgList[2:]))
        elif msgList[0] == 'Q':
            do_quit(s, user, msgList[1])


# 做管理員喊話
def do_child(s, addr):
    while True:
        msg = input("管理元消息:")
        msg = 'C 管理員 ' + msg
        s.sendto(msg.encode(), addr)


# 創建網路創建進程調用功能函數
def main():
    # server address
    ADDR = ('0.0.0.0', 8888)

    # 創建套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    # 創建一個單獨的進程處理管理員喊話功能
    pid = os.fork()
    if pid < 0:
        sys.exit("創建程失敗")
    elif pid == 0:
        do_child(s, ADDR)
    else:
        do_parent(s)


if __name__ == "__main__":
    main()
