from tkinter import *

ventana_principal = Tk()
ventana_principal.geometry("500x500")
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.config(bg="black")

BASE=460
ALTURA=220

frme_graficacion = Frame(ventana_principal)
frme_graficacion.config(bg="white", width=480, height=240)
frme_graficacion.place(x=10, y=10)

c = Canvas(frme_graficacion, width= BASE, height= ALTURA)
c.config(bg="yellow")
c.place(x=10,y=10)

linea1= c.create_line(10,10, BASE-10, 10, fill="red")
linea2= c.create_line(BASE-10,10, BASE-10,ALTURA-10, fill="red")
linea3= c.create_line(BASE-10, ALTURA-10, 10, ALTURA-10, fill="red")
linea4= c.create_line(10,10, BASE-10, ALTURA-10, fill="red")
linea5= c.create_line(BASE-10, 10, 10, ALTURA-10, fill="red")
linea6= c.create_line(10,10, 10, ALTURA-10, fill="red")
linea7= c.create_line(10,30,ALTURA-10, 30)

ventana_principal.mainloop()