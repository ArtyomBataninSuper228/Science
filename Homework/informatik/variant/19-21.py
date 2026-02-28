

def f(x, y, m):
    if x+y >= 841:
        return m%2==0
    if m == 0:
        return 0
    h = [f(x+20, y, m-1), f(x*3, y, m-1), f(x, y+20, m-1), f(x, y*3, m-1)]
    return any(h) if m%2 == 1 else all(h)

print([x for x in range(1, 805) if f(36, x, 1)==0 and f(36, x, 2)==1])
print([x for x in range(1, 805) if f(36, x, 1)==0 and f(36, x, 3)==1])
print([x for x in range(1, 805) if f(36, x, 2)==0 and f(36, x, 4)==1])