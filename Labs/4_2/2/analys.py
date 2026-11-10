from matplotlib import pyplot as plt

data = []
f = open('resistance', 'r')
f.readline()

L = []
R = []
for line in f.readlines():
    l, n, r = map(float, line.split())
    r *= n
    L.append(l)
    R.append(r)

L1 = []
R1 = []
l = 0
dl = 0.01
while l <= max(L) + dl:
    L1.append(l)
    R1.append((max(R))/(max(L))*l)
    l += dl

plt.plot(L, R, color = "orange")
plt.errorbar(L, R, 10**(-6), fmt = "o", color = "r")
plt.plot(L1, R1, color = "g")
plt.grid()
plt.show()
