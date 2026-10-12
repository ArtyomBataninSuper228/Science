import matplotlib.pyplot as plt
import numpy as np

from Simulation import *
import json


def main():
    DATA = []
    c = 343
    dt = 1/10000
    shape = (1000, 1000)
    sim = Simulation(shape, c=c, dt=dt)  # , device = torch.device("cpu"))
    sim.field[500][500] = 10
    for i in range(100):
        for j in range(100):
            if ((i - 50) ** 2 + (j - 50) ** 2) <= 50 ** 2:
                sim.field[i + 450][j + 450] = 10
    i = 0
    sim.set_max_dt()
    sim.toe = (500 - 50) / 343

    '''
    sim.update()
    x = []
    y = []
    for i in range(500, 1000):
        x.append(float(sim.field[i][500]))
        y.append(i)
    plt.plot(y, x)
    plt.show()


    '''
    while sim.T < sim.toe:
        DATA.append(float(sim.field[500][300]))
        sim.do_step()
    DATA = np.array(DATA)
    DATA -= DATA.min()
    DATA /= DATA.max()
    DATA.astype(np.float32).tofile("data.bin")
    plt.plot(DATA)
    plt.show()
    print(sim.dt)
if __name__ == '__main__':
    main()


