

for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count("1")%2 == 0:
        s = '10'+s[2:]+'0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if n ==6 or n == 4:
        print(r)
    if r%2 == 0 and r > 367 and n%2 == 1:
        print(n)
        break