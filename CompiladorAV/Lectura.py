class Lectura():
  def __init__(self,archivo):
    self.archivo = archivo
  def leer_archivo(self):
    self.por_cadenas = []
    self.por_filas = []
    with open(self.archivo, "r") as archivo:
      for linea in archivo:
        self.por_filas.extend(linea.splitlines())
        self.por_cadenas.extend(linea.split())