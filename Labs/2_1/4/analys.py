from math import *
from matplotlib import pyplot as plt
import numpy as np



#U 0.029, 0.057, 0.092


data = [
    ["Вольтметр", "Предел шкалы", "U",          "dU",                "U_расч", "R_v",       "I, ма"],
    ["GDM",            200,         66.44,       66.44*0.0003+4*0.01,           0,       10**7,        0],
    ["M2044",          150,         48.5,       150 * 0.002,                   0,       1000 * 150 / 0.15,     0.15],
    ["M2044",          75,         37.5,        75*0.002,                     0,       75/0.15*1000,            0.15],


]

####Решение системы уравнений для нахождения U_0 и R_v:
###/ I1 = U0/(R_v1+ r)
###\ I2 = U0/(R_v2 + r)
#R_v известно - система не нужна
for i in range(1, len(data)-1):
    line = data[i]
    line1 = data[i+1]
    U_0 = np.array([line[5], line1[5]])
    R = np.array([-line[2], -line1[2]])
    V = np.array([line[2]*line[5], line1[2]*line1[5]])
    M = np.matrix([U_0, R]).transpose()
    #print(M)
    d = np.linalg.det(M)
    M_U0 = np.matrix([V, R]).transpose()
    #print(M_U0)
    d_u0 = np.linalg.det(M_U0)
    M_R = np.matrix([U_0, V]).transpose()
    #print(M_R)
    d_r = np.linalg.det(M_R)
    r = d_r/d
    u0 = d_u0/d
    print(r, u0)
    delta = u0*line[5] - line[2]*r - line[2]*line[5]
    delta1 = u0 * line1[5] - line1[2] * r - line1[2] * line1[5]
    print(delta, delta1)

###
r = 428612
U = 69.28
for i in range(1, len(data)):
    line = data[i]
    line[4] = U*line[5]/(line[5]+r)


for line in data:
    for el in line:
        el2 = ""
        if type(el) == str:
            el2 = el
        else:
            el2 = str(round(el, 2))
        print(el2, end = " "*(16-len(el2)))
    print()

print(4428*0.02)