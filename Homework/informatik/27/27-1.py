from matplotlib import pyplot as plt
from sys import *
def dist(a, b):
    return (((a[0] - b[0]) ** 2) + (a[1] - b[1]) ** 2)**0.5
setrecursionlimit(10**8)

def do_cls(m, cls, star):
    cls.append(star)
    i = 0
    while i < len(m):
        dot = m[i]
        if dot[0] - star[0] > 1:
            break
        if dist(dot, star) < 1:
            m.pop(i)
            do_cls(m, cls, dot)

        else:
            i += 1

def split_to_cls(m):
    clusters = []
    i = 0
    while i < len(m):
        dot = m[i]
        m.pop(i)
        cluster = []
        do_cls(m, cluster, dot)
        clusters.append(cluster)
    return clusters


ma = []
with open('27B_18678.txt') as f:
    for i in f.readlines():
        ma.append(list(map(float, i.replace(",", ".").split())))
ma.sort()




clusters = split_to_cls(ma)
#print(clusters)
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