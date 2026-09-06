import time
from matplotlib import pyplot as plt
import math


x = 0
y = 10
v = 1
dt = 10**(-6)
d = (x**2+y**2)**0.5
t = 0
X = []
Y = []
t1 = time.time_ns()
while d > dt:
    d = (x**2+y**2)**0.5
    sina = -x/d
    cosa = -y/d
    vx = -v + 2*v*sina
    vy =  2*v*cosa
    x += vx*dt
    y += vy*dt
    t += dt
    #X.append(t)
    #Y.append(sina)
t2 = time.time_ns()
print(t, 20/3, (t2-t1)/10**9)
