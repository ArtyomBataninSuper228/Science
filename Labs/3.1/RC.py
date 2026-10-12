from Labs.methods import *

f = open("data.txt")
x = []
y = []
for line in f:
    a, b = map(float, line.split())
    x.append(a)
    y.append(b)
plt.plot(x, y)
plt.show()