from threading import Thread

import serial
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
import dearpygui.dearpygui as dpg
import numpy as np


ser = None
for port in ports:
  # Выводим имя порта, описание и аппаратный ID
  print(f"{port.device}: {port.description} [{port.hwid}]")
  if port.description == "RaspberryPi Pico":
      ser = serial.Serial(port.device, 2000000)
      #ser.set_buffer_size(100)


if ser == None:
    print("Serial port not found")



N = 10000
N_otbr = 10000
x = 0
t = 0
trig_mode = 3
data= np.zeros(N, dtype=np.float64)
rng = np.arange(N)
ons = np.ones(N, dtype=np.float64)
trig_line = np.ones(N, dtype=np.float64)
times = np.zeros(N, dtype=np.float64)

def render():
    dpg.set_value('data_tag',
                  [times.tolist()[0:N], data.tolist()[0:N]])
    dpg.set_axis_limits("x_axis", x*t/1000000/N, t / 1000000 * 1.1 * (N_otbr+x) / N)
    dpg.set_axis_limits("y_axis", -0.1, 3.4)


def reading():
    global data,ser, times, t
    a = ser.readline()
    while b"START" not in a:
        a = ser.readline()
    while 1:
        a = ser.readline()
        while b"START" not in a:
            a = ser.readline()
        a = ser.readline()
        t = int(a)
        times = rng*t/1000000/N
        for i in range(N):
            bin = ser.read(2)
            a = int.from_bytes(bin, byteorder='little')
            data[i] = (a/4096*3.3)
        render()

def update():
    trig_level = dpg.get_value('trig_level')
    trig_line = trig_level/4096*3.3*ons
    dpg.set_value('trig_line_tag', [times.tolist(), trig_line.tolist()])
    ser.write(b"6626\n")
    ser.write(f"{N}\n".encode("utf-8"))
    print(f"{N}")
    ser.write(f"{trig_level}\n".encode("utf-8"))
    print(f"{trig_level}")
    ser.write(f"{trig_mode}\n".encode("utf-8"))
    print(f"{trig_mode}")

def new_n():
    global N_otbr
    N_otbr = dpg.get_value('N')
    render()

def new_x():
    global x
    x = dpg.get_value('X')
    render()


dpg.create_context()
with dpg.font_registry():
    with dpg.font('/Users/artembatanin/PycharmProjects/messenger/notomono-regular.ttf', 25, default_font=True, id="Default25"):
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

with dpg.value_registry():
    dpg.add_int_value(default_value=20, tag="trig_level")
    dpg.add_int_value(default_value=10000, tag="datalength")



dpg.bind_font("Default25")

dpg.create_viewport(title='Oscilloscope', width=1500, height=900)

with dpg.window(label="Lamp", width=1500, height=900, no_move=True, no_close=True, no_resize=True, no_collapse=True):

    with dpg.plot(label="Line Series", height=500, width=1200, pos = (50, 50)):
        # optionally create legend
        #dpg.add_plot_legend(location=100)

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="Время сек", tag = "x_axis")
        dpg.add_plot_axis(dpg.mvYAxis, label="Напряжение", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(times.tolist(), data.tolist(), parent="y_axis", tag="data_tag")
        dpg.add_line_series(times.tolist(), trig_line.tolist(), parent="y_axis", tag="trig_line_tag")
    dpg.set_axis_limits("x_axis", 0,  10000/120000 * 1.1)
    dpg.set_axis_limits("y_axis", -0.1, 3.4)
    dpg.add_slider_int(min_value= 0, max_value = 4096 , pos = (1300, 50), vertical=True, height=500, width = 50, source = "trig_level", callback = update)
    dpg.add_slider_int(min_value=-N//2, max_value=N, pos=(50, 650), height=50, width=1200, callback=new_x, tag="X")
    dpg.add_slider_int(min_value=10, max_value=N, pos=(50, 700), height=50, width=1200, callback=new_n, tag="N", default_value=N)
    th = Thread(target=reading)
    th.start()


dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui()
is_run = False
dpg.destroy_context()

