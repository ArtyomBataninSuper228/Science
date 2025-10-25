from methods import *
from matplotlib import pyplot as plt



for i in range(0, len(M)):
    M[i] = M[i]%31 # данные от 0 до 30

Median = median(M)
D = dispersion(M)
columns = split_to_columns(M, 4)
print("Среднее время ожидания: ",Median)
print("Дисперсия: ", D, "Стандартное отклонение: ", D**0.5)

step = (30)/4
for i in range(4):
    print(f"От {step*i} до {step*(i+1)} минут:", columns[i])
print("Сгенерированные значения:" , end=" ")
for i in M:
    print(i, end=" ")



