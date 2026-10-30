import math
from matplotlib import pyplot as plt
C = 347
fr = 39900
f = open("data.txt")
data = []
f.readline()
X = []
for line in f.readlines():
    l, x0, xmax, y0, ymax = map(float, line.split())
    dfx = math.asin(x0/xmax)
    dfy = math.asin(y0/ymax)
    vx = dfx*C**2/(2*math.pi*l*fr)
    vy = dfy*C**2/(2*math.pi*l*fr)
    print( vx, vy)
    X.append(vx)
    X.append(vy)
plt.plot(X, 'o')
plt.show()
