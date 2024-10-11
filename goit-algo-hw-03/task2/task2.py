import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(t, order, size=300):
    #одну сторону сніжинки Коха
    for _ in range(3):  #3 сторони сніжинки
        koch_curve(t, order, size)
        t.right(120)  #поворот на 120 градусів

def main():

    order = int(input("Enter the recursion depth: "))  #юзер вводить глибину рекурсії

    window = turtle.Screen()  #екран для малювання
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100) #початкова позиція малювання
    t.pendown()

    draw_koch_curve(t, order, 300)

    t.hideturtle()
    window.mainloop()

if __name__ == '__main__':
    main()