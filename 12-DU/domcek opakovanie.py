import tkinter
import random

canvas = tkinter.Canvas(width = 1000, height = 800)
canvas.pack()
x = 10
y = 10
d = 50
pocet = 950//d         # // je celociselne delenie
dalsi = 450//d
for j in range(dalsi):
    for i in range(pocet):
        canvas.create_polygon(x + d // 2, y, x + d, y + d // 2, x, y + d // 2, fill="white", outline="black")
        canvas.create_line(x + d // 2, y, x + d, y + d // 2, x + d, y + d * 1.5, x, y + d * 1.5, x, y + d // 2,
                           x + d // 2, y)
        canvas.create_line(x, y + d // 2, x + d, y + d // 2)
        canvas.create_rectangle(x + d * 0.25, y + d * 0.75, x + d * 0.75, y + d * 1.25, fill="blue")
        canvas.create_line(x + d // 2, y + d * 0.75, x + d // 2, y + d * 1.25)
        canvas.create_line(x + d * 0.25, y + d, x + d * 0.75, y + d)
        x = x+d
    x = x-d*pocet
    y = y+x+x+x+d

canvas.mainloop()