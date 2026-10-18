from numpy import *

g = [0, -9.8, 0]

def do_system(l,n, k,dim = 3, def_pos = (0,0,0)):
    def_pos = array(def_pos)
    pos = zeros((n+1, dim), dtype=float64)
    speeds = zeros((n+1, dim), dtype=float64)
    pos[0] = (k, l/n, 0)
    for i in range(1,n+1):
        pos[i] = def_pos
        pos[i, 1] = -i*l/n
    return array([pos, speeds])
def get_diff(sys):
    lo = sys[0][0][1]
    k = sys[0][0][0]
    pos = sys[0]
    dpos = sys[1]
    dv = zeros(sys[1].shape, dtype=float64)
    for i in range(2, len(sys[1])):
        dr = pos[i] - pos[i-1]
        dv[i] = -k*(linalg.norm(dr)/lo - 1)*dr/linalg.norm(dr)

        dv[i-1] -= dv[i]
        dv[i] += g
    dv[0] = 0
    dv[1] = 0
    return array([dpos, dv])





