from multiprocessing import Process
from time import sleep, ctime


def tm():
    while True:
        sleep(2)
        print(ctime())


p = Process(target=tm)

p.daemon = True

p.start()
sleep(5)
print("main process exit")


# ubuntu@ubuntu-VirtualBox:~/aid1805/python thread/day02$ python3 daemon.py
# Tue Jul 30 17:21:42 2019
# Tue Jul 30 17:21:44 2019
# main process exit
