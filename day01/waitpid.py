import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    sleep(3)
    print("Child process exit", os.getpid())
    os._exit(2)
else:
    while True:
        sleep(1)
        # 通過非阻塞形式捕獲子進程的退出
        pid, status = os.waitpid(-1, os.WNOHANG)
        print(pid, status)
        print(os.WEXITSTATUS(status))  # 獲取子進程退出狀態
    while True:
        pass
