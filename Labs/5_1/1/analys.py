from matplotlib import pyplot as plt

#Resonance: 39700
#T = 23°
R =[]
U = []
I = []
P = []
R0 = []
f = open("datab.txt")
for line in f:
    r, u  = map(float, line.split())
    R.append(r)
    U.append(u*r)


plt.plot(R, U, label="R")
plt.xlabel("R")
plt.ylabel("U")
plt.ylim( ymin = 0, ymax = 0.005 )

plt.show()

