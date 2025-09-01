from matplotlib import pyplot
from integral import *
from integral import do_backward_2_step
from integration_systems import air_systems
from integration_systems import pendulum_mono_systems# as pend
from integration_systems import spring_pendulum
from integration_systems import pendulum_systems as pend
s = pend
p0 = copy.copy(s.classic_sys)
p1 = s.classic_sys
p2 = copy.copy(p1)
p3 = copy.copy(p1)
p4 = copy.copy(p1)
p5 = copy.copy(p1)
p6 = copy.copy(p1)
p7 = copy.copy(p1)
p8 = copy.copy(p1)
x = []
y = []
x2 = []
y2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
t = []
time = 0
h = 10**(-4)
toe = 10


while time <= toe:
    p1 = s.do_step(p1, h, s.get_diff(p1))
    p2 = do_runge_kutta_classic_step(p2, s.get_diff, s.do_step, h)
    p3 = do_my4_1_step(p3, s.get_diff, s.do_step, h)
    p4 = do_my4_2_step(p4, s.get_diff, s.do_step, h)
    p5 = do_my4_3_step(p5, s.get_diff, s.do_step, h)
    p6 = do_backward_euler_step(p6, s.get_diff, s.do_step, h)
    p7 = do_new_method_step(p7, s.get_diff, s.do_step, h)
    p8 = do_backward_2_step(p8, s.get_diff, s.do_step, h)
    time += h
    """x.append(p1[0, 0])
    y.append(p1[0, 1])
    x2.append(p2[0, 0])
    y2.append(p2[0, 1])
    """
    true_val = 0#s.get_true_ans(s.classic_sys, 1, time)[0]
    x.append(s.get_errors(p0, p1)[0,0])
    x2.append(s.get_errors(p0, p2)[0,0])
    x3.append(s.get_errors(p0, p3)[0,0])
    x4.append(s.get_errors(p0, p4)[0,0])
    x5.append(s.get_errors(p0, p5)[0,0])
    x6.append(s.get_errors(p0, p6)[0,0])
    x7.append(s.get_errors(p0, p7)[0,0])
    x8.append(s.get_errors(p0, p8)[0,0])
    t.append(time)

xaxis = 'time'
yaxis = 'х'

pyplot.subplot(3, 3, 1)
pyplot.title('Euler', fontsize=17)
pyplot.plot(t, x)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 3, 2)
pyplot.title('RK 4 classic', fontsize=17)
pyplot.plot(t, x2)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 3, 3)
pyplot.title('my 1', fontsize=17)
pyplot.plot(t, x3)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 3, 4)
pyplot.title('my 2', fontsize=17)
pyplot.plot(t, x4)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 3, 5)
pyplot.title('my 3', fontsize=17)
pyplot.plot(t, x5)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')


pyplot.subplot(3, 3, 6)
pyplot.title('backward euler', fontsize=17)
pyplot.plot(t, x6)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')


pyplot.subplot(3, 3, 7)
pyplot.title('new method', fontsize=17)
pyplot.plot(t, x7)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.subplot(3, 3, 8)
pyplot.title('backward 2', fontsize=17)
pyplot.plot(t, x8)
pyplot.xlabel(xaxis, fontsize=12, color='blue')
pyplot.ylabel(yaxis, fontsize=12, color='blue')

pyplot.show()
a = s.get_errors(p0, p1)[0, 1] - 1
b = s.get_errors(p0, p8)[0, 1] - 1
d = a - b
print(a, b, d, a/d, -b/d)
