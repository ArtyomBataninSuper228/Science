from math import *
from matplotlib import pyplot as plt
from integral import *
def C(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
T = 4000
t = 100
N = 2000
P =[]
n = []
pred = N*(1-2**(-t/T))
mn = max((0, pred - 3*sqrt(pred)))
mx = pred +  3*sqrt(pred)
k = 1000



for i in range(round(mn), round(mx)+1):
    P.append(C(N, i)*(1-2**(-t/T))**i *2**(-(N-i)*t/T))
    n.append(i)
x = mn
Norm = []
X = []
dx = 10**(-3)
while x<= mx:
    X.append(x)
    Norm.append(normal_disp(x, pred, pred**0.5))
    x+= dx


plt.plot(n, P)
plt.plot(X, Norm)
plt.show()