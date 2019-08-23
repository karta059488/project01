from multiprocessing import Pool
import time


def fun(n):
    time.sleep(1)
    print("執行pool map事件")
    return n * n


pool = Pool(4)
# 使用map將事件放入進程池
r = pool.map(fun, range(10))
pool.close()
pool.join()
print(r)


# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# 執行pool map事件
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
