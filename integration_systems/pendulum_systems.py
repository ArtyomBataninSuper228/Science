from math import *
import numpy as np
import copy

g = 9.8

classic_pandulum_sys = np.matrix([1, 1, 0, 0, 1], dtype=float)#x y x' y' m
def create_pendulum_sys(x, y, vx, vy, mass):
    return np.matrix([x, y, vx, vy, mass], dtype= float)
def get_diff(sys):
    #print(sys[0][0])
    l = (sys[0, 0]**2 + sys[0,1]**2)**0.5
    v2 = (sys[0,2] ** 2 + sys[0,3] ** 2)
    sina = sys[0,0]/l
    cosa = -sys[0,1]/l
    ax = -sina*(v2/l + g*cosa)
    ay =  - g + cosa*(v2/l + g*cosa)
    return np.matrix([[sys[0,2], ax], [sys[0,3], ay]])

def do_step(sys, h, k):
    sys = copy.copy(sys)
    sys[0, 2] += k[0, 1]*h
    sys[0, 3] += k[1, 1]*h
    sys[0, 0] += sys[0, 2]*h
    sys[0, 1] += sys[0, 3] * h
    return sys