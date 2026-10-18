from math import *
from numpy import *
import matplotlib.pyplot as plt


R =-1
w =2*pi
g = 9.8
alpha = arctan(g/w**2*R)
l = 0
dl = 0.001
F = array([g, w**2*R ])
new_F = array([0, 0])
print(F)
ALPHA = []
L = []

while l < 2.178*10:
    ALPHA.append(alpha / pi * 180)
    R -= dl*sin(alpha)
    new_F[0] = g
    new_F[1] = w**2*R
    F += new_F
    alpha = arctan(F[1]/F[0])
    l += dl

    L.append(l)
plt.plot(L, ALPHA)
plt.show()