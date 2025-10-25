from methods import *

M1 = list(randomfile.read(35)) # часы
M2 = list(randomfile.read(35)) # минуты
M = []
for i in range(0, len(M1)):
    M.append(M1[i]%4 + M2[i]%60/60)

Median = median(M)
columns = split_to_columns(M, 4)
print(f"Среднее время: {int(Median)} {int(Median%1*60)}/60")

step = (4)/4
for i in range(4):
    print(f"От {step*i} до {step*(i+1)} ч:", columns[i], " дней")
print("Сгенерированные значения:" , end=" ")
for i in M:
    print(f"{int(i)} {int(i%1*60)}/60  ", end=" ")



