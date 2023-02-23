# import tkinter as tk

# class Ventana:
#     def __init__(self):
#         self.ventana = tk.Tk()
        
#         self.boton = tk.Button(self.ventana, text='Imprimir tabla de lexemas y tipos de datos', command=self.mostrar_mensaje)
#         self.boton.pack(pady=20)
        
#         self.label_mensaje = tk.Label(self.ventana, text='', font=('Arial', 14))
#         self.label_mensaje.pack()
        
#     def mostrar_mensaje(self):
#         self.boton.destroy()
#         self.boton = tk.Button(self.ventana, text="Finalizar",command=self.fin)
#         self.boton.pack(pady=20)

#         self.archivo = open('./datos.txt')
#         self.mensaje = self.archivo.readlines()
#         print(len(self.mensaje))
#         self.archivo.close()

#         self.label_mensaje.config(text=self.mensaje)
    
#     def fin(self):
#         self.ventana.destroy()
        
#     def ejecutar(self):
#         self.ventana.mainloop()



# mi_ventana = Ventana()
# mi_ventana.ejecutar()

with open('./datos.txt') as archivo:
    lineas = archivo.read()
    lineas = [linea.strip() for linea in lineas]

print(lineas)



