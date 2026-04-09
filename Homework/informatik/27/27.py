from sys import *
from matplotlib import pyplot as plt

setrecursionlimit(10**8)


ma = []
with open('27B_18678.txt') as f:
    for i in f.readlines():
        ma.append(list(map(float, i.replace(",", ".").split())))
ma.sort()


def dist(d1, d2):
    return ((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)**0.5


def do_cls(m, cls, star):
    cls.append(star)
    i = 0
    while i < len(m):
        dot = m[i]
        if dot[0]-star[0] >= 1:
            break
        if dist(dot, star) <= 1:
            m.pop(i)
            do_cls(m, cls, dot)
        else:
            i += 1


def split_to_clusters(m):
    clusters = []
    i = 0
    while i < len(m):
        star = m[i]
        m.pop(i)
        cluster = []
        do_cls(m, cluster, star)
        clusters.append(cluster)
    return clusters

clusters = split_to_clusters(ma)
print(len(clusters))


colors = ['cyan', 'blue', 'red', 'green', 'yellow', 'magenta']
for i in range(len(clusters)):
    color = colors[i%6]
    cluster = clusters[i]
    x = []
    y = []
    for d in cluster:
        x.append(d[0])
        y.append(d[1])
    plt.scatter(x, y, color=color)
plt.show()

