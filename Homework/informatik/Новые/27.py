from matplotlib import pyplot as plt
m = []
with open("27B_27780.txt") as f:
    for line in f.readlines():
        m.append(list(map(float, line.replace(",", ".").split())))

clusters = []
f = lambda x: x[0]
m.sort(key=f)

def distance(point1, point2):
    r = 0
    for i in range(len(point1)):
        r += (point1[i] - point2[i]) ** 2
    return r**0.5

def get_stars(star, m):
    res = []
    i = 0
    while i < len(m):
        s = m[i]
        if s[0] - star[0] > 1:
            break
        if distance(s, star) < 1:
            res.append(s)
            m.pop(i)
            for j in get_stars(s, m):
                res.append(j)
        else:
            i+= 1
    return res

def split_to_clusters():
    i = 0
    while i < len(m):
        star = m[i]
        m.pop(i)
        cluster = [star]
        for j in get_stars(star, m):
            cluster.append(j)
        clusters.append(cluster)
split_to_clusters()

summa = 0
for cluster in clusters:
    center = []
    ln = float("inf")
    for star in cluster:
        s = 0
        for st in cluster:
            s += distance(star, st)
        if s < ln:
            center = star
            ln = s
    min_distanse = float("inf")
    num =0

    for star in cluster:
        d = distance(star, center)
        if d == 0:
            continue
        if d <= 1.2:
            num += 1
        if d< min_distanse:
            min_distanse = d

    print(center, len(cluster), min_distanse*10000, num   )
    summa += distance([1.0, 1.5], center)*10000
print(summa)



#A:
#344
#294354

#B:
#152
#528