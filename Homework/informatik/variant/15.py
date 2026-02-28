

for a in range(1, 1000):
    fl = 1
    for x in range(1, 1000):
        f = (x%56== 0)<= ((not(x%a == 0)) <= (not(x%120 == 0)))
        if f == 0:
            fl = 0
            break
    if fl:
        print(a)