from multiprocessing import Queue
from time import sleep

# 創建隊列
q = Queue(3)

q.put(1)
sleep(0.5)
print(q.empty())
q.put(2)
print(q.full())
q.put(3)
print(q.qsize())
# q.put(4, True, 3)

print(q.get())
print(q.qsize())
q.close()  # 關閉隊列


# ubuntu@ubuntu-VirtualBox:~/aid1805/python thread/day02$ python3 queue1.py
# False
# False
# 3
# 1
# 2
