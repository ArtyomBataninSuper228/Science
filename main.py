from matplotlib import pyplot
from integral import *
from integration_systems import air_systems
from integration_systems import pendulum_systems as pend

p1 = pend.create_pendulum_sys(0.1, 1, 0,0, 1)
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
h = 10**(-3)
toe = 10
get_diff = pend.get_diff
do_step = pend.do_step
while time <= toe:
    p1 = do_step(p1, h, get_diff(p1))
    p2 = do_runge_kutta_classic_step(p2, get_diff, do_step, h)
    p3 = do_rk4_1_step(p3, get_diff, do_step, h)
    p4 = do_rk4_2_step(p4, get_diff, do_step, h)
    time += h
    """x.append(p1[0, 0])
    y.append(p1[0, 1])
    x2.append(p2[0, 0])
    y2.append(p2[0, 1])
    """
    #true_val = air_systems.get_true_ans(p1, 1, time) [0]
    x.append(p1[0, 0])
    x2.append(p2[0, 0])
    x3.append( p3[0, 0])
    x4.append(p4[0, 0])
    t.append(time)

xaxis = 'time'
yaxis = 'x'

pyplot.subplot(2, 2, 1)
pyplot.title('Euler', fontsize=17)
pyplot.plot(t, x)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(2, 2, 2)
pyplot.title('RK 4 classic', fontsize=17)
pyplot.plot(t, x2)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(2, 2, 3)
pyplot.title('my 1', fontsize=17)
pyplot.plot(t, x3)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(2, 2, 4)
pyplot.title('my 2', fontsize=17)
pyplot.plot(t, x4)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.show()
