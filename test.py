from matplotlib import pyplot
from math import *
import numpy as np
from copy import *
from integration_systems import spring_pendulum
from integration_systems import air_systems
s = spring_pendulum
sys = s.classic_sys
for i in range(1000):
    k1 = s.get_diff(sys)
    sys = s.do_step(sys, 10**(-3), k1)
def test(sys, fd, fs, k, h):
    sys2 = fs(copy(sys), h, k)
    delta =  fd(sys2) - k
    return delta
def seek_solution(sys, fd, fs, h):
    st_sys = copy(sys)
    k1 = fd(sys)
    sys = fs(sys, h, k1)
    k2 = fd(sys)
    delta = k2-k1
    t1 = test(st_sys, fd, fs, k1, h)
    t2 = test(st_sys, fd, fs, k2, h)
    a = t2-t1
    b = t1 - a
    n = -b/a - 1
    return k1 + delta*n



seek_solution(sys, s.get_diff, s.do_step, 10**(-4))