#import torch
import time
import sys
import numpy as np
import copy

x = [[5], [-2], [1]]
y = [[-1], [7], [1]]
z = [[0], [1], [-2]]
w = [[1], [1], [1]]

a = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     ]

a = np.matrix(a)
a[:, 0] = x
a[:, 1] = y
a[:, 2] = z
print(a)
d = np.linalg.det(a)



ax = copy.copy(a)
ax[:, 0] = w
dx = np.linalg.det(ax)

ay = copy.copy(a)
ay[:, 1] = w
dy = np.linalg.det(ay)

az = copy.copy(a)
az[:, 1] = w
dz = np.linalg.det(az)


print(dx/d, dy/d, dz/d, d)
x = dx/d
y = dy/d
z = dz/d
print(12*x-15*y-7*z)