from matplotlib import pyplot as plt
from math import *
f =open("data.txt","r")
F = []
U1 = []
U2 = []
f.readline()
for line in f:
    fr, u1, u2  = map(float, line.split())
    F.append(log(fr, 10))
    U1.append(u1)
    U2.append(u2)
plt.plot(F, U1)
plt.plot(F, U2)
plt.show()