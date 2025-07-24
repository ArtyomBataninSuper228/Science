from matplotlib import pyplot
from math import *
import numpy as np
from copy import *
from integration_systems import spring_pendulum
from integration_systems import air_systems
from integration_systems import pendulum_systems
#from integral import *
s = spring_pendulum
sys = s.classic_sys
for i in range(1000):
    k1 = s.get_diff(sys)
    sys = s.do_step(sys, 10**(-3), k1)
a = np.matrix([[5, 1], [0, 3]])



def get_length(vector):
    if type(vector) != np.matrix:
        return vector
    elif vector.shape[0] == 1:
        sm = 0
        for i in range(vector.shape[1]):
            sm += get_length(vector[0, i])**2
        return sm**0.5

    else:
        sm = 0
        for i in range(len(vector)):
            sm += get_length(vector[i])**2
        return sm**0.5
def test(sys, fd, fs, k, h):
    sys2 = fs(copy(sys), h, k)
    delta =  fd(sys2) - k
    return get_length(delta)
def seek_solution(sys, fd, fs, h):
    st_sys = copy(sys)
    k1 = fd(sys)
    sys = fs(sys, h, k1)
    k2 = fd(sys)
    delta = k2-k1
    #t1 = test(st_sys, fd, fs, k1, h)
    #t2 = test(st_sys, fd, fs, k2, h)
    #a = t2-t1
    #b = t1 - a
    #n = -b/a - 1
    num = 5
    '''
    ks = []
    errors = []
    for i in range(num*2):
        errors.append(float(test(st_sys, fd, fs, k1 + delta/num*i, h)))
        ks.append(i)
    pyplot.plot(ks, errors)
    pyplot.show()
    '''
    t1 = test(st_sys, fd, fs, k1, h)
    t2 = test(st_sys, fd, fs, k1 + delta/num, h)
    a = t2 - t1
    b = t1 - a
    n = -b/a - 1
    #print(test(st_sys, fd, fs, k1 + delta*n/num, h), n)
    return k1 + delta*n/num

seek_solution(sys, s.get_diff, s.do_step, 10**(-1))

