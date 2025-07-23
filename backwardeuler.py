import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Параметры маятника
g = 9.8  # ускорение свободного падения (м/с²)
L = 1.0  # длина маятника (м)
mu = 0.1  # коэффициент трения (1/с)

# Начальные условия
theta0 = np.pi / 4  # начальный угол (45 градусов)
omega0 = 0.0  # начальная угловая скорость

# Временные параметры
t_start = 0.0
t_end = 10.0
dt = 10**(-2)  # шаг по времени
num_steps = int((t_end - t_start) / dt)
t = np.linspace(t_start, t_end, num_steps)


# Явный метод Эйлера
def explicit_euler():
    theta = np.zeros(num_steps)
    omega = np.zeros(num_steps)
    theta[0] = theta0
    omega[0] = omega0

    for i in range(num_steps - 1):
        theta[i + 1] = theta[i] + dt * omega[i]
        omega[i + 1] = omega[i] + dt * (-mu * omega[i] - (g / L) * np.sin(theta[i]))

    return theta, omega


# Неявный метод Эйлера
def implicit_euler():
    theta = np.zeros(num_steps)
    omega = np.zeros(num_steps)
    theta[0] = theta0
    omega[0] = omega0

    for i in range(num_steps - 1):
        # Функция для решения нелинейного уравнения
        def equations(vars):
            theta_next, omega_next = vars
            eq1 = theta_next - theta[i] - dt * omega_next
            eq2 = omega_next - omega[i] - dt * (-mu * omega_next - (g / L) * np.sin(theta_next))
            return [eq1, eq2]

        # Начальное приближение (можно взять значения из явного метода)
        initial_guess = (theta[i] + dt * omega[i], omega[i] + dt * (-mu * omega[i] - (g / L) * np.sin(theta[i])))

        # Решаем систему уравнений
        theta[i + 1], omega[i + 1] = fsolve(equations, initial_guess)

    return theta, omega


# Решение обоими методами
theta_explicit, omega_explicit = explicit_euler()
theta_implicit, omega_implicit = implicit_euler()

# Построение графиков
plt.figure(figsize=(12, 6))

# График угла theta(t)
plt.subplot(1, 2, 1)
plt.plot(t, theta_explicit, label='Явный Эйлер', color='blue', alpha=0.7)
plt.plot(t, theta_implicit, label='Неявный Эйлер', color='red', linestyle='--', alpha=0.7)
plt.xlabel('Время (с)')
plt.ylabel('Угол θ (рад)')
plt.title('Сравнение методов: угол θ(t)')
plt.legend()
plt.grid()

# График угловой скорости omega(t)
plt.subplot(1, 2, 2)
plt.plot(t, omega_explicit, label='Явный Эйлер', color='blue', alpha=0.7)
plt.plot(t, omega_implicit, label='Неявный Эйлер', color='red', linestyle='--', alpha=0.7)
plt.xlabel('Время (с)')
plt.ylabel('Угловая скорость ω (рад/с)')
plt.title('Сравнение методов: угловая скорость ω(t)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Сравнение ошибок (разница между методами)
error_theta = np.abs(theta_explicit - theta_implicit)
error_omega = np.abs(omega_explicit - omega_implicit)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(t, error_theta, color='green')
plt.xlabel('Время (с)')
plt.ylabel('Ошибка угла |Δθ|')
plt.title('Ошибка между методами: угол')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(t, error_omega, color='purple')
plt.xlabel('Время (с)')
plt.ylabel('Ошибка скорости |Δω|')
plt.title('Ошибка между методами: угловая скорость')
plt.grid()

plt.tight_layout()
plt.show()