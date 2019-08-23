from threading import Thread
from time import ctime, sleep


class MyThread(Thread):
    def __init__(self, target, name="tedu",
                 args=(), kwargs={}):

        super().__init__()   # 調用父類init方法
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


def player(song, sec):
    for i in range(2):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=('Google',), kwargs={'sec': 1})
t.start()
t.join()
