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
        suma = '+'
        resta = '-'
        multi = '*'
        igual = '='

        # Abrir archivo para imprimir en tabla
        with open('./datos.txt', 'r') as f:
            leyendo = f.read()
            separando_lineas = leyendo.split(' ')
            self.arreglosinespacios = separando_lineas
            nueva_arreglosinespacios = ""

            for i in range(len(self.arreglosinespacios)):
                tempo = self.arreglosinespacios[i]
                for caracter in tempo:
                    if caracter == "\n":
                        nueva_arreglosinespacios += " \n "
                    else:
                        nueva_arreglosinespacios += caracter
                self.arreglosinespacios[i] = nueva_arreglosinespacios
                nueva_arreglosinespacios = ''
            
            cadenatemporal = " ".join(self.arreglosinespacios)
            self.arreglosinespacios = cadenatemporal.split(" ")

                

        self.sinvacio1 = [elemento for elemento in self.arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
        self.sinvacio = [elemento for elemento in self.sinvacio1 if elemento !='\n']
        self.sinrepeticion = set(self.sinvacio)
        
        #creando tabla
        tabla = ttk.Treeview(self.master,columns=('tipo','lexema',))
        tabla.heading('lexema',text='Lexemas')
        tabla.heading('tipo', text='Tipos de datos')
        tabla.heading('#0',text='')

        sinrepeticion2 = self.identifica_enteros()

        # Agregar las inrepeticion as tabla
        for i, tipo in enumerate(self.sinrepeticion):
            tabla.insert('', 'end', text=i,values=(tipo.strip(),sinrepeticion2[i].strip()))

        # Configurando ancho de columna
        tabla.column('#0',width=0)

        # Empaquetatabla y mostrar la master
        tabla.pack(expand=True, fill='both')
        self.boton.destroy()#destuir el boton y dejar nomas la tabla
        # self.identificar_errores()
    
    def identifica_enteros(self):
        arreglo1 = list(self.sinrepeticion)
        arreglo2 = self.sinvacio1
        arreglo2 = [elemento for elemento in arreglo2 if elemento !=',']
        arreglo2 = [elemento for elemento in arreglo2 if elemento !='(']
        arreglo2 = [elemento for elemento in arreglo2 if elemento !=')']
        arreglo2 = [elemento for elemento in arreglo2 if elemento !='{']
        arreglo2 = [elemento for elemento in arreglo2 if elemento !='}']
        print(arreglo2)


        for i in range(len(arreglo2)):
            if i == 'NTR':
                if i+1 == ';' or i+1 == '\n' or i+1 == '=':
                    print('llego breark')
                    break
                print('encontrontr')

        
        
        return arreglo1

    
    def identificar_errores(self):
        segunda_ventana = tk.Toplevel()
        segunda_ventana.title("Errores")
        tabla = ttk.Treeview(segunda_ventana,columns=('tipo','lexema',))
        tabla.heading('lexema',text='Lexemas')
        tabla.heading('tipo', text='Tipos de datos')
        tabla.heading('#0',text='')

        tabla.insert(parent='',index=0,iid=0,text='error',values=('uno','dos'))

        
        tabla.pack(fill=tk.BOTH,expand=1)



        

raiz = tk.Tk()
mi_ventana = Ventana(raiz)
raiz.mainloop()




