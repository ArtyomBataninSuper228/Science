

for x in range(32):
    a = int("54045", 32) + int("960", 32) + int("1201", 32) + x*32**2 + x + x*32
    if a%8== 0:
        print((bin(a)[2:]).count("1"))