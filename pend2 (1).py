import math
import sys
import time
from traceback import print_tb

import pygame as pg
from matplotlib import pyplot
from math import *
from threading import Thread

num = (-1)**0.5
num **= 3
print(num**2)
class pendulum:
    x = 0
    y = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    m = 0
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

dt = 10**(-5)
g = 9.8
tm = 0

p1 = pendulum(100, -100, 1)
p2 = pendulum(0, 100, 1)
len1 = (p1.x ** 2 + p1.y ** 2) ** 0.5

def update():
    global p1, p2, tm
    T2 = 0
    while 1:
        #p1.ax = 10
        #p1.ay = 0
        l1 = (p1.x ** 2 + p1.y ** 2) ** 0.5

        l2 = (p2.x ** 2 + p2.y ** 2) ** 0.5
        p1.ax *= -1
        p1.ay *= -1
        cosa = p1.y / l1
        sina = p1.x / l1
        cosb = p2.y / l2
        sinb = p2.x / l2
        cosy = p1.ax / (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5
        siny = (p1.ay - g )/ (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5
        a = acos(cosa)
        b = acos(cosb)
        #p1.x = len1 * sina
        #p1.y = len1 * cosa
        if p2.x!= 0:
            k = p2.x/abs(p2.x)
        else:
            k = 1
        if p1.ax!= 0:
            k *= p1.ax/abs(p1.ax)
        y = k*acos(siny)

        T2 = p2.m * (p2.vx ** 2 + p2.vy ** 2) / l2 + p2.m * (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5 * cos(b - y)
        T1 = p1.m * (p1.vx ** 2 + p1.vy ** 2) / l1 - p1.m * g * cosa + T2 * cos(a-b)


        p2.ax = -T2 * sinb / p2.m + p1.ax
        p2.ay = -T2 * cosb / p2.m + p1.ay - g
        p2.vx += p2.ax * dt
        p2.vy += p2.ay * dt
        p2.x += p2.vx * dt
        p2.y += p2.vy * dt
        p1.ax *= -1
        p1.ay *= -1
        p1.ax = -T1 * sina / p1.m + T2 * sinb / p1.m
        p1.ay = -T1 * cosa / p1.m - g + T2 * cosb / p1.m
        p1.vx += p1.ax * dt
        p1.vy += p1.ay * dt
        p1.x += p1.vx * dt
        p1.y += p1.vy * dt






        #time.sleep(1/10)
        tm += dt
        if tm*10%1 < dt:
            if abs(l1 - len1) > 1 and 0:
                break
            print(cosa)




pg.init()
sc = pg.display.set_mode((500, 1000))
prev = pg.surface.Surface(size=(500, 500))
prev.fill((0,0,0))
prev.set_alpha(10)
t1 = Thread(target=update)
t1.start()
while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
    sc.fill((0,0,0))
    pg.draw.circle(sc, (255, 255, 255), center=(250 + p1.x, 250 - p1.y), radius = 3)
    pg.draw.circle(sc, (255, 255, 255), center=(250 + p1.x + p2.x, 250 - p1.y - p2.y), radius=3)
    #sc.blit(prev, (0,0))
    #prev.fill((0,0,0))
    pg.draw.circle(sc, (255, 255, 255), center=(250, 250), radius=10)
    pg.draw.aaline(sc, (255, 255, 255), (250, 250), (250 + p1.x, 250 - p1.y))
    pg.draw.aaline(sc, (255, 255, 255), (250 + p1.x, 250 - p1.y), (250 + p1.x + p2.x, 250 - p1.y - p2.y))

    pg.display.update()




