import os
import signal

# 向4935方送信號
os.kill(4935, signal.SIGKILL)
