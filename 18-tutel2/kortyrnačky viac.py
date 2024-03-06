import turtle

t = turtle.Turtle()
t.speed(0)
t2 = turtle.Turtle()
t2.speed(0)
t3 = turtle.Turtle()
t3.speed(0)
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

for i in range(20):
    stvorec(100)
    t.left((360/20))

turtle.mainloop()