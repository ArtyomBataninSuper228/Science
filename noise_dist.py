import random
from integral import *
from matplotlib import pyplot as plt
import rawpy
import numpy as np
m = []
base = 0


def open_row_photo(filename):
    return rawpy.imread(filename).postprocess()

for i in range(545*3632):
    k = random.randint(0, 1)+ random.randint(0, 2)+ random.randint(-1, 3) + random.randint(-2, 4)
    res = base+k
    if random.random() < 0.6:
        res -= k
    if res <0:
        res = 0
    m.append(res)
a, b = get_distribution(m)
a.pop(0)
b.pop(0)

 # Импортируем библиотеку rawpy
print(1)
rgb = open_row_photo("20250602_161531.dng")
print(2)
m2 = []
for x in rgb:
    for y in x:
        m2.append(int(y[0]) + int(y[1]) + int(y[2]))

c, d = get_distribution(m2)
c.pop(0)
d.pop(0)
print(list(map(int, c)))
print(d)


plot = plt.plot( c, d)
plt.show()



