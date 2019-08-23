from multiprocessing import Semaphore, Process
from time import sleep
import os

# 創建信號量
sem = Semaphore(3)


def fun():
    print("進程%d等待信號量" % os.getpid())
    # 消耗一個信號量
    sem.acquire()
    print("進程%d消耗信號量" % os.getpid())
    sleep(3)
    sem.release()
    print("進程%d添加進程量" % os.getpid())


jobs = []
for i in range(4):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print(sem.get_value())
