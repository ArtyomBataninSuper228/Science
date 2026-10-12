import matplotlib.pyplot as plt

from Labs.methods import *

f = open("first.dat")
data = f.read()
data = data.replace(",", ".")



x = []
y = []
for line in data.split("\n"):
    if line == "":
        continue
    a, b = map(float, line.split())
    x.append(a)
    y.append(b)
plt.plot(x, y)
plt.xlabel("Время (сек)")
plt.ylabel("Напряжение (В)")
plt.show()

f = open("characteristics.txt")
t = []
u = []
for line in f.readlines():
    a, b = map(float, line.split())
    t.append(a)
    u.append(b)
du = []
for i in range(len(u) - 1):
    du.append(10/(u[i+1] - u[i]))
du.append(du[-1])

def binary_search(m, a):
    st = 0
    end = len(m) -1
    if a > m[-1]:
        return end
    if a <= m[0]:
        return 0
    while st < end:
        if m[(st + end)//2] < a:
            st = (st+end)//2 +1
        else:
            end = (end+st)//2
    return st
print(binary_search(u, 0.0001), u[17])

def get_temp(U):
    i = binary_search(u, U*1000)-1
    d = U*1000 - u[i]
    T = t[i]  + d*du[i]
    return T, d
T = []
k = 0
for i in y:
    T.append(get_temp(i)[0])
    k += 1
plt.plot(x, T)
plt.xlabel("Время (сек)")
plt.ylabel("Температура (°C)")
plt.show()



N = 8
n = 200
temp_pl = []
for i in T:
    if  210 < i < 212:
        temp_pl.append(i)
temp_pl = array(temp_pl)
mn = mean(temp_pl)
sigma = temp_pl.std()
print(mn, sigma)
columns = split_to_columns(temp_pl, N)
vals = []
m = temp_pl.min()
mx = temp_pl.max()
for i in range(N):
    vals.append(m + (mx-m)/N*i)
approx = []
x = []
for i in range(n):
    approx.append(normal_disp(m + (mx-m)/n*i, mn, sigma)*len(temp_pl)/N*(mx-m))
    x.append(m + (mx-m)/n*i)


plt.bar(vals, columns, width=(mx-m)/N*0.8, align='center')
plt.plot(x, approx, color = "red")
plt.xlabel("Температура (°C)")
plt.ylabel("Кол-во выборок")
print(t.index(210), du[21])
#plt.show()