import random
from integral import *
from matplotlib import pyplot as plt
import rawpy
import numpy as np
m = []
base = 0

for i in range(5456*3632):
    k = random.randint(-2, 2)+ random.randint(-4, 4)+ random.randint(-6, 6)
    res = base+k
    if res <0:
        res = 0
    m.append(res)
a, b = get_distribution(m)

k = np.ndarray((3, 2, 7))
print(k.shape)

 # Импортируем библиотеку rawpy

raw_filename = 'DSC03411.ARW'  # Указываем путь к файлу
with rawpy.imread(raw_filename) as raw:  # Открываем файл и получаем объект raw
    #print(raw.raw_type)  # Выводим тип данных (плоский или стопка)
    #print(raw.num_colors)  # Указываем количество цветовых компонентов
    #print(raw.color_desc)  # Описываем описание цветов
    #print(raw.raw_pattern.tolist())  # Выводим шаблон сенсора
    #print(raw.black_level_per_channel)  # Указываем коррекцию чёрного уровня
    #print(raw.white_level)  # Указываем уровень белого камеры
    #print(raw.color_matrix.tolist())
    rgb = raw.postprocess()
    m2 = []
    for x in rgb:
        for y in x:
            m2.append(y[1])
    print(1)
    c, d = get_distribution(m2)

    print(2)
    plot = plt.plot(a, b, c, d)
    plt.show()
    print(m2)
print(m2[26])



