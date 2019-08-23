import signal
from time import sleep

signal.alarm(5)

# 使用默認方法處理信號
# signal.signal(signal.SIGALRM, signal.SIG_DFL)


# 忽律信號
signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.signal(signal.SIGINT, signal.SIG_IGN)


while True:
    sleep(2)
    print("恩 ctrl-c")
    print("等待時鐘...")
