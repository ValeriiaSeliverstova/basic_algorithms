import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()



#Метод Монте-Карло для обчислення площі 

max_f = b ** 2  # для f(x) = x^2, максимальне значення на [0, 2] дорівнює 4

def is_under_curve(x, y):
    """Перевіряє, чи знаходиться точка (x, y) під кривою f(x) = x^2."""
    return y <= x ** 2

# Генерація випадкових точок
n_samples = 15000
points = [(random.uniform(a, b), random.uniform(0, max_f)) for _ in range(n_samples)]

# Відбір точок, що знаходяться під кривою
under_curve_points = [point for point in points if is_under_curve(point[0], point[1])]

# Кількість усіх точок та точок під кривою
N = len(points)
M = len(under_curve_points)

# Площа за методом Монте-Карло
S_monte_carlo = (M / N) * (b * max_f)  # Площа за методом Монте-Карло
print(f"Кількість точок під кривою: {M}, загальна кількість точок: {N}")
print(f"Площа за методом Монте-Карло: {S_monte_carlo}")

# Обчислення точного значення інтегралу, обчислення інтеграла

result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)
