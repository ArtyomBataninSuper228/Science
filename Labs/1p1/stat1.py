import os
import json
import matplotlib.pyplot as plt

from Labs.methods import *
from fnmatch import *


x = []
y = []
a = []

for i in os.listdir(os.getcwd()):

    if i[-3:] == "txt":
        if fnmatch(i, "dt10_n*.txt"):
            print(i)
            d = json.load(open(i))
            a.append((int(i.split("_")[1][1:].split(".")[0]), copy.copy(d)))
a.sort(key=lambda x: x[0])
for i in a:
    print(i)

    y.append(i[1]['accuracy:']/i[1]["mean"])
    x.append(i[0])

plt.plot(x, y)
plt.xlabel("кол-во выборок")
plt.ylabel("sigma/sqrt(n)/mean(x)")
plt.savefig("Error_n.png")
plt.show()

