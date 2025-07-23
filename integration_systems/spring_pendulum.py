from math import *
import numpy as np
import copy

g = 9.8

classic_spring_pendulum_sys = np.matrix([1, 0, 1, 1], dtype=float)#x, vx, k, m
def create_pendulum_sys(x, v, k, m):
    return np.matrix([x, v, k, m], dtype= float)
def get_diff(sys):
    return -sys[0, 0]*sys[0, 2]/sys[0, 3]

def do_step(sys, h, k):
    #sys = copy.copy(sys)
    sys[0, 1] += k*h
    sys[0, 0] += sys[0, 1]*h
    return sys
def get_true_ans(sys, x0, t):
    return x0*cos(sys[0, 2]/sys[0, 3]*t)
