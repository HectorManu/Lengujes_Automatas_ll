import re

class OptimizarCodigo():
  def __init__(self,por_filas):
    self.por_filas = por_filas

  def eliminarFuncion(self):
    existe = False
    for i in range(len(self.por_filas)):
      if (self.opasig.search(self.por_filas[i])) == None and (self.funciones.search(self.por_filas[i])) != None:
        inicio = i
        existe = True
        func = self.funciones.search(self.por_filas[i])
        self.nombreFuncion1 = func.group(0)

      if existe:
        if (self.opasig.search(self.por_filas[i])) != None and (self.funciones.search(self.por_filas[i])) != None:
          self.validar = True
          func = self.funciones.search(self.por_filas[i])
          self.nombreFuncion2 = func.group(0)

        if "}" in self.por_filas[i]:
          if self.validar == False:
            self.nombreFuncion1 = ""
            existe = False
          else:
            fin = i
            break

    if self.validar:
      for i in range(len(self.por_filas)):
        if i < inicio or i > fin:
          self.nuevoCodigo.append(self.por_filas[i])

  def modificarLLmado(self):
    for i in range(len(self.nuevoCodigo)):
      if (self.opasig.search(self.nuevoCodigo[i])) != None and (self.funciones.search(self.nuevoCodigo[i])) != None:
        func = self.funciones.search(self.nuevoCodigo[i])
        func = func.group(0)
        if func == self.nombreFuncion1:
          self.nuevoCodigo[i] = self.nuevoCodigo[i].replace(self.nombreFuncion1,self.nombreFuncion2)

  def crearArchivo(self):
      with open("cOptimizado.txt", "w") as archivo:
        for linea in self.nuevoCodigo:
          archivo.write(linea + "\n")


  def recorrerCodigo(self):
    self.funciones = re.compile(r"(?!CH|\")\b[A-Z]\w*\b(?!RA|\")")
    self.parentinic = re.compile(r"\(")
    self.opasig = re.compile('=')
    self.nuevoCodigo = []
    self.validar = False

    self.eliminarFuncion()

    if self.validar == True:
      self.modificarLLmado()

    self.crearArchivo()


