from matplotlib import pyplot
from math import *


m1 = []
def is_isi(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            #print(i)
            return False
    return True
for i in range(1, 100000):
    if is_isi(i) == True:
        m1.append(i)
m2 = []
m3 = []
n = 1
print(is_isi(2311))
for i in m1:
    n *= i
    m2.append((log(n, e))/1)
    m3.append(i)
#print(m2[m1.index(1997)])
pyplot.plot(m1, m2, m1, m3)
pyplot.show()