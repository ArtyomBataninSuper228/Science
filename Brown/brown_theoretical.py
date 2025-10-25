from bisect import insort_right
from matplotlib import pyplot
import json
from integral import *
#from brown_distance import sigmas
mxt = []
mpt = []
file = open("sigmas.json", "r")
sigmas = json.load(file)
file.close()
x = 0.0001
dx = 1/1000
#sigma = 0.08840690030781344
while x <= 1:
    mxt.append(x)
    r1 = 1-x
    r2 = x
    def f(t):
        x = r1
        if t > 0 and t < 10:
            sigma = 10*sigmas[round(t * 100)-1]
        elif t > 10:
            sigma = t
        else:
            sigma = 0
        return 1/(sqrt(2*pi)*sigma)*(e)**(-0.5*(x/sigma)**2)
    a = integral(0.01, 100, 1/100, f)
    def f(t):
        x = r2
        if t > 0 and t < 10:
            sigma = 10 * sigmas[round(t * 100) - 1]
        elif t > 10:
            sigma = t
        else:
            sigma = 0
        return 1/(sqrt(2*pi)*sigma)*(e)**(-0.5*(x/sigma)**2)
    b = integral(0.01, 100, 1/100, f)
    k = a/b
    q = 1/(1+k)
    p = 1-q
    mpt.append(p)
    x += dx
pyplot.plot(mxt, mpt)
pyplot.xlabel("X")
pyplot.ylabel("P")
pyplot.show()
file = open("theory.json", "w")
file.write(json.dumps({"mpt":mpt, "mxt":mxt}))
file.close()

