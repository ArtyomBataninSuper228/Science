import time
import sounddevice as sd
from matplotlib import pyplot as plt

to_play = []
dt = 1/1000
t = 0.2
f = 40000
pos = 1
T = 0
while T < t:
    to_play.append(float(T%dt < dt/2)*4)
    T+= 1/f

sd.play(to_play, f)
sd.wait()
tos = time.time()
last = tos
while 1:
    if time.time() - last > 60:
        last = time.time()
        sd.play(to_play, f)
        sd.wait()

    time.sleep(1)
    print(time.time()-tos)
