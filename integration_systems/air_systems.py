from math import *
import numpy as np
import copy

g = 9.8

classic_sys = np.matrix([0, 1, 0.001, 1], dtype=float)#x, v, k, m
def create_pendulum_sys(x, v, k, m):
    return np.matrix([x, v, k, m], dtype= float)
def get_diff(sys):
    return -sys[0, 2]*sys[0, 1]/sys[0, 3]

def do_step(sys, h, k):
    sys = copy.copy(sys)
    sys[0, 1] += k*h
    sys[0, 0] += sys[0, 1]*h
    return sys
def get_true_ans(sys, v0, t):
    v = v0*e**(-sys[0, 2]/sys[0, 3]*t)
    x = sys[0, 3]*v0/sys[0, 2] - sys[0, 3]*v/sys[0, 2]
    return x, v
