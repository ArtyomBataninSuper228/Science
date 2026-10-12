from matplotlib import pyplot as plt
from math import *
f =open("data.txt","r")
R = []
U = []
I = []
P = []
DR = []
f.readline()
for line in f:
    r, i, u  = map(float, line.split())
    R.append(r)
    U.append(u)
    I.append(i)
    P.append(u*i)
    DR.append(u/i - r)


plt.plot(DR)
plt.show()