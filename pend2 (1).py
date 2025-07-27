import copy
import math
import sys
import time

from integration_systems import pendulum_mono_systems as pend
import pygame as pg
from matplotlib import pyplot
from math import *
from threading import Thread
from integral import *

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

dt = 10**(-4)
g = 9.8
tm = 0

system = pend.classic_sys
system2 = copy.copy(system)
s = pend

def update():
    global system, s, tm, system2
    while 1:
        system = do_backward_euler_step(system, s.get_dif, s.do_step, dt)
        system2 = do_runge_kutta_classic_step(system2, s.get_dif, s.do_step, dt)
        tm += dt




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
    #system = do_backward_euler_step(system, s.get_dif, s.do_step, dt)
    #tm += dt
    x, y = system[0, 0], system[0, 1]
    x2, y2 = system2[0, 0], system2[0, 1]
    pg.draw.circle(sc, (255, 255, 255), center=(250, 250), radius=10)
    pg.draw.circle(sc, (25, 255, 255), center=(250 + x*100, 250 - y*100), radius = 10)
    pg.draw.line(sc, (255, 255, 255), (250, 250), (250 + x*100, 250 - y*100))
    pg.draw.circle(sc, (255, 255, 255), center=(250 + x2*100, 250 - y2*100), radius = 10)
    pg.draw.line(sc, (255, 255, 255), (250, 250), (250 + x2*100, 250 - y2*100))
    print(tm)
    #pg.draw.aaline(sc, (255, 255, 255), (250 + p1.x, 250 - p1.y), (250 + p1.x + p2.x, 250 - p1.y - p2.y))

    pg.display.update()




