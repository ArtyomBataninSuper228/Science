import matplotlib.pyplot as plt

from integral import *
from scipy.io import wavfile
import os
m_t = []
m_d = {}
dir = "/Users/artembatanin/PycharmProjects/Science/Labs/Coffee/ryad/1"
samplerate = 0
for i in os.listdir(dir):
    print(i)
    if i[-4:] == ".txt":
        m_t.append([int(i.split(".")[0]), float(open(os.path.join(dir, i)).read())])
    if i[-4:] == ".wav":
        file = wavfile.read(os.path.join(dir, i))
        m_d[int(i.split(".")[0])] = file[1]
        samplerate = file[0]
m_t.sort(key = lambda x: x[1])
print(m_t)
hlops = []
print(samplerate)
for hlop in m_t:
    hlops.append([hlop[1], m_d[hlop[0]]])

F = []
t = []
i = 0
for hlop in hlops:
    mf, ma, s, c = fourie_torch(torch.tensor(hlop[1].astype("float64")), 1/samplerate, max_f= 5000)
    #plt.plot(mf, ma)
    #plt.show()
    f = 0
    n = 0
    for j in range(len(mf)):
        if (ma[j] > ma.sum()/len(ma)*1.4 and mf[j] != 0):
            f += mf[j]
            n += 1
    #plt.figure(i+1)
    #plt.plot(mf, ma)
    F.append(f/n)
    t.append(hlop[0])
    i += 1
plt.plot(t, F)
plt.show()