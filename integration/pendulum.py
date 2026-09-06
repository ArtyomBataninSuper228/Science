import pygame as pg
import sys
import time
W = 800
H = 600
sc = pg.display.set_mode((W, H))



m = 1
k = 100
x = 2
vx = 0
t = 0
dt = 0.01
toe = 10

X = []
T = []
st = time.time_ns()
framerate = 60

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    a = -(k*x)/m
    vx += a*dt
    x += vx*dt
    X.append(x)
    T.append(t)
    t += dt
    sc.fill((0,0,0))
    pg.draw.circle(sc, (255,255,255), (W/2 + x*100, H/2), 20)
    pg.display.update()
    st += 1/framerate*10**9
    while time.time_ns() < st:
        pass



