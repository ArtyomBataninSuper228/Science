from Labs.methods import *

f = open("data_stas+.txt")
x = []
y = []
for line in f:
    a, b = map(float, line.split())
    x.append(a)
    y.append(b)
u0 = max(y)
for i in range(len(y)):
    y[i] = log(y[i]/ u0, e)
plt.plot(x, y)
plt.ylabel("ln(U/U0)")
plt.xlabel("Время (Мин)")
plt.show()