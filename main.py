from matplotlib import pyplot
from integral import *
from integration_systems import air_systems
from integration_systems import pendulum_systems as pend
from integration_systems import spring_pendulum

p1 = pend.classic_pandulum_sys
p2 = copy.copy(p1)
p3 = copy.copy(p1)
p4 = copy.copy(p1)
p5 = copy.copy(p1)
x = []
y = []
x2 = []
y2 = []
x3 = []
x4 = []
x5 = []
t = []
time = 0
h = 10**(-3)
toe = 100

s = pend
while time <= toe:
    p1 = s.do_step(p1, h, s.get_diff(p1))
    p2 = do_runge_kutta_classic_step(p2, s.get_diff, s.do_step, h)
    p3 = do_rk4_1_step(p3, s.get_diff, s.do_step, h)
    p4 = do_rk4_2_step(p4, s.get_diff, s.do_step, h)
    p5 = do_rk4_3_step(p5, s.get_diff, s.do_step, h)
    time += h
    """x.append(p1[0, 0])
    y.append(p1[0, 1])
    x2.append(p2[0, 0])
    y2.append(p2[0, 1])
    """
    true_val = 0#s.get_true_ans(s.classic_spring_pendulum_sys, 1, time)
    x.append(p1[0, 0] - true_val)
    x2.append(p2[0, 0] - true_val)
    x3.append( p3[0, 0] - true_val)
    x4.append(p4[0, 0] - true_val)
    x5.append(p5[0, 0] - true_val)
    t.append(time)

xaxis = 'time'
yaxis = 'x'

pyplot.subplot(3, 2, 1)
pyplot.title('Euler', fontsize=17)
pyplot.plot(t, x)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 2, 2)
pyplot.title('RK 4 classic', fontsize=17)
pyplot.plot(t, x2)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 2, 3)
pyplot.title('my 1', fontsize=17)
pyplot.plot(t, x3)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 2, 4)
pyplot.title('my 2', fontsize=17)
pyplot.plot(t, x4)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 2, 5)
pyplot.title('my 3', fontsize=17)
pyplot.plot(t, x5)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.show()
