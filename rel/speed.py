from matplotlib import pyplot as plt

V = 0.001
T = 0
c = 3*10**8
a = 100
dt = 10**(0)
v = []
t = []
m = 1
Pp = 0
f = []

while V < 0.9*c:
    E = (m*c**2/(1-(V/c)**2)**0.5)
    V += a*dt*(1-(V/c)**2)**(3/2)
    P = m*V/(1-(V/c)**2)**0.5
    F = (P-Pp)/dt*m
    Pp = P
    T += dt
    f.append(F)
    v.append(V)
    t.append(T)

plt.plot(t, f)
plt.show()
