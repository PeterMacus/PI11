import tkinter
import random
vyska = int(input("Zadaj výšku obrazu:"))
sirka = int(input("Zadaj výšku obrazu:"))
canvas = tkinter.Canvas(width= sirka, height= vyska)
canvas.pack()
medzera = int(input("Zadaj veľkosť medzery:"))
hrubka = int(input("Zadaj šírku čiary:"))
x = medzera
farba = "blue"
for i in range(sirka // x):
    canvas.create_line(x,0,x,vyska, fill=farba, width=hrubka)
    canvas.create_line(0,x,sirka,x, fill=farba, width=hrubka)
    x= x+medzera
    if farba == "blue":
        farba = "red"
    else:
        farba = "blue"




canvas.mainloop()