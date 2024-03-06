import turtle
import random

t = turtle.Turtle()
turtle.delay(0)
turtle.speed(0)

# for i in range(50):
#     t.penup()
#     t.setpos(random.randint(-200, 200), random.randint(-200, 200))
#     t.seth(random.randint(0, 359))
#     t.pendown()
#     t.fillcolor(random.choice(("red", "green", "blue", "yellow")))
#     t.begin_fill()
#     stvorec(30)
#     t.end_fill()
def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)

def lupen(d):
    for i in range(2):
        obluk(d)
        t.left(90)

def kvet(n, d):
    for i in range(n):
        t.fillcolor(random.choice(("blue", "yellow", "purple")))
        t.begin_fill()
        lupen(d)
        t. left(360 / n)
        t.end_fill()


kvet(10, 10)

turtle.mainloop()