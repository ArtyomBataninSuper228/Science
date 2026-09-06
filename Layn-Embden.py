from numpy import*
#import copy
from matplotlib import pyplot as plt


def do_rk4_step(sys, diff, h):
    k1 = diff(sys)
    k2 = diff(sys + h * k1 / 2)
    k3 = diff(sys + h * k2 / 2)
    k4 = diff(sys + h * k3)
    new_sys = sys + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return new_sys

n = 3
sys = array([1, 0, 0], dtype = float64) #thetta, dthetta/dksi, ksi

def diff(sys):
    ddthetta = - sys[0]**n-2/sys[2]*sys[1] #d^2thetts/dksi^2
    return array([sys[1], ddthetta, 1])

dksi = 10**(-5)
sys[2] = dksi
thetta = []
ksi = []
while sys[0]>= 10**(-7):
    sys = do_rk4_step(sys, diff, dksi)
    thetta.append(sys[0])
    ksi.append(sys[2] )
plt.plot(ksi, thetta)
plt.show()



