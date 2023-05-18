import random
from tkinter import *

ventana_principal = Tk()
ventana_principal.geometry("500x500")
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="white")

BASE=460
ALTURA=220

frme_graficacion = Frame(ventana_principal)
frme_graficacion.config(bg="black", width=480, height=240)
frme_graficacion.place(x=10, y=10)

c = Canvas(frme_graficacion, width= BASE, height= ALTURA)
c.config(bg="green")
c.place(x=10,y=10)

for i in range(100):
   x= random.randint(0, BASE-20)
   y= random.randint(0, ALTURA-20)
   color = "#"
   for caracter in range(6):
      color = color + random.choice("1234567890ABCDEF")
   circulo = c.create_oval(x, y, x+20, y+20, fill=color)

ventana_principal.mainloop()