# 創建二級子進程避免殭屍

import os
from time import sleep


def f1():
    sleep(3)
    print("做第一件事")


def f2():
    sleep(4)
    print("做第二件事")


pid = os.fork()

if pid < 0:
    print("error")
elif pid == 0:
    # 創建二己子進程
    p = os.fork()
    if p == 0:
        f2()  # 做第二件事
    else:
        os._exit(0)

else:
    os.wait()  # 第一級子進程退出
    f1()  # 做第一件事
