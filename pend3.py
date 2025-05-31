import copy
import sys
import time
import pygame as pg
from matplotlib import pyplot as plt
from math import *
from threading import Thread
import integral



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

dt = 10**(-5.5)
g = 9.8
time_of_simulation = 0
massive_of_angles = []
massive_of_times = []
massive_of_angle_speed = [[]]
p1 = pendulum(1, 1, 1)
p2 = pendulum(-1, 1, 1)
l1 = (p1.x ** 2 + p1.y ** 2) ** 0.5
l2 = (p2.x ** 2 + p2.y ** 2) ** 0.5
cosa = p1.y / l1
sina = p1.x / l1
cosb = p2.y / l2
sinb = p2.x / l2

a = acos(-cosa)
if sina != 0:
    a *= asin(sina)/abs(asin(sina))
b = acos(-cosb)
if sinb != 0:
    b *= asin(sinb)/abs(asin(sinb))


def update():
    time.sleep(1)
    global p1, p2, time_of_simulation, a, b, cosa, cosb, sina, sinb, l1, l2
    T1 = 0
    T2 = 0
    l1 = (p1.x ** 2 + p1.y ** 2) ** 0.5
    l2 = (p2.x ** 2 + p2.y ** 2) ** 0.5
    cosa = p1.y / l1
    sina = p1.x / l1
    cosb = p2.y / l2
    sinb = p2.x / l2
    # cosy = p1.ax / (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5

    a = acos(-cosa)
    if sina != 0:
        a *= asin(sina) / abs(asin(sina))
    b = acos(-cosb)
    if sinb != 0:
        b *= asin(sinb) / abs(asin(sinb))


    while time_of_simulation < 20:
        t2 = T2
        #preva = a


        pcosb = cosb
        psinb = sinb
        pcosa = cosa
        psina = sina

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

        if (p1.ax ** 2 + (p1.ay - g) ** 2)!= 0:
            cosy = (p1.ay - g )/ (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5
            siny = p1.ax / (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5
        else:
            siny = 0
            cosy = 0



        T2 = p2.m * (p2.vx ** 2 + p2.vy ** 2) / l2 + p2.m * (p1.ax ** 2 + (p1.ay - g) ** 2) ** 0.5 *(cosb*cosy + siny*sinb)
        T1 = p1.m * (p1.vx ** 2 + p1.vy ** 2) / l1 - p1.m * g * cosa + t2  * (pcosa*pcosb + psina*psinb)
        p2.ax = -T2 * sinb / p2.m + p1.ax
        p2.ay = -T2 * cosb / p2.m + p1.ay - g
        p2.vx += p2.ax * dt
        p2.vy += p2.ay * dt
        p2.x += p2.vx * dt
        p2.y += p2.vy * dt
        p1.ax *= -1
        p1.ay *= -1

        p1.ax = -T1 * sina / p1.m + t2*psinb/p1.m
        p1.ay = -T1 * cosa / p1.m - g +  t2*pcosb/p1.m
        p1.vx += p1.ax * dt
        p1.vy += p1.ay * dt
        p1.x += p1.vx * dt
        p1.y += p1.vy * dt
        preva = a
        a = acos(-cosa)
        if sina != 0 :
            a *= asin(sina) / abs(asin(sina))
        # i = p2.y/abs(p2.y)

        b = acos(-cosb)
        if sinb != 0:
            b *= asin(sinb) / abs(asin(sinb))




        va = a/abs(a)*(abs(a)-abs(preva))/dt
        if a/abs(a) != preva/abs(preva) and abs(a) < 1.5:
            va = (a-preva)/dt
        if va > 100:
            print(va, preva, a, sina, cosa)

        nb = asin(sinb)
        prevb = asin(psinb)
        vb = (nb - prevb)/dt
        massive_of_angles.append(a)
        massive_of_angle_speed[0].append(va)
        massive_of_times.append(time_of_simulation)
        time_of_simulation += dt

        #print(a, b, y, a+b)
        #time.sleep(dt)


#update()
#plt.plot(massive_of_angles, massive_of_angle_speed[0])
#plt.xlabel('Угол отклонения (рад)')# (𝜑0 = 180°)')
#plt.ylabel("Угловая скорость (рад/сек)")
#plt.show()
#integral.create_grafic(massive_of_angles, massive_of_angle_speed)
pg.init()
pg.font.init()
font = pg.font.Font(None, 32)
sc = pg.display.set_mode((500, 1000))
t1 = Thread(target=update)
t1.start()
while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
    sc.fill((0,0,0))
    pg.draw.circle(sc, (255, 255, 255), center=(250 + p1.x*100, 250 - p1.y*100), radius = 10)
    pg.draw.circle(sc, (255, 255, 255), center=(250 + p1.x*100 + p2.x*100, 250 - p1.y*100 - p2.y*100), radius=10)
    pg.draw.circle(sc, (255, 255, 255), center=(250, 250), radius=10)
    pg.draw.aaline(sc, (255, 255, 255), (250, 250), (250 + p1.x*100, 250 - p1.y*100))
    pg.draw.aaline(sc, (255, 255, 255), (250 + p1.x*100, 250 - p1.y*100), (250 + p1.x*100 + p2.x*100, 250 - p1.y*100 - p2.y*100))
    text = font.render(f"{round(time_of_simulation, 3)}", True, (255, 255, 255))
    sc.blit(text, (150, 600))
    texta = font.render(f"{round(a, 3)}", True, (255, 25, 25))
    sc.blit(texta, (350, 600))
    textb = font.render(f"{round(b, 3)}", True, (25, 255, 25))
    sc.blit(textb, (350, 700))

    pg.display.update()




