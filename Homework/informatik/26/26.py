import copy
import sys
from functools import *
import time

m = []
with open("26_2653.txt") as f:
    for i in f.readlines():
        m.append(int(i))



m.sort()
mx = sum(m)
mn = min(m)
res = []
black = set()
print(m)
for i in range(1, len(m)):
    s = sum(m[:i])
    if s < m[i]:
        for j in range(s+1, m[i]):
            black.add(j)
#print((mx-max(black))/max(m))
sm = set(m)
for i in range(14):
    bs = copy.copy(black)
    for i in bs:
        for j in sm:
            black.add(i + j)






#@lru_cache(maxsize=None)
def rucksack(a, massive, p):
    global m
    if sum(massive) < a:
            return 0
    ok = 1
    k = a
    for j in m:
        k-= j
        if k in black:
            ok = 0
            break
    if ok == 0:
        return 0
    #if a in black or a in res:
    #    return 0
    massive  =list(massive)
    sm = 0
    i = len(massive)-1
    while i >=0:
        if i == len(massive):
            i -=1
        if sm == a:
            return 1
        if sm > a:
            i -= 1
            continue
        massive.pop(i)
        if rucksack(a-sm, tuple(massive), p+1) == 1:
            return 1
        #i -= 1
    return 0
ind = 0
#print(rucksack(97251, tuple(m), 0))
#print(rucksack(32224, tuple(m)))
t1 = time.time()
#r = rucksack(2472084, tuple(m), 1)
t2 = time.time()
#print(r, (t2-t1)*10**6)#64738
#sys.exit()

while ind <= mx:
    if ind in black:
        res.append(ind)
        ind += 1
        #print(ind / mx, ind)
        continue
    if rucksack(ind, tuple(m), 0) == 0:
        res.append(ind)
    ind += 1
    print(ind/mx, ind)
print(len(res), max(res), res)