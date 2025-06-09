from matplotlib import pyplot as plt
from math import *
from numpy import *
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

def get_a(sys):
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

def make_step(sys, h, a):
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

mx = []
my = []
mt = []
h = 10**(-5)
sys = array([1, 0, 0, 0, 1])
tm = 0


while tm < 10:
    k1 = get_a(sys)
    k2 = get_a(make_step(sys, h/2, k1))
    k3 = get_a(make_step(sys, h / 2, k2))
    k4 = get_a(make_step(sys, h, k3))
    a = (k1 + k2 * 2 + k3 * 2 + k4) / 6
    sys = make_step(sys, h, k1)
    tm += h
    mx.append(sys[0])
    my.append(sys[1])
    mt.append(tm)
plt.plot(mt, mx)
plt.show()
