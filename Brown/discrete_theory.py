import copy
import random
from math import *
from random import *
from matplotlib import pyplot as plt

randomfile = open("/dev/random", "rb")
N = 20
A = []
B = []
exp = []
for x in range(0, N+1):
    P = 0
    for i in range(10000):
        X = x
        while X != 0 and X != N:
            if int(randomfile.read(1)[0])%2 == 0:
                X += 1
            else:
                X -= 1
        if X == N:
            P += 1
    P/= 10000
    exp.append(P)
plt.plot(exp)
plt.show()

for x in range(1, N):
    P = 0.5 ** (N - x)
    for i in range(1, x):
        P += 0.5**i*A[i-1]
    A.append(P)
#B = copy.copy(A[::-1])

for k in range(1):

    NA = []
    for x in range(1, N):
        P = 0
        for i in range(1, N):
           P += 0.5 ** (abs(x - i)) * A[i - 1]
        NA.append(P)
    A = NA
    B = copy.copy(A[::-1])
P = []
for i in range(1, N):
    sm = A[i-1] + B[i-1]
    P.append(A[i-1]/sm)
plt.plot(exp)
plt.show()