import os
from multiprocessing import Process

filename = "./3.png"
# 獲取文件大小
size = os.path.getsize(filename)  # 返回文件大小，如果文件不存在就返回错误

# 如果子進程使用父近程的對象，那互相有偏移輛的影響
# f = open(filename, 'rb')


# 複製前半部份


def copy1():
    f = open(filename, 'rb')
    n = size // 2
    fw = open('file1.png', 'wb')

    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
            data = f.read(1024)
            fw.write(data)
            n -= 1024
    f.close()
    fw.close()


# 複製下半部份

def copy2():
    f = open(filename, 'rb')
    fw = open('file2.png', 'wb')

    f.seek(size // 2, 0)
# 改变数据流的位置，返回新的绝对位置
# 可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；
# 0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()


p1 = Process(target=copy1)
p2 = Process(target=copy2)
p1.start()
p2.start()
p1.join()
p2.join()
