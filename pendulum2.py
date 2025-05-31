import copy
import math
import sys
import time
from  matplotlib import pyplot
from threading import Thread

import pygame as pg

import matplotlib.pyplot as plt

pg.init()
sc = pg.display.set_mode((500, 500))
is_run = False
prev = pg.surface.Surface(size=(500, 500))
prev.fill((0,0,0))
prev.set_alpha(1)
g = 9.8
dt = 0.00001
class pendulum:
    m = 1
    x = 0
    y = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    l = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = pendulum(50, 100)
p2 = pendulum(0, 200)
p2.m = 1
r2 = ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
r = (p1.x ** 2 + p1.y ** 2) ** 0.5
tim = 0
#

def update():
    global p1, g, dt, r2, tim
    while 1:
        #print(p1.x, p1.y)
        r2 = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
        r = (p1.x ** 2 + p1.y ** 2) ** 0.5
        sina = p1.x / r
        cosa = p1.y / r
        sinb = (p2.x-p1.x)/r2
        cosb = (p2.y-p1.y)/r2
        if (p1.ax ** 2 + (p1.ay - g) ** 2) != 0:
            cosy = (-p1.ay - g) / (p1.ax ** 2 + (-p1.ay - g) ** 2) ** 0.5
            siny = p1.ax / (p1.ax ** 2 + (-p1.ay - g) ** 2) ** 0.5
        else:
            siny = 0
            cosy = 0
        a = math.acos(cosa)
        b = math.acos(cosb)
        k = 1
        if p2.x != 0:
            k *= p2.x/abs(p2.x)
        if p1.ax != 0:
            k *= p1.x/abs(p1.x)
        gamma = math.asin(siny*k)




        if (p2.x ** 2 + p2.y ** 2) ** 0.5 != r2 and 0:
            p2.x = r2 * ((p2.x-p1.x) / ((p2.x-p1.x) ** 2 + (p2.y-p1.y) ** 2) ** 0.5) + p1.x
            p2.y = r2 * ((p2.y-p1.y) / ((p2.x-p1.x) ** 2 + (p2.y-p1.y) ** 2) ** 0.5) + p1.y
        T2 = (((p2.vx-p1.vx) ** 2 + (p2.vy-p1.vy) ** 2)*p2.m / r2)  -p2.m * (p1.ax ** 2 + (-p1.ay - g) ** 2) ** 0.5 *(cosb*cosy + siny*sinb)  #- Fcentr*math.cos(b-y)
        T = (p1.vx ** 2 + p1.vy ** 2) * p1.m / r + p1.m * g * cosa + T2 * (cosa*cosb + sina*sinb)

        p2.ax = (-T2 * sinb) / p2.m
        p2.ay = (p2.m * (g) + T2 * cosb) / p2.m
        p2.vx += p2.ax * dt
        p2.vy += p2.ay * dt
        p2.x += p2.vx * dt
        p2.y += p2.vy * dt
        tim += dt

        p1.ax = (-T * sina + T2*sinb)/p1.m
        p1.ay = (p1.m * g - T*cosa + T2*cosb)/p1.m
        #p1.ax = 0
        #p1.ay = 0
        p1.vx += p1.ax * dt
        p1.vy += p1.ay * dt
        p1.x += p1.vx * dt
        p1.y += p1.vy * dt
        #p1.x = 0
        #p1.y = 100


        #break





t = Thread(target=update)
t.start()
#update()

while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()

        elif e.type==pg.KEYDOWN:
            is_run = not is_run
    pg.draw.aaline(sc, color = (255, 255, 255), start_pos=(250,250), end_pos=(p1.x+250, 250+p1.y))
    pg.draw.aaline(sc, color=(255, 255, 255), start_pos=(p1.x+250, 250+p1.y), end_pos=(p2.x + 250, 250 + p2.y))
    pg.draw.circle(sc, color=(255, 255,255), radius=5, center=(250, 250))
    pg.draw.circle(sc, color=(255, 255, 255), radius=5, center=(p1.x + 250, 250 + p1.y))
    pg.draw.circle(sc, color=(255, 255, 255), radius=5, center=(p2.x + 250, 250 + p2.y))
    sc.blit(prev, (0, 0))
    pg.display.update()
    sc.fill((0,0,0))


