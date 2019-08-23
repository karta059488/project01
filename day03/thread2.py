from threading import Thread, currentThread
from time import sleep

# 線程函數


def fun(sec):
    print("線程屬性測試")
    sleep(sec)
    # 線程對象的屬性獲取名稱
    print("%s 現成結束" % currentThread().getName())


# 創建線程
thread = []
for i in range(3):
    t = Thread(name="tedu%d" % i, target=fun, args=(2,))
    thread.append(t)
    t.start()


print("is alive:", t.is_alive())  # 查看線程狀態
thread[1].setName("sam")  # 設置線程名稱
print(thread[1].name)

# 回收線程
for i in thread:
    i.join()
