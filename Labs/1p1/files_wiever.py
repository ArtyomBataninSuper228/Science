import matplotlib.pyplot as plt
from scipy import stats as stats2
from Labs.methods import *
import os
import json


def process(name):
    f = open(name + ".dat")
    M = []
    length = (int(name.split("_")[0][2:].split(".")[0]))
    N = 2000
    for line in f:
        M.append(int(line))
    n =  max((5, round((len(M) ** 0.5))))
    dX = max((1, round((max(M)-min(M))/n)))
    n = ceil((max(M)-min(M))/dX)



    M = array(M)
    sigma = M.std()
    m = M.mean()
    mn = min(M)
    mx = max(M)
    columns = split_to_columns(M, n, dX)
    print(columns, len(columns), n)
    #columns = array(columns, dtype=int32)
    if max(m) < 30:
        f = lambda x: ((len(M)) * (mx - mn) / n)*poison(int(mn + dX*x), m)
    else :
        f = lambda x: ((len(M)) * (mx - mn) / n)*normal_disp(int(mn + dX*x), m, m**0.5)
    xi = get_xi_square(columns, f)

    f = open(name + ".txt", mode="w")
    f.write(json.dumps({"mean": M.mean(), "𝜎": M.std(), "central_moment_3": stats.moment(M, 3) / sigma ** 3, "accuracy:":
          sigma / sqrt(len(M)), "xi^2": xi, "Bins:": float(n), "p-value": float(stats.chi2.sf(xi, n-1))}))

    f.close()

    dx = []

    for i in range(n):
        dx.append(int(round(mn + dX * i)))
    print(len(dx), dx)
    maxx = max(dx)
    plt.bar(dx, columns, dX*0.8)

    dp = []
    if max(M) < 50:
        for i in range(n):
            dp.append(((len(M)) * (mx - mn) / n) * poison_2(mn+dX*i, m))
        plt.plot(dx, dp, color='orange', marker='.')

    dy = []



    # print(integral.integral(1000, 3000, 1/100, lambda x: normal_disp(x, m, sigma)))
    # print(sum(columns))
    # stats.norm.pdf(dx, loc=mn, scale=sigma)

    dx = []
    for i in range(N):
        dx.append((mn + (mx - mn) / N * i))
    for i in range(N):
        dy.append(((len(M)) * (mx - mn) / n)*normal_disp(((mx - mn) / N * i + mn), m, m**0.5))


    plt.plot(dx, dy, color='red')

    plt.xlim(min(dx) - ((mx - mn) / (n))*1.6, maxx + ((mx - mn)) / (n)*0.8)
    plt.xlabel(f"Кол-во зарегестрированных распадов (Ширина бина: {int(dX)})")
    plt.ylabel("Кол-во измерений")
    if max(M) < 50:
        plt.legend([  "Распр. Пуассона", "Норм. распр", "Эксп."])
    else:
        plt.legend(["Норм. распр", "Эксп."])

    plt.grid()
    plt.savefig(name + ".png", dpi=600)
    plt.close()
    print(name, n, dX * 0.8)
    print()
    print()




for i in os.listdir(os.getcwd()):
    #print(i)
    if i[-3:] == "dat": #and i == "dt1000_n200_no_Pu.dat":
        process(i[:-4])
