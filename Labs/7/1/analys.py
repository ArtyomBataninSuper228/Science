from matplotlib import pyplot as plt
dh = 0.5/(12**0.5)#Погрешность линейки
noise_A = 340# Наведенный шум в катушках (Амплитуда)
noise_RMS = noise_A*0.5**0.5 #
noise_F  =50#Частота шума
h0 = 0.167

f =open("data.txt","r")
S = []
T1 = []
T2 = []
dT = []
U0 = []
U1 = []
U2 = []
dU = []
dS = 0.005
S1 = []
S_1 = []
S_2 = []
S_0 = []
U_1 = []
f.readline()
for line in f:
    print(line)
    s,t1, t2, u0, u1, u2, dt, du  = map(float, line.split())
    S.append(s+h0)
    T1.append(t1)
    T2.append(t2)
    dT.append(dt/25)
    U0.append(u0)
    U1.append(u1)
    U2.append(u2)

    S_0.append(h0)
    S_1.append(s+h0)
    S_2.append(2*s+h0)



    S1.append(h0)
    U_1.append(u0)
    S1.append(s+h0)
    U_1.append(u1)
    S1.append(2*s+h0)
    U_1.append(u2)

    dU.append(du/25)
plt.errorbar(S,T1, fmt = ".", xerr = dS, yerr = dT, label = "T1")
plt.errorbar(S,T2, fmt = ".", xerr= dS, yerr = dT, label = "T2")
plt.errorbar([0],[0], fmt = ".")
#plt.show()



#plt.errorbar(S_0,U0, fmt = ".", label = "U0")
#plt.errorbar(S_1,U1, fmt = ".", label = "U1")
#plt.errorbar(S_2,U2, fmt = ".", label ="U2")
plt.legend()
plt.show()