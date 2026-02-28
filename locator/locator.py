import copy
import json
import random
import sys
import numpy as np
import torch
from math import *
import pygame as pg
import serial
from random import randint
import time
from matplotlib import pyplot as plt, pyplot
import datasayver2

pg.init()
sc = pg.display.set_mode((1400, 700))
layer  = pg.Surface((1400, 700))

k =1
c = 331.46
def create_diagram(A, B, tos, toe, l, width, heigth):
    array = torch.zeros([width, heigth, 3], dtype=torch.float)
    global k
    minX = -c*toe/2 +l/2
    maxX = c*toe/2 - l/2
    maxY = (c*toe)/2
    #print(maxX, maxY)
    h = (toe-tos)/len(A)
    dl = (maxX-minX)
    k1 = dl/width
    k2 = maxY/heigth
    k = max(k1, k2)
    #kx = (maxX-minX)/width
    #ky = maxY/heigth
    for x in range(-width//2, width//2):
        for y in range(0, heigth):
            realX = x*k
            realY = y*k
            a, b = 0, 0
            T0 = (((realX)**2 + realY**2)**0.5)/c
            #T0b = (((realX + 0.49) ** 2 + realY ** 2) ** 0.5) / c
            Ta = (((realX-0.46)**2 + realY**2)**0.5)/c + T0
            Tb = (((realX+0.02)**2 + realY**2)**0.5)/c + T0
            #print((Ta-Tb)*343)

            if  tos< Ta < toe:
                a = A[round((Ta - toe)/h)]

            if tos < Tb < toe:
                b = B[round((Tb - toe) / h)]
            #a *= ((T0a + Ta)*c)
            #b *= ((T0b + Tb)*c)
            amp = (abs(a*b))
            #if amp != 0:
                #print(amp)
            #print(amp)
            #print(res)
            array[width//2 + x, heigth - y-1] = amp
            #pg.draw.rect(sc, (res, res, res), (x + width/2, heigth - y, 1, 1))
    array/= array.max()
    array *= 255
    pg.surfarray.blit_array(layer, array.numpy())
    #sc.blit(layer, (0,0))
#ser = serial.Serial('/dev/cu.usbmodem101', 2000000)






f = open("LOCATOR2_0/izmer2.json", mode ="rb")
data = json.loads(f.read())
f.close()
rawA = np.array(data["mA"])
plt.plot(data["mA"])
plt.show()
A = torch.tensor(data["mA"])
B = torch.tensor(data["mB"])
A -= A.min()
B -= B.min()
A/=A.max()
B/=B.max()
A += 0.4
B += 0.4





tos = data["tos"]
f = 1/data["dt"]
toe  = len(A) / f
print(toe, tos)
#pyplot.plot(rawA)
#pyplot.plot(rawB)
#pyplot.show()

create_diagram(A, B, tos, toe, 0.5, 1400, 700)


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            x -= 700
            y = 700 - y
            x*= k
            y*= k
            print(x, y)

    #read(n = 10)
    #plt.plot(T, A, T, B)
    #plt.show()

    sc.fill((0, 0, 0))
    sc.blit(layer, (0,0))
    #pg.draw.line(sc, (255, 0, 0), (700, 0), (700, 700), 2)
    pg.display.update()
    time.sleep(1/60)






