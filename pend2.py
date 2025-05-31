import math
import sys
from threading import Thread
import pygame as pg
import matplotlib.pyplot as plt

pg.init()
sc = pg.display.set_mode((800, 600))
is_run = False
prev = pg.Surface((800, 600))
prev.fill((0, 0, 0))
prev.set_alpha(1)

# Параметры первого маятника
m1 = 1
L1 = 1
x1 = 1
y1 = 0
vx1 = 0
vy1 = 0
ax1 = 0
ay1 = 0

# Параметры второго маятника
m2 = 1
L2 = 1
x2 = 2
y2 = 0
vx2 = 0
vy2 = 0
ax2 = 0
ay2 = 0

g = 9.8
dt = 0.0000001
tm = 0

# Списки для хранения данных (для второго маятника)
time_data = []
angle_data = []

def update():
    global x1, y1, vx1, vy1, ax1, ay1, x2, y2, vx2, vy2, ax2, ay2, tm
    while True:
        if is_run:
            # Вычисление углов
            theta1 = math.atan2(x1, y1)
            theta2 = math.atan2(x2-x1, y2-y1)

            # Уравнения движения для двойного маятника 
            num1 = -g * (2 * m1 + m2) * math.sin(theta1)
            num2 = -m2 * g * math.sin(theta1 - 2 * theta2)
            num3 = -2 * math.sin(theta1 - theta2) * m2 * (vy2**2 * L2 + vx2**2 * L2 + vx1**2 * L1 * math.cos(theta1 - theta2) + vy1**2 * L1* math.cos(theta1 - theta2))
            den = L1 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2))
            alpha1 = (num1 + num2 + num3) / den

            num4 = 2 * math.sin(theta1 - theta2)
            num5 = vx1**2 * L1 * (m1 + m2) + vy1**2 * L1 * (m1+m2)
            num6 = g * (m1 + m2) * math.cos(theta1)
            num7 = vx2**2 * L2 * m2 * math.cos(theta1 - theta2) + vy2**2 * L2* m2 * math.cos(theta1 - theta2)
            den2 = L2 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2))
            alpha2 = (num4 * (num5 + num6 + num7)) / den2

            # Обновление угловых скоростей и углов
            vx1 += alpha1 * dt
            vy1 += alpha2 * dt
            theta1 += vx1 * dt
            theta2 += vy1 * dt

            # Обновление координат первого маятника
            x1 = L1 * math.sin(theta1)
            y1 = L1 * math.cos(theta1)

            # Обновление координат второго маятника
            x2 = x1 + L2 * math.sin(theta2)
            y2 = y1 + L2 * math.cos(theta2)


            # Сохранение данных
            time_data.append(tm)
            angle_data.append(theta2)  # Угол второго маятника



t = Thread(target=update)
t.start()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif e.type == pg.KEYDOWN:
            is_run = not is_run

    #sc.fill((0, 0, 0))  # Очистка экрана
    pg.draw.circle(sc, (255, 255, 255), (400, 100), 5)  # Точка подвеса

    # Отрисовка первого маятника
    x1_screen = int(x1 + 400)
    y1_screen = int(y1 + 100)
    #pg.draw.line(sc, (255, 255, 255), (400, 100), (x1_screen, y1_screen), 2)
    #pg.draw.circle(sc, (255, 0, 0), (x1_screen, y1_screen), 10)

    # Отрисовка второго маятника
    x2_screen = int(x2*100 + 400)
    y2_screen = int(y2*100 + 100)
    #pg.draw.line(sc, (255, 255, 255), (x1_screen, y1_screen), (x2_screen, y2_screen), 2)
    pg.draw.circle(sc, (0, 0, 255), (x2_screen, y2_screen), 1)


    pg.display.update()
"""
    # Построение графика
    if not is_run:
        plt.figure(figsize=(10, 5))
        plt.plot(time_data, angle_data, label='Угол отклонения (рад)')
        plt.xlabel('Время (с)')
        plt.ylabel('Угол (рад)')
        plt.title('Изменение угла отклонения второго маятника во времени')
        plt.legend()
        plt.grid()
        plt.show()
        time_data = []
        angle_data = []
"""