import tkinter
import random
canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()


color = f'#{random.randrange(256**3):06x}'
x = 10
y = 10
d = 20
pocet = 20//d         # // je celociselne delenie
dalsi = 80//d
for j in range(dalsi):
    for i in range(pocet):
        #robime velke pisamenko P
        canvas.create_rectangle(x,y,x + d,y + d, fill=color)
        canvas.create_rectangle(x+d,y,x+2*d,y+d, fill=color)
        canvas.create_rectangle(x+2*d,y,x+3*d,y+d, fill=color)
        canvas.create_rectangle(x+3*d,y,x+4*d,y+d, fill=color)
        canvas.create_rectangle(x+4*d,y+d,x+5*d,y+2*d, fill=color)
        canvas.create_rectangle(x+4*d,y+2*d,x+5*d,y+3*d, fill=color)
        canvas.create_rectangle(x,y+d,x+d,y+2*d, fill=color)
        canvas.create_rectangle(x,y+2*d,x+d,y+3*d, fill=color)
        canvas.create_rectangle(x,y+3*d,x+d,y+4*d, fill=color)
        canvas.create_rectangle(x+2*d,y+3*d,x+1*d,y+4*d, fill=color)
        canvas.create_rectangle(x+3*d,y+3*d,x+2*d,y+4*d, fill=color)
        canvas.create_rectangle(x+4*d,y+3*d,x+3*d,y+4*d, fill=color)
        canvas.create_rectangle(x,y+5*d,x+d,y+4*d, fill=color)
        canvas.create_rectangle(x,y+6*d,x+d,y+5*d, fill=color)
        canvas.create_rectangle(x,y+7*d,x+d,y+6*d, fill=color)
        #E
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+6*d,y+6*d,x+7*d,y+7*d, fill=color)
        canvas.create_rectangle(x+6*d,y+5*d,x+7*d,y+6*d, fill=color)
        canvas.create_rectangle(x+6*d,y+4*d,x+7*d,y+5*d, fill=color)
        canvas.create_rectangle(x+6*d,y+3*d,x+7*d,y+4*d, fill=color)
        canvas.create_rectangle(x+6*d,y+2*d,x+7*d,y+3*d, fill=color)
        canvas.create_rectangle(x+6*d,y+1*d,x+7*d,y+2*d, fill=color)
        canvas.create_rectangle(x+6*d,y,x+7*d,y+1*d, fill=color)
        canvas.create_rectangle(x+7*d,y+6*d,x+8*d,y+7*d, fill=color)
        canvas.create_rectangle(x+8*d,y+6*d,x+9*d,y+7*d, fill=color)
        canvas.create_rectangle(x+9*d,y+6*d,x+10*d,y+7*d, fill=color)
        canvas.create_rectangle(x+10*d,y+6*d,x+11*d,y+7*d, fill=color)
        canvas.create_rectangle(x+7*d,y,x+8*d,y+1*d, fill=color)
        canvas.create_rectangle(x+8*d,y,x+9*d,y+1*d, fill=color)
        canvas.create_rectangle(x+9*d,y,x+10*d,y+1*d, fill=color)
        canvas.create_rectangle(x+10*d,y,x+11*d,y+1*d, fill=color)
        canvas.create_rectangle(x+7*d,y+4*d,x+8*d,y+3*d, fill=color)
        canvas.create_rectangle(x+8*d,y+4*d,x+9*d,y+3*d, fill=color)
        canvas.create_rectangle(x+9*d,y+4*d,x+10*d,y+3*d, fill=color)
        #T
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+12*d,y,x+13*d,y+1*d, fill=color)
        canvas.create_rectangle(x+13*d,y,x+14*d,y+1*d, fill=color)
        canvas.create_rectangle(x+14*d,y,x+15*d,y+1*d, fill=color)
        canvas.create_rectangle(x+15*d,y,x+16*d,y+1*d, fill=color)
        canvas.create_rectangle(x+16*d,y,x+17*d,y+1*d, fill=color)
        canvas.create_rectangle(x+14*d,y+d,x+15*d,y+2*d, fill=color)
        canvas.create_rectangle(x+14*d,y+2*d,x+15*d,y+3*d, fill=color)
        canvas.create_rectangle(x+14*d,y+3*d,x+15*d,y+4*d, fill=color)
        canvas.create_rectangle(x+14*d,y+4*d,x+15*d,y+5*d, fill=color)
        canvas.create_rectangle(x+14*d,y+5*d,x+15*d,y+6*d, fill=color)
        canvas.create_rectangle(x+14*d,y+6*d,x+15*d,y+7*d, fill=color)
        #E
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+18*d,y,x+19*d,y+1*d, fill=color)
        canvas.create_rectangle(x+19*d,y,x+20*d,y+1*d, fill=color)
        canvas.create_rectangle(x+20*d,y,x+21*d,y+1*d, fill=color)
        canvas.create_rectangle(x+21*d,y,x+22*d,y+1*d, fill=color)
        canvas.create_rectangle(x+22*d,y,x+23*d,y+1*d, fill=color)
        canvas.create_rectangle(x+18*d,y+d,x+19*d,y+2*d, fill=color)
        canvas.create_rectangle(x+18*d,y+2*d,x+19*d,y+3*d, fill=color)
        canvas.create_rectangle(x+18*d,y+3*d,x+19*d,y+4*d, fill=color)
        canvas.create_rectangle(x+18*d,y+4*d,x+19*d,y+5*d, fill=color)
        canvas.create_rectangle(x+18*d,y+5*d,x+19*d,y+6*d, fill=color)
        canvas.create_rectangle(x+18*d,y+6*d,x+19*d,y+7*d, fill=color)
        canvas.create_rectangle(x+19*d,y+6*d,x+20*d,y+7*d, fill=color)
        canvas.create_rectangle(x+20*d,y+6*d,x+21*d,y+7*d, fill=color)
        canvas.create_rectangle(x+21*d,y+6*d,x+22*d,y+7*d, fill=color)
        canvas.create_rectangle(x+22*d,y+6*d,x+23*d,y+7*d, fill=color)
        canvas.create_rectangle(x+19*d,y+3*d,x+20*d,y+4*d, fill=color)
        canvas.create_rectangle(x+20*d,y+3*d,x+21*d,y+4*d, fill=color)
        canvas.create_rectangle(x+21*d,y+3*d,x+22*d,y+4*d, fill=color)
        #R
        color = f'#{random.randrange(256**3):06x}'
        canvas.create_rectangle(x+24*d,y,x+25*d,y+1*d, fill=color)
        canvas.create_rectangle(x+24*d,y+1*d,x+25*d,y+2*d, fill=color)
        canvas.create_rectangle(x+24*d,y+2*d,x+25*d,y+3*d, fill=color)
        canvas.create_rectangle(x+24*d,y+3*d,x+25*d,y+4*d, fill=color)
        canvas.create_rectangle(x+24*d,y+4*d,x+25*d,y+5*d, fill=color)
        canvas.create_rectangle(x+24*d,y+5*d,x+25*d,y+6*d, fill=color)
        canvas.create_rectangle(x+24*d,y+6*d,x+25*d,y+7*d, fill=color)
        canvas.create_rectangle(x+25*d,y,x+26*d,y+1*d, fill=color)
        canvas.create_rectangle(x+26*d,y,x+27*d,y+1*d, fill=color)
        canvas.create_rectangle(x+27*d,y,x+28*d,y+1*d, fill=color)
        canvas.create_rectangle(x+28*d,y+2*d,x+29*d,y+1*d, fill=color)
        canvas.create_rectangle(x+28*d,y+3*d,x+29*d,y+2*d, fill=color)
        canvas.create_rectangle(x+25*d,y+3*d,x+26*d,y+4*d, fill=color)
        canvas.create_rectangle(x+26*d,y+3*d,x+27*d,y+4*d, fill=color)
        canvas.create_rectangle(x+27*d,y+3*d,x+28*d,y+4*d, fill=color)
        canvas.create_rectangle(x+26*d,y+4*d,x+27*d,y+5*d, fill=color)
        canvas.create_rectangle(x+27*d,y+5*d,x+28*d,y+6*d, fill=color)
        canvas.create_rectangle(x+28*d,y+6*d,x+29*d,y+7*d, fill=color)
        x = x+d
    x = x-d*pocet
    y = y+7*d
canvas.mainloop()

