from test import *
import time

t = time.time()
# for i in range(10):
#     count(1, 1)

for i in range(10):
    write()
    read()


print("Line cpu:", time.time() - t)


# Line cpu: 21.857405185699463
# Line cpu: 11.287047863006592
