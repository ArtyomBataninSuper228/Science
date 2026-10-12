from math import *
from matplotlib import pyplot as plt


data = [
    ["Предел мА", "Iэксп", "dI", "R_A Ом", "I_p с учётом Ra", "I_p без учёта Ra"],
    [200,           7.2,      0.072+0.2,           0,          0,              0],
    [20,            4.19,      0.0419 + 0.02,      0,          0,              0],
    [2,             8.14,      0.08 + 0.0002,      0,          0,              0],

]


for line in data:
    for el in line:
        el2 = ""
        if type(el) == str:
            el2 = el
        else:
            el2 = str(round(el, 2))
        print(el2, end = " "*(16-len(el2)))
    print()