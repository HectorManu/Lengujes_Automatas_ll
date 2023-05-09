import re

class Tabla_Lexemas():
    def __init__(self,por_cadenas):
        self.por_cadenas = por_cadenas

    def analizar_lexema(self,palabra):
        self.ident = re.compile('CH[0-9A-Z_]*RA')
        self.separadrs1 = re.compile('[({]')
        self.separadrs2 = re.compile('[,;)}]')
        self.oparit = re.compile('[-+*%/]')
        self.opasig = re.compile('=')
        self.funciones = re.compile(r"(?!CH|\")\b[A-Z]\w*\b(?!\")")
        self.retorno = re.compile('return')
        self.datos = re.compile('(van|echi|ntr)')
        self.enteros = re.compile('^-?(1\d+1)')
        self.reales = re.compile('^-?(\d+\.1\d+1)')
        self.cadenas = re.compile('"[\w]*"')

        if (self.separadrs1.search(palabra)) != None:
            cad = self.separadrs1.search(palabra)
            return cad.group(0)
        elif (self.funciones.search(palabra)) != None:
            cad = self.funciones.search(palabra)
            return cad.group(0)
        elif (self.datos.search(palabra)) != None:
            cad = self.datos.search(palabra)
            return cad.group(0)
        elif (self.ident.search(palabra)) != None:
            cad = self.ident.search(palabra)
            return cad.group(0)
        elif (self.cadenas.search(palabra)) != None:
            cad = self.cadenas.search(palabra)
            return cad.group(0)
        elif (self.opasig.search(palabra)) != None:
            cad = self.opasig.search(palabra)
            return cad.group(0)
        elif (self.enteros.search(palabra)) != None:
            cad = self.enteros.search(palabra)
            return cad.group(0)
        elif (self.reales.search(palabra)) != None:
            cad = self.reales.search(palabra)
            return cad.group(0)
        elif (self.oparit.search(palabra)) != None:
            cad = self.oparit.search(palabra)
            return cad.group(0)
        elif (self.retorno.search(palabra)) != None:
            cad = self.retorno.search(palabra)
            return cad.group(0)
        elif (self.separadrs2.search(palabra)) != None:
            cad = self.separadrs2.search(palabra)
            return cad.group(0)
        else:
            return ""

    def analizar_tipo_dato(self):
        if (self.datos.search(self.lexema)) != None:
            return 1
        elif (self.ident.search(self.lexema)) != None:
            return 2
        elif (self.enteros.search(self.lexema)) != None:
            return 3
        elif (self.reales.search(self.lexema)) != None:
            return 4
        elif (self.cadenas.search(self.lexema)) != None:
            return 5
        elif self.lexema == ";":
            return 6
        elif self.lexema == "(":
            self.r = True
            return 6
        elif self.lexema == ")":
            self.r = False
            return 6
        else:
            return 0

    def recorrer_archivo(self):
        self.column_tipos = []       #columna tipo
        self.column_lexemas = []    #almacena los lexemas sin repetir (columna lexemas)
        cont = 0
        swich = True
        ntipo = ""
        self.r=False

        while cont < len(self.por_cadenas):
            if swich == True: #Cambia a la cadena siguiente
                self.cadena = self.por_cadenas[cont]
                swich = False
            self.lexema = self.analizar_lexema(self.cadena) #se filtra la cadena y se obtiene 1 lexema
            if self.lexema == "": #Se ejecuta cuando se analizan todos los elementos de la cadena
                cont += 1
                swich = True
            #Elemina los lexemas repetidos y maneja algunos tipos de datos
            elif self.lexema in  self.column_lexemas:
                self.cadena = self.cadena.replace(self.lexema,"")  #Elimina el lexema repetido de la cadena
                #Almacena el tipo de dato que sera atribuido a los identificadores
                if self.lexema == "ntr" or self.lexema == "van" or self.lexema == "echi":
                    ntipo = self.lexema
                #Establece el tipo de dato en vacio en caso de leer ; o =
                elif self.lexema == ";" or self.lexema == "=":
                    ntipo = ""
                elif self.lexema == "(":
                    self.r = True
                elif self.lexema == ")":
                    self.r = False
                elif self.lexema == ",":
                    if self.r == True:
                        ntipo = ""
            #Comrpueba el tipo de dato del lexema a agregar
            else:
                n = self.analizar_tipo_dato()        #se llama a la funcion tipos y se le manda el lexema
                if n == 1:
                    ntipo = self.lexema
                    self.column_tipos.append("")
                elif n == 2:
                    self.column_tipos.append(ntipo) #se agrega a la tabla el lexema (van,ntr o echi)
                elif n == 3:
                    self.column_tipos.append("ntr")
                elif n == 4:
                    self.column_tipos.append("van")
                elif n == 5:
                    self.column_tipos.append("echi")
                elif n == 6:
                    ntipo = ""
                    self.column_tipos.append(ntipo)
                else:
                    self.column_tipos.append("")  #agrega un espacio vacio a los lexemas que no sean ntr,van o echi
                self.column_lexemas.append(self.lexema)  #se agrega el lexema a la tabla
                self.cadena = self.cadena.replace(self.lexema,"")  #se elimina el lexema de la cadena