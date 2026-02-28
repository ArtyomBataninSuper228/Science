

for x in range(21):
    a = int("EF067", 21) + int("3H04C", 21) + 2*x*21**2
    if a%20 == 0:
        print(x, a//7)