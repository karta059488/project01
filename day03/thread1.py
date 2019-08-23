import threading
from time import sleep
import os


a = 1
# 線程函數(pid號會一樣—----視同一個進程)


def music():
    global a
    print("a = ", a)
    a = 20000
    for i in range(5):
        sleep(2)
        print("播放：911", os.getpid())


# 創建線程對象
t = threading.Thread(target=music)
t.start()

for i in range(5):
    sleep(1.5)
    print("聽灌籃高手", os.getpid())
t.join()

print("main Thread a =", a)


# a =  1
# 聽灌籃高手 3985
# 播放：911 3985
# 聽灌籃高手 3985
# 播放：911 3985
# 聽灌籃高手 3985
# 聽灌籃高手 3985
# 播放：911 3985
# 聽灌籃高手 3985
# 播放：911 3985
# 播放：911 3985
# main Thread a = 20000   共用進程空間所以會一樣，跟進程不同不是複製過去用同一個全局變量

