from matplotlib import pyplot as plt
f = open("logic-1-1", mode = "rb")
a = []
BIT_REVERSE_TABLE = bytes(
    int(f"{i:08b}"[::-1], 2) for i in range(256)
)
data = f.read()
for i in range(0,len(data)//1, 2):
    a.append(int(data[i], ))

plt.plot(a)

plt.show()