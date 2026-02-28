from integral import *
import numpy as np

dx = 0.0001# 100 на 100 мкм обьект
dz = 0.000005# 10 мкм - глубина слоя
ds = dx**2
dv = ds*dz # обьём рассматриваемого слоя
Tk = 273.15
T0 = 273.15 + 20 #начальная температура слоя
ro = 7800 # плотность стали
dm =ro*dv
c = 500# теплоёмкость
k = 50# теплопроводность материала
P = 5*0.3# пять ватт мощность лазера плюс коэффициент поглощения
r = 10**(-4)#  радиус пятна фокусировки
S = pi*r**2 # площадь пятна
dt = 10**(-6)
#410.42522934
#410.44011601
L = 0.002
N = int(L/dz)
layers = []
for i in range(N):
    layers.append(T0)
layers = np.matrix(layers, dtype = np.float64)


def get_diff(matrix):
    res = copy.copy(matrix)
    p = ds/S*P# мощность лазера, приходящего на 1 слой
    Q = k*ds*(matrix[0, 0] - matrix[0, 1])/dz
    res[0, 0] = (p-Q)/(c*(dv*ro))
    for i in range(1, N-1):
        Q1 = k * ds * (matrix[0, i-1] - matrix[0, i]) / dz
        Q2 = k * ds * (matrix[0, i] - matrix[0, i+1]) / dz
        res[0, i] = (Q1-Q2)/(c*(dv*ro))
    res[0, N-1] = 0
    return res
def do_step(sys, h, diff):
    sys += diff*h
    return sys

mT1 = []
mT2 = []
mT3 = []
mt = []
t = 0
while t < 1/100:
    layers = do_backward_euler_step(layers, get_diff, do_step, dt )
    t += dt
    mT1.append(layers[0, 0]- Tk)
    mT2.append(layers[0, 1] - Tk)
    mT3.append(layers[0, 2] - Tk)
    mt.append(t)
print(layers)
plt.plot(mt, mT1, mt, mT2, mt,  mT3)
plt.show()
gradient = []
for i in range(N):
    gradient.append(layers[0, i]- Tk)
plt.plot(gradient)
plt.show()