from signal import *
import time


def handler(sig, frame):
    if sig == SIGALRM:
        print("接受到時鐘信號")
    elif sig == SIGINT:
        print("不想結束")


alarm(5)

signal(SIGALRM, handler)
signal(SIGINT, handler)

while True:
    print("Waiting for a signal")
    time.sleep(2)
