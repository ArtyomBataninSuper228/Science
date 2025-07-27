import copy
import math
import sys
import time

import numpy as np
from  matplotlib import pyplot
from threading import Thread
import pygame as pg
import matplotlib.pyplot as plt
import numpy

pg.init()
sc = pg.display.set_mode((500, 500))
is_run = True
prev = pg.surface.Surface(size=(500, 500))
prev.fill((0,0,0))
prev.set_alpha(1)
#mass = 1
g = 9.8
x = 1
y = -1
vx = 0
vy = 0
ax = 0
ay = 0
dt = 10**(-4.5)
tm = 0
a = 0
r = (x**2 + y**2)**0.5
cosa = y / r
sina = x / r
siny = g/(g**2+a**2)**0.5
gamma = math.acos(siny)
alf = math.acos(cosa)
#print(cosa, siny, math.cos(gamma-alf), gamma, alf)
color = (255, 255, 255)
#ang = math.asin(sina)
l = ((x ** 2 + y ** 2) ** 0.5)
ang = math.asin(abs(sina))
if math.asin(sina) != 0:
    ang *= math.asin(sina) / abs(math.asin(sina))
'''
if x>0 and y <= 0:
    ang = math.pi - ang
if x<0 and y < 0:
    ang = -math.pi + ang
if x < 0 and y > 0:
    ang =  - ang
'''
angspeed = []
angls = []
times = []

def update():
    global x, y,vx, vy,ax, ay, tm, color, ang, angls
    while tm < 11600000:#36.46:
        if is_run:
                l = ((x ** 2 + y ** 2) ** 0.5)
                cosa = y / l
                sina = x / l
                alf = math.acos(cosa)
                cosy = g/(g**2+a**2)**0.5
                siny = a/(g**2+a**2)**0.5
                gamma = math.acos(cosy)
                if (x ** 2 + y ** 2) ** 0.5 != r and 0:
                    x = r * (x / (x ** 2 + y ** 2) ** 0.5)
                    y = r * (y / (x ** 2 + y ** 2) ** 0.5)
                T = (((vx ** 2 + vy ** 2) / r) +(a**2+g**2)**0.5*(cosa*cosy + sina*siny)) #+(g * cosa)) + a*math.cos(gamma-alf)
                if tm % 1 < dt:
                    pass
                    #print(gamma-alf, x)

                ax = (-T * sina) + a
                ay = (g - T * cosa)
                vx += ax * dt
                vy += ay * dt
                x += vx * dt
                y += vy * dt
                tm += dt
                if x -100 < 0.000001 and y + 100 < 0.000001 and 0:
                    color = (255, 25, 255)
                    #print(tm)
                else:
                    color = (255, 255, 255)
                prev = ang

                ang = math.acos(cosa)
                if math.asin(sina)!= 0:
                    ang*=math.asin(sina)/abs(math.asin(sina))


                va = (ang-prev)/dt

                if abs(va) < 100:
                    angspeed.append(va)

                    angls.append(ang)
                times.append(tm)
    plt.plot(angls, angspeed)
    plt.xlabel('Угол (рад)')# (𝜑0 = 180°)')
    plt.ylabel("Уголовая скорость (рад/сек)")
    plt.show()


#update()
##sys.exit()
t = Thread(target=update)
t.start()
#update()

while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()

        elif e.type==pg.KEYDOWN:
            is_run = not is_run
    pg.draw.aaline(sc, color = (255, 255, 255), start_pos=(250,250), end_pos=(x*100+250, 250+y*100))
    pg.draw.circle(sc, color=(255, 255,255), radius=5, center=(250, 250))
    pg.draw.circle(sc, color=color, radius=5, center=(x*100 + 250, 250 + y*100))
    sc.blit(prev, (0, 0))


    pg.display.update()
    sc.fill((0, 0, 0))
