from multiprocessing import Process
import os
from signal import *
from time import sleep

'''司機和售票員的故事
   * 創建父子進程分別代表司機和售票員
   * 當售票員收到SIGINT信號，給司機發送SIGUSR1信號此時司機打印"老司機開車了"
     當售票員收到SIGQUIT信號，給司機發送SIGUSR2信號此時司機打印"車速有點快，係好安全帶"
     當司機捕捉到SIGTSTP信號，給售票員發送SIGUSR1，售票員打印"到站了，請下車"
   * 到站後售票員先下車，司機下車（子進程先退出）'''


def saler_handler(sig, frame):
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(), SIGUSR2)
    elif sig == SIGUSR1:
        print("到站了，請下車")
        os._exit(0)


def driver_handler(sig, frame):
    if sig == SIGUSR1:
        print("老司機開車了")
    elif sig == SIGUSR2:
        print("車速有點快，係好安全帶")
    elif sig == SIGTSTP:
        os.kill(p.pid, SIGUSR1)


#　子進程代表售票員
def saler():
    signal(SIGINT, saler_handler)
    signal(SIGQUIT, saler_handler)
    signal(SIGUSR1, saler_handler)
    signal(SIGTSTP, SIG_IGN)
    while True:
        sleep(2)
        print("python代你上車去遠方")


p = Process(target=saler)
p.start()

# 父近程
signal(SIGUSR1, driver_handler)
signal(SIGUSR2, driver_handler)
signal(SIGTSTP, driver_handler)
signal(SIGINT, SIG_IGN)
signal(SIGQUIT, SIG_IGN)

p.join()
