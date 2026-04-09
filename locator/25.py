import time
import random

def f(x): ### Рекурсивная функция
    if x == 1:
         return []
    for i in range(2, int(x**0.5+1)):
        if x%i == 0:
            res = [i]
            for j  in f(x//i):
                res.append(j)
            return res
    return [x]

def f2(x):
    r = []
    d = 2
    while d <= x **0.5:
        while x%d == 0:
            r.append(d)
            x//= d
        d += 1
    if x > 1:
        r.append(x)
    return r


r = []
for i in range(1000):
    r.append(random.randint(100000, 10**12))

t1 = time.time()
for i in r:
    f2(i)
t2 = time.time()
f2_t = t2 - t1
print("Обычная:", t2-t1)

t1 = time.time()
for i in r:
    f(i)
t2 = time.time()
f_t = t2 - t1
print("Рекурсивная:", t2-t1)
print("Разница раз:",  f2_t/f_t)

