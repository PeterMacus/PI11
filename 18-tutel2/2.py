import turtle

t = turtle.Turtle()
turtle.delay(0)
turtle.speed(10000)
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
        lupen(d)
        t. left(360 / n)

kvet(1000, 20)

turtle.mainloop()