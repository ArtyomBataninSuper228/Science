import time
import integral
from matplotlib import pyplot as plt
from math import *
import numpy as np
f =open("data.txt","r")
R = []
U = []
I = []
P = []
DR = []
f.readline()
PERR = []
for line in f:
    r, i, u  = map(float, line.split())
    R.append(r)
    U.append(u)
    I.append(i)
    P.append(u*i)
    DR.append(u/i - r)
    perr = u*0.00006 + i*0.01
    PERR.append(perr)

for i in range(len(R)):
    print(f"{R[i]} & \\num{{{U[i]} \pm 0.01}} & \\num{{{round(I[i]*1000, 2)} \\pm 0.06}} & {round(P[i], 3)}   \\\\ \hline")


plt.errorbar(R, I,  0.06/1000, fmt = ".")

plt.xlabel("R")
plt.ylabel("I")
plt.grid(True, which="both", ls="-")
plt.savefig("R_I.png", dpi = 600)
plt.close()

plt.errorbar(R, U, 0.01, fmt = ".")

plt.xlabel("R")
plt.ylabel("U")
plt.grid(True, which="both", ls="-")
plt.savefig("R_U.png", dpi = 600)
plt.close()

plt.errorbar(R, P, PERR, fmt = ".")

plt.xlabel("R")
plt.ylabel("P")
plt.grid(True, which="both", ls="-")
plt.savefig("R_P.png", dpi = 600)
plt.close()

dU = []
dI = []
for i in range(len(R)):
    dU.append(20*0.0003 + 0.04)
    dI.append(0.2*0.0003 + 0.0004)

def Xi_2(r, E):
    Xi_2 = 0
    for i in range(len(R)):
        pred_I = E /(R[i] + r)
        pred_U = R[i]*pred_I
        Xi_2 += ((I[i] - pred_I)**2)/((dI[i]**2))
        Xi_2 += ((U[i] - pred_U) ** 2) / ((dU[i] ** 2))
    return Xi_2

dx = 10**(-6)
def dXi_2(dot):
    x0 = Xi_2(dot[0], dot[1])
    x1 = Xi_2(dot[0] + dx, dot[1])
    x2 = Xi_2(dot[0], dot[1] + dx)
    return np.array([(x1-x0)/dx, (x2-x0)/dx])
def ddXi_2(dot):

    x0 = np.linalg.norm(dXi_2((dot[0], dot[1])))
    x1 = np.linalg.norm(dXi_2((dot[0] + dx, dot[1])))
    x2 = np.linalg.norm(dXi_2((dot[0], dot[1] + dx)))
    return np.array([(x1-x0)/dx, (x2-x0)/dx])

dot = np.array([55.14643962848311, 7.26], dtype=np.float64)
prev = 10000000
delta = 10
vm = []
im = []
mn = 10**100
k = 1
while k < 2**16:
    dv = dXi_2(dot)/ddXi_2(dot)/k
    if( np.linalg.norm(dXi_2(dot + dv)) < mn) :
        dot += dv
        mn = np.linalg.norm(dXi_2(dot))
    else:
        k *= 2
    vm.append(log(np.linalg.norm(dXi_2(dot))))
    im.append(i)


my_Xi_2 = lambda x: Xi_2(dot[0], dot[1])
mdXi_2 = lambda x : integral.div(my_Xi_2, x, dx)
print(dot, mdXi_2(dot), dXi_2(dot), 2/ddXi_2(dot))

#print(integral.get_min_Xi_2(my_Xi_2, np.array([55, 7.2]), 10**-4))







XX = np.arange(7, 9)
YY = np.ones(2, dtype=np.float64)
YY *= Xi_2(dot[0], dot[1])

u = (R[0]-R[1])/(1/I[0] - 1/I[1])
du = sqrt((1/I[0]*0.00006) + 1/I[1])
print(u)

for i in range(len(R)):
    dr = (1/I[i])**2 * u*0.00006
    r = 1/I[i]*u - R[i]
    #print(dr, r)

mXi = []
me = []
e = 7

while e < 8:
    mXi.append(Xi_2(55, e))
    me.append(e)
    e += 0.0001
plt.plot(me, mXi)
plt.plot(XX, YY)
plt.show()
