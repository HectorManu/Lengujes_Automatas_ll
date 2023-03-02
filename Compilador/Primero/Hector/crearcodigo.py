from tkinter import *
import subprocess

 
root = Tk()
root.title("Ventana de texto")
 
text_box = Text(root)
text_box.pack()
 
def guardar_texto():
    texto = text_box.get("1.0", END)
    with open("datos.txt", "w") as archivo:
        archivo.write(texto)
    subprocess.run(['python', '/Compilador/Primero/Hector/main.py'])

 
boton_guardar = Button(root, text="Guardar texto", command=guardar_texto)
boton_guardar.pack()
 
root.mainloop()
