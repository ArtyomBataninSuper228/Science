
def f(s):
    for i in range(3):
        s *= 1.2
        s -= 1
        #print(s)
    return s
def f2(s):
    for i in range(2):
        s *= 1.24
        s -= 1
    return s
#6/5*(6/5*s-x)-x=5/6x
#6/5*(6/5*S-x)= 5/6 + 1
s   = 3
for i in range(100):
    r = f(s)
    #print(r)
    if f(s) >0:
        s-= abs(r)/2
    else:
        s += abs(r)/2
print(s)
s1 = 5/6*(5/6*(5/6 +1)+1)
s2 = 25/31*(25/31 + 1)
print(s1, s2)
print(f2(s2))
w1 = 1/s1*3
w2 = 1/s2*2
print(w1, w2)
print((s2-s1)*373600)