import json
import math
from Navigation import *
from matplotlib import pyplot as plt
f = open("Path.csv")
m = []

for line in f.readlines():
    line = line.replace("\"", "")
    a = list(map(str, line.split(',')))
    t = a[1].split("T")[-1].replace("Z", "")
    t = t.split(":")
    sec = 0
    for i in range(3):
        sec += 60**(2-i)*int(t[i])
    lat = float(a[2])
    lon = float(a[3])
    h = float(a[4])
    a = [sec, get_x_y_z(lon, lat, h), h]
    m.append(a)
    #print(sec, lon, lat, h, a)

L = 0
v = []
t = []
l = []
h = []
for i in range(0, len(m)-4, 20):
    dl = 0
    dt = 0
    for j in range(0, 20):
        dl += get_l(m[i+j][1] - m[i+j+1][1])
        dt += m[i+j+1][0] - m[i+j][0]

    #dl = get_l(m[i+1][1] - m[i][1])
    L += dl
    V = dl/dt*3.6
    v.append(V)
    t.append(m[i][0])
    l.append(L)
    h.append(m[i][2])
x = 8
print((x**0.5)**(math.log(8, x**0.5)))
#plt.plot(l, v)
#plt.show()

#l = get_l(m[0][1] - m[1][1])
#print(l)