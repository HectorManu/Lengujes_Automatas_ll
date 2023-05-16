import re

class Tabla_Errores():
  def __init__(self, por_filas, column_lexemas, column_tipos):
    self.por_filas = por_filas
    self.column_lexemas = column_lexemas
    self.column_tipos = column_tipos

  def analizarAsignacion(self):
    self.var1 = self.fila[(self.fila.index("=")) - 1]  #obtiene el lexema a la izq del "="
    self.var2 = self.fila[(self.fila.index("=")) + 1]   #obtiene el lexema a la der del "="
    self.tipo1 = self.column_tipos[self.column_lexemas.index(self.var1)]  #tipo de dato de var1
    self.tipo2 = self.column_tipos[self.column_lexemas.index(self.var2)]  #tipo de dato de var2

    #error de asignacion con variable indefinida
    if self.tipo1 == "" or self.tipo2 == "":
      tipovacio = []
      if self.tipo1 == "":
        tipovacio.append(self.var1)
      if self.tipo2 == "":
        tipovacio.append(self.var2)
      varnd = ",".join(tipovacio) #almacena las viariables no definidas
      self.tupla = ("Errsem"+str(self.ertoken),varnd,self.linea_error,"Variable indefinida")
      self.tabla.append(self.tupla)
      self.ertoken += 1

    # errores de asignacion de incompatibilidad  #
    elif self.tipo1 == "ntr":
      if (self.asigntr.search(self.tipo2)) != None:
        self.tupla = ("Errsem"+str(self.ertoken),self.var2,self.linea_error,"Incompatibilidad de tipo " + self.tipo1)
        self.tabla.append(self.tupla)
        self.ertoken += 1
    elif self.tipo1 == "van":
      if (self.asigvan.search(self.tipo2)) != None:
        self.tupla = ("Errsem"+str(self.ertoken),self.var2,self.linea_error,"Incompatibilidad de tipo " + self.tipo1)
        self.tabla.append(self.tupla)
        self.ertoken += 1
    elif self.tipo1 == "echi":
      if (self.asigechi.search(self.tipo2)) != None:
        self.tupla = ("Errsem"+str(self.ertoken),self.var2,self.linea_error,"Incompatibilidad de tipo " + self.tipo1)
        self.tabla.append(self.tupla)
        self.ertoken += 1
    return


  def analizarFuncion(self):
    self.funcionName = (self.funciones.search(self.por_filas[self.x]).group(0)) #guarda el nombre de la funcion
    self.argumentos = []
    self.tipoArgumentos=[]
    self.tipoFuncion = self.fila[0] #guarda el tipo de la funcion

    #Obtiene la posicioon del parentesis "("
    for x in range(len(self.fila)):
      if self.parentinic.search(self.fila[x]) != None:
        inic = x
        break

    #Se obtienen los argumentos de la funcion
    for x in range(inic,len(self.fila)):
      if self.ident.search(self.fila[x]) != None:
        self.argumentos.append(self.ident.search(self.fila[x]).group(0)) #Obtiene los argumentos de la funcion
        ident = (self.ident.search(self.fila[x]).group(0))
        self.tipoArgumentos.append(self.column_tipos[self.column_lexemas.index(ident)]) #Obtiene el tipo de dato de cada argumento

    #Si un argumento no esta declarado
    if "" in self.tipoArgumentos:
      arguvacio=[]
      for x in range(len(self.tipoArgumentos)):
        if self.tipoArgumentos[x] == "":
          arguvacio.append(self.argumentos[x])
      argund = ",".join(arguvacio) #almacena las viariables no definidas
      self.tupla = ("Errsem"+str(self.ertoken),argund,self.linea_error,"Variable indefinida")
      self.tabla.append(self.tupla)
      self.ertoken += 1
    return

  def analizarReturn(self):
    self.varReturn = self.fila[1] #Nombre del return
    self.tipoReturn = self.column_tipos[self.column_lexemas.index(self.varReturn)] #Tipo del return

    # Valida que el valor de retorno no sea una variable indefinida #
    if self.tipoReturn == "":
      self.tupla = ("Errsem"+str(self.ertoken),self.varReturn,self.linea_error,"Variable indefinida")
      self.tabla.append(self.tupla)
      self.ertoken += 1

    #  Valida que el tipo dato de retorno sea el mismo que el de la funcion  #
    elif self.tipoFuncion != self.tipoReturn:
      self.tupla = ("Errsem"+str(self.ertoken),self.varReturn,self.linea_error,"Incompatibilidad de tipo " + self.tipoFuncion)
      self.tabla.append(self.tupla)
      self.ertoken += 1
    return

  def analizarArgumentos(self,palabra):
    self.enteros = re.compile('^-?(1\d+1)')
    self.reales = re.compile('^-?(\d+\.1\d+1)')
    self.cadenas = re.compile('"[\w]*"')
    if (self.ident.search(palabra)) != None:
      cad = self.ident.search(palabra)
      return cad.group(0)
    elif (self.enteros.search(palabra)) != None:
      cad = self.enteros.search(palabra)
      return cad.group(0)
    elif (self.reales.search(palabra)) != None:
      cad = self.reales.search(palabra)
      return cad.group(0)
    elif (self.cadenas.search(palabra)) != None:
      cad = self.cadenas.search(palabra)
      return cad.group(0)

  def analizarLlamadaFuncion(self):
    self.funcionName2 = (self.funciones.search(self.por_filas[self.x]).group(0)) #guarda el nombre de la funcion
    self.argumentos2 = []
    self.tipoArgumentos2 =[]
    self.var1 = self.fila[(self.fila.index("=")) - 1]  #obtiene el lexema a la izq del "="
    self.tipo1 = self.column_tipos[self.column_lexemas.index(self.var1)]  #tipo de dato de var1

    #Obtiene la posicioon del parentesis "("
    for x in range(len(self.fila)):
      if self.parentinic.search(self.fila[x]) != None:
        inic = x
        self.fila[x] = self.fila[x].replace("(","")
        break

    #Se obtienen los argumentos de la funcion
    for x in range(inic,len(self.fila)):

      if self.analizarArgumentos(self.fila[x]) != None:
        self.argumentos2.append(self.analizarArgumentos(self.fila[x])) #Obtiene los argumentos de la funcion
        variable = (self.analizarArgumentos(self.fila[x]))
        self.tipoArgumentos2.append(self.column_tipos[self.column_lexemas.index(variable)]) #Obtiene el tipo de dato de cada argumento

    ###  valida que la variable a la izq del "=" o que la funcion llamada no sean indefinidinas  ###
    if self.tipo1 == "" or self.funcionName != self.funcionName2:
      if self.tipo1 == "":
        self.tupla = ("Errsem"+str(self.ertoken),self.var1,self.linea_error,"Variable indefinida")
        self.tabla.append(self.tupla)
        self.ertoken += 1
      else:
        self.tupla = ("Errsem"+str(self.ertoken),self.funcionName2,self.linea_error,"Variable indefinida")
        self.tabla.append(self.tupla)
        self.ertoken += 1

    #Valida que los argumentos enviados esten declarados#
    elif "" in self.tipoArgumentos2:
      arguvacio=[]
      for x in range(len(self.tipoArgumentos2)):
        if self.tipoArgumentos2[x] == "":
          arguvacio.append(self.argumentos2[x])
      argund = ",".join(arguvacio) #almacena las viariables no definidas
      self.tupla = ("Errsem"+str(self.ertoken),argund,self.linea_error,"Variable indefinida")
      self.tabla.append(self.tupla)
      self.ertoken += 1


    #  Valida que los argumentos sean del mismo tipo  #
    elif not any(self.tipoArgumentos == self.tipoArgumentos2[i:i+len(self.tipoArgumentos)] for i in range(len(self.tipoArgumentos2) - len(self.tipoArgumentos)+1)):
      arguvacio=[]
      argutipovacio=[]
      for x in range(len(self.tipoArgumentos)):
        if self.tipoArgumentos[x] != self.tipoArgumentos2[x]:
          arguvacio.append(self.argumentos2[x])
          argutipovacio.append(self.tipoArgumentos[x])
      argund = ",".join(arguvacio) #almacena las viariables no definidas
      argutipond = ",".join(argutipovacio)
      self.tupla = ("Errsem"+str(self.ertoken),argund,self.linea_error,"Incompatibilidad de tipo " + argutipond)
      self.tabla.append(self.tupla)
      self.ertoken += 1


    #Validar el dato a la izq del "=" sea del mismo tipo que el del valor retornado#
    elif self.tipo1 != self.tipoReturn:
      if self.tipo1 == "van":
        if self.tipoReturn == "echi":
          self.tupla = ("Errsem"+str(self.ertoken),self.varReturn,self.linea_error,"Incompatibilidad de tipo " + self.tipo1)
          self.tabla.append(self.tupla)
          self.ertoken += 1
      else:
        self.tupla = ("Errsem"+str(self.ertoken),self.varReturn,self.linea_error,"Incompatibilidad de tipo " + self.tipo1)
        self.tabla.append(self.tupla)
        self.ertoken += 1
    return




  def recorrerCodigo(self):
    self.parentinic = re.compile('[(]')
    self.parentfin = re.compile('[)]')
    self.oparit = re.compile('[-+*%/]')
    self.ident = re.compile('CH[0-9A-Z_]*RA')
    self.funciones = re.compile(r"(?!CH|\")\b[A-Z]\w*\b(?!\")")
    self.asigntr = re.compile('^(echi|van)(;?)$')    #asignacion ntr
    self.asigvan = re.compile('^(echi)(;?)$')      #asignacion van
    self.asigechi = re.compile("^(ntr|van)(;?)$")    #asignacion echi
    self.ertoken = 1
    self.tabla = []

    for i in range(len(self.por_filas)):
      self.fila = self.por_filas[i].split()
      self.linea_error = str(i+1)
      if len(self.fila) > 1:
          self.fila[-1] = self.fila[-1][:-1]#Elimina el ; de la fila

      if "=" in self.fila and self.oparit.search(self.por_filas[i]) == None: #Asignaciones
        if self.funciones.search(self.por_filas[i]) != None: #Llamada a la funcion
          self.x = i
          self.analizarLlamadaFuncion()
        else:
          self.analizarAsignacion()
      elif self.parentinic.search(self.por_filas[i]) != None and "=" not in self.fila: #Funciones
        self.x = i
        self.analizarFuncion()
      elif "return" in self.fila: #Retornos
        self.analizarReturn()