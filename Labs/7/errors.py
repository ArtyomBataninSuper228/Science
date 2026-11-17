u = 4.68
r = 10**6
dt = 20*10**-3
p = u**2/r
dE = dt*p
print(dE)
m = 0.01
l = 0.33
T = 0.093
V = l/T
E = m*V**2/2
print(dE/E, E)