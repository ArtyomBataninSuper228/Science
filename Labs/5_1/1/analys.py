from matplotlib import pyplot as plt

#Resonance: 39700
#T = 23°
R =[]
U = []
I = []
P = []
R0 = []
R_err = []
U_err = []
f = open("dataa.txt")
for line in f:
    r, u  = map(float, line.split())
    R.append(r)
    U.append(u*r)



#plt.errorbar(R, U, label="R", xerr=0.01/1000, fmt="o")
plt.plot(R, U,color='b')
plt.errorbar(R, U, fmt='o', color='b')
plt.xlabel("Расстояние между источниками, М")
plt.ylabel("$U \cdot R$, ($B \cdot M$)")
#plt.ylabel("U, (B)")
plt.grid()
#plt.ylim( ymin = 0, ymax = 0.005 )
plt.savefig("blr.png")

for i in range(len(U)):
    print(f"{R[i]*1000} & {U[i]} & {round(U[i]*R[i]*1000, 2)} \\\ \\hline")



