import tkinter as tk
from tkinter import ttk
import re

class Ventana:
    def __init__(self, master):
        self.master = master
        
        # HACEMOS EL BOTON
        self.boton = tk.Button(self.master, text='Imprimir tablas', command=self.datosprimeratabla)
        self.boton.pack(pady=20)

        # arreglos necesarios para la segunda tabla
        self.tokenerror = []
        self.lexema = []
        self.linea = []
        self.descripcion = []
        self.funcion = []
        self.lineasanalizar = []
        self.invocacion = []

# En este método nosotros mostramos la tabla
    def datosprimeratabla(self):
        self.master.title('Tabla de símbolos')


        # Abrir archivo para imprimir en tabla
        with open('./datos.txt', 'r') as f:

            # esto nos devuelve una cadena de todo el texto
            leyendo = f.read()

            # nos separa en base a los espacios y guarda en un arreglo
            separando_lineas = leyendo.split(' ')

            # utilizamos self. para que otros metodos de la clase puedan acceder a la variable
            self.arreglosinespacios = separando_lineas

            # creo esta variable para guardar un string temporal y sobreecribir en el ciclo for
            nueva_arreglosinespacios = ""
            
            for i in range(len(self.arreglosinespacios)):
                tempo = self.arreglosinespacios[i]
                for caracter in tempo:
                    # en caso de encontrarse esta variable
                    if caracter == "\n":
                        # se añade con dos espacios a los lados
                        nueva_arreglosinespacios += " \n "
                    else:
                        # para poder guardar todas las variables
                        nueva_arreglosinespacios += caracter
                #guardamos
                self.arreglosinespacios[i] = nueva_arreglosinespacios
                # volvemos a nada la variable para no concadenar
                nueva_arreglosinespacios = ''
            
            # unimos el arreglo con espacios debido a que antes teniamos ';\n' juntos
            cadenatemporal = " ".join(self.arreglosinespacios)
            # como ya añadimos espacios en el for de arriba ahora separamos el arreglo
            # quedando ';' '\n'
            self.arreglosinespacios = cadenatemporal.split(" ")

        # eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
        self.sinvacio1 = [elemento for elemento in self.arreglosinespacios if elemento != ""]
        self.sinvacio = [elemento for elemento in self.sinvacio1 if elemento != '\n']

        # Para eliminar los valores repeditos
        # usamos set ya que en python un conjunto no tiene variables repetidas
        self.sinrepeticion = set(self.sinvacio)

        self.imprimirprimeratabla()

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

        # declaramos estas variables para poder ser utilizados
        # por todos los métodos 
        self.enteros = []
        self.reales = []
        self.cadenas = []

        #expresiones regulares
        expresion_int = re.compile('1[0-9]+1')
        expresion_real = re.compile('[0-9]+.1[0-9]+1')
        expresion_cadena = re.compile('"[A-Za-z0-9]"*')
        expresion = re.compile('CH[0-9A-Z_]*RA$')
        
        # aqui analizamos si encontramos una declaración de variable
        # entonces en base a esa declaración guardamos la variable siguiente
        # también e evalua que cumpla con la expresión regular de variables
        for i in range(len(arreglo2)):
            tempo = arreglo2[i]
            if 'ntr' == tempo:
                for f in range(len(arreglo2)):
                    f += i
                    if arreglo2[f+1] == ';' or arreglo2[f+1] == '\n' or arreglo2[f+1] == '=' or expresion.match(arreglo2[f+1]) == None:
                        break
                    else:
                        # Se usa por primera vez el método para añadir a un arreglo una variable
                        self.enteros.append(arreglo2[f+1])

            # se evalua que cumpla la expreción regular con match
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
        
        # aquí eliminamos de arreglo1 que es donde tenemos las variables no repetidas
        # encaso de encontrarse las variables iguales se coloca el tipo de dato que es
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

        # como los tipos de datos se encuentran en el arreglo que no se repite
        # eliminamos del lado de la tabla de tipo si encuentra el tipo en la misma linea
        for i in range(len(arreglo1)):
            if arreglo1[i] != 'ntr' and arreglo1[i] != 'van' and arreglo1[i] != 'echi':
                arreglo1[i] = ''
            if arreglo1[i] == temporal[i]:
                arreglo1[i] = ''
    
        # Retornamos areglo1 con los tipos de variable
        return arreglo1

    def identificar_errores(self):

        # Arreglos para este metodo
        arreglo = self.arreglosinespacios
        

        # Limpieza de datos
        arreglo = [elemento for elemento in arreglo if elemento != ',']
        arreglo = [elemento for elemento in arreglo if elemento != '}']
        arreglo = [elemento for elemento in arreglo if elemento != '{']

        # Identificando las lineas en las cuales hay un = de asignación y un parentesis 
        
        for i in range(len(arreglo)):
            if arreglo[i] == '=':
                self.lineasanalizar.append(arreglo[i-1])
                for s in range(len(arreglo)):
                    s += i
                    self.lineasanalizar.append(arreglo[s])
                    if arreglo[s] == ';':
                        break
        
        # En esta parte se guardan los metodos y return en un arreglo 
        # ejemplo se guarda tipo funcion ( variable ) { return variable} 
        for i in range(len(arreglo)):
            if arreglo[i] == '(':
                if arreglo[i-2] == '=':
                    self.invocacion.append(arreglo[i-3])
                    self.invocacion.append(arreglo[i-2])
                    self.invocacion.append(arreglo[i-1])
                    self.invocacion.append(arreglo[i])
                    self.invocacion.append(arreglo[i+1])
                    self.invocacion.append(arreglo[i+2])
                    self.invocacion.append(arreglo[i+3])
                else:
                    self.funcion.append(arreglo[i-2])
                    self.funcion.append(arreglo[i-1])
                    self.funcion.append(arreglo[i])
                    self.funcion.append(arreglo[i+1])
                    self.funcion.append(arreglo[i+2])
                    self.funcion.append(arreglo[i+3])
            if arreglo[i] == 'return':
                self.funcion.append(arreglo[i])
                self.funcion.append(arreglo[i+1])
                                
        # Aqui guardamos en la variable global de enteros o reales o cadenas
        # El tipo de función que es es decir tipo Funcion ( variable )
        # EL NOMBRE DE LA FUNCIÓN SE GUARDA EN LAS CADENAS GLOBALES
        for i in range(len(self.funcion)):
            if self.funcion[i] == '(':
                # es un i-2 debido a que encontramos esto ['tipo', 'funcion', '(',]
                if self.funcion[i-2] == 'ntr':
                    self.enteros.append(self.funcion[i-1])
                elif self.funcion[i-2] == 'van':
                    self.reales.append(self.funcion[i-1])
                elif self.funcion[i-2] == 'echi':
                    self.cadenas.append(self.funcion[i-1])
                else:
                    # En caso de que no haya tipo se guarda como un ERROR INDEFINIDO
                    self.rellenaerrores('1',self.funcion[i-1],self.idenlinea((self.funcion[i-2]+' '+self.funcion[i-1])),self.idendescripcion('funcionindefinida'))
                    
        # Aqui validamos que cuando se invoque una función como variable = funcion ( variable )
        # se pasen los valores correctos que recibe la variable 
        for i in range(len(self.invocacion)):
            if self.invocacion[i] == '=':
                # PRIMERA VEZ QUE USAMOS EL MÉTODO IDENTYPE
                # el cual ya tiene arreglos con entero, real, cadena 
                # en esos arreglos tiene los nombres de las variables
                # al invocarse nos devuelve el tipo 
                if 'ntr' == self.identype(self.invocacion[i-1]):
                    # aquí en en i+1 es igual a analizar el nombre de la función y el tipo que ya debe estar guardado
                    if 'ntr' == self.identype(self.invocacion[i+1]):
                        # CHRA =                  Funcion (          CHRA ,               )
                        # primer uso de self.invocacion metodo
                        error = self.invocacionmetodo(self.invocacion[i+1],self.invocacion[i+3])
                        if error == 'ntr':
                            self.rellenaerrores('1',self.invocacion[i+3],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('ntr'))   
                        elif error == 'van':
                            self.rellenaerrores('1',self.invocacion[i+3],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('van'))
                        elif error == 'echi':
                            self.rellenaerrores('1',self.invocacion[i+3],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('echi'))
                        elif error == 'indefinida':
                            self.rellenaerrores('1',self.invocacion[i+3],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('indefinida'))
                        else:
                            print(self.invocacion[i+3])
                            if self.invocacion[i+4] == ',':
                                print('encontre un pinche ,')
                            print(error+'linea 243')
                    elif 'van' == self.identype(self.invocacion[i+1]) or 'echi' == self.identype(self.invocacion[i+1]):
                        self.rellenaerrores('1',self.invocacion[i-1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('indefinida'))
                    else:
                        self.rellenaerrores('1',self.invocacion[i-1],self.idenlinea((' = '+self.invocacion[i-1])),self.idendescripcion('ntr'))
                elif 'van' == self.identype(self.invocacion[i-1]):
                    if 'van' == self.identype(self.invocacion[i+1]) or 'ntr' == self.identype(self.invocacion[i+1]):
                        # CHRA =                  Funcion (          CHRA               )
                        error = self.invocacionmetodo(self.invocacion[i+1],self.invocacion[i+3])
                        if error == 'ntr':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('ntr'))
                        elif error == 'van':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('van'))
                        elif error == 'echi':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('echi'))
                        elif error == 'indefinida':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('indefinda'))
                        else:
                            print(error+'linea 243')
                    elif 'echi' == self.identype(self.invocacion[i+1]):
                        self.rellenaerrores('1',self.invocacion[i-1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('van'))
                    else:
                        self.rellenaerrores('1',self.invocacion[i-1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('indefinda'))
                elif 'echi' == self.identype(self.invocacion[i-1]):
                    
                    if 'echi' == self.identype(self.invocacion[i+1]):
                        # CHRA =                  Funcion (          CHRA               )
                        error = self.invocacionmetodo(self.invocacion[i+1],self.invocacion[i+3])
                        if error == 'ntr':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('ntr'))
                        elif error == 'van':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('van'))
                        elif error == 'echi':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('echi'))
                        elif error == 'indefinida':
                            self.rellenaerrores('1',self.invocacion[i+1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('indefinda'))
                        else:
                            print(error+'linea 243')
                    elif 'van' == self.identype(self.invocacion[i+1]) or 'ntr' == self.identype(self.invocacion[i+1]):
                        self.rellenaerrores('1',self.invocacion[i-1],self.idenlinea((' = '+self.invocacion[i-1])),self.idendescripcion('echi'))
                    else:
                        self.rellenaerrores('1',self.invocacion[i-1],self.idenlinea((self.invocacion[i-1]+' '+self.invocacion[i]+' '+self.invocacion[i+1])),self.idendescripcion('indefinida'))
                else:
                    if 'ntr' == self.identype(self.invocacion[i+1]):
                        print('en efecto ')
                    else:
                        print('en efecto no existe')

        self.identificandoerroresdos()
        self.imprimirlasegundatabla()

    def invocacionmetodo(self,uno,dos):
        # aqui se le mandan dos parámetros el cual es el nombre de la funciion
        # y también se le manda qué es lo que le enviamos cuando 
        # variable = funcion ( variable )
        #             uno       dos
        for i in range(len(self.funcion)):
            if uno in self.funcion[i]:
                # Funcion ( int entrada )
                entrada = self.funcion[i+3]
                if self.identype(entrada) == 'ntr':
                    if self.identype(dos ) == 'ntr':
                        return('Es correcto')
                    elif self.identype(dos) == 'van' or self.identype(dos) == 'echi':
                        return('ntr')
                    else:
                        return('indefinida')
                elif self.identype(entrada) == 'van':
                    if self.identype(dos) == 'van' or self.identype(dos) == 'ntr':
                        return('Correcto')
                    elif self.identype(dos) == 'echi':
                        return('van')
                    else:
                        return('indefinida')
                elif self.identype(entrada) == 'echi':
                    if self.identype(dos) == 'echi':
                        return('Correcto')
                    elif self.identype(dos) == 'van' or self.identype(dos) == 'ntr':
                        return('echi')
                    else:
                        return('indefinida')

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
        # abrimos el archivo
        with open('./datos.txt', 'r') as f:
            # separamos el archivo en un arreglo de acuerdo a los saltos de línea
            leyendo = f.readlines()
        
        # limpiamos el arreglo si se encuentra = ()
        for i in range(len(leyendo)):
            if '=' in leyendo[i] or '(' in leyendo[i]:
                leyendo[i] = leyendo[i]
            else:
                leyendo[i] = ''

        # for para encontrar coincidencia del tipo 
        # tipo es el código y buscamos en qué indice se encuentra
        # ya que el indice es el número de línea
        for i in leyendo:
            if tipo in i:
                tipo = str((leyendo.index(i))+1)
                return tipo

    def identype(self,tipo):
        # aquí recorremos los arreglos de tipos 
        # que previamente se llenaron
        # buscamos coincidencias en todos 
        # de encontrar coincidencia en uno retorna

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

    def rellenaerrores(self,dato1,dato2,dato3,dato4):
        self.tokenerror.append(dato1)
        self.lexema.append(dato2)
        self.linea.append(dato3)
        self.descripcion.append(dato4)

    def imprimirprimeratabla(self):
        # creando tabla
        tabla = ttk.Treeview(self.master, columns=('tipo', 'lexema','valor'))
        tabla.heading('valor',text='Valor')
        tabla.heading('lexema', text='Lexemas')
        tabla.heading('tipo', text='Tipo')
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

    def imprimirlasegundatabla(self):
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
        for i, tipo in enumerate(self.lexema):
            tabla.insert('', 'end', text="ErrSem "+str(i+1), values=(tipo.strip(), self.linea[i].strip(), self.descripcion[i]))
            # volerlo int para que pueda seguir el ciclo
            int(i)

        #Configurando las columnas
        tabla.column('#0',anchor='center')
        tabla.column('lexema',anchor='center')
        tabla.column('linea',anchor='center')
        tabla.column('descripcion',anchor='center')
        
        segunda_ventana.geometry('+800+200')
        
        # Empaquetatabla y mostrar la master
        tabla.pack(expand=True, fill='both')

    def identificandoerroresdos(self):
        # Aqui analizamos si las reglas aritmeticas se cumplen e decir entero = entero + entero 
        for i in range(len(self.lineasanalizar)):
            if self.lineasanalizar[i] == '=':
                self.envio = self.lineasanalizar[i-1]
                tipo = self.identype(self.envio)
                if tipo == 'ntr':
                    operando = self.identype(self.lineasanalizar[i+1])
                    if operando == 'ntr':
                        if self.lineasanalizar[i+3] == ';':
                            break
                        else: 
                            operando2 = self.identype(self.lineasanalizar[i+3])
                            if operando2 == 'ntr':
                                print('')
                            else:
                                self.rellenaerrores('1',self.lineasanalizar[i+3],self.idenlinea((' '+self.lineasanalizar[i+3] + ' '+self.lineasanalizar[i+4])),self.idendescripcion(tipo))
                            # if simbolo == '+' or simbolo == '-':
                    else:
                        self.rellenaerrores('1',self.lineasanalizar[i+1],self.idenlinea((' '+self.lineasanalizar[i+1]+' '+self.lineasanalizar[i+2])),self.idendescripcion(tipo))
                if tipo == 'van':
                    operando = self.identype(self.lineasanalizar[i+1])
                    if operando == 'van' or operando == 'ntr':
                        if self.lineasanalizar[i+3] == ';':
                            break
                        else: 
                            operando2 = self.identype(self.lineasanalizar[i+3])
                            if operando2 == 'van' or operando2 == 'ntr':
                                print('')
                            else:
                                self.rellenaerrores('1',self.lineasanalizar[i+3],self.idenlinea((' '+self.lineasanalizar[i+3] + ' '+self.lineasanalizar[i+4])),self.idendescripcion(tipo))
                            # if simbolo == '+' or simbolo == '-':
                    else:
                        self.rellenaerrores('1',self.lineasanalizar[i+1],self.idenlinea((' '+self.lineasanalizar[i+1]+' '+self.lineasanalizar[i+2])),self.idendescripcion(tipo))
                if tipo == 'echi':
                    operando = self.identype(self.lineasanalizar[i+1])
                    if operando == 'echi':
                        if self.lineasanalizar[i+3] == ';':
                            break
                        else: 
                            operando2 = self.identype(self.lineasanalizar[i+3])
                            if operando2 == 'echi':
                                print('echi = echi + echi')
                            else:
                                self.rellenaerrores('1',self.lineasanalizar[i+3],self.idenlinea((self.lineasanalizar[i+3] + ' '+self.lineasanalizar[i+4])),self.idendescripcion(tipo))
                            # if simbolo == '+' or simbolo == '-':
                    else:
                        self.rellenaerrores('1',self.lineasanalizar[i+1],self.idenlinea((' '+self.lineasanalizar[i+1]+' '+self.lineasanalizar[i+2])),self.idendescripcion(tipo))
                if tipo == 'indefinida':
                    self.rellenaerrores('1',self.envio,self.idenlinea(self.envio),self.idendescripcion(tipo))
# raiz es nuestro objeto 
raiz = tk.Tk()

#llamamos a la clase y le pasamos el objeto
mi_ventana = Ventana(raiz)

# ciclo infinito para imprimir la gráfica   
raiz.mainloop()
