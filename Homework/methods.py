import copy

randomfile = open("/dev/random", "rb")

M = randomfile.read(100)

def median(M):
    return sum(M)/len(M)

def dispersion(M):
    dispersion = 0
    med = median(M)
    for i in range(0, len(M)):
        dispersion += (M[i] - med)**2
    return dispersion/len(M)

def split_to_columns(M, n):
    M = copy.copy(M)
    M.sort()# сортировка массива в порядок элементов по возрастанию
    colums = []
    for i in range(n):# заполняем массив нулями
        colums.append(0)
    mn = min(M)
    mx = max(M)
    step = (mx - mn)/n # определение ширины колонки
    i = 0
    num_colum = 0
    while i < len(M) and num_colum < n:
        if mn + step*num_colum <= M[i] and M[i] <= mn + step*(num_colum+1): # проверка входит ли элемент в промежуток
            colums[num_colum] += 1
            i += 1
        else:
            num_colum += 1 # переход к следующей колонке

    return colums

