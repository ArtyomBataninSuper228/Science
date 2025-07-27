import copy

from matplotlib import pyplot
from integration_systems import pendulum_systems as pend
from integration_systems import pendulum_mono_systems# as pend
from integration_systems import spring_pendulum
from integral import *

def Gamma(z):
    def f(t):
        return t**(z-1) * e**(-t)
    mx = 500
    dt = 1/100
    return integral(0, mx, dt, f)

def my_derivate(x, f, h):
    return abs(f(x+h)/f(x))**(1/h)
def f(x):
    return sin(x)+1.1
def f2(x):
    return cos(x)+1.1

def error_correction(m, dif, step, h):
    m2 = []
    m2.append(m[0])
    for i in range(0, len(m)-2):
        k = (dif(m[i+2]) + dif(m[i+1]) + 4*dif(m[i]))/6
        m2.append(step(copy.copy(m[i]), h, k))
    m2.append(step(copy.copy(m2[-1]), h, dif(m2[-1])))
    return m2



s = pend
sys = copy.copy(s.classic_sys)
tm = 0
h = 10**(-4)
end = 10

true_t = []
true_x = []
while tm < end:
    sys = s.do_step(copy.copy(sys), h, s.get_diff(sys))
    true_t.append(tm)
    true_x.append(sys[0,0])
    tm += h

sys = copy.copy(s.classic_sys)
tm = 0
h = 10**(-2.5)
end = 10
mt = []
ms = []
while tm < end:
    sys = s.do_step(copy.copy(sys), h, s.get_diff(sys))

    ms.append(sys)
    mt.append(tm)
    tm += h
ms2 = copy.deepcopy(ms)
print(-1)
iter = 0
while 1:
    for i in range(20):
        ms2 = error_correction(ms2, s.get_diff, s.do_step, h)
        print(i + iter)
    mx2 = []
    mx1 = []
    for i in range(len(ms)):
        mx1.append(ms[i][0, 0])
        mx2.append(ms2[i][0, 0])
    iter += 20
    pyplot.plot(mt, mx1, mt, mx2, true_t, true_x)
    pyplot.savefig(f"images/{iter} iter.png")
    pyplot.close()




