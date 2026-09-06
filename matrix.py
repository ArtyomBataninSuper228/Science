
from numpy import *

a = matrix([[0, 1], [1,1]], dtype = 'float64')
b = matrix([[2, 2], [1 + 5**0.5, 1-5**0.5]], dtype = 'float64')
print(-4*5**0.5*b**-1)
print(a*b)
print((b**-1*(a*b)))