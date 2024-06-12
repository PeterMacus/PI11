import tkinter

canvas = tkinter.Canvas()
canvas.pack()

subor = open("cvič.txt", encoding="utf-8")
for riadok in subor:

    medzera = riadok.find(" ")
    tvar = riadok[:medzera]
    riadok = riadok[medzera+1:]

    medzera = riadok.find(" ")
    x = int(riadok[:medzera])
    riadok = riadok[medzera+1:]
    medzera = riadok.find(" ")
    y = int(riadok[:medzera])
    riadok = riadok[medzera + 1:]

    print(tvar, x, y, r, g, b)
    if tvar == "r":
        canvas.create_rectangle(x, y, x+20, y+20)
    else:
        canvas.create_oval(x, y, x+20, y+20)








subor.close()


tkinter.mainloop()