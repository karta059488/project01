import multiprocessing as mp
from time import sleep

a = 1


def fun():
    sleep(3)
    global a
    print("a = ", a)
    a = 10000
    print("子進程事件")


# 創建進程對象
p = mp.Process(target=fun)  # 運行子進程函數

# 啟動進程
p.start()


sleep(2)
print("這是父進程")

# 回收進程
p.join()

print("parent a =", a)
while True:
    pass


# 這是父進程
# a =  1
# 子進程事件
# parent a = 1
