import matplotlib.pyplot as plt
import math

# Функція для побудови Дерева Піфагора
def draw_pythagoras_tree(ax, x, y, length, angle, depth):
    if depth == 0:
        return

    # Обчислення координат вершин квадрату
    x0, y0 = x + length * math.cos(angle), y + length * math.sin(angle)
    x1, y1 = x0 + length * math.cos(angle + math.pi / 2), y0 + length * math.sin(angle + math.pi / 2)
    x2, y2 = x1 - length * math.cos(angle), y1 - length * math.sin(angle)
    
    # Відображення квадрату
    ax.plot([x, x0, x1, x2, x], [y, y0, y1, y2, y], color="brown")

    # Наступні гілки (квадрати та кути) 
    new_length = length * math.sqrt(2) / 2  # зменшуємо розмір кожної нової гілки
    angle_left = angle + math.pi / 4        # поворот лівої гілки
    angle_right = angle - math.pi / 4       # поворот правої гілки

    # Рекурсивно малюємо ліву та праву гілки
    draw_pythagoras_tree(ax, x2, y2, new_length, angle_left, depth - 1)
    draw_pythagoras_tree(ax, x1, y1, new_length, angle_right, depth - 1)

# Основна функція для побудови
def plot_pythagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Початкова позиція та розмір
    x, y = 0, 0
    length = 100  # розмір початкового квадрату
    angle = math.pi / 2  # початковий кут (вертикально вгору)

    # Виклик функції побудови дерева
    draw_pythagoras_tree(ax, x, y, length, angle, depth)
    plt.show()

# Визначення глибини рекурсії (глибини дерева)
plot_pythagoras_tree(depth=7)
