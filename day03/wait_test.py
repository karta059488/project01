from multiprocessing import Event

# 創建事件對象
e = Event()

e.set()  # 設置事件

print(e.is_set())

e.wait(3)

e.clear()
e.wait()