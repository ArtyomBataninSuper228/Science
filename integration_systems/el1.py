from math import *
import numpy as np
import copy

g = 9.8

classic_sys = np.matrix([-10000, 1, 1, 1], dtype=float)#z, v, q1*q2, m
def create_sys(z, v, q1q2, m):
    return np.matrix([z, v, q1q2, m], dtype= float)
def get_diff(sys):
    return sys[0,2]/sys[0,3]*(sys[0,0]**(-3))

def do_step(sys, h, k):
    sys = copy.copy(sys)
    sys[0, 1] += k*h
    sys[0, 0] += sys[0, 1]*h
    return sys
def get_R(sys):
    return abs(sys[0, 0])

a = (2 - 3j)
print(a**2)
