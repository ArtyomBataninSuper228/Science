import serial
from matplotlib import pyplot as plt
import json

f = open("data2.txt")
data = json.load(f)
f.close()
plt.plot(data[2], data[1])
plt.show()