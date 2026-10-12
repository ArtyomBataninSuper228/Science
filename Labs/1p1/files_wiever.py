import matplotlib.pyplot as plt

from Labs.methods import *
import integral
import os
import json


def process(name):
    f = open(name + ".dat")
    M = []
    length = (int(name.split("_")[0][2:].split(".")[0]))
    N = 2000
    for line in f:
        M.append(int(line))
    n = max((5, int((len(M) ** 0.5) + 1)))
    print(n, int((len(M) ** 0.5) + 1))
    M = array(M)
    sigma = M.std()
    m = M.mean()
    mn = min(M)
    mx = max(M)
    columns = split_to_columns(M, n)
    columns = array(columns, dtype=float64)
    columns /= (len(M)) * (mx - mn) / n
    xi = get_xi_square(columns, lambda x: normal_disp(mn + (mx - mn) * x / n, m, sigma))

    f = open(name + ".txt", mode="w")
    staticerror = 1/(12**0.5)/length
    print(staticerror)
    f.write(json.dumps({"mean": M.mean(), "𝜎": M.std(), "central_moment_3": stats.moment(M, 3) / sigma ** 3, "accuracy:":
          sigma / sqrt(len(M)) + staticerror, "xi^2": xi}))

    f.close()
    dx = []

    for i in range(n):
        dx.append((mn + (mx - mn) / n * i))
    plt.bar(dx, columns, (mx - mn) // n+1)
    print()
    dy = []

    # print(integral.integral(1000, 3000, 1/100, lambda x: normal_disp(x, m, sigma)))
    # print(sum(columns))
    # stats.norm.pdf(dx, loc=mn, scale=sigma)

    dx = []
    for i in range(N):
        dx.append((mn + (mx - mn) / N * i))
    for i in range(N):
        dy.append(normal_disp(((mx - mn) / N * i + mn), m, sigma))
    if name == "dt10_n1000":
        print(columns)

    plt.plot(dx, dy, color='red')
    plt.savefig(name + ".png", dpi=350)
    plt.close()




for i in os.listdir(os.getcwd()):
    print(i)
    if i[-3:] == "dat" and i == "dt10_n1000.dat":
        process(i[:-4])
