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
            self.master, text='Imprimir tablas', command=self.mostrar_lexematipo)
        self.boton.pack(pady=20)

    def mostrar_lexematipo(self):

        # self.boton = tk.Button(self.master, text="Finalizar",command=self.fin)
        # self.boton.pack(pady=20)
        self.master.title('Tabla de símbolos')


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
        tabla.column('tipo',anchor='center')
        tabla.column('lexema',anchor='center')
        tabla.column('valor',anchor='center')

        # Empaquetatabla y mostrar la master
        tabla.pack(expand=True, fill='both')
        self.boton.destroy()  # destuir el boton y dejar nomas la tabla
        self.identificar_errores()

    def identifica_tipos(self):
        arreglo1 = list(self.sinrepeticion)# convierto a lista el conjunto
        arreglo2 = self.sinvacio1 # variable en la cual iremos identificando los tipos
        # Limpieza de características que no nos sirven para encontrar los tipos de datos
        arreglo2 = [elemento for elemento in arreglo2 if elemento != ',']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != '(']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != ')']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != '{']
        arreglo2 = [elemento for elemento in arreglo2 if elemento != '}']

        self.enteros = []
        self.reales = []
        self.cadenas = []

        #expresiones regulares
        expresion_int = re.compile('1[0-9]+1')
        expresion_real = re.compile('[0-9]+.1[0-9]+1')
        expresion_cadena = re.compile('"[A-Za-z0-9]*')
        expresion = re.compile('CH[0-9A-Z_]*RA$')
        
        for i in range(len(arreglo2)):
            tempo = arreglo2[i]
            if 'ntr' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=' or expresion.match(arreglo2[f+1]) == None:
                        break
                    else:
                        self.enteros.append(arreglo2[f+1])
            if expresion_int.match(tempo) != None:
                self.enteros.append(tempo)
            if 'van' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=' or expresion.match(arreglo2[f+1]) == None:
                        break
                    else:
                        self.reales.append(arreglo2[f+1])
            if expresion_real.match(tempo) != None:
                self.reales.append(tempo)
            if 'echi' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=' or expresion.match(arreglo2[f+1]) == None:
                        break
                    else:
                        self.cadenas.append(arreglo2[f+1])
            if expresion_cadena.match(tempo) != None:
                self.cadenas.append(tempo)
        
        for i in range(len(arreglo1)):
            tempo = arreglo1[i]
            for k in range(len(self.enteros)):
                if tempo == self.enteros[k]:
                    arreglo1[i] = 'ntr'
            for s in range(len(self.reales)):
                if tempo == self.reales[s]:
                    arreglo1[i] = 'van'
            for c in range(len(self.cadenas)):
                if tempo == self.cadenas[c]:
                    arreglo1[i] = 'echi'
        
        temporal = list(self.sinrepeticion)

        for i in range(len(arreglo1)):
            if arreglo1[i] != 'ntr' and arreglo1[i] != 'van' and arreglo1[i] != 'echi':
                arreglo1[i] = ''
            if arreglo1[i] == temporal[i]:
                arreglo1[i] = ''
    
        return arreglo1

    def identificar_errores(self):
        tokenerror = []
        lexema = []
        self.linea = []
        self.descripcion = []
        lineasanalizar = []
        funcion = []
        invocacion = []
        retorno = []
        arreglo = self.arreglosinespacios
        arreglo2 = arreglo
        expresionfunciones = re.compile('[A-Z][A-Za-z0-9]*')
        

        # Limpieza de datos
        arreglo = [elemento for elemento in arreglo if elemento != ',']
        arreglo = [elemento for elemento in arreglo if elemento != '}']
        arreglo = [elemento for elemento in arreglo if elemento != '{']

        # Identificando las lineas en las cuales hay un = de asignación y un parentesis 
        
        for i in range(len(arreglo)):
            if arreglo[i] == '=':
                lineasanalizar.append(arreglo[i-1])
                for s in range(len(arreglo)):
                    s += i
                    lineasanalizar.append(arreglo[s])
                    if arreglo[s] == ';':
                        break
        
        for i in range(len(arreglo)):
            if arreglo[i] == '(':
                if arreglo[i-2] == '=':
                    invocacion.append(arreglo[i-3])
                    invocacion.append(arreglo[i-2])
                    invocacion.append(arreglo[i-1])
                    invocacion.append(arreglo[i])
                    invocacion.append(arreglo[i+1])
                    invocacion.append(arreglo[i+2])
                    invocacion.append(arreglo[i+3])
                else:
                    funcion.append(arreglo[i-2])
                    funcion.append(arreglo[i-1])
                    funcion.append(arreglo[i])
                    funcion.append(arreglo[i+1])
                    funcion.append(arreglo[i+2])
                    funcion.append(arreglo[i+3])
            if arreglo[i] == 'return':
                retorno.append(arreglo[i+1])
                                

        for i in range(len(funcion)):
            if funcion[i] == '(':
                if funcion[i-2] == 'ntr':
                    self.enteros.append(funcion[i-1])
                elif funcion[i-2] == 'van':
                    self.reales.append(funcion[i-1])
                elif funcion[i-2] == 'echi':
                    self.cadenas.append(funcion[i-1])
                else:
                    tokenerror.append('1')
                    lexema.append(funcion[i-1])
                    self.linea.append(self.idenlinea((funcion[i-2]+' '+funcion[i-1])))
                    self.descripcion.append(self.idendescripcion('funcionindefinida'))
                    
        
        for i in range(len(invocacion)):
            if invocacion[i] == '=':
                if 'ntr' == self.identype(invocacion[i-1]):
                    if 'ntr' == self.identype(invocacion[i+1]):
                        print('es ntr')
                        for g in range(len(retorno)):
                            if self.identype(retorno[g])=='ntr':
                                print(retorno[g])
                    elif 'van' == self.identype(invocacion[i+1]) or 'echi' == self.identype(invocacion[i+1]):
                        print('no es ntr')
                        tokenerror.append('1')
                        lexema.append(invocacion[i-1])
                        self.linea.append(self.idenlinea((' = '+invocacion[i-1])))
                        self.descripcion.append(self.idendescripcion('ntr'))
                    else:
                        tokenerror.append('1')
                        lexema.append(invocacion[i-1])
                        self.linea.append(self.idenlinea((' = '+invocacion[i-1])))
                        self.descripcion.append(self.idendescripcion('ntr'))
                # elif 'van' == self.identype(invocacion[i-1]):
                #     if 'van' == self.identype(invocacion[i+1]):

            
                        


        
        for i in range(len(lineasanalizar)):
            if lineasanalizar[i] == '=':
                self.envio = lineasanalizar[i-1]
                tipo = self.identype(self.envio)
                if tipo == 'ntr':
                    operando = self.identype(lineasanalizar[i+1])
                    if operando == 'ntr':
                        if lineasanalizar[i+3] == ';':
                            break
                        else: 
                            operando2 = self.identype(lineasanalizar[i+3])
                            if operando2 == 'ntr':
                                print('')
                            else:
                                tokenerror.append('1')
                                lexema.append(lineasanalizar[i+3])
                                idlinea = lineasanalizar[i+3] + ' '+lineasanalizar[i+4]
                                self.linea.append(self.idenlinea(idlinea))
                                self.descripcion.append(self.idendescripcion(tipo))

                            # if simbolo == '+' or simbolo == '-':
                    else:
                        tokenerror.append('1')
                        lexema.append(lineasanalizar[i+1])
                        idlinea = lineasanalizar[i+1]+' '+lineasanalizar[i+2]
                        self.linea.append(self.idenlinea(idlinea))
                        self.descripcion.append(self.idendescripcion(tipo))
                if tipo == 'van':
                    operando = self.identype(lineasanalizar[i+1])
                    if operando == 'van' or operando == 'ntr':
                        if lineasanalizar[i+3] == ';':
                            break
                        else: 
                            operando2 = self.identype(lineasanalizar[i+3])
                            if operando2 == 'van' or operando == 'ntr':
                                print('')
                            else:
                                tokenerror.append('1')
                                lexema.append(lineasanalizar[i+3])
                                idlinea = lineasanalizar[i+3] + ' '+lineasanalizar[i+4]
                                self.linea.append(self.idenlinea(idlinea))
                                self.descripcion.append(self.idendescripcion(tipo))

                            # if simbolo == '+' or simbolo == '-':
                    else:
                        tokenerror.append('1')
                        lexema.append(lineasanalizar[i+1])
                        idlinea = lineasanalizar[i+1]+' '+lineasanalizar[i+2]
                        self.linea.append(self.idenlinea(idlinea))
                        self.descripcion.append(self.idendescripcion(tipo))
                if tipo == 'echi':
                    operando = self.identype(lineasanalizar[i+1])
                    if operando == 'echi':
                        if lineasanalizar[i+3] == ';':
                            break
                        else: 
                            operando2 = self.identype(lineasanalizar[i+3])
                            if operando2 == 'echi':
                                print('echi = echi + echi')
                            else:
                                tokenerror.append('1')
                                lexema.append(lineasanalizar[i+3])
                                idlinea = lineasanalizar[i+3] + ' '+lineasanalizar[i+4]
                                self.linea.append(self.idenlinea(idlinea))
                                self.descripcion.append(self.idendescripcion(tipo))

                            # if simbolo == '+' or simbolo == '-':
                    else:
                        tokenerror.append('1')
                        lexema.append(lineasanalizar[i+1])
                        idlinea = lineasanalizar[i+1]+' '+lineasanalizar[i+2]
                        self.linea.append(self.idenlinea(idlinea))
                        self.descripcion.append(self.idendescripcion(tipo))
                if tipo == 'indefinida':
                    tokenerror.append('1')
                    lexema.append(self.envio)
                    self.linea.append(self.idenlinea(self.envio))
                    self.descripcion.append(self.idendescripcion(tipo))
            
        
        
        # Imprimir Tabla

        segunda_ventana = tk.Toplevel()
        segunda_ventana.title("Tabla de error")
        
        # creando tabla
        tabla = ttk.Treeview(segunda_ventana, columns=('lexema','linea','descripcion'))
        tabla.heading('lexema', text='Lexema')
        tabla.heading('linea', text='Línea')
        tabla.heading('descripcion',text='Descripción')
        tabla.heading('#0', text='Token error')
        
        # Agregar las inrepeticion as tabla
        for i, tipo in enumerate(lexema):
            tabla.insert('', 'end', text="ErrSem "+str(i+1), values=(tipo.strip(), self.linea[i].strip(), self.descripcion[i]))
            int(i)

        #Configurando las columnas
        tabla.column('#0',anchor='center')
        tabla.column('lexema',anchor='center')
        tabla.column('linea',anchor='center')
        tabla.column('descripcion',anchor='center')
        
        segunda_ventana.geometry('+800+200')
        
        # Empaquetatabla y mostrar la master
        tabla.pack(expand=True, fill='both')
        
    
    def idendescripcion(self,tipo):
        if tipo == 'indefinida':
            return('Variable indefinida')
        elif tipo == 'ntr':
            return('Imcompatibilidad de tipos, ntr')
        elif tipo == 'echi':
            return('Imcompatibilidad de tipo, echi')
        elif tipo == 'van':
            return('Imcompatibilidad de dipo, van')
        elif tipo == 'tipofunindefi':
            return('Tipo de función indefinida')
        elif tipo == 'nohayreturn':
            return('No hay return de esta funcion')
        elif tipo == 'returnincorrectontr':
            return('Tipo de return no es ntr')
        elif tipo == 'funcionindefinida':
            return('Tipo de función indefinita')

    def idenlinea(self,tipo):
        tipo = tipo
        with open('./datos.txt', 'r') as f:
            leyendo = f.readlines()
        
        for i in range(len(leyendo)):
            if '=' in leyendo[i] or '(' in leyendo[i]:
                leyendo[i] = leyendo[i]
            else:
                leyendo[i] = ''
        for i in leyendo:
            
            if tipo in i:
                tipo = str((leyendo.index(i))+1)
                return tipo
    


    def identype(self,tipo):

        for i in range(len(self.enteros)):
            if self.enteros[i] == tipo:
                tipo = 'ntr'
                return tipo
                    
        for i in range(len(self.reales)):
            if self.reales[i] == tipo:
                tipo = 'van'
                return tipo
        
        for i in range(len(self.cadenas)):
            if self.cadenas[i] == tipo:
                tipo = 'echi'
                return tipo
            
        if tipo != 'ntr' and tipo != 'van' and tipo != 'echi':
            tipo = 'indefinida'
            return tipo
        
        

raiz = tk.Tk()
mi_ventana = Ventana(raiz)
raiz.mainloop()
