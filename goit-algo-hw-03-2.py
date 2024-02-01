import turtle
import os


def clear_screen():
    os_name = os.name
    if os_name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=150):
    window = turtle.Screen()
    window.bgcolor("white")
    size = size * (order * 0.5)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


if __name__ == '__main__':
    while True:
        recursion_level = input("Please enter recursion level: ")
        if recursion_level.isdigit():
            recursion_level = int(recursion_level)
            draw_koch_snowflake(recursion_level, 150)
            break
        else:
            input('You need to enter number!')
            clear_screen()
