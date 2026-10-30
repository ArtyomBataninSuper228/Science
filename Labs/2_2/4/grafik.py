from matplotlib import pyplot as plt
from math import *
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

'''
plt.errorbar(R, I,  0.06/1000, fmt = ".")

plt.xlabel("R")
plt.ylabel("I")
plt.savefig("R_I.png", dpi = 600)
plt.close()

plt.errorbar(R, U, 0.01, fmt = ".")

plt.xlabel("R")
plt.ylabel("U")
plt.savefig("R_U.png", dpi = 600)
plt.close()

plt.errorbar(R, P, PERR, fmt = ".")

plt.xlabel("R")
plt.ylabel("P")
plt.savefig("R_P.png", dpi = 600)
plt.close()
'''
U = (R[0]-R[1])/(1/I[0] - 1/I[1])
du = sqrt((1/I[0]*0.00006) + 1/I[1])
print(U)
for i in range(len(R)):
    dr = (1/I[i])**2 * U*0.00006

    r = 1/I[i]*U - R[i]
    print(dr, r)