from tkinter import *

#CAMBIAR LA EXTENCIÓN A .PYW PARA QUE SEA WINDOWS Y SOLO DAR CLIC PARA EMPEZAR 

raiz = Tk()

raiz.title("Primer Ejercicio")

#raiz.resizable() este admite valores booleanos el primero es a lo ancho y el segundo a lo alto de la ventana

#raiz.geometry("650x650")

miFrame = Frame(raiz,width=500,height=500)


miFrame.pack() #fill = "both", expand = "True"



#miFrame.config(width=650,height=650)

#miFrame.config(relief="groove")

#miFrame.config(cursor='hand2')

milabel = Label(miFrame,text="hola perros")
milabel.place(x=100,y=200)



raiz.mainloop() # SIEMPRE AL FINAL es para que la ventana este en un buble infinito