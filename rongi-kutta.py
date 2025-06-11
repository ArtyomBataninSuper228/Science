from matplotlib import pyplot as plt
from math import *
from numpy import *
import pygame as pg
"""
x = 0
v0 = 1
v = v0
k = 0.1
a = 0
T = 0
h = 10**(-5)
mT = []
mv = []
mx = []
mf = []
while T<100:
    k1 = -k*v
    k2 =-k*(v+k1/2*h)
    k3 =-k*(v+k2/2*h)
    k4 = -k*(v+k3*h)
    a = (k1 +k2*2+k3*2+k4)/6
    v += a*h
    x += v*h
    T += h
    mT.append(T)
    mv.append(v)
    mx.append(x)
    mf.append(abs(v0*e**(-k*T) - v))
plt.plot( mT, mf)
plt.show()
print(max(mf))
"""





g = 9.8

def pendulum_get_a(sys):
    x = sys[0]
    y = sys[1]
    vx = sys[2]
    vy = sys[3]
    m = sys[4]
    l = (x**2+y**2)**0.5
    v = (vx**2+vy**2)**0.5
    ax = -(m*v**2/l - m*g*y/l)*x/l
    ay = -m*g - (m*v**2/l - m*g*y/l)*y/l

    return array([ax, ay])

def pendulum_do_step(sys, h, a):
    x = sys[0]
    y = sys[1]
    vx = sys[2]
    vy = sys[3]
    m = sys[4]
    vx += a[0]*h/m
    vy += a[1]*h/m
    x += vx*h
    y += vy*h
    sys = array([x, y, vx, vy, sys[0]])
    return sys

def do_runge_kutta_step(sys, f1, f2, h):
    k1 = f1(sys)
    k2 = f1(f2(sys, h / 2, k1))
    k3 = f1(f2(sys, h / 2, k2))
    k4 = f1(f2(sys, h, k3))
    a = (k1 + k2 * 2 + k3 * 2 + k4) / 6
    sys = f2(sys, h, a)
    return sys
double_pendulum_sys = array([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]) # x1, y1, x2, y2, vx1, vy1, vx2, vy2, ax1, ay1, m1, m2
def double_pendulum_get_a(sys):
    l1 = (sys[0] ** 2 + sys[1] ** 2) ** 0.5
    l2 = (sys[2] ** 2 + sys[3] ** 2) ** 0.5
    sina = sys[0]/l1
    cosa = sys[1]/l1
    sinb = sys[2]/l2
    cosb = sys[3]/l2

    Fravn = (sys[8] ** 2 + (sys[9] + g) ** 2) ** 0.5
    if Fravn != 0:
        siny = sys[8]/Fravn
        cosy = (sys[9]+g)/Fravn
    else:
        cosy = 0
        siny = 0
    T2 = sys[11] * (sys[6]** 2 + sys[7] ** 2) / l2 + sys[11] * Fravn * (cosb * cosy + siny * sinb)
    T1 = sys[10] * (sys[4] ** 2 + sys[5] ** 2) / l1 - sys[10] * g * cosa + T2 * (cosa * cosb + sina * sinb) #t2

    p2ax = -T2 * sinb / sys[11] + sys[8]
    p2ay = -T2 * cosb / sys[11] + sys[9] - g

    p1ax = -T1 * sina / sys[10] + T2 * sinb / sys[10]#t2
    p1ay = -T1 * cosa / sys[10] - g + T2 * cosb / sys[10] #t2

    return array([p1ax, p1ay, p2ax, p2ay])

def double_pendulum_do_step(sys, h, a):
    sys[8] = a[0]
    sys[9] = a[1]
    sys[4] += a[0] * h
    sys[5] += a[1] * h
    sys[6] += a[2] * h
    sys[7] += a[3] * h
    sys[0] += sys[4] * h
    sys[1] += sys[5] * h
    sys[2] += sys[6] * h
    sys[3] += sys[7] * h
    return sys






mx = []
my = []
mt = []
h = 10**(-5)
sys = array([1, 0, 0, 0, 1]) # Система: математический маятник x, y, vx, vy, m
tm = 0



while tm < 1:
    double_pendulum_sys = do_runge_kutta_step(double_pendulum_sys, double_pendulum_get_a, double_pendulum_do_step, h)
    tm += h
    mx.append(sys[0])
    my.append(sys[1])
    mt.append(tm)
plt.plot(mt, mx)
plt.show()
