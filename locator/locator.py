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
            T0 = ((realX**2 + realY**2)**0.5)/c
            Ta = (((realX-l)**2 + realY**2)**0.5)/c + T0
            Tb = (((realX+l)**2 + realY**2)**0.5)/c + T0

            if  tos< Ta < toe:

                a = A[int((Ta - toe)/h)]
            if tos < Tb < toe:
                b = B[int((Tb - toe) / h)]
            a *= ((T0 + Ta)*c)**2
            b *= ((T0 + Tb)*c)**2
            amp = (abs(a*b))
            #print(amp)
            #print(res)
            array[width//2 + x, heigth - y-1] = amp
            #pg.draw.rect(sc, (res, res, res), (x + width/2, heigth - y, 1, 1))
    array/= array.max()
    array *= 255
    pg.surfarray.blit_array(layer, array.numpy())
    #sc.blit(layer, (0,0))
#ser = serial.Serial('/dev/cu.usbmodem101', 2000000)
A = []
B = []
T = []
t = 0
f = 60000
tos = 10**-4
toe = len(A)/f

def read(l = 1000, n = 10):
    try:
        global A, B, T, t, toe, toe
        A = []
        B = []
        T = []
        t = 0
        a = ser.readline()
        while a != b'Start\r\n':
            a = ser.readline()
            # print(bytes(a, "utf-8") )
        for i in range(l):
            a, b = list(map(int, ser.readline().split()))
            A.append(a / n)
            B.append(b / n)
            T.append(t)
            t += 1 / f
        for i in range(n - 1):
            a = ser.readline()
            while a != b'Start\r\n':
                a = ser.readline()
            for i in range(l):
                a, b = list(map(int, ser.readline().split()))
                A[i] += (a / n)
                B[i] += (b / n)
    except:
        read(l, n)




    mediana = sum(A) / len(A)
    medianb = sum(B) / len(B)
    for i in range(l):
        A[i] = (A[i] - mediana)
        B[i] = (B[i] - medianb)
    tos = 0
    toe = len(A) / f





f = open("Locator_experimentFurie", mode ="rb")
data = json.loads(f.read())
f.close()
rawA = np.array(data["mA"])
A = []

for i in rawA:
    A.append(abs(i - rawA.mean()))

A = np.array(A)
A -= A.min()

A *= 10
rawB = np.array(data["mB"])
B = []
for i in rawB:
    B.append(abs(i - rawB.mean()))

B = np.array(B)
B -= B.min()
B *= 10
tos = data["tos"]
f = 1/data["dt"]

toe  = len(A) / f
#pyplot.plot(rawA)
#pyplot.plot(rawB)
#pyplot.show()

create_diagram(A, B, tos, toe, 0.27, 1400, 700)


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






