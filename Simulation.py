import cmath
import sys
import os
import copy
import time
import cv2
import math
import numpy as np
import pygame as pg
from threading import Thread
import sys
import multiprocessing





pg.init()

is_stopped = True

w, h = 900, 900  # размер окна
wm, hm = 200, 200  # размер модели на экране
is_run = True
h_bomb = 100
r_bomb = 26
text = ["Высота взрыва: " + str(h_bomb) + " Радиус взрыва: "+ str(r_bomb)]
text_size = 32
font = pg.font.Font(None, text_size)
ground = 700
fps_model = 0

a = pg.surface.Surface(size=(w, h))
a.set_alpha(255)

ma = np.zeros((wm, hm, 3), float)
ms = np.zeros((wm, hm), float)
mm = np.ones((wm, hm), float)
mm.fill(1) # Влияет на скорость волны в модели. при еденице волна проходит пол пикселя за итерацию
ma.fill(100)
#ma = np.arange(w*h).reshape(w, h)

for x in range(wm):
    for y in range(hm):
        if math.sqrt((x - wm/2)**2 + (y - int((ground - h_bomb)/(w/wm)))**2) < int(r_bomb/(w/wm)):
            ma[x][y][0] = 250

for x in range(wm):
    for y in range(int(ground/(w/wm)), hm):
        mm[x][y] = 2000


values = np.zeros(wm, float)

def update():  #Обновление модели
    global ma, values, fps_model
    iteration = 0
    while is_run:
        t1 = time.time()

        if  is_stopped == False:
            ma1 = copy.deepcopy(ma)
            for x in range(wm):
                for y in range(hm):

                    i = ms[x][y]
                    a = ma1[x][y][0]
                    num = 0
                    val = 0
                    dy = y
                    for dx in range(x - 1, x + 2, 2):

                        if dx == x:
                            continue
                        if dx < 0:
                            continue
                        if dx >= wm:
                            continue
                        num += 1
                        val += ma1[dx][dy][0]
                    dx = x
                    for dy in range(y - 1, y + 2, 2):

                        if dy == y:
                            continue
                        if dy < 0:
                            continue
                        if dy >= hm:
                            continue

                        num += 1
                        val += ma1[dx][dy][0]
                    if num != 4:  # Подавление отражения от стенок
                        i = 0
                    i += ((val / num) - a) / mm[x][y]

                    # print(x, y, ma[x][y], ms[x][y], sv)
                    a += i

                    ms[x][y] = i
                    if a > 255:
                        a = 255
                    if a < 0:
                        a = 0
                    ma[x][y][0] = a
                    ma[x][y][1] = a
                    ma[x][y][2] = a
                    # print(num, val, i)

            # ma = ma1
            # break
            v = ms[0:, int(ground / (w / wm) - 1):int(ground / (w / wm))]
            for x in range(wm):
                values[x] = max(abs(v[x]), values[x])

            #values = values.reshape(100)
        else:
            time.sleep(1/60)
        t2 = time.time()
        if t2!= t1:
         fps_model = 1/(t2 - t1)



class stroenie:
    x = 0
    h = 0
    l = 0
    num = 0
    def __init__(self, x, h, l, num):
        self.x = x
        self.h = h
        self.l = l
        self.num = num
    def draw(self):
        pg.draw.rect(a, color = (50, 50,   75), rect=(self.x, ground - self.h, self.l, self.h))
    def add_in_model(self):
        global  text
        text.append(f"Строение {self.num} Высота: {self.h} Ширина: {self.l} Позиция: {self.x}")
        global w, wm, mm
        for x in range(int(self.x/ (w/wm)), int((self.x + self.l)/ (w/wm))):
            for y in range(int(ground/(w/wm) - (self.h/(w/wm))), int(ground/(w/wm))):
                mm[x][y] = 2000


objects = []
s = stroenie(250, 100, 40, 1)
objects.append(s)
s = stroenie(650, 100, 40, 2)
objects.append(s)
s = stroenie(500, 100, 40, 3)
objects.append(s)


s = stroenie(320, 40, 20, 4)
objects.append(s)
s = stroenie(600, 40, 20, 5)
objects.append(s)


for o in objects:
    o.add_in_model()
t = Thread(target=update)
t.start()

sc = pg.display.set_mode((w, h))


fps = 0
text.append(f"Display FPS: {int(fps)} Model FPS: {int(fps_model)}")
while  1:
    t1 = time.time()
    for event in pg.event.get():
        if event.type== pg.QUIT:
            is_run = False
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                is_stopped = bool( not is_stopped)# Пробел - начало симуляции
                #t.start()
    sc.fill((0, 0, 0))
    mb = cv2.resize(ma, (h, w), interpolation=cv2.INTER_CUBIC)  # Масштабирование матрицы под размер экрана



    pg.surfarray.blit_array(a, mb)
    for o in objects:
        o.draw()

    pg.draw.rect(a, rect=(0, ground, w, h), color=(101, 67, 33))

    x = 0
    dx = w/wm
    k = 255//(math.log(max(values + 1)) + 1)
    for val in values:
        #v = abs(int(val))
        pg.draw.rect(a, rect=(x, ground, dx, 10), color=(math.log(val + 1)* k, 255 - math.log(val + 1)* k, 25))
        x += dx
    y = 0
    dy = text_size*1.25
    text[-1] = f"Display FPS: {int(fps)} Model FPS: {int(fps_model)}"
    for tx in text:
        t = font.render(tx, True, (255, 255, 255))
        a.blit(t, (0, y))
        y += dy


    sc.blit(a, (0, 0))
    pg.display.update()
    t2 = time.time()
    fps = 1/(t2 - t1)
    #time.sleep(1/62)