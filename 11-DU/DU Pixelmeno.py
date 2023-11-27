import tkinter
import random
canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()



x = 10
y = 10
d = 20

#robime velke pisamenko P
canvas.create_rectangle(x,y,x + d,y + d, fill="yellow")
canvas.create_rectangle(x+d,y,x+2*d,y+d, fill="black")
canvas.create_rectangle(x+2*d,y,x+3*d,y+d)
canvas.create_rectangle(x+3*d,y,x+4*d,y+d)
canvas.create_rectangle(x+4*d,y+d,x+5*d,y+2*d)
canvas.create_rectangle(x+4*d,y+d,x+5*d,y+3*d)
canvas.create_rectangle(x,y+d,x+d,y+2*d)
canvas.create_rectangle(x,y+2*d,x+d,y+3*d, fill="black")
canvas.create_rectangle(x,y+3*d,x+d,y+4*d)
canvas.create_rectangle(x+2*d,y+3*d,x+1*d,y+4*d)
canvas.create_rectangle(x+3*d,y+3*d,x+2*d,y+4*d)
canvas.create_rectangle(x+4*d,y+3*d,x+3*d,y+4*d)
canvas.create_rectangle(x,y+5*d,x+d,y+4*d,fill="green")
canvas.create_rectangle(x,y+6*d,x+d,y+5*d)
canvas.create_rectangle(x,y+7*d,x+d,y+6*d)
#E
canvas.create_rectangle(x+6*d,y+6*d,x+7*d,y+7*d)
canvas.create_rectangle(x+6*d,y+5*d,x+7*d,y+6*d)
canvas.create_rectangle(x+6*d,y+4*d,x+7*d,y+5*d)
canvas.create_rectangle(x+6*d,y+3*d,x+7*d,y+4*d)
canvas.create_rectangle(x+6*d,y+2*d,x+7*d,y+3*d)
canvas.create_rectangle(x+6*d,y+1*d,x+7*d,y+2*d)
canvas.create_rectangle(x+6*d,y,x+7*d,y+1*d)
canvas.create_rectangle(x+7*d,y+6*d,x+8*d,y+7*d)
canvas.create_rectangle(x+8*d,y+6*d,x+9*d,y+7*d)
canvas.create_rectangle(x+9*d,y+6*d,x+10*d,y+7*d)
canvas.create_rectangle(x+10*d,y+6*d,x+11*d,y+7*d)
canvas.create_rectangle(x+7*d,y,x+8*d,y+1*d)
canvas.create_rectangle(x+8*d,y,x+9*d,y+1*d)
canvas.create_rectangle(x+9*d,y,x+10*d,y+1*d)
canvas.create_rectangle(x+10*d,y,x+11*d,y+1*d)
canvas.create_rectangle(x+7*d,y+4*d,x+8*d,y+3*d)
canvas.create_rectangle(x+8*d,y+4*d,x+9*d,y+3*d)
canvas.create_rectangle(x+9*d,y+4*d,x+10*d,y+3*d)
#T
canvas.create_rectangle(x+12*d,y,x+13*d,y+1*d)
canvas.create_rectangle(x+13*d,y,x+14*d,y+1*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+1*d)
canvas.create_rectangle(x+15*d,y,x+16*d,y+1*d)
canvas.create_rectangle(x+16*d,y,x+17*d,y+1*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+2*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+3*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+4*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+5*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+6*d)
canvas.create_rectangle(x+14*d,y,x+15*d,y+7*d)
#E
canvas.create_rectangle(x+18*d,y,x+19*d,y+1*d)
canvas.create_rectangle(x+19*d,y,x+20*d,y+1*d)
canvas.create_rectangle(x+20*d,y,x+21*d,y+1*d)
canvas.create_rectangle(x+21*d,y,x+22*d,y+1*d)
canvas.create_rectangle(x+22*d,y,x+23*d,y+1*d)
canvas.create_rectangle(x+18*d,y,x+19*d,y+2*d)
canvas.create_rectangle(x+18*d,y,x+19*d,y+3*d)
canvas.create_rectangle(x+18*d,y,x+19*d,y+4*d)
canvas.create_rectangle(x+18*d,y,x+19*d,y+5*d)
canvas.create_rectangle(x+18*d,y,x+19*d,y+6*d)
canvas.create_rectangle(x+18*d,y,x+19*d,y+7*d)
canvas.create_rectangle(x+19*d,y+6*d,x+20*d,y+7*d)
canvas.create_rectangle(x+20*d,y+6*d,x+21*d,y+7*d)
canvas.create_rectangle(x+21*d,y+6*d,x+22*d,y+7*d)
canvas.create_rectangle(x+22*d,y+6*d,x+23*d,y+7*d)
canvas.create_rectangle(x+19*d,y+3*d,x+20*d,y+4*d)
canvas.create_rectangle(x+20*d,y+3*d,x+21*d,y+4*d)
canvas.create_rectangle(x+21*d,y+3*d,x+22*d,y+4*d)
#R
canvas.create_rectangle(x+24*d,y,x+25*d,y+1*d)
canvas.create_rectangle(x+24*d,y,x+25*d,y+2*d)
canvas.create_rectangle(x+24*d,y,x+25*d,y+3*d)
canvas.create_rectangle(x+24*d,y,x+25*d,y+4*d)
canvas.create_rectangle(x+24*d,y,x+25*d,y+5*d)
canvas.create_rectangle(x+24*d,y,x+25*d,y+6*d)
canvas.create_rectangle(x+24*d,y,x+25*d,y+7*d)






























































canvas.mainloop()