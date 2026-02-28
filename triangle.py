from matplotlib import pyplot as plt
from integral import *
from math import *
from integration_systems import el1
from integration_systems import el2



R0 = 100
V0 = 2**0.5

sys1 = el1.create_sys(z = -R0,  v = V0, q1q2 = 1/100, m = 1)
sys2 = el2.create_sys(-R0, 0, V0, 0, 1/100, 1)

T = 200
dt = 10**(-3)
mR1 = []
mR2 = []
mT = []
t = 0
while t<T:
    sys1 = do_runge_kutta_classic_step(sys1, el1.get_diff, el1.do_step, dt)
    sys2 = do_runge_kutta_classic_step(sys2, el2.get_diff, el2.do_step, dt)
    t += dt
    mR1.append(el1.get_R(sys1))
    mR2.append(el2.get_R(sys2))
    mT.append(t)
plt.plot(mT, mR1)
plt.plot(mT, mR2)
plt.show()
