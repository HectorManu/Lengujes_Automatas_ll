from tkinter import *

#CAMBIAR LA EXTENCIÓN A .PYW PARA QUE SEA WINDOWS Y SOLO DAR CLIC PARA EMPEZAR 

raiz = Tk()

raiz.title("Primer Ejercicio")

#raiz.resizable() este admite valores booleanos el primero es a lo ancho y el segundo a lo alto de la ventana

#raiz.geometry("650x650")

miFrame = Frame()

miFrame.pack()

miFrame.config(bg="black")

miFrame.config(width=650,height=650)

raiz.mainloop() # SIEMPRE AL FINAL es para que la ventana este en un buble infinito