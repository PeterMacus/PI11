def karticka(x,y, text):
    canvas.create_rectangle(x,y,x+d,y+dd, fill="light gray")
    canvas.create_text(x+50, y+20, font="arial 14",text="Python" )

import tkinter
import random

canvas = tkinter.Canvas(height= 350 , width= 350)
canvas.pack()

for i in range(10):
    x = random.randint(0,300)
    y = random.randint(0,300)
    d = 100
    dd = 40
    karticka(x,y,"Python")


canvas.mainloop()