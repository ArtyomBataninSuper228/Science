import matplotlib.pyplot as plt
import sounddevice as sd
import torch
from scipy.io import wavfile
from integral import *
import os

samplerate, data = wavfile.read('/Users/artembatanin/PycharmProjects/Science/Labs/Coffee/Coffe.wav')
data = torch.Tensor(data)
ddata = data - torch.roll(data, 1, 0)


mt = numpy.zeros(shape = (len(data)), dtype=numpy.float32)
for i in range(len(data)):
    mt[i] = i/samplerate
Porog = 500 # Порог срабатывания на хлопок
T_O_H = 0.25 # Время хлопка
TOH_i = T_O_H*samplerate

hlops = []

i = 0
while i < len(ddata):
    if ddata[i] >= Porog:
        hlops.append([i/samplerate, torch.slice_copy(data, 0, i+1, int(i+TOH_i+1))])
        i += int(TOH_i)
        continue
    i += 1

print(len(hlops))
for i in range(len(hlops)):
    hlops[i][1] = hlops[i][1]/hlops[i][1].max()

ryads = []
i = 0
while i < len(hlops)-1:
    ryads.append([])
    ryads[-1].append(hlops[i])
    while i < len(hlops)-1:
        if hlops[i+1][0] - hlops[i][0] <= 1.5:
            ryads[-1].append(hlops[i])
            i += 1
        else:
            break

    i+= 1

mx = 0
top = None
for i in ryads:
    if len(i) > mx:
        mx = len(i)
        top = copy.copy(i)

i = 0
for ryad in ryads:
    if len(ryad) < 6:
        continue
    os.mkdir(f"/Users/artembatanin/PycharmProjects/Science/Labs/Coffee/ryad/{i}")
    j = 0
    for hlop in ryad:
        sd.play(hlop[1], samplerate=samplerate)
        f = open(f"/Users/artembatanin/PycharmProjects/Science/Labs/Coffee/ryad/{i}/{j}.wav", "wb")
        soundfile.write(f, hlop[1], samplerate=samplerate)
        f.close()
        f = open(f"/Users/artembatanin/PycharmProjects/Science/Labs/Coffee/ryad/{i}/{j}.txt", "w")
        f.write(str(hlop[0]))
        j+=1
    i += 1


