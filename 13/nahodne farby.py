import tkinter
import random
canvas = tkinter.Canvas(height=500 ,width=500)
canvas.pack()

meno = "Ján"
priezvisko = "Mrkvička"
vek = 255

print("Volám sa",meno,"",priezvisko)
print(f"Volam sa {meno} {priezvisko} a mam {vek:02x} rokov")#vek:02x , prevedie do 16 sustavy
polomer = 20
for i in range(20):
    x = random.randint(2, 480)
    y = random.randint(2,480)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_oval(x- polomer, y- polomer, x + polomer, y + polomer, fill=farba)
canvas.mainloop()