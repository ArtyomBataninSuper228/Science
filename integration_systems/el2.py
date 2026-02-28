from math import *
import numpy as np
import copy

g = 9.8

classic_sys = np.matrix([-10000, 1, 0, 1, 1, 1], dtype=float)#x, y, vx, vy, q1*q2, m
def create_sys(x, y, vx, vy, q1q2, m):
    return np.matrix([x, y, vx, vy, q1q2, m], dtype= float)
def get_diff(sys):
    R2 = (sys[0, 0]**2 + sys[0, 1]**2)
    ax = sys[0, 4]*sys[0, 0]/sys[0, 5]/R2**(2.5)
    ay = sys[0, 4]*sys[0, 1]/sys[0, 5]/R2**(2.5)
    return np.matrix([ax, ay], dtype=float)

def do_step(sys, h, k):
    sys = copy.copy(sys)
    sys[0, 2] += k[0, 0]*h
    sys[0, 3] += k[0, 1] * h
    sys[0, 0] += sys[0, 2]*h
    sys[0, 1] += sys[0, 3] * h
    return sys
def get_R(sys):
    return (sys[0, 0]**2+sys[0, 1]**2)**0.5

