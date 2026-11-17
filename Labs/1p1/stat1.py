\usepackage{upgreek}\usepackage{upgreek}import os
import json
import matplotlib.pyplot as plt

from Labs.methods import *
from fnmatch import *


x = []
y = []
a = []

for i in os.listdir(os.getcwd()):

    if i[-3:] == "txt":
        if fnmatch(i, "*_n10.txt"):
            print(i)
            d = json.load(open(i))
            a.append((int(i.split("_")[1][1:].split(".")[0]), copy.copy(d), int(i.split("_")[0][2:])))
a.sort(key=lambda x: x[0])
for i in a:
    y.append(i[1]['accuracy:']/i[1]["mean"]*100)
    x.append(i[2])
    #print(i)



plt.errorbar(x, y, fmt = "o", label = "Неопределённость среднего (Эксперимент)")
plt.grid()
plt.xlabel("Время выборки (мс)")
plt.ylabel(r"Относительная ошибка %")

X  = []
Y = []
x_ = min(x)
dx_ = 1
k = y[-2]*sqrt(x[-2])
while x_ <= max(x):
    X.append(x_)
    Y.append(k/sqrt(x_))
    x_ += dx_
plt.plot(X, Y, label = r"Теоретическая кривая ($\frac{\sigma}{\sqrt{t}}$)")
plt.legend()
plt.savefig("Error_dt.png", dpi=600)
#plt.show()



