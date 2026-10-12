import fnmatch

from Labs.methods import *
import os
import json

f = open("dt500_n2000.txt").readline()
print(f)
d = json.loads(f)


Nmax = d["mean"] + d["accuracy:"]
Nmin = d["mean"] - d["accuracy:"]

def m(N):
    T = 24110 * 360*24*60*60
    k = log(2, e)/T
    Na = 6.67*20**23
    dm = N*239/Na
    m = N*239/Na*log(2, e) * T
    return m*1000
print(m(Nmax), m(Nmin), (m(Nmax)-m(Nmin))*10**11)

