import gevent
from time import sleep


def foo(a, b):
    print("a = %d,b = %d" % (a, b))
    gevent.sleep(2)
    print("Running foo again")


def bar():
    print("Running int bar")
    gevent.sleep(3)
    print("Running bar again")


# 生成斜成
f = gevent.spawn(foo, 1, 2)
g = gevent.spawn(bar)
print("====================")
gevent.joinall([f, g])
print("zzzzzzzzzzzzzzzzzzzzzz")


# ====================
# a = 1,b = 2
# Running int bar
# Running foo again
# Running bar again
# zzzzzzzzzzzzzzzzzzzzzz
