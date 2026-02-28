import numpy
import serial
import json
from matplotlib import pyplot as plt
ser = serial.Serial('/dev/cu.usbmodem1101', 2000000)
A = []
B = []
T = []
def read(l = 1000, n = 10):
    try:
        global A, B, T, t, toe, toe
        A = []
        B = []
        T = []
        t = 0

        ser.write(b"start")
        a = ser.readline()
        while a != b'Start\r\n':
            a = ser.readline()
        for i in range(l):
            a, b = list(map(int, ser.readline().split()))
            A.append(a / n)
            B.append(b / n)
            T.append(t)
            t += 1 / f
        for i in range(n - 1):
            ser.write(b"start")
            a = ser.readline()
            while a != b'Start\r\n':
                a = ser.readline()

            for i in range(l):
                a, b = list(map(int, ser.readline().split()))
                A[i] += (a / n)
                B[i] += (b / n)
    except:
        read(l, n)
f = 600000
tos = 10/100000
read(10000, 1)
dt = 1/f
l = 1000
file = open("staticerror.json", mode="r")
dat = json.load(file)
Ap = numpy.array(dat["mA"])
Bp = numpy.array(dat["mB"])
Anp = numpy.array(A)
Bnp = numpy.array(B)
#Anp -= Ap#Anp.min()
#Bnp -= Bp#Bnp.min()
A =Anp.tolist()
B = Bnp.tolist()
js = {
    "f": f,
    "dt":dt*100,
    "desc":"Статическая ошибка",
    "tos":100/1000000,
    "mA":A,
    "mB":B
}
plt.plot(js["mA"])
plt.plot(js["mB"])
plt.show()
file = open("staticerror.json", mode="w")
json.dump(js, file)
file.close()
