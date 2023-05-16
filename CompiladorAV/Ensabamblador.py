import re
class Ensabamblador():
  def __init__(self, por_filas, saltoFuncion, saltoLLamadaFuncion, saltoReturn, argumentosFuncion):
    self.por_filas = por_filas
    self.saltoFuncion = saltoFuncion
    self.saltoLLamadaFuncion = saltoLLamadaFuncion
    self.saltoReturn = saltoReturn
    self.argumentosFuncion = argumentosFuncion

  def generarAsignaciones(self):
    self.tabla.append("MOV AX, "+ self.operando1 + ";")
    self.tabla.append("MOV " + self.asig +", AX;")
    self.tabla.append("")

  def generarAritmeticos1(self): #2 (+ - *)

    if self.operador == "+":
      self.tabla.append("MOV AX, "+ self.operando1 + ";")
      self.tabla.append("ADD AX, "+ self.operando2 + ";")

    elif self.operador == "-":
      self.tabla.append("MOV AX, "+ self.operando1 + ";")
      self.tabla.append("SUB AX, "+ self.operando2 + ";")

    else:
      self.tabla.append("MOV AL, "+ self.operando1 + ";")
      self.tabla.append("MOV BL, "+ self.operando2 + ";")
      self.tabla.append("MUL BL")

    self.tabla.append("MOV " + self.asig +", AX;")
    self.tabla.append("")

  def generarAritmeticos2(self): #2 (/ %)

    self.tabla.append("MOV AX, "+ self.operando1 + ";")
    self.tabla.append("MOV BL, "+ self.operando2 + ";")
    self.tabla.append("DIV BL;")

    if self.operador == "/":
      self.tabla.append("MOV " + self.asig +", AL;")
    else:
      self.tabla.append("MOV " + self.asig +", AH;")

    self.tabla.append("")

  def generarLlamadaFuncion(self):
    self.enteros = re.compile('^-?(1\d+1)')
    self.reales = re.compile('^-?(\d+\.1\d+1)')
    self.cadenas = re.compile('"[\w]*"')
    self.argumentosLlamadaFuncion = []

    for i in range(len(self.fila)):
      if i > self.indice:
        if self.ident.search(self.fila[i]) != None:
          argumento = self.ident.search(self.fila[i])
          argumento = argumento.group(0)

        elif self.enteros.search(self.fila[i]) != None:
          argumento = self.enteros.search(self.fila[i])
          argumento = argumento.group(0)

        elif self.reales.search(self.fila[i]) != None:
          argumento = self.reales.search(self.fila[i])
          argumento = argumento.group(0)

        elif self.cadenas.search(self.fila[i]) != None:
          argumento = self.cadenas.search(self.fila[i])
          argumento = argumento.group(0)

        self.argumentosLlamadaFuncion.append(argumento)

    for i in range(len(self.argumentosFuncion)):
      self.tabla.append("MOV AX, "+self.argumentosLlamadaFuncion[i]+";")
      self.tabla.append("MOV "+self.argumentosFuncion[i]+", AX;")
      self.tabla.append("")

    self.tabla.append("JMP RENGLON"+self.saltoLLamadaFuncion)
    self.tabla.append("RENGLON"+self.saltoReturn+":")
    self.tabla.append("")

    self.tabla.append("MOV AX, "+self.valorRetornado+";")
    self.tabla.append("MOV "+self.asig+", AX;")
    self.tabla.append("")

  def generarTxt(self):
    with open("cEnsamblador.txt", "w") as archivo:
      for linea in self.tabla:
        archivo.write(linea + "\n")




  def recorrerCodigo(self):
    validar = True
    self.fila=[]
    self.tabla = []
    self.oparit = re.compile('[-+*%/]')
    self.aritmeticos1 = re.compile('[-+*]')
    self.aritmeticos2 = re.compile('[/%]')
    self.funciones = re.compile(r"(?!CH|\")\b[A-Z]\w*\b(?!RA|\")")
    self.ident = re.compile('CH[0-9A-Z_]*RA')

    # self.division = re.compile('[/]')
    # self.modulo = re.compile('[%]')

    for i in range(len(self.por_filas)):
      if validar == True:
          self.fila =  self.por_filas[i].split()
          if len(self.fila) > 1:
            self.fila[-1] = self.fila[-1][:-1]#Elimina el ; de la fila
          validar = False

      #4 Asignaciones
      if "=" in self.por_filas[i] and (self.oparit.search(self.por_filas[i])) == None and (self.funciones.search(self.por_filas[i])) == None:
        self.asig = self.fila[(self.fila.index("="))-1]
        self.operando1 = self.fila[(self.fila.index("="))+1]
        self.generarAsignaciones()
        validar = True


      #4 OPERACIONES ARITMETICAS
      elif (self.oparit.search(self.por_filas[i])) != None:
          self.asig = self.fila[(self.fila.index("="))-1]
          self.operando1 = self.fila[(self.fila.index("="))+1]
          self.operador = self.fila[(self.fila.index("="))+2]
          self.operando2 = self.fila[(self.fila.index("="))+3]
          validar = True
          #5 Suma,Resta y Multiplicacion
          if (self.aritmeticos1.search(self.por_filas[i])) != None:
            self.generarAritmeticos1()
          else:
          #5 Division y Modulo
            self.generarAritmeticos2()

      #4 Inicio de una Funcion
      elif (self.funciones.search(self.por_filas[i])) != None and "{" in self.por_filas[i]:
        self.funcion = self.funciones.search(self.por_filas[i])
        self.funcion = self.funcion.group(0)
        self.tabla.append("JMP RENGLON"+self.saltoFuncion)
        self.tabla.append("RENGLON"+self.saltoLLamadaFuncion+":")
        self.tabla.append("")
        validar = True

      #4 Valor de retorno
      elif "return" in self.por_filas[i]:
        self.valorRetornado = self.ident.search(self.por_filas[i])
        self.valorRetornado = self.valorRetornado.group(0)
        self.tabla.append("JMP RENGLON"+self.saltoReturn)
        self.tabla.append("")
        validar = True

      #4 Llamada de la funcion
      elif (self.funciones.search(self.por_filas[i])) != None and "=" in self.por_filas[i]:
        self.indice = self.fila.index("=") + 1
        self.asig = self.fila[(self.fila.index("="))-1]
        self.generarLlamadaFuncion()
        validar = True

      else:
        validar = True

    self.generarTxt()
