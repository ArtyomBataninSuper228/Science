

f = open("17-4.txt")

m = []

for line in f:
    m.append(int(line))
f.close()

num = len([x for x in m if abs(x)%3 == 0])
res = []
for i in range(num-1):
    a = m[i]
    b = m[i+1]
    if ((a<0 and b%2 == 0) or (a%2 == 0 and b< 0)) and a+b > num:
        res.append(a+b)
print(len(res), max(res))