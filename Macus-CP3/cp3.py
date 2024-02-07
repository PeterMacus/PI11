import tkinter

canvas = tkinter.Canvas(width= 1000, height= 1000)
canvas.pack()
r = int(input("Zadaj počet štvorcov v riadku:"))
s = int(input("Zadaj počet štvorcov pod seba:"))
x, y = 20,30
d = 30
m = 3
color1 = "maroon"
color2 = "gold"
c1 = color1
c2 = color2
for i in range(r):
    color1,color2 = color2,color1
    for j in range(s):
        canvas.create_rectangle(x+(d + m) * j ,y+(d + m) * i, x+(d+m) * j +d, y+(d+m) * i + d, fill= color2)
        if color2:
            c1 = color1
        else:
            c2






canvas.mainloop()