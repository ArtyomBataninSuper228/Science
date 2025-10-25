import sys

from matplotlib import pyplot
from math import *
from integral import *

randomfile = open("/dev/random", "rb")
def generate_random(min= 0, max = 10000):
    res = list(randomfile.read(10))
    bn = ""
    for i in range(10):
        bn += bin(res[i])[2:].zfill(8)
    num = int(bn,2)
    #print(num, nm)
    return num%(max-min) + min

def get_distance(toe = 10, h = 10**(-1), maxa = 1):
    x = 0
    vx = 0
    num = round(toe/h)
    randoms = randomfile.read(num)
    for i in range(num):
        vx += (randoms[i]-127.5)*maxa/127*h
        x += vx*h
    return x

def get_distribution(Time, h, maxa, num):
    md = []
    for i in range(num):
        d = get_distance(Time, h, maxa)
        md.append(d)
    return md


sigmas = []
tm = []
for tr in range(1, 1001):
    t = tr/100
    print(t)
    tm.append(t)
    md = get_distribution(t, 10**(-2), 1, 10**4)
    sigma = get_variance(md) ** 0.5
    sigmas.append(sigma)


#pyplot.plot(tm, sigmas)
#pyplot.xlabel("T")
#pyplot.ylabel("Стандартное отклонение")
#pyplot.show()




randomfile.close()