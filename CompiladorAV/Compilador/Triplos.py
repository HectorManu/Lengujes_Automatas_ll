import re
class Triplos():
  def __init__(self,por_filas):
    self.por_filas = por_filas

  def asignar_argumentos(self,limit1,limit2):
    i = limit1
    while i < limit2:
      if self.parentinic.search(self.fila[i]) != None:
        self.fila[i] = self.fila[i].replace("(","")
      if (self.ident.search(self.fila[i])) != None or (self.enteros.search(self.fila[i])) != None or (self.reales.search(self.fila[i])) != None or (self.cadenas.search(self.fila[i])) != None:
        if self.parentfin.search(self.fila[i]) != None:
          self.fila[i] = self.fila[i].replace(")","")
        if self.coma.search(self.fila[i]) != None:
          self.fila[i] = self.fila[i].replace(",","")
        self.operador1 = self.fila[i]
        self.tupla = (str(self.linea),"T1",self.operador1,"=")
        self.triplo.append(self.tupla)
        self.linea += 1
        self.fila[i] = ""
        return
      else:
        i += 1

  def encontrar_argumentos(self,limit1,limit2):
    i = limit1
    while i < limit2:
      if (self.ident.search(self.fila[i])) != None:
        if self.parentfin.search(self.fila[i]) != None:
          self.fila[i] = self.fila[i].replace(")","")
        if self.coma.search(self.fila[i]) != None:
          self.fila[i] = self.fila[i].replace(",","")
        self.argumentos.append(self.fila[i])
        self.fila[i] = ""
      else:
        i += 1
    return

  def operaciones_arit(self,limit1,limit2):
    i = limit1
    while i < limit2:
      if (self.oparit.search(self.fila[i])) != None:
        self.operando = self.fila[i]
        self.operador1 = self.fila[i-1]
        self.operador2 = self.fila[i+1]

        #Crea T1
        if "T1" not in self.fila:
          self.fila[i-1]  = "T1" #Agrego T1 a la operacion como operador1
          self.tupla = (str(self.linea),"T1",self.operador1,"=")
          self.triplo.append(self.tupla)
          self.linea += 1
          return

        else:
          self.fila[i-1:i+2] = [self.operador1]
          self.tupla = (str(self.linea),self.operador1,self.operador2,self.operando)
          self.triplo.append(self.tupla)
          self.linea += 1
          return
      i += 1

  def recorrer_codigo(self):
    self.ident = re.compile('CH[0-9A-Z_]*RA')
    self.enteros = re.compile('^-?(1\d+1)')
    self.reales = re.compile('^-?(\d+\.1\d+1)')
    self.cadenas = re.compile('"[\w]*"')
    self.oparit = re.compile('[-+*%/]')
    self.opasig = re.compile('=')
    self.funciones = re.compile(r"(?!CH|\")\b[A-Z]\w*\b(?!\")")
    self.coma = re.compile("[,]")
    self.retorno = re.compile('return')
    self.parentinic = re.compile(r"\(")
    self.parentfin = re.compile(r"\)")
    self.datos = re.compile('(van|echi|ntr)')
    i = 0
    self.linea = 1
    validar = True
    self.triplo = []
    self.fila = []
    self.argumentos=[]
    while i < len(self.por_filas):
      if validar == True:
        self.fila =  self.por_filas[i].split()
        if len(self.fila) > 1:
          self.fila[-1] = self.fila[-1][:-1]#Elimina el ; de la fila
        validar = False
      #Asignaciones
      if (self.opasig.search(self.por_filas[i])) != None and (self.oparit.search(self.por_filas[i])) == None:
        #Llamada a una funcion
        if (self.parentinic.search(self.por_filas[i])) != None:
          for argu in self.argumentos:
            for x in range(len(self.fila)):
              if (self.parentinic.search(self.fila[x]) != None):
                l1 = x
              if (self.parentfin.search(self.fila[x]))!= None:
                l2 = x+1
            self.asignar_argumentos(l1,l2)

            self.tupla = (str(self.linea),argu,"T1","=")
            self.triplo.append(self.tupla)
            self.linea += 1

          self.tupla = (str(self.linea),"",self.inicioFuncion,"JMP")
          self.triplo.append(self.tupla)
          self.linea += 1

          self.triplo[self.filaIndice] = (self.lineaFunc,"",str(self.linea),"JMP")

          self.tupla = (str(self.linea),"T1",self.valorRetorno,"=")
          self.triplo.append(self.tupla)
          self.linea += 1
          if self.datos.search(self.fila[0]) != None:
            self.tupla = (str(self.linea),self.fila[1],"T1","=")
          else:
            self.tupla = (str(self.linea),self.fila[0],"T1","=")
          self.triplo.append(self.tupla)
          self.linea += 1
          validar = True
          i += 1
        else:
            if self.fila[(self.fila.index("="))+1] != "T1" and self.fila[(self.fila.index("="))+1] != "T2":
              self.operador1 = "T1"
              self.operador2 = self.fila[(self.fila.index("="))+1]
              self.fila[(self.fila.index("="))+1] = "T1"
            else:
              self.operador1 = self.fila[(self.fila.index("="))-1]
              self.operador2 = self.fila[(self.fila.index("="))+1]
              self.fila[0:len(self.fila)] = [self.operador1]

            self.tupla = (str(self.linea),self.operador1,self.operador2,"=")
            self.triplo.append(self.tupla)
            self.linea += 1
            self.por_filas[i] = " ".join(self.fila)

      # #Aritmeticas
      elif (self.oparit.search(self.por_filas[i])) != None:
        self.operaciones_arit(0,len(self.fila))
        self.por_filas[i] = " ".join(self.fila)

      #Funciones
      elif (self.funciones.search(self.por_filas[i])) != None and (self.parentinic.search(self.por_filas[i])) != None:
        self.tupla = (str(self.linea),"","","JMP")
        self.triplo.append(self.tupla)
        self.lineaFunc = str(self.linea) #numero de fila
        self.filaIndice = len(self.triplo) - 1 #Indice de la fila a editar
        self.linea += 1
        self.inicioFuncion = str(self.linea)
        #if para saber si existen variables en self.por_filas[i], si no aumentar 1 a i
        for x in range(len(self.fila)):
          if (self.parentinic.search(self.fila[x]) != None):
            l1 = x
          if (self.parentfin.search(self.fila[x]))!= None:
            l2 = x+1
        self.encontrar_argumentos(l1,l2)
        self.por_filas[i] = " ".join(self.fila)
        validar = True
        i += 1

      #Returns
      elif (self.retorno.search(self.por_filas[i])) != None:
        self.valorRetorno = self.fila[-1]

        self.triplo[self.filaIndice] = (self.lineaFunc,"",str(self.linea + 1),"JMP")

        self.tupla = (str(self.linea),"","","JMP")
        self.triplo.append(self.tupla)
        self.lineaFunc = str(self.linea) #numero de fila
        self.filaIndice = len(self.triplo) - 1 #Indice de la fila a editar
        self.linea += 1

        validar = True
        i += 1
      else:
        validar = True
        i += 1
