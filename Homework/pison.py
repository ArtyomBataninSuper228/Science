from methods import *
from matplotlib import pyplot as plt
import numpy as np

l = 6# 6 посетителей за 30 минут в среднем
m = []
for line in range(10):#10 подходов
    m.append([])
    print()
    for col in range(4):#4 раза по пол часа в 2х часах
        print(np.random.poisson(l), end=" ")
        m[-1].append(np.random.poisson(l))