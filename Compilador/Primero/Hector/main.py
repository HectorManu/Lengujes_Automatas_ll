import tkinter as tk
from tkinter import ttk
import re


class Ventana:
    def __init__(self, master):
        self.master = master

        # Esta variable esa para guardar los tipos de datos en el futuro debo poner aquí todos los datos
        self.identificados = []
        self.sinrepeticion = []

        # HACEMOS EL BOTON
        self.boton = tk.Button(
            self.master, text='Imprimir tabla de lexemas y tipos de datos', command=self.mostrar_lexematipo)
        self.boton.pack(pady=20)

    def mostrar_lexematipo(self):

        # self.boton = tk.Button(self.master, text="Finalizar",command=self.fin)
        # self.boton.pack(pady=20)
        self.master.title('Tabla lexemas')


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

        # eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
        self.sinvacio1 = [elemento for elemento in self.arreglosinespacios if elemento != ""]
        self.sinvacio = [elemento for elemento in self.sinvacio1 if elemento != '\n']
        self.sinrepeticion = set(self.sinvacio)

        # creando tabla
        tabla = ttk.Treeview(self.master, columns=('tipo', 'lexema','valor'))
        tabla.heading('valor',text='Valor')
        tabla.heading('lexema', text='Lexemas')
        tabla.heading('tipo', text='Tipos de datos')
        tabla.heading('#0', text='')

        sinrepeticion2 = self.identifica_tipos()

        # Agregar las inrepeticion as tabla
        for i, tipo in enumerate(self.sinrepeticion):
            tabla.insert('', 'end', text=i, values=(tipo.strip(), sinrepeticion2[i].strip()))

        # Configurando ancho de columna
        tabla.column('#0', width=0)

        # Empaquetatabla y mostrar la master
        tabla.pack(expand=True, fill='both')
        self.boton.destroy()  # destuir el boton y dejar nomas la tabla
        # self.identificar_errores()

    def identifica_tipos(self):
        arreglo1 = list(self.sinrepeticion)# convierto a lista el conjunto
        arreglo2 = self.sinvacio1 # variable en la cual iremos identificando los tipos
        # Limpieza de características que no nos sirven para encontrar los tipos de datos
        arreglo2 = [elemento for elemento in arreglo2 if elemento != ',']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != '(']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != ')']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != '{']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != '}']

        enteros = []
        reales = []
        cadenas = []
        expresion_int = re.compile('1[0-9]+1')
        expresion_real = re.compile('[0-9]+.1[0-9]+1')
        expresion_cadena = re.compile('"[A-Za-z0-9]*')
        expresion_variables = re.compile('CH[0-9A-Z_]*RA$')


        for i in range(len(arreglo2)):
            tempo = arreglo2[i]
            if 'ntr' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=':
                        break
                    else:
                        enteros.append(arreglo2[f+1])
            if expresion_int.match(tempo) != None:
                enteros.append(tempo)
                # enteros.append(tempo)
                # for f in range(len(arreglo2)):
                #     f += i
                #     if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=':
                #         break
                #     else:
                #         enteros.append(arreglo2[f+1])
            if 'van' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=':
                        break
                    else:
                        reales.append(arreglo2[f+1])
            if expresion_real.match(tempo) != None:
                reales.append(tempo)
            if 'echi' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=':
                        break
                    else:
                        cadenas.append(arreglo2[f+1])
            if expresion_cadena.match(tempo) != None:
                cadenas.append(tempo)
        
        for i in range(len(arreglo1)):
            tempo = arreglo1[i]
            for k in range(len(enteros)):
                if tempo == enteros[k]:
                    arreglo1[i] = 'ntr'
            for s in range(len(reales)):
                if tempo == reales[s]:
                    arreglo1[i] = 'van'
            for c in range(len(cadenas)):
                if tempo == cadenas[c]:
                    arreglo1[i] = 'echi'
        
        for i in range(len(arreglo1)):
            if arreglo1[i] != 'ntr' and arreglo1[i] != 'van' and arreglo1[i] != 'echi':
                arreglo1[i] = ''
    
        
        print(enteros)



        return arreglo1

    def identificar_errores(self):
        segunda_ventana = tk.Toplevel()
        segunda_ventana.title("Errores")
        tabla = ttk.Treeview(segunda_ventana, columns=('tipo', 'lexema',))
        tabla.heading('lexema', text='Lexemas')
        tabla.heading('tipo', text='Tipos de datos')
        tabla.heading('#0', text='')

        tabla.insert(parent='', index=0, iid=0,text='error', values=('uno', 'dos'))

        tabla.pack(fill=tk.BOTH, expand=1)


raiz = tk.Tk()
mi_ventana = Ventana(raiz)
raiz.mainloop()
