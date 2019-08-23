from multiprocessing import Process
import time


class ClockProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()   # 調用父類init方法

        # 重寫run方法(把它變成進程方法)
    def run(self):
        for i in range(5):
            print("The time is {}".
                  format(time.ctime()))
            time.sleep(self.value)


# 創建字定義進程類的對象
p = ClockProcess(2)

# 自動調用run
p.start()
p.join()


# ubuntu@ubuntu-VirtualBox:~/aid1805/python thread/day02$ python3 pool.py 
# hello 0
# hello 1
# hello 3
# hello 2
# hello 4
# hello 5
# hello 6
# hello 7
# hello 8
# hello 9
# Tue Jul 30 17:10:15 2019
# Tue Jul 30 17:10:15 2019
# Tue Jul 30 17:10:15 2019
# Tue Jul 30 17:10:15 2019
# Tue Jul 30 17:10:17 2019
# Tue Jul 30 17:10:17 2019
# Tue Jul 30 17:10:17 2019
# Tue Jul 30 17:10:17 2019
# Tue Jul 30 17:10:19 2019
# Tue Jul 30 17:10:19 2019
