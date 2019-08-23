from multiprocessing import Process
from time import sleep
import os


def th1():
    sleep(3)
    print("吃飯")
    print(os.getppid(), '-----', os.getpid())


def th2():
    sleep(2)
    print("睡覺")
    print(os.getppid(), '-----', os.getpid())


def th3():
    sleep(4)
    print("打遊戲")
    print(os.getppid(), '-----', os.getpid())


things = [th1, th2, th3]
process = []

for th in things:
    p = Process(target=th)
    process.append(p)
    p.start()

# 循環回收進程
for i in process:
    i.join()


# 睡覺
# 4279 ----- 4281
# 吃飯
# 4279 ----- 4280
# 打遊戲
# 4279 ----- 4282
# 工同的父近程
