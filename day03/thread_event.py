import threading
from time import sleep

s = None
e = threading.Event()


def bar():
    print("bar敗山頭")
    global s
    s = "天王概第虎"


def foo():
    print("說出口令就是自己人")
    sleep(3)
    if s == "天王概第虎":
        print("我是坐山雕，自己人")
    else:
        print("打它")
    e.set()   # 等foo驗證完畢其他才執行


def fun():
    print("呵呵:...")
    sleep(1)
    global s
    s = "小雞燉鍋"


b = threading.Thread(target=bar)
f = threading.Thread(target=foo)
b.start()
f.start()
e.wait() # 運行b之後其他內容不準執行

fun()
b.join()
f.join()
