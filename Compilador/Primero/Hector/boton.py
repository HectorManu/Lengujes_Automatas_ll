import tkinter as tk
from tkinter import ttk

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        
        self.boton = tk.Button(self.ventana, text='Imprimir tabla de lexemas y tipos de datos', command=self.mostrar_lexematipo)
        self.boton.pack(pady=20)
        
        self.label_mensaje = tk.Label(self.ventana, text='', font=('Arial', 14))
        self.label_mensaje.pack()
        
    def mostrar_lexematipo(self):
        self.boton.destroy()
        self.boton = tk.Button(self.ventana, text="Finalizar",command=self.fin)
        self.boton.pack(pady=20)

        self.archivo = open('./datos.txt')
        self.mensaje = self.archivo.readlines()
        print(len(self.mensaje))
        self.archivo.close()

        self.label_mensaje.config(text=self.mensaje)
    
    def fin(self):
        self.ventana.destroy()
        
    def ejecutar(self):
        self.ventana.mainloop()



mi_ventana = Ventana()
mi_ventana.ejecutar()

# import tkinter as tk
# from tkinter import ttk


# # Caracteres a eliminar 
# coma = ','
# puntocoma = ';'
# parentesis1 = '('
# parentesis2 = ')'
# corchete1 = '{'
# corchete2 = '}'
# saltolinea = '\n'
# comilla = '"'


# # Abrir el archivo y leer las líneas
# with open('./datos.txt', 'r') as f:
#     leyendo = f.read()
#     separando_lineas = leyendo.split(' ')
#     print(leyendo)
#     arreglosinespacios = separando_lineas
#     for i in range(len(arreglosinespacios)):
#         arreglosinespacios[i] = arreglosinespacios[i].replace(coma,'').replace(puntocoma,'').replace(parentesis1,'').replace(parentesis2,'').replace(corchete1,'').replace(corchete2,'').replace(saltolinea,'').replace(comilla,'')

#     sinvacio = [elemento for elemento in arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
#     sinrepeticion = set(sinvacio)
#     #print(sinrepeticion)

# #Lo que haremos para identificar los tipos de datos será lo siguiente: 
# # Primero recorreremos cada línea buscando una declaración de variable es decir si empieza con ntr van echi entonces lo que sigue es un nombre de variable entonces realizaremos un arreglo por cada variable que no se repita es decir guardaremos los valores y cuando lo comparemos en la otra lista 

# # Arreglos para tipos de datos
# ntr = [] # Enteros
# van = [] # Reales
# echi = [] # Cadena

# with open('./datos.txt','r') as f:
#     arreglolineas = f.readlines()
#     print(arreglolineas)


# # Crear la ventana
# ventana = tk.Tk()
# ventana.title('Tabla de líneas')

# # Crear la tabla
# tabla = ttk.Treeview(ventana, columns=('tipo',))
# tabla.heading('tipo', text='Tipos de datos')
# tabla.heading('#0', text='Lexemas')

# # Agregar lasinrepeticion as a la tabla
# for i, tipo in enumerate(sinrepeticion):
#     tabla.insert('', 'end', text=(tipo.strip(),),values=(tipo.strip(),))

# # Empaquetar la tabla y mostrar la ventana
# tabla.pack(expand=True, fill='both')
# ventana.mainloop()



