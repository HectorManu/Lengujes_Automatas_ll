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

import tkinter as tk
from tkinter import ttk


# Caracteres a eliminar 
coma = ','
puntocoma = ';'
parentesis1 = '('
parentesis2 = ')'
corchete1 = '{'
corchete2 = '}'
saltolinea = '\n'
comilla = '"'


# Abrir el archivo y leer las líneas
with open('./datos.txt', 'r') as f:
    leyendo = f.read()
    separando_lineas = leyendo.split(' ')
    print(leyendo)
    arreglosinespacios = separando_lineas
    for i in range(len(arreglosinespacios)):
        arreglosinespacios[i] = arreglosinespacios[i].replace(coma,'').replace(puntocoma,'').replace(parentesis1,'').replace(parentesis2,'').replace(corchete1,'').replace(corchete2,'').replace(saltolinea,'').replace(comilla,'')

    sinvacio = [elemento for elemento in arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
    sinrepeticion = set(sinvacio)
    #print(sinrepeticion)

#es agarrar un if y ver si una linea empieza en ntr y en van y en echi entonces cuando encuentre un ; todas las variables anteriores son ntr y entonces en el lugar donde se encuentre la primera varialbe estara ntr xd y pues así con todas las demás hasta encontrar un ntr nuevo o algo así pero debe recorrerse todo el arreglo de readlines  mm interesante 



# Crear la ventana
ventana = tk.Tk()
ventana.title('Tabla de líneas')

# Crear la tabla
tabla = ttk.Treeview(ventana, columns=('tipo',))
tabla.heading('tipo', text='Tipos de datos')
tabla.heading('#0', text='Lexemas')

# Agregar lasinrepeticion as a la tabla
for i, tipo in enumerate(sinrepeticion):
    tabla.insert('', 'end', text=(tipo.strip(),),values=str(i+1))

# Empaquetar la tabla y mostrar la ventana
tabla.pack(expand=True, fill='both')
ventana.mainloop()



