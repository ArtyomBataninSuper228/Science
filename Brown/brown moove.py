import json
import sys
import time
from math import *
import random
from threading import Thread
#from brown_theoretical import *

import pygame as pg
from matplotlib import pyplot

randomfile = open("/dev/random", "rb")
maxA = 10 # Максимальное ускорение частицы при столкновении
scale_factor = 1000
scale = 500
resolution = 100
num = 100000
h = 10**(-3)
x = 0.5
y = 0
vx = 0
vy = 0


def generate_random(min= 0, max = 10000):
    res = list(randomfile.read(10))
    bn = ""
    nm = 0
    for i in range(10):
        bn += bin(res[i])[2:]
        #nm += res[9-i]*256**i
        #bn += bin(res[i])[2:].zfill(8)
        #print(bin(nm)[2:], bn)
        #time.sleep(1/10)
    num = int(bn,2)
    #print(num, nm)
    return num%(max-min) + min


def start_simulating():
    global vx, vy, x, y
    while 1:
        a = (list(randomfile.read(1))[0]) -127.5
        #print(a)
        #generate_random(0, maxA*scale_factor)/scale_factor#random.randint(0, maxA*scale_factor)/scale_factor#
        #angle = generate_random(0, 360*scale_factor)/scale_factor
        vx += a*h#a*cos(angle/180*pi)*h
        #vy += a*sin(angle/180*pi)*h
        x += vx*h
        #y += vy*h
        if x > 1:
            return 1
        if x < 0:
            return -1


def start_research(l, x0 = 0.5):
    massive = []
    global vx, vy, x, y
    for i in range(l):
        massive.append(start_simulating())
        x = x0
        y = 0
        vx = 0
        vy = 0
    return massive
mx = []
mp = []
for i in range(0, resolution + 1):
    t1 = time.time()
    print(i)
    mx.append(i/resolution)
    mp.append(start_research(num, i/resolution).count(1)/num)
    t2 = time.time()
file = open("theory.json", "w")
mpt, mxt = json.load(file)
file.close()
file = open("experiment.json", "w")
file.write(json.dumps([mx, mp]))
file.close()
pyplot.plot(mx, mp, mxt, mpt)
pyplot.xlabel("X")
pyplot.ylabel("P")
pyplot.show()
sys.exit()

pg.init()
sc = pg.display.set_mode((1600,900))
t = Thread(target=start_research)
t.start()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    #sc.fill((0,0,0))
    pg.draw.line(sc, (255,255,255), (-1*scale + 800, 0), (-1*scale + 800, 900), 2)
    pg.draw.line(sc, (255, 255, 255), (1 * scale + 800, 0), (1 * scale + 800, 900), 2)
    pg.draw.circle(sc, (255,255,255), (x*scale + 800, y * scale + 450), 1)
    pg.display.update()
    #time.sleep(1/62)


randomfile.close()