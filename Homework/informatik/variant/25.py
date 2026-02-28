

def isi_dels(x):
    res = []
    for i in range(2, int(x**0.5) + 1):
        if x%i==0:
            res.append(i)
            for j in isi_dels(x//i):
                res.append(j)
            return res
    return[x]
print(isi_dels(3103))
k = 0
for n in range(2142577, 21425770):
    d = isi_dels(n)
    if len(d) == 2 and sum(d) %2 == 1:
        print(n, max(d))
        k += 1
        if k == 5:
            break