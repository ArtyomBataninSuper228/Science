import sounddevice as sd
import json
from matplotlib import pyplot as plt
import numpy as np
import soundfile as sf
import copy

d = open("simulation_output.txt")
data = json.loads(d.read())
d.close()
dt = data[1][1:-1]
da = data[0][1:-1]
da1 = da[::100]
da2 = copy.copy(da1)
for i in range(100):
    da2+=da1
da1 = np.array(da2, dtype=np.float32)
plt.plot(dt, da)
plt.show()

f = 1/(dt[1])
print(f/130000)
sd.play(da1, 200000)
sd.wait()
sf.write("sim.wav", da1, 130000)