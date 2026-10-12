


from methods import *
f = open("dt_500_n2000.dat")
m = []
for  line in f:
    m.append(int(line))

colms = split_to_columns(m, 30)
plt.bar(range(len(colms)), colms)
#plt.plot(colms)
plt.show()