# import tkinter as tk

# # Función que se ejecutará al hacer clic en el botón
# def boton_presionado():
#     print("¡El botón ha sido presionado!")

# # Crear una ventana
# ventana = tk.Tk()

# # Añadir un título a la ventana
# ventana.title("Ventana con Botón")

# # Añadir un botón a la ventana
# boton = tk.Button(ventana, text="Presionar", command=boton_presionado)
# boton.pack(pady=10)

# # Mostrar la ventana
# ventana.mainloop()

# import tkinter as tk

# # Función que se ejecutará al hacer clic en el botón
# def boton_presionado():
#     # Crear la segunda ventana
#     ventana2 = tk.Toplevel(ventana)
#     ventana2.title("Ventana de Mensaje")
#     mensaje = tk.Label(ventana2, text="¡Botón presionado!")
#     mensaje.pack(pady=10)
#     ventana.destroy()

# # Crear la primera ventana
# ventana = tk.Tk()
# ventana.title("Ventana con Botón")

# # Crear un botón en la ventana
# boton = tk.Button(ventana, text="Presionar", command=boton_presionado)
# boton.pack(pady=10)

# # Mostrar la ventana
# ventana.mainloop()



# import tkinter as tk

# class Ventana:
#     # Función que se ejecutará al hacer clic en el botón
#     def crear_ventana(self):
#         # Limpiar la ventana principal
#         for widget in ventana.winfo_children():
#             widget.destroy()
        
#         # Mostrar un mensaje
#         mensaje = tk.Label(ventana, text="¡Botón presionado!")
#         mensaje.pack(pady=10)

#     # Crear la ventana principal
#     ventana = tk.Tk()
#     ventana.title("Ventana con Botón")

#     # Crear un botón en la ventana
#     boton = tk.Button(ventana, text="Presionar", command=boton_presionado)
#     boton.pack(pady=10)

#     # Mostrar la ventana
#     ventana.mainloop()

# # Crear una instancia de la clase Ventana
# mi_ventana = Ventana()

# # Llamar al método crear_ventana para desplegar la ventana
# mi_ventana.crear_ventana()

# import tkinter as tk

# class Ventana:
#     def __init__(self):
#         self.ventana = tk.Tk()
#         self.ventana.geometry('300x200')
        
#         self.boton = tk.Button(self.ventana, text='Imprimir tabla de lexemas y tipos de datos', command=self.mostrar_mensaje)
#         self.boton.pack(pady=20)
        
#         self.label_mensaje = tk.Label(self.ventana, text='', font=('Arial', 14))
#         self.label_mensaje.pack()
        
#     def mostrar_mensaje(self):
#         self.boton.destroy()
#         self.boton = tk.Button(self.ventana, text="Finalizar",command=self.fin)
#         self.boton.pack(pady=20)

#         self.archivo = open('./datos.txt','r')
#         self.mensaje = self.archivo.readline()
#         print(self.mensaje)
#         self.archivo.close()

#         self.label_mensaje.config(text='¡Hola, mundo!')
    
#     def fin(self):
#         self.ventana.destroy()
        
#     def ejecutar(self):
#         self.ventana.mainloop()



# mi_ventana = Ventana()
# mi_ventana.ejecutar()


import tkinter as tk

class VentanaConBoton:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.root = tk.Tk()
        self.root.title("Ventana con botón")
        self.label = tk.Label(self.root, text="Presiona el botón para ver el contenido del archivo")
        self.label.pack()
        self.boton = tk.Button(self.root, text="Mostrar contenido", command=self.mostrar_contenido)
        self.boton.pack()

    def mostrar_contenido(self):
        with open(self.ruta_archivo, "r") as archivo:
            contenido = archivo.read()
            contenido_label = tk.Label(self.root, text=contenido)
            contenido_label.pack()

    def iniciar(self):
        self.root.mainloop()

# Ejemplo de uso:
ventana = VentanaConBoton("datos.txt")
ventana.iniciar()