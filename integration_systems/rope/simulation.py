#from integral import *
import rope_sys
import pygame as pg
import numpy as np
import threading
from integral import *

pg.init()
d_size = np.array([1400, 900])
ds = pg.display.set_mode(d_size)
k = 500
def_pos = d_size / 3
def_pos[1] = -50
print("start")
x= []
t = []
T = 0
dt = 10**-4
w = 2*pi*4
NUM = 100
font = pg.font.SysFont("Arial", 36)
sys = rope_sys.do_system(1, NUM, 10**5, 3, def_pos=(0.05, 0, 0))
def do_step(sys, h, k):
    sys += k*h
    return sys
def updater():
    global sys, T, dt
    while 1:
        #dsys = do_my4_2_step(sys, rope_sys.get_diff, dt)#rope_sys.get_diff(sys)
        sys2 = copy.copy(sys)
        dsys = seek_solution_nd(sys2, rope_sys.get_diff, do_step, dt)
        #dt = 1 / np.linalg.norm(dsys) / (10*NUM)
        sys += dsys * dt
        T += dt
        sys[0][1] = [0.05*cos(w*T), -1/NUM, 0.05*sin(w*T)]
t = threading.Thread(target=updater)
t.start()
while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()


    ds.fill((0,0,0))
    #for i in range(len(sys[0])):
    #    pos = def_pos + sys[0][i][:-1]*k
    #    pg.draw.circle(ds,  (255, 255, 255), (int(pos[0]), -int(pos[1])), 1)
    for x in range(int(def_pos[0])-50,int(def_pos[0])+501-50, 50 ):
        pg.draw.line(ds, (50, 50, 50), (x, 900), (x, 40))
        pg.draw.line(ds, (25, 255, 255), (x, 50), (x, 40))
    for y in range(40,541, 50 ):

        pg.draw.line(ds, (50, 50, 50), (int(def_pos[0])-50, y), (int(def_pos[0]) +1000, y))
        pg.draw.line(ds, (25, 255, 255), (int(def_pos[0]) - 10-50, y), (int(def_pos[0])-50, y))
    points = []
    for i in range(1,len(sys[0])):
            pos = def_pos + sys[0][i][:-1] * k
            try:
                points.append((int(pos[0]), -int(pos[1])))
            except:
                print("error", pos)
            #pg.draw.circle(ds, (255, 255, 255), (int(pos[0]), -int(pos[1])), 1)


    pg.draw.aalines(ds, (255,255,255), False, points)

    text_surface = font.render(f"Время: {round(T, 4)} сек", True, (255, 255, 255))
    ds.blit(text_surface, [100, d_size[1]//1.5])
    #for i in range(1,len(sys[0])):
    #    pg.draw.
    pg.display.update()
    time.sleep(1/70)





