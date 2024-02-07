import tkinter
import random

canvas = tkinter.Canvas(width=500, height=400)
canvas.pack()
r = 10

color = ("gold")
for i in range(10000):
    x = random.randint(10,350)
    y = random.randint(10,250)

    if y < 90:
        color = ("black")
    elif y < 170:
         color = ("red")
    else:
        color = ("gold")
    canvas.create_oval(x,y,x+r,y+r,outline="", fill=color)



canvas.mainloop()