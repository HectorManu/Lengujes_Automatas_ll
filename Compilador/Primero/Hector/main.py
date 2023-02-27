import tkinter as tk
from tkinter import ttk

class Ventana:
    def __init__(self, master):
        self.master = master

        # Esta variable esa para guardar los tipos de datos en el futuro debo poner aquí todos los datos
        self.identificados = []
        self.sinrepeticion = []
        
        # HACEMOS EL BOTON
        self.boton = tk.Button(self.master, text='Imprimir tabla de lexemas y tipos de datos', command=self.mostrar_lexematipo)
        self.boton.pack(pady=20)

        
    def mostrar_lexematipo(self):
        
        # self.boton = tk.Button(self.master, text="Finalizar",command=self.fin)
        # self.boton.pack(pady=20)
        self.master.title('Tabla lexemas')

        # # Caracteres a eliminar QUE NO APARECERAN EN LA TABLA
        coma = ','
        puntocoma = ';'
        parentesis1 = '('
        parentesis2 = ')'
        corchete1 = '{'
        corchete2 = '}'
        saltolinea = '\n'
        comilla = '"'

        # Abrir archivo para imprimir en tabla
        with open('./datos.txt', 'r') as f:
            leyendo = f.read()
            separando_lineas = leyendo.split(' ')
            # print(leyendo)
            arreglosinespacios = separando_lineas
            for i in range(len(arreglosinespacios)):
                arreglosinespacios[i] = arreglosinespacios[i].replace(coma,'').replace(puntocoma,'').replace(parentesis1,'').replace(parentesis2,'').replace(corchete1,'').replace(corchete2,'').replace(saltolinea,'').replace(comilla,'')

        sinvacio = [elemento for elemento in arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
        self.sinrepeticion = set(sinvacio)
        

        #creando tabla
        tabla = ttk.Treeview(self.master,columns=('tipo','lexema',))
        tabla.heading('lexema',text='Lexemas')
        tabla.heading('tipo', text='Tipos de datos')
        tabla.heading('#0',text='')

        sinrepeticion2 = self.identificar_tipos()

        # Agregar las inrepeticion as tabla
        for i, tipo in enumerate(self.sinrepeticion):
            tabla.insert('', 'end', text='',values=(tipo.strip(),sinrepeticion2[i].strip()))

        # Configurando ancho de columna
        tabla.column('#0',width=0)

        # Empaquetatabla y mostrar la master
        tabla.pack(expand=True, fill='both')
        self.boton.destroy()#destuir el boton y dejar nomas la tabla
        return self.sinrepeticion
    
    def identificar_tipos(self):
        arreglo1 = list(self.sinrepeticion)

        with open('datos.txt','r') as f:
            lineas = f.readlines()
        
        
        
        return arreglo1
    
    def identificar_errore(self):
        arreglo2 = []
        return arreglo2
        

raiz = tk.Tk()
mi_ventana = Ventana(raiz)
raiz.mainloop()




