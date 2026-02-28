import sys

import numpy
import serial
from integral import *
import pygame as pg
from threading import Thread

import json
from matplotlib import pyplot as plt
import torch
#pg.init()
w = 1000
h = 500
#sc = pg.display.set_mode((w, h))

ser = serial.Serial('/dev/cu.usbmodem1101', 2000000)
def get_signal(data, dt, f, packetsz):
    data -= data.min()
    data /= data.max()
    N = len(data)//packetsz
    basetenzor = torch.zeros(packetsz, dtype=torch.float64)
    sine = torch.zeros(packetsz, dtype=torch.float64)
    cosine = torch.zeros(packetsz, dtype=torch.float64)
    result = torch.zeros(packetsz, dtype=torch.float64)
    T = torch.zeros(N, dtype=torch.float64)
    Ampl = torch.zeros(N, dtype=torch.float64)
    for i in range(packetsz):
        basetenzor[i] = 2*pi*i*dt*f
    torch.sin(basetenzor, out=sine)
    torch.cos(basetenzor, out=cosine)
    for n in range(N-1):
        st = n*packetsz
        end = n*packetsz + packetsz
        data_m = data[st:end]
        torch.mul(sine, data_m, out=result)
        S = result.sum()
        torch.mul(cosine, data_m, out=result)
        C = result.sum()
        A = S**2+C**2
        T[n] = n*dt*packetsz
        Ampl[n] = A
    return T, Ampl






A = torch.zeros(50000, device=torch.device('cpu'))
B = torch.zeros(50000, device=torch.device('cpu'))
dt = 1 / 129000
F = 40000
psz = 50

def READ():
    global A, B
    # print(ser.readline())
    ser.write(b"START")
    for i in range(50000):
        A[i] = (int(ser.readline()))
    for i in range(50000):
        B[i] = (int(ser.readline()))
    #plt.plot(A)
    #plt.plot(B)
    #plt.show()
    print("reading_completed")
def get_data():
    READ()
    T, Aa = get_signal(A, dt, F, psz)
    T, Ab = get_signal(B, dt, F, psz)
    return T, Aa, Ab

if __name__ == "__main__":
    READ()
    T, Aa = get_signal(A, dt, F, psz)
    T, Ab = get_signal(B, dt, F, psz)
    d = 7*dt*psz
    N = int(0.0117322 / dt / psz)+7
    end = int(15/343/dt/psz+N)
    print(N, end)
    T = T[N:end]
    Ab = Ab[N:end]
    Aa = Aa[N:end]
    js = {
        "f": F,
        "dt": dt*psz,
        "desc": "Измерение 2 (тест)",
        "tos": d,
        "mA": Aa.tolist(),
        "mB": Ab.tolist(),
    }

    json.dump(js, open("LOCATOR2_0/izmer2.json", "w"))

    plt.plot( Aa.tolist())
    plt.plot(Ab.tolist())
    plt.show()



