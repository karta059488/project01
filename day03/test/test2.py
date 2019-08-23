from test import *
import threading
import time


def io():
    write()
    read()


counts = []
t = time.time()
for x in range(10):
    th = threading.Thread(target=io)
    counts.append(th)
    th.start()

for i in counts:
    i.join()
print("thread cpu:", time.time() - t)


# thread cpu: 22.5899019241333
# ubuntu@ubuntu-VirtualBox:~/aid1805/python thread/day03/test$ python3 test2.py 
# thread cpu: 11.074638843536377