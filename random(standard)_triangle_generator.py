import turtle
import math
import random

turtle.hideturtle()
t = turtle.Turtle()


def equi_triangle():
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    turtle.done()


def right_triangle():
    t.forward(60 * math.sqrt(3))
    t.right(150)
    t.forward(120)
    t.right(120)
    t.forward(60)
    turtle.done()


def fortyfive_fortyfive_ninety():
    t.forward(60)
    t.right(135)
    t.forward(60 * math.sqrt(2))
    t.right(135)
    t.forward(60)
    turtle.done()


def random_triangle():
    a = random.randint(0, 15)
    b = random.randint(0, 15)
    c = random.randint(0, 15)
    print(a)
    print(b)
    print(c)
    if a > 1 <= 5.0:
        equi_triangle()
    elif b > 5 <= 10.0:
        right_triangle()

    elif c > 10 <= 15.0:
        fortyfive_fortyfive_ninety()



random_triangle()
