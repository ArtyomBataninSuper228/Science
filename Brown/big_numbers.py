from matplotlib import pyplot

randomfile = open("/dev/random", "rb")


def generate_random(min= 0, max = 10000):
    res = list(randomfile.read(10))
    bn = ""
    for i in range(10):
        bn += bin(res[i])[2:].zfill(8)
    num = int(bn,2)
    return num%(max-min) + min


m1 = []
m2 = []
m3 = []
N = 10000
for i in range(N):
    m1.append(generate_random(0, 100))
    m2.append(i)
    m3.append(sum(m1)/(i+1))
pyplot.plot(m2,m3)
pyplot.xlabel("Количесвто испытаний")
pyplot.ylabel("Среднее")
pyplot.show()