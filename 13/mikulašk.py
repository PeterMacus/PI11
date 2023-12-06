import tkinter, time, random

canvas_width = 400
canvas_height = 600
santa_x = canvas_width // 2
santa_y = 66
santa_posun = 1
santa_2x = canvas_width//5
santa_2y = 544
santa_3x = canvas_width // 1.25
santa_3y = 544
santa_posun23 = -1
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(santa_x, santa_y, image=image_santa)
santa2 = canvas.create_image(santa_2x, santa_2y, image=image_santa)
santa3 = canvas.create_image(santa_3x, santa_3y, image=image_santa)
while True:
    canvas.update()
    time.sleep(0.01)
    canvas.move(santa, 0, santa_posun)
    canvas.move(santa2, 0, santa_posun23)
    canvas.move(santa3, 0, santa_posun23)
    santa_y = santa_y + santa_posun
    santa_2y = santa_2y + santa_posun23
    santa_3y = santa_2y + santa_posun23
    if santa_y == canvas_height + 64:
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)
        canvas.delete(santa2)
        santa_2y = 544
        santa2 = canvas.create_image(santa_2x, santa_2y, image=image_santa)


canvas.mainloop()
