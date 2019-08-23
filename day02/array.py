from multiprocessing import Process, Array
import time

# 創建共享內存初始放入列表
# shm = Array('i', [1, 2, 3, 4, 5])

# 創建共享內存開闢五個整形空間
# shm = Array('i', 5)

# 存入字符串
# 要求bytes格式
shm = Array('c', b'hello world')


def fun():
    for i in shm:
        print(i)
    shm[0] = b"J"


p = Process(target=fun)
p.start()
p.join()

# for i in shm:
#     print(i)
print(shm.value)  # 打印字符串
