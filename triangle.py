a, b, c = map(complex, input().split())

d1 = (a-b)+c
d2 = (b-a)+c
d3 = (a-c)+b
d4 = (c-a)+b
d5 = (b-c)+a
d6 = (c-b)+a
print(d1, d2, d3, d4, d5, d6)
