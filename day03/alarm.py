import signal
import time

signal.alarm(3)
time.sleep(4)
signal.alarm(5)

signal.pause()  # 阻塞等待信號

while True:
    time.sleep(1)
    print("等待時鐘信號...")
