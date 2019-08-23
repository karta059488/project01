from multiprocessing import Pool
from time import sleep, ctime


def worker(msg):
    sleep(2)
    print(msg)
    return ctime()


# 創建進程池
pool = Pool(processes=4)

result = []
for i in range(10):
    msg = "hello %d" % i
    # 將事件放入進程池對列等待執行
    r = pool.apply_async(func=worker, args=(msg,))  # r只是返回對象
    result.append(r)

# 關閉進程池
pool.close()

# 回收
pool.join()

for i in result:
    print(i.get())   # 獲取事件函數的返回質
    