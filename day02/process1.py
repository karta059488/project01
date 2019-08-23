from multiprocessing import Process
from time import sleep

# 代參數的進程函數


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")


p = Process(target=worker, args=(2,),
            kwargs={'name': 'Daivl'}, name="Worker")
p.start()

print("Process name:", p.name)  # 打印進程名稱
print("Process PID:", p.pid)   # 獲取相應的pid號
print("Process is alive:", p.is_alive())   # True

p.join(3)   # 超時屬性3
print("=====================")
