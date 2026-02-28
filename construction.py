import copy
import threading
import time

import pygame as pg
import math
import numpy as np
import torch

def length(p):
    r = 0
    for i in range(len(p)):
        r += p[i] ** 2
    return r**0.5
W = 800
H = 600
DOTS = []
FITTINGS = []
dt = 10**(-4)
g = 9.8
T = 0
class Dot:
    def __init__(self, x, y, vx = 0, vy = 0, m = 1):
        self.x = x
        self.y = y + 100
        self.vx = vx
        self.vy = vy
        self.m = m
        self.index = len(DOTS)
        DOTS.append(self.to_vector())


    def to_vector(self):

        return np.array((self.x, self.y, self.vx, self.vy, self.m), dtype=np.float64)


class Fitting:
    def __init__(self, dot1, dot2, k = 1000000):
        self.dot1 = DOTS[dot1.index]
        self.dot2 = DOTS[dot2.index]
        self.l0 = length(self.dot1[0:2] - self.dot2[0:2])
        self.k = k
        FITTINGS.append(self)
    def update(self):
        F = (length(self.dot1[0:2] - self.dot2[0:2]) - self.l0)/self.l0*self.k
        self.dot1[2:4] += F/self.dot1[4] * (self.dot2-self.dot1)[0:2]*dt
        self.dot2[2:4] += F / self.dot2[4] * (self.dot1 - self.dot2)[0:2]*dt

def updating_model():
    global T, FITTINGS, DOTS
    while 1:
        for fit in FITTINGS:
            fit.update()
        for dot in DOTS:
            if dot[1] < 0:
                dot[3] -= dot[1]*10000*dt
            dot[3] -= g * dt
            dot[0:2] += dot[2:4]*dt
            #print(dot[0:2], dot[2:4])

        T += dt

t = threading.Thread(target=updating_model)
t.start()
d1 = Dot(0, 100, 0, 0, 1)
d2 = Dot(0, 50, 0, 0, 1)
d3 = Dot(50, 75, 0, 0, 1)
d4 = Dot(-50, 75, 0, 0, 1)
d5 = Dot(0, 200, 0, 0, 1)
d6 = Dot(75, 200, 0, 0, 1)
d7 = Dot(175, 200, 0, 0, 1)
Fit1 = Fitting(d1, d2)
Fit2 = Fitting(d2, d3)
Fit3 = Fitting(d3, d1)
Fit4 = Fitting(d4, d1)
Fit5 = Fitting(d2, d4)
Fit6 = Fitting(d5, d4)
Fit7 = Fitting(d5, d3)
Fit8 = Fitting(d6, d5)
Fit9 = Fitting(d6, d3)
Fit10 = Fitting(d6, d7)
pg.init()
sc = pg.display.set_mode((W, H))
campos = np.array((400, 300))
k = 1.4
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    sc.fill((0, 0, 0))
    for dot in DOTS:
        pos = copy.copy(dot[0:2])
        pos[1] = -pos[1]
        pos += campos
        pos *= k
        pos = np.array(pos, dtype=np.int64)
        #pg.draw.circle(sc, (255, 255, 255), pos, 4)
    for fit in FITTINGS:
        pos1 = copy.copy(fit.dot1[0:2])
        pos1[1] = -pos1[1]
        pos1 += campos
        pos1 *= k
        pos1 = np.array(pos1, dtype=np.int64)

        pos2 = copy.copy(fit.dot2[0:2])
        pos2[1] = -pos2[1]
        pos2 += campos
        pos2 *= k
        pos2 = np.array(pos2, dtype=np.int64)
        pg.draw.aaline(sc, (25, 255, 255), pos1, pos2, 2)
    y = campos[1]
    y *= k
    r = pg.rect.Rect(0, y, W, H)
    pg.draw.rect(sc, (155, 255, 25), r)
    pg.display.update()
    time.sleep(1/100)
