from numpy import *
import copy
from scipy import stats
from matplotlib import pyplot as plt
from math import *

def split_to_columns(M, n = 20):
    M = copy.copy(M)
    M.sort()# сортировка массива в порядок элементов по возрастанию
    colums = []
    for i in range(n):# заполняем массив нулями
        colums.append(0)
    mn = min(M)
    mx = max(M)
    step = (mx - mn)/n # определение ширины колонки
    i = 0
    num_colum = 0
    while i < len(M) and num_colum < n:
        if mn + step*num_colum <= M[i] and M[i] <= mn + step*(num_colum+1): # проверка входит ли элемент в промежуток
            colums[num_colum] += 1
            i += 1
        else:
            num_colum += 1 # переход к следующей колонке

    return colums
def normal_disp(x, m, sigma):
    return 1/((2*pi)**0.5 * sigma) * exp(-1/2*(((x-m))/sigma)**2)

def get_xi_square(columns,  f):
    res = 0
    for i in range(0, len(columns)):
        E = f(i)
        res += (columns[i] - E)**2/E
    return res

if __name__ == '__main__':

    a = array([1,2,3,4,5, 4, 3, 2, 1], dtype = float64)
    sigma = a.std()
    mn = min(a)
    mx = max(a)
    m = mean(a)
    m3 = stats.moment(a, 3)
    print(a)


    c = []
    for i in range(len(a)):
        c.append(normal_disp(mn + (mx - mn) * i / len(a), m, sigma))
    a /= len(a)
    xi = get_xi_square(a, lambda x: normal_disp(mn + (mx - mn) * x / len(a), m, sigma))
    xi2 = get_xi_square(c, lambda x: normal_disp(mn + (mx - mn) * x / len(a), m, sigma))

    print("mean:", m, "𝜎:", sigma, "central_moment_3:", m3, xi, xi2)
    plt.plot(c)
    plt.plot(a)
    #plt.show()
    n = 27000000  # Частота ПЛИС (27 МГц)
    f = 40000  # Частота звука (40 кГц)
    N = 40  # Число импульсов
    num_emitters = 8

    t_start = 0
    t_stop = int(n * (N / f))  # 27000 тактов

    # Упаковка 1 канала: [32 бита t_stop][32 бита t_start]
    channel_val = (t_stop << 32) | t_start

    # Сборка 512-битного вектора для 8 каналов
    times = 0
    for i in range(num_emitters):
        times |= channel_val << (i * 64)

    print("Dec:", times)
    print("bin", bin(times))
    print("Hex for Verilog:", f"512'h{times:0128x}")


