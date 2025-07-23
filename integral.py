
import copy
import modulefinder
import time
from math import *
import dearpygui.dearpygui as dpg
import math
import numpy
import soundfile
import rawpy



e = math.e
m = []
mv = []
mt = []
mex = []
sp = 40
x = 0
a = 0
t = 0
dt = 0.001
K = 0.1



def tn(A, B):
    dx = A[0] - B[0]
    dy = A[1] - B[1]
    if dx == 0:
        return 0
    else:
        return dy/dx

def func(x):
    return mv[round(x/dt)]
def func2(x):
    return x%10<5#math.sin(math.pi*x/4) + math.sin(math.pi*x/10) +  math.sin(math.pi*x/3)*0.25
def create_grafic(massiv, data):
    nums = len(data)
    dpg.create_context()
    dpg.create_viewport(title='График', width=1500, height=900)
    dpg.show_imgui_demo()
    with dpg.window(pos = (0, 0), width=1500, height=890):
        with dpg.plot(width=1400, height=850):
            plot = dpg.last_item()
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis)
            xaxis = dpg.last_item()
            # dpg.set_axis_limits(xaxis, massiv[0], massiv[-1])
            dpg.add_plot_axis(dpg.mvYAxis)
            yaxis = dpg.last_item()
            dpg.set_axis_limits_auto(yaxis)
            for i in range(nums):
                #dpg.add_series
                dpg.add_line_series(massiv, data[i], parent=yaxis, label=str(i + 1))
            # dpg.add_line_series(massiv, volts, parent=yaxis, label="")
            # dpg.add_line_series(massiv, dv1, parent=yaxis, label="∆U1")
            # dpg.add_line_series(massiv, dv2, parent=yaxis, label="∆U2")
            # dpg.add_line_series(massiv, power, parent=yaxis, label="Power")

    dpg.create_viewport(title='Grafik', width=1440, height=850)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

    dpg.destroy_context()
def integral(min, max, dx, f):
    x = min
    S = 0
    while x < max:
        A = [x, f(x)]
        x += dx
        B = [x, f(x)]
        S += dx * (A[1]+B[1])/2
    return S
def differenzial(f, dx, x=0):
    yf = f(x)
    ys = f(x + dx)
    t = tn([x, yf], [x +dx, ys])
    return t
def fourie(func, max, min, dx):
    num = (max-min)/dx
    min_f = 1/(2*num*dx)
    max_f = 1/(2*dx)
    f = min_f
    res = []

    while f <= max_f:
        freq = copy.deepcopy(f)
        def fns(x):
            #print(math.sin(math.pi*x*freq))
            return math.sin(math.pi*x*freq)*func(x)
        def fnc(x):
            #print(math.sin(math.pi*x*freq))
            return math.cos(math.pi*x*freq)*func(x)
        res.append((f, math.sqrt(integral(min, max, dx, fns)**2+ integral(min, max, dx, fns)**2)))
        f += 1/(2*num*dx)
    return res


def obrat_fourie(freq, ampls, min, max, dx):

    res = numpy.zeros(int((max-min)/dx + 1))
    massiv = []
    num = 0
    while min < max:
        massiv.append(min)
        for    i in range(len(freq)):
            if ampls[i] > 1:
                print(freq[i])
                res[num] += ampls[i]*math.sin(math.pi*freq[i]* min)
        min += dx
        num += 1
    return massiv, res


    #pass
#dat = [32, 10.5, 6.3, 4.5, 3.5, 2.7, 2.3, 2, 1.7, 1.5, 1.3, 1.14]
#massiv = [1/5, 0.6, 1, 1.4, 1.8, 2.2, 2.6, 3, 3.4, 3.8, 4.2, 4.6]
#massiv, res = obrat_fourie(massiv, dat, -1000, 1000, 1)
#create_grafic(massiv, [dat])

def sin(x):
    x=((x/(2*math.pi))%1)*2*math.pi
    ret = 0
    minus = False
    if x > math.pi:
        x -= math.pi
        minus = True
    for n in range(1, 80, 2):
        if minus:
            ret -= (x**n)/math.factorial(n)
            minus = False
        else:
            ret += (x ** n) / math.factorial(n)
            minus = True
    return ret
def s(t):
    t = ((t / (2 * math.pi)) % 1) * 2 * math.pi
    dt = 1 / 100
    x1 = 0
    sp = dt
    T = 0
    if t > math.pi:
        t -= math.pi
        sp = -dt

    while T < t:
        sp += -x1*(dt**2)
        x1 += sp
        T += dt
    return x1



def callback(sender, app_data):

    _helper_data = app_data[0]
    transformed_x = app_data[1]
    transformed_y = app_data[2]
    #transformed_y1 = app_data[3] # for channel = 3
    #transformed_y2 = app_data[4] # for channel = 4
    #transformed_y3 = app_data[5] # for channel = 5
    #mouse_x_plot_space = _helper_data["MouseX_PlotSpace"]   # not used in this example
    #mouse_y_plot_space = _helper_data["MouseY_PlotSpace"]   # not used in this example
    mouse_x_pixel_space = _helper_data["MouseX_PixelSpace"]
    mouse_y_pixel_space = _helper_data["MouseY_PixelSpace"]
    dpg.delete_item(sender, children_only=True, slot=2)
    dpg.push_container_stack(sender)
    dpg.configure_item("demo_custom_series", tooltip=False)
    for i in range(0, len(transformed_x)):
        #dpg.draw_text((transformed_x[i]+15, transformed_y[i]-15), str(i), size=20)
        dpg.draw_circle((transformed_x[i], transformed_y[i]), 2, fill=(50+i*5, 50+i*50, 0, 255))
        if mouse_x_pixel_space < transformed_x[i]+15 and mouse_x_pixel_space > transformed_x[i]-15 and mouse_y_pixel_space > transformed_y[i]-15 and mouse_y_pixel_space < transformed_y[i]+15:
            dpg.draw_circle((transformed_x[i], transformed_y[i]), 30)
            dpg.configure_item("demo_custom_series", tooltip=True)
            dpg.set_value("custom_series_text", "Current Point: " + str(i))
    dpg.pop_container_stack()
'''
with dpg.window(label="Tutorial") as win:
    dpg.add_text("Hover an item for a custom tooltip!")
    with dpg.plot(label="Custom Series", height=400, width=-1):
        dpg.add_plot_legend()
        xaxis = dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis):
            with dpg.custom_series(x_data, y_data, 2, label="Custom Series", callback=callback, tag="demo_custom_series"):
                dpg.add_text("Current Point: ", tag="custom_series_text")
            dpg.fit_axis_data(dpg.top_container_stack())

dpg.set_primary_window(win, True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
'''

def get_distribution(m):
    a = list(set(m))
    l = len(m)
    a.sort()
    numbers = []
    for el in a:
        numbers.append(m.count(el)/l)
    return a, numbers


def do_runge_kutta_classic_step(sys, dif, step, h):
    sys2 = copy.copy(sys)
    k1 = dif(sys2)
    sys2 = step(sys2, h / 2, k1)
    k2 = dif(sys2)
    sys2 = step(sys2, h / 2, k2)
    k3 = dif(sys2)
    sys2 = step(sys2, h, k3)
    k4 = dif(sys2)
    k = (k1 + k2 * 2 + k3 * 2 + k4) / 6
    sys = step(sys, h, k)
    return sys


def do_rk4_1_step(sys, dif, step, h):
    sys2 = copy.copy(sys)
    k1 = dif(sys2)
    sys2 = step(sys2, h, k1)
    k2 = dif(sys2)
    sys2 = step(sys2, h, k2)
    k3 = dif(sys2)
    sys2 = step(sys2, h, k3)
    k4 = dif(sys2)
    k = (k1*15 + k2 * 7 + k3  + k4) / 24
    sys = step(sys, h, k)
    return sys

def do_rk4_2_step(sys, dif, step, h):
    sys2 = copy.copy(sys)
    k1 = dif(sys2)
    sys2 = step(sys2, h / 2, k1)
    k2 = dif(sys2)
    sys2 = step(sys2, h / 2, k2)
    k3 = dif(sys2)
    sys2 = step(sys2, h/2, k3)
    k4 = dif(sys2)
    k = (k4 - k3  + k2 * 2 + k1) / 3
    sys = step(sys, h, k)
    return sys

def do_rk4_3_step(sys, dif, step, h):
    sys2 = copy.copy(sys)
    k1 = dif(sys2)
    sys2 = step(sys2, h / 3, k1)
    k2 = dif(sys2)
    sys2 = step(sys2, h / 3, k2)
    k3 = dif(sys2)
    sys2 = step(sys2, h/3, k3)
    k4 = dif(sys2)
    k = (27*k4 - 69*k3 + 69*k2 - 19*k1)/8
    sys = step(sys, h, k)
    return sys


def test_sys(sys, fd, fs, k, h):
    sys2 = fs(copy.copy(sys), h, k)
    delta =  fd(sys2) - k
    return delta
def seek_solution(sys, fd, fs, h):
    st_sys = copy.copy(sys)
    k1 = fd(sys)
    sys = fs(sys, h, k1)
    k2 = fd(sys)
    delta = k2-k1
    t1 = test_sys(st_sys, fd, fs, k1, h)
    t2 = test_sys(st_sys, fd, fs, k2, h)
    a = t2-t1
    b = t1 - a
    n = -b/a - 1
    return k1 + delta*n

def do_backward_euler_step(sys, dif, step, h):
    sys2 = copy.copy(sys)
    k = seek_solution(sys2, dif, step, h)
    sys = step(sys, h, k)
    return sys

