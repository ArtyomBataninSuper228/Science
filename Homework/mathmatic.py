from math import *
from matplotlib import pyplot as plt


def f(x):
    return  ((5*x)**0.5+1)*log((1+atan(1/(x**0.5))), e)
x = []
y = []
for i in range(1, 10):
    x.append(i)
    X = 10**(i)
    y.append(f(X))
print(7/(192*30*log(3, e)), 30*log(3, e), 9/192, 1/24-1)
plt.plot(x, y)
plt.show()
