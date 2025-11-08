import json
from integral import *
import numpy as np
import matplotlib.pyplot as plt

file = open("Locator_experiment (8).")
data = json.load(file)
file.close()
freq = 10000
c = 343

tos = data['tos']
toe = len(data["mA"])*data["dt"]
dt = data["dt"]
h = len(data["mA"])/100
f = 1/data["dt"]




def furie_sample(data, toe, dt, freq = 10000, sampels = 100):
    furiea = []
    times = []
    f = 1/dt
    def func(time):
        return data[round(time * f)]

    def sinus(time):
        return math.sin(2 * math.pi * freq * time)

    def cosinus(time):
        return math.cos(2 * math.pi * freq * time)

    prev = 0
    for i in range(sampels - 1):
        st = (toe / sampels) * i
        end = st + toe / sampels
        time = st

        A = 0
        while time < end:
            A += log((func(time) * sinus(time)) ** 2 + (func(time) * cosinus(time)) ** 2 + 1)*time*c

            time += dt
        furiea.append(A-prev)
        prev = A
        times.append(st)
    return times, furiea
furieA = np.array(furie_sample(data["mA"], toe, dt, freq, sampels= 100))
furieB = np.array(furie_sample(data["mB"], toe, dt, freq, sampels= 100))
print(median(furieA[1]), dispersion(furieA[1])**0.5)
Da = 1.5*dispersion(furieA[1])**0.5
Db = 1.5*dispersion(furieB[1])**0.5
for i in range(len(furieA[1])):
    if furieA[1][i] < Da:
        furieA[1][i] = 0
    if furieB[1][i] < Db:
        furieB[1][i] = 0
furieA[1]/= furieA[1].max()
furieB[1]/= furieB[1].max()
file = open("Locator_experiment Furie.", mode = "w")
data ={
    "dt": (toe-tos)/len(furieA[1]),
    "l": 0.27,
    "tos": tos,
    "mA": list(furieA[1]),
    "mB": list(furieB[1]),
}
json.dump(data, file)
file.close()

pyplot.plot(furieA[0], furieA[1], furieB[0], furieB[1])
#pyplot.plot(furieB[0], furieB[1], color= (0, 1,0))
pyplot.show()





