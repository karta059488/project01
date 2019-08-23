from multiprocessing import Process, Value
import time
import random

# 創建共享內存

money = Value('i', 20)


# 操作共享內存增加
def deposite():
    for i in range(100):
        time.sleep(0.05)
        # 對value屬性操作集操作共享內存
        money.value += random.randint(1, 200)


# 取錢
def withdrasw():
    for i in range(100):
        time.sleep(0.04)
        money.value -= random.randint(1, 180)


d = Process(target=deposite)
w = Process(target=withdrasw)
d.start()
w.start()
d.join()
w.join()

print("餘額：", money.value)
