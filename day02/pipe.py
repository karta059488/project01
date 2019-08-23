from multiprocessing import Process, Pipe
import os
import time

# 創建管道對象
fd1, fd2 = Pipe(False)


def fun(name):
    time.sleep(3)
    # 巷管道寫入內容
    fd2.send("hello " + str(name))


jobs = []
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    # 讀取管道
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
