def f(x, y, m):
    #print(x+ y, m)
    if x+y >= 154:
        return m%2 == 0
    if m == 0:
        return 0
    h = [f(x+1, y, m-1), f(x*2, y, m-1), f(x, y+1, m-1), f(x, y*3, m-1)]
    #print(h, x+y)
    #print(h, any(h), all(h), m)
    return any(h) if m%2== 1 else all(h)
#print(f(5, 50, 1))
#print([x for x in range(1, 131) if f(5, x, 2) == 1])#17
print([x for x in range(1, 131) if  f(5, x, 3) == 1])#49 50
print([x for x in range(1, 131) if f(5, x, 2) == 0 and f(5, x, 4) == 1])#48