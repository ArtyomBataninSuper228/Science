from matplotlib import pyplot as plt
from math import *
R1 = 148.74*10**3 ##
dR1 = R1*0.0001 + 0.02*10**3
R2 = 152.85*10**3 ##
dR2 = R2*0.0001 + 0.02*10**3
U0 = 12



GDM_V = 5.89
GDM_R = 10**(7)
M2044 = {75:(5, 0.15*10**(-3), 0.1), 30:(12/5, 0.6*(10**-3), 0.2), 15:(2.4, 0.3*10**(-3))} #Предел: напряжение, ток, шкала
parralel = [[5.13,2.38,2.38], [5.05,12/5, 2.4]] #GDM, M2044 (75, 30, 15)


print(f"R1 = {int(R1)}+-{round(dR1)}, R2 = {int(R2)}+-{round(dR2)}")
data = [
    ["Шкала, В", "U В", "dU В", "Uрасч", "R_v", "Uпаралл_GDM", "Uпаралл_M2044", "I, мА"],
    [20,        5.89,    0,         0,      0,      0,          0,                  0],
    [75,        5,       0,         0,      0,      5.13,          5.05,                  0.15],
    [30,        12/5,     0,         0,      0,      2.38,          2.4,                  0.6],
    [15,        2.4,     0,         0,      0,      2.38,          2.4,                  0.3],

]
data[1][4] = GDM_R
data[1][-1] = GDM_V/GDM_R*1000
for i in range(2, len(data)):
    line = data[i]
    line[4] = line[0]/line[-1]*1000
data[1][2] = data[1][1]*0.0003+4*10**-3
data[2][2] = 0.25
data[3][2] = 0.1
data[4][2] = 0.005

for i in range(1, len(data)):
    r1 = 1/(1/R1 + 1/data[i][4])
    R = r1+R2
    U = 12*r1/R
    data[i][3] = U
for line in data:
    for el in line:
        el2 = ""
        if type(el) == str:
            el2 = el
        else:
            el2 = str(round(el, 2))
        print(el2, end = " "*(16-len(el2)))
    print()