# daemon屬性
from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("daemon 測試")


t = Thread(target=fun)

t.setDaemon(True)
print(t.isDaemon())

t.start()

print("========================")
