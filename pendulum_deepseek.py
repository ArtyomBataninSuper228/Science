import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Параметры системы
g = 9.81  # ускорение свободного падения (м/с²)
L1 = 1.0  # длина первого стержня (м)
L2 = 1.0  # длина второго стержня (м)
m1 = 100.0  # масса первого груза (кг)
m2 = 1.0  # масса второго груза (кг)

# Начальные условия: [угол1, скорость1, угол2, скорость2]
initial_state = [np.pi/2, 0, np.pi / 2, 0]  # 90 градусов для обоих маятников

# Временной интервал
t = np.linspace(0, 20, 1000)  # 20 секунд, 500 кадров


# Функция для вычисления производных
def derivatives(state, t):
    theta1, z1, theta2, z2 = state

    # Разность углов
    delta = theta2 - theta1

    # Производные (уравнения движения двойного маятника)
    dtheta1 = z1
    dtheta2 = z2
    denominator1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) * np.cos(delta)
    dz1 = (m2 * L1 * z1 * z1 * np.sin(delta) * np.cos(delta)
            + m2 * g * np.sin(theta2) * np.cos(delta)
            + m2 * L2 * z2 * z2 * np.sin(delta)
            - (m1 + m2) * g * np.sin(theta1)) / denominator1

    denominator2 = (L2 / L1) * denominator1
    dz2 = (-m2 * L2 * z2 * z2 * np.sin(delta) * np.cos(delta)
            + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
            - (m1 + m2) * L1 * z1 * z1 * np.sin(delta)
            - (m1 + m2) * g * np.sin(theta2)) / denominator2

    return [dtheta1, dz1, dtheta2, dz2]


# Решаем систему ОДУ
solution = odeint(derivatives, initial_state, t)

# Извлекаем углы
theta1 = solution[:, 0]
theta2 = solution[:, 2]

# Координаты маятников
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Создаем фигуру для анимации
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2, color='blue')
trace, = ax.plot([], [], '-', lw=1, color='red', alpha=0.5)


# Инициализация анимации
def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace


# Функция анимации
def animate(i):
    # Текущие координаты
    x = [0, x1[i], x2[i]]
    y = [0, y1[i], y2[i]]

    line.set_data(x, y)

    # Добавляем след для второго груза
    if i == 0:
        trace_x = []
        trace_y = []
    else:
        trace_x = x2[:i + 1]
        trace_y = y2[:i + 1]

    trace.set_data(trace_x, trace_y)

    return line, trace


# Создаем анимацию
ani = FuncAnimation(fig, animate, frames=len(t),
                    init_func=init, blit=True, interval=20)

plt.title('Симуляция двойного маятника')
plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.show()