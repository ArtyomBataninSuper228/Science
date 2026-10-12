#from integral import *
import rope_sys
import pygame as pg
import numpy as np
import threading
from integral import *

pg.init()
d_size = np.array([1600, 900])
ds = pg.display.set_mode(d_size)
k = 500
def_pos = d_size / 2
print("start")
x= []
t = []
T = 0
dt = 10**-4
NUM = 20
sys = rope_sys.do_system(1, NUM, 10000, 3)
def updater():
    global sys, T, dt
    while 1:
        dsys = do_my4_2_step(sys, rope_sys.get_diff, dt)#rope_sys.get_diff(sys)
        dt = 1 / np.linalg.norm(dsys) / (100*NUM)
        sys += dsys * dt
        T += dt
t = threading.Thread(target=updater)
t.start()
while 1:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()


    ds.fill((0,0,0))
    for i in range(len(sys[0])):
        pos = def_pos + sys[0][i][:-1]*k
        pg.draw.circle(ds,  (255, 255, 255), (int(pos[0]), int(pos[1])), 1)
    pg.display.update()
    time.sleep(1/30)





