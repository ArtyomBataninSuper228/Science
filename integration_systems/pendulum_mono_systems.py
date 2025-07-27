from math import *
import numpy as np
import copy


g = 9.8

#classic_sys =  #np.matrix([1, -1, 0, 0, 1, 2**0.5], dtype=float)#x y x' y' m, l
def create_pendulum_sys(x, y, vx, vy, mass):
    E0 = mass*(vx**2+vy**2)/2 + mass*g*((x**2 + y **2)**0.5 + y)
    return np.matrix([x, y, vx, vy, mass, (x**2 + y **2)**0.5, E0], dtype= float)
classic_sys =  create_pendulum_sys(1, -0.1, 0, 0, 1)
def get_diff(sys):
    #print(sys[0][0])
    l = sys[0,5]#(sys[0, 0]**2 + sys[0,1]**2)**0.5
    v2 = (sys[0,2] ** 2 + sys[0,3] ** 2)
    sina = sys[0,0]/l
    cosa = -sys[0,1]/l
    Ep = sys[0, 4]*g*(l + sys[0, 1])
    Ek = sys[0,6] - Ep
    T = 2*Ek/l + sys[0,4]*g * cosa # 2Ek/R + mgcosa
    ax = -sina*T/sys[0, 4]
    #ay =  - g + cosa*(v2/l + g*cosa)
    return ax#np.matrix([[sys[0,2], ax], [sys[0,3], ay]])

def do_step(sys, h, k):
    #sys = copy.copy(sys)
    sys[0, 2] += k*h
    sys[0, 0] += sys[0, 2]*h
    sys[0, 1] = -(sys[0,5]**2 - sys[0,0]**2)**0.5
    return sys