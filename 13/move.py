import tkinter, time
import random
canvas = tkinter.Canvas()
canvas.pack()

stvorec1 = canvas.create_rectangle(10 , 10, 110, 110, fill="red")
for i in range(250):
    canvas.update()
    time.sleep(0.01)
    canvas.move(stvorec1, 1, 0) # stvorec 1 je objekt ktory sa bude posuvať , 100 je o kolko sa posunie na osy x a 0 je o kolko sa posunie na osy y
    farba = random.choice(("red", "green", "orange", "purple"))
    canvas.itemconfig(stvorec1, fill=farba)

canvas.mainloop()
