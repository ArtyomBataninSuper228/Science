
def f(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        raise ZeroDivisionError
    x1  = (-b + D) / (2*a)
    x2 = (-b - D) / (2*a)
    return x1, x2



a = []
b = []
for i in range(0, 200):
    a.append(6 + 48*i)
    b.append(616 + 17.5*i)
for i in b:
    if i in a:
        print(i)
print(966//60, 966%60)