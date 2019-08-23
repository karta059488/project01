from multiprocessing import Process, Lock
import sys
from time import sleep


def write1():
    lock.acquire()
    for i in range(15):
        sys.stdout.write("write1想先向終端寫入\n")
    lock.release()


def write2():
    lock.acquire()
    for i in range(20):
        sys.stdout.write("write2想先向終端寫入\n")
    lock.release()


lock = Lock()

w1 = Process(target=write1)
w2 = Process(target=write2)

w1.start()
w2.start()
w1.join()
w2.join()
