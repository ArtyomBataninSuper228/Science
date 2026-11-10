import math
from matplotlib import pyplot as plt
from integral import *
C = 347
fr = 39900
f = open("data.txt")

dr = 0.025/1000
r = 0.145
data = []
f.readline()
X = []
Y = []
N = []
n = 0
V =[]
PHI =[]
for line in f.readlines():
    l, x0, xmax, y0, ymax = map(float, line.split())
    dfx = math.asin(x0/xmax)
    dfy = math.asin(y0/ymax)
    vx = dfx*C**2/(2*math.pi*l*fr)
    vy = dfy*C**2/(2*math.pi*l*fr)
    if vx < 1.01 or vy < 1.01:
        continue
    X.append(dfx)
    Y.append(dfy)
    N.append(n+1)
    V.append(vx)
    V.append(vy)
    PHI.append(dfx)
    PHI.append(dfy)
    print(f" {n+1} & {x0} & {xmax} & {y0} & {ymax}  & {round(dfx, 3)} & {round(dfy, 3)} \\\ \hline")
    n+= 1

print(median(V), dispersion(V)**0.5 /((len(V)-1)**0.5), len(X), dr/r*1000)
dphi = dispersion(PHI)**0.5/(len(PHI)-1)**0.5/median(PHI)
dC = 0.9/348
dR = dr/r
df = 90/39800
dV = 2*dC + dR + df + dphi
dV = median(V)*dV

print(f"dv: {dV}, phi: {median(PHI)}, dphi: {dphi*median(PHI)}")


plt.errorbar(N, X, fmt = 'o',color = "b")
plt.errorbar(N, Y, fmt = 's', color = "r")
plt.legend(['Измерение сдвига по оси x', 'Измерение сдвига по оси y'])
plt.ylim(0, max(max(X), max(Y))*1.2)
plt.grid()
plt.xlabel("Номер измерения")
plt.ylabel("Сдвиг, рад")
plt.savefig("phase_shift.png", dpi = 600)
#plt.show()
