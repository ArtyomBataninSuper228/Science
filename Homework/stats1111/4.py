from matplotlib import pyplot
from Homework.methods import *
m0 = [19, 8, 7, 7, 3, 5, 1, 0]
m2 = [5, 10, 15, 20, 25, 30, 35, 40]
m = [] # записываем в список время опоздания для каждого ученика
for i in range(len(m0)):
    for k in range(m0[i]):
        m.append(m2[i])


pyplot.hist(m, bins = m2, density=True, edgecolor = 'black')
pyplot.show()

print(median(m), dispersion(m))