from multiprocessing import Process, Event
from time import sleep


def wait_event():
    print("想操作臨界區")
    e.wait()
    print("開始操作臨界區資源", e.is_set())
    with open("file") as f:
        print(f.read())


def wait_event_timeout():
    print("我也想操作臨界區")
    e.wait(2)
    if e.is_set():
        with open("file") as f:
            print(f.read())
    else:
        print("不能讀取文件")


# 事件對象     人為控制進程先後順序
e = Event()
p1 = Process(target=wait_event)
p1.start()
p2 = Process(target=wait_event_timeout)
p2.start()


print("主進程操作")
with open("file", 'w') as f:
    sleep(3)
    f.write("I Love You")
e.set()
print("釋放臨界區")

p1.join()
p2.join()


# ubuntu@ubuntu-VirtualBox:~/aid1805/python thread/day03$ python3 process_event.py
# 主進程操作
# 釋放臨界區
# 想操作臨界區
# 開始操作臨界區資源 True
# I Love You
