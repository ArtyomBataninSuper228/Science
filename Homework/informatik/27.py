from math import *
import copy
from matplotlib import pyplot as plt
def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

data = []
f = open("27B_18630.txt")
for line in f:
    data.append(list(map(float,line.replace(",", ".").split())))
f.close()
def f(el):
    return el[0]
data.sort(key=f)

clusters = []
clusters_maxmin = []

for dt in data:
    data.remove(dt)
    clusters.append([dt])
    clusters_maxmin.append([dt])
    maxmin = clusters_maxmin[-1]
    maxmin.append(dt)
    cluster = clusters[-1]
    i = 0
    cop = copy.copy(data)
    def add(dot, f):
        if (dot[0] > maxmin[0][0] and dot[0] < maxmin[1][0] and dot[1] > maxmin[0][1] and dot[1] < maxmin[1][1]): # проверка по границам кластера
            cluster.append(dot)
            data.remove(dot)
            cop.remove(dot)
            return 1
        if dot[0] - maxmin[1][0] > 1:# если далеко за границей
            return -1
        if f == 0:
            if dist(dot, cluster[-1]) < 1:# если проверяем предыдущие
                cluster.append(dot)
                data.remove(dot)
                cop.remove(dot)

                # i = 0
                if dot[0] < maxmin[0][0]:
                    maxmin[0][0] = dot[0]
                if dot[0] > maxmin[1][0]:
                    maxmin[1][0] = dot[0]
                if dot[1] < maxmin[0][1]:
                    maxmin[0][1] = dot[1]
                if dot[1] > maxmin[1][1]:
                    maxmin[1][1] = dot[1]
                return 1
            else:
                return 0


        for cl_dot in cluster:## проверяем по расстояниям

            if dist(cl_dot, dot) <= 1:
                cluster.append(dot)
                data.remove(dot)
                cop.remove(dot)

                #i = 0
                if dot[0] < maxmin[0][0]:
                    maxmin[0][0] = dot[0]
                if dot[0] > maxmin[1][0]:
                    maxmin[1][0] = dot[0]
                if dot[1] < maxmin[0][1] :
                    maxmin[0][1] = dot[1]
                if dot[1] > maxmin[1][1]:
                    maxmin[1][1] = dot[1]
                return 1
                #break
        return 0
    def seek(mx, f):
        global cop
        cop = copy.copy(data)
        i = 0
        while i < len(cop) and i < mx:
            a = add(cop[i], f)
            if a < 0:# далеко
                break
            if a > 0:
                seek(i, 0)#нашли
            else:# проверяем предыдущие отброшенные если нашли новую точку
                i += 1
    seek(len(data), 1)

    



colors = ["red", "green", "blue", "black", "yellow", "purple", "cyan", "magenta"]
centers = []
for i in range(len(clusters)):
    cluster = clusters[i]
    if len(cluster) < 30:
        continue
    print("cluster", len(cluster))
    x = []
    y = []
    srx = 0
    sry = 0
    for dot in cluster:
        x.append(dot[0])
        y.append(dot[1])
        srx += dot[0]
        sry += dot[1]
    srx /= len(cluster)
    sry /= len(cluster)
    plt.scatter(x, y, color=colors[i % 7], marker='o')
    mn = float("inf")
    d = None
    for j in cluster:
        ds = 0#dist((srx, sry), j)
        for dot in cluster:
            ds += dist(j, dot)
        if ds< mn:
            mn = ds
            d = j
    plt.scatter([d[0]], d[1], color="cyan", marker='o')
    centers.append(d)
x = 0
y = 0
for i in centers:
    x += i[0]
    y += i[1]
x /= len(centers)
y /= len(centers)
print(x*100000, y*100000)





plt.show()


'''
A:
285843.0150081365 92124.68991100442
402077.0252344673 360358.4553648382
B:
61448.117015069 313725.84659321746
487471.1693152832 424667.7439855832
808843.9774672112 474617.51928845973

'''
