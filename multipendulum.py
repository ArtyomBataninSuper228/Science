import time

from numpy import *
import pygame as pg
from threading import Thread

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

class pend:
    def __init__(self, m = 1, x = 0, y = 0, vx = 0, vy = 0):
        self.m = m
        self.pos = array([x,y], dtype=float64)
        self.speed = array([vx,vy], dtype=float64)
        self.force = array([0,0], dtype=float64)
    def add_force(self, force):
        self.force += force
    def update(self, dt):
        self.speed += self.force*dt
        self.pos += self.speed*dt
        self.force = array([0,0], dtype=float64)
        self.speed *= 1 - (10 ** (-3.25))
class pend_system:
    def __init__(self, num = 0, r0 = 1, k = 1000000, dt = 10**(-3)):
        self.num = num
        self.r0 = r0
        self.pends = []
        self.k = k
        self.dt = dt
        y = 0
        for i in range(num):
            self.pends.append(pend(y = y))
            y -= self.r0
    def update(self):
        for i in range(1, self.num):
            dr = dist(self.pends[i].pos, self.pends[i-1].pos) - self.r0
            force = (self.pends[i-1].pos - self.pends[i].pos)*dr*self.k
            self.pends[i].add_force(force)
            self.pends[i-1].add_force(-force)
            self.pends[i].add_force(force)
            self.pends[i].add_force(array([0, -9.8]))
        for i in range(1, self.num):
            self.pends[i].update(self.dt)

p = pend_system(30, dt=10 ** (-3.5))
def update():
    global p
    n = 0
    for i in range(29):
        p.pends[i+1].pos = p.pends[i].pos + array([1,0], dtype=float64)
    while 1:
        n += 1
        if n % 10000 == 0:
            print(p.pends[-1].pos)
        p.update()

t = Thread(target=update)
t.start()
pg.init()
sz = array([800, 600])
sc =  pg.display.set_mode(sz)
st = array(sz[0]/2, sz[1]//5)

while 1:
    for e in pg.event.get():
        pass

    for pend in p.pends:
        pg.draw.circle(sc, (255, 255, 255), st + 5 * array([pend.pos[0], -pend.pos[1]]), 2)
    pg.display.update()
    time.sleep(1 / 60)
    sc.fill((0, 0, 0))
