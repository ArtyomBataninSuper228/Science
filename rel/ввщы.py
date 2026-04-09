import copy

import numpy as np
from itertools import *
V0 = 490
vx = V0/(3**0.5)
vy = V0/(3**0.5)
vz = V0/(3**0.5)
vect = np.array([vx, vy, vz])
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def get_len(x):
    l = 0
    for i in x:
        if is_iterable(i):
            l += get_len(i) ** 2
        else:
            l += i ** 2
    return l**0.5
V = 20
S = 2
P0 = 10**5

v1 = copy.copy(vect)
v1[0] += V
F0 = S * P0
F = S * P0*get_len(v1)**2/get_len(vect)**2
print(F-F0)

