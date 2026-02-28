from matplotlib import pyplot as plt
from math import *

dvx = 10**(-4)
vx = 0
md = []
while vx<= 1:
    vy = (1-vx**2)**0.5
    t = 80/vy
    d = (1.5-vx)*t
    if d == 89.44271926100137:
        print(vx)
    md.append(d)
    vx += dvx
print(min(md))
