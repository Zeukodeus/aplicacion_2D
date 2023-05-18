from tkinter import *

# Variables globales
base = 460
altura = 240
radio = 50

def modificar_arco_1(angulo):
    c.itemconfigure(arco, extent=angulo)
    c.itemconfigure(arco, start=angulo)
    c.itemconfigure(arco2, extent=angulo)
    c.itemconfigure(arco2, start=angulo+90)
    c.itemconfigure(arco3, extent=angulo)
    c.itemconfigure(arco3, start=angulo+180)
    c.itemconfigure(arco4, extent=angulo)
    c.itemconfigure(arco4, start=angulo+270)

# Crear la ventana principal
ventana_principal = Tk()
ventana_principal.title("Molino de Viento")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

# Frame de la graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="gray", width=480, height=250)
frame_graficacion.place(x=10, y=10)

# Crear el lienzo (canvas)
c = Canvas(frame_graficacion, width=base, height=altura)
c.config(bg="black")
c.place(x=10, y=10)

# Crear los arcos del molino
arco = c.create_arc(base/2-radio, altura/2-radio, base/2+radio, altura/2+radio, start=0, extent=45, fill="red")
arco2 = c.create_arc(base/2-radio, altura/2-radio, base/2+radio, altura/2+radio, start=90, extent=45, fill="green")
arco3 = c.create_arc(base/2-radio, altura/2-radio, base/2+radio, altura/2+radio, start=180, extent=45, fill="blue")
arco4 = c.create_arc(base/2-radio, altura/2-radio, base/2+radio, altura/2+radio, start=270, extent=45, fill="orange")

# Frame de los controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="gray", width=480, height=240)
frame_controles.place(x=10, y=260)

# Barra de deslizamiento para controlar el ángulo
barra_deslizamiento = Scale(frame_controles, label="Ángulo", from_=0, to=45, orient="horizontal", length=200, tickinterval=90, command=modificar_arco_1)
barra_deslizamiento.place(x=20, y=10)

# Desplegar la ventana
ventana_principal.mainloop()
