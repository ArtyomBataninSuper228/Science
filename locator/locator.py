import copy
import random
import sys
from math import *
#from numpy import *
import pygame as pg
import serial
from random import randint
import time
from matplotlib import pyplot as plt, pyplot

pg.init()
sc = pg.display.set_mode((1400, 700))



c = 331.46
def create_diagram(A, B, tos, toe, l, width, heigth):

    minX = -c*toe/2 +l/2
    maxX = c*toe/2 - l/2
    maxY = (c*toe)/2
    print(maxX, maxY)
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
            a *= ((T0 + Ta)*c)
            b *= ((T0 + Tb)*c)
            amp = (abs(a*b)+1)/50
            #print(amp)
            res = int(amp)%255
            #print(res)
            pg.draw.rect(sc, (res, res, res), (x + width/2, heigth - y, 1, 1))
ser = serial.Serial('/dev/cu.usbmodem101', 2000000)
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




read(n = 1)
A1 = copy.copy(A)
B1 = copy.copy(B)
read(n = 1)
A2 = A
B2 = B
DeltaA = []
DeltaB = []
for i in range(len(A)):
    DeltaA.append(A2[i] - A1[i])
    DeltaB.append(B2[i] - B1[i])
pyplot.plot(T,A1, T, B1)
pyplot.show()




while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    read(n = 10)
    #plt.plot(T, A, T, B)
    #plt.show()
    sc.fill((0, 0, 0))
    create_diagram(A, B, tos, toe, 0.27, 1400, 700)
    pg.display.update()






