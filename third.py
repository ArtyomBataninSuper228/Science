from integral import *
from integration_systems.third import *
from matplotlib import pyplot as plt
sys = classic_sys
sys[0, 3] = 1
sys[0, 2] = 1
t = 0
xm = []
tm = []
toe = 100
h = 10**(-2)
while t < toe:
    sys = do_step(sys, h, get_diff(sys))
    xm.append(sys[0, 0])
    tm.append(t)
    t += h
plt.plot(tm, xm)
plt.show()