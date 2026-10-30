from matplotlib import pyplot as plt
from math import *
f =open("data.txt","r")
F = []
U1 = []
U2 = []
f.readline()
for line in f:
    fr, u1, u2  = map(float, line.split())
    F.append(fr)#log(fr, 10))
    U1.append(u1)
    U2.append(u2)
plt.plot(F, U1, label = "DT838")
plt.plot(F, U2, label = "GDM")
plt.xscale('log')
plt.xlabel('Частота, Гц')
plt.ylabel('Измеренное напряжение, В')
plt.grid(True, which="both", ls="-")
plt.legend()
#plt.show()
for i in range(len(F)):
    f = round(F[i])
    if f>10000:
        f = f" $ {round(f/(10**(int(log(f, 10)))), 2)} \\cdot 10^{int(log(f, 10))} $"
    print(f"{f} & {U2[i]} & {U1[i]}   \\\\ \hline")


mx1 = max(U1)
mx2 = max(U2)
for i in range(len(U1)):
    if U1[i] <  mx1*0.9:
        print(f"DT838 {F[i]}" )
        break
for i in range(len(U2)):
    if U2[i] <  mx2*0.9:
        print(f"GDM {F[i]}" )
        break