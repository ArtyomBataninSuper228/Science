from matplotlib import pyplot as plt

R =[]
U = []
I = []
P = []
R0 = []
f = open("datab.txt")
for line in f:
    r, u  = map(float, line.split())
    R.append(r)
    U.append(u)


plt.plot(R, U, label="R")
plt.xlabel("R")
plt.ylabel("U")
plt.show()

