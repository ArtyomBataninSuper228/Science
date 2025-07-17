import numpy as np
from math import *
from matplotlib import pyplot
from pendulum_systems import *
from integral import *
import air_systems

p1 = air_systems.create_pendulum_sys(0, 1, 1, 1)#create_pendulum_sys(1, -1, 0,0, 1)
p2 = copy.copy(p1)
p3 = copy.copy(p1)
p4 = copy.copy(p1)
x = []
y = []
x2 = []
y2 = []
x3 = []
x4 = []
t = []
time = 0
h = 10**(-5)
toe = 100
while time <= toe:
    p1 = air_systems.do_step(p1, h, air_systems.get_diff(p1))
    p2 = do_runge_kutta_classic_step(p2, air_systems.get_diff, air_systems.do_step, h)
    p3 = do_rk4_1_step(p3, air_systems.get_diff, air_systems.do_step, h)
    p4 = do_rk4_2_step(p4, air_systems.get_diff, air_systems.do_step, h)
    time += h
    """x.append(p1[0, 0])
    y.append(p1[0, 1])
    x2.append(p2[0, 0])
    y2.append(p2[0, 1])
    """
    x.append(air_systems.get_true_ans(p1, 1, time)[0] - p1[0, 0])
    x2.append(air_systems.get_true_ans(p1, 1, time)[0] - p2[0, 0])
    x3.append(air_systems.get_true_ans(p1, 1, time)[0] - p3[0, 0])
    x4.append(air_systems.get_true_ans(p1, 1, time)[0] - p4[0, 0])
    t.append(time)


pyplot.subplot(2, 2, 1)
pyplot.title('Euler', fontsize=17)
pyplot.plot(t, x, label = 'euler')
pyplot.xlabel('time', fontsize=12, color='blue')
pyplot.ylabel('Error', fontsize=12, color='blue')

pyplot.subplot(2, 2, 2)
pyplot.title('RK 4 classic', fontsize=17)
pyplot.plot(t, x2, label = 'euler')
pyplot.xlabel('time', fontsize=12, color='blue')
pyplot.ylabel('Error', fontsize=12, color='blue')

pyplot.subplot(2, 2, 3)
pyplot.title('my 1', fontsize=17)
pyplot.plot(t, x3, label = 'euler')
pyplot.xlabel('time', fontsize=12, color='blue')
pyplot.ylabel('Error', fontsize=12, color='blue')

pyplot.subplot(2, 2, 4)
pyplot.title('my 2', fontsize=17)
pyplot.plot(t, x4, label = 'euler')
pyplot.xlabel('time', fontsize=12, color='blue')
pyplot.ylabel('Error', fontsize=12, color='blue')

pyplot.show()
