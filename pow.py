from math import *
def get_pascal_triangle_layer(n):
    prev = [1]
    for i in range(1, n):
        new = []
        for k in range(0, i+1):
            sm = 0
            if k - 1 > -1:
                sm += prev[k-1]
            if k<len(prev):
                sm += prev[k]
            new.append(sm)
        prev = new
    return prev
print(get_pascal_triangle_layer(10))

def pow(c,  step:(int)):
    if step == 0:
        return 1
    k = 0
    koeff = get_pascal_triangle_layer(step+1)
    res = 0
    a = c.real
    b = c.imag
    while k <= step:
        res += koeff[k]*a**(step-k)*(b*1j)**k
        k += 1
    return res

def pow2(c, step:(int)):
    if step == 0:
        return 1
    a = c.real
    b = c.imag
    r = (a**2+b**2)**0.5
    sina = a/r
    cosa = b/r
    ang = atan2(sina, cosa)
    res = r**step*(cos(ang*step)+1J*sin(ang*step))
    return res

num = 8+8j
step = 5
print(f"Алгебраическая {pow(num,step)} Показательная {pow2(num,step)} Встроенная {num**step}")




