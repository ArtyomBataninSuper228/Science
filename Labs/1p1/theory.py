from math import *
from matplotlib import pyplot as plt
from integral import *
def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
T = 4000
t = 10
N = 2000
P =[]
n = []
pred = N*(1-2**(-t/T))
mn = max((0, pred - 3*sqrt(pred)))
mx = pred +  3*sqrt(pred)
k = 1000
Poi = []



for i in range(round(mn), round(mx)+1):
    P.append(C(N, i)*(1-2**(-t/T))**i *2**(-(N-i)*t/T))
    Poi.append(poison(i, pred))
    n.append(i)
x = mn
Norm = []

X = []
dx = 10**(-3)
while x<= mx:
    X.append(x)
    Norm.append(normal_disp(x, pred, pred**0.5))

    x+= dx


plt.plot(n, P, marker='+', markersize = 8, linestyle='None')
plt.xlabel("n")
plt.ylabel("P")

plt.plot(n, Poi, marker='x', markersize = 8, linestyle='None')
plt.plot(X, Norm)
plt.grid()
plt.legend(["Биноминальное распределение", "Распределение пуассона", "Нормальное распределение"])
plt.savefig("raspr.png", dpi = 600)
#plt.show()