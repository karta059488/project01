from test import *
import multiprocessing
import time


# def io():
#     write()
#     read()


counts = []
t = time.time()
for x in range(10):
    p = multiprocessing.Process(target=count, args=(1, 1))
    counts.append(p)
    p.start()

for i in counts:
    i.join()
print("Process cpu:", time.time() - t)


# thread cpu: 22.5899019241333
# ubuntu@ubuntu-VirtualBox:~/aid1805/python thread/day03/test$ python3 test2.py
# thread cpu: 11.074638843536377
