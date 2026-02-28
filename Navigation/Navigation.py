from math import *
from numpy import *
R = 6371.3*1000
def get_l(m):
    res = 0
    for i in m:
        res += i**2
    return res**0.5

def get_x_y_z(lon, lat, h):
    lon = lon/180*pi
    lat = lat/180*pi
    r = R + h
    y = r*sin(lat)
    x = r*cos(lat)*sin(lon)
    z = r*cos(lat)*cos(lon)
    return array([x, y, z])

if __name__ == "__main__":
    a  = get_x_y_z(56.07998, 60.71997, 200)
    b = get_x_y_z(56.06552, 60.76917, 200)
    print(get_l(a-b))
