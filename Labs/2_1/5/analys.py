from matplotlib import pyplot as plt

R =[]
U = []
I = []
P = []
R0 = []
f = open("data.txt")
for line in f:
    r, u, i  = map(float, line.split())
    R.append(r)
    U.append(u)
    I.append(i)
    p = u*i
    P.append(p)
    R0.append(u/i)

plt.plot(R, I, label="R")
plt.xlabel("R")
plt.ylabel("I")
plt.show()

plt.plot(R, U, label="U")
plt.xlabel("R")
plt.ylabel("U")
plt.show()

plt.plot(R, P, label="P")
plt.xlabel("R")
plt.ylabel("P")
plt.show()

plt.plot(R, R0, label="R0")
plt.xlabel("R")
plt.ylabel("R0")
plt.show()