import numpy as np
import time

a=np.ndarray([30,2000],dtype='U50')
# a.fill('\033[31;1;42mS')
a[0:1,:2000]='\033[31;1;42mS'
def printit():
    s=0
    e=169;
    for i in range(30):
        for j in range(s,e):
            print(a[i][j],end='')
        print()
        if e<2000:
            s+=1;
            e+=1

while True:
    printit()
    time.sleep(1/24)
