from math import *
from matplotlib import pyplot as plt

R = 10
I = 0.1
U = 0.1

#U 0.029, 0.057, 0.092


data = [
    ["Предел мА", "Iэксп", "dI", "R_A Ом", "I_p с учётом Ra", "I_p без учёта Ra"],
    [200,           7.2,      0.072+0.2,           4,          0,              U/R*1000],
    [20,            4.19,      0.0419 + 0.02,      13.6,          0,              U/R*1000],
    [2,             0.814,      0.08 + 0.0002,      113,          0,              U/R*1000],

]

for i in range(1, len(data)):
    line = data[i]
    line[4] = U/(line[3] + R)*1000


for line in data:
    for el in line:
        el2 = ""
        if type(el) == str:
            el2 = el
        else:
            el2 = str(round(el, 2))
        print(el2, end = " "*(16-len(el2)))
    print()