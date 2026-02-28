from sys import *
from functools import *

setrecursionlimit(10**9)

@lru_cache(maxsize=10**9)
def f(n):
    if n >= 14000:
        return f(n-7) + 3*n
    else:
        return g(n-3) + 3*n

#@lru_cache(maxsize=None)
def g(n):
    if 80000-n < len(m) and n < 80000:
        return m[80000-n]
    if n < 80000:
        return 5*n + g(n+4)
    else:
        return 2*n+1
m = []
for i in range(80000, 1, -1):
    a = g(i)
    m.append(a)
    print(i)
for i in range(1, 49999):
    f(i)
    print(i)
print(f(50000))