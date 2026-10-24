from matplotlib import pyplot as plt
from math import *
from scipy import stats
f =open("data","r")
x = []
y = []
pred = []
y_err = []
my = 0
def ln_U(ln_Uo, CR, t):
    return ln_Uo - t/CR
for line in f:
    X, Y  = map(float, line.split())
    my = max(my, Y)
    if X > 500:
        x.append(X)
        y.append(log(Y/my))
        y_err.append(log(Y + 1/sqrt(12)) - log(Y))

plt.errorbar(x, y, yerr = y_err, fmt = ".")
plt.ylabel("ln(U/U0)")
plt.xlabel("Время")
plt.show()

def f(CR):
    U0 = max(y) + min(x)/CR
    Xi_2 = 0
    X = []
    Y = []
    Y1 = []
    for i in range(len(y)):
        t = x[i]
        Xi_2 += (ln_U(max(y)+min(x)/CR, CR, t)-y[i])**2/(y_err[i])**2
        X.append(t)
        Y.append(y[i])
        Y1.append(ln_U(max(y)+min(x)/CR, CR, t))
    return Xi_2
Xi_2 = []
CR = []
cr = 10000
dcr = 0.1
while cr < 16000:
    cr += dcr
    CR.append(cr)
    Xi_2.append(f(cr))



dcr = 10**-3
def d_Xi_2(x): # Производная dXi_2/dCR
    return (f(x+dcr) - f(x-dcr))/(2*dcr)

def d2_Xi_2(x): # Производная d2Xi_2/dCR
    return (d_Xi_2(x+dcr) - d_Xi_2(x-dcr))/(2*dcr)

def d3_Xi_2(x): # Производная d2Xi_2/dCR
    return (d2_Xi_2(x+dcr) - d2_Xi_2(x-dcr))/(2*dcr)

#Находим 0 производной методом ньютона
x_min = 13000 # Начальное приближение
delta = 1000
prev_delta = 1000
dx = 10**-3# С какой точностью


plt.plot(CR, Xi_2)
plt.xlabel("CR")
plt.ylabel("Xi_2")
plt.show()
print(f"{len(x)} измерений")
print("Поиск минимума Xi_2 ")
while 1:
    prev_delta = delta
    delta = d_Xi_2(x_min)
    x_min += -delta*d2_Xi_2(x_min)/abs(delta*d2_Xi_2(x_min))*max(abs(delta*d2_Xi_2(x_min)/2), dx*100)
    if prev_delta < delta:
        break



# Площадь ПРАВЕЕ (p-value)
p_value = stats.chi2.sf(f(x_min), len(x)-1)

print(f"p-value: {p_value}")

print(f"Минимум функции: {x_min}, delta: {delta}, 1/d2: {1/d2_Xi_2(x_min)}, Xi_2: {f(x_min)}, стат неопределенность {sqrt(2/d2_Xi_2(x_min))}"
      f", систем неопр: {x_min*0.005}, p-value {p_value}")
print(x_min*10**11)
for i in range(len(x)):
    t = x[i]
    Y = ln_U(max(y)+min(x)/x_min, x_min, t)
    pred.append(Y)
plt.errorbar(x, y, yerr = y_err, fmt = ".")
plt.plot(x, pred)
plt.ylabel("ln(U)")
plt.xlabel("Время")
plt.show()