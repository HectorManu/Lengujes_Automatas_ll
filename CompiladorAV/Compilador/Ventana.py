from Lectura import *
from Tabla_Lexemas import *
from Tabla_Errores import *
from Triplos import *
from OptimizarCodigo import *
from tkinter import *
from tkinter import ttk
import tkinter as tk
import re

class Ventana():
  def __init__(self,ventana1,column_lexemas,column_tipos,tabla_errores,triplo):
    self.ventana1 = ventana1
    self.column_lexemas = column_lexemas
    self.column_tipos = column_tipos
    self.tabla_errores = tabla_errores
    self.triplo = triplo
    self.boton = tk.Button(self.ventana1, text='Imprimir tablas', command=self.imprimir_panel)
    self.boton.pack(pady=20)

  def imprimir_panel(self):
    #Tabla de lexemas
    self.ventana1.title('Tabla De Lexemas')
    self.ventana1.geometry('300x500')

    tabla1 = ttk.Treeview(self.ventana1, columns=("col1"))

    tabla1.column("#0", width=150,anchor=CENTER)
    tabla1.column("col1", width=150, anchor=CENTER)

    tabla1.heading("#0", text="Lexema", anchor=CENTER)
    tabla1.heading("col1", text="Tipo", anchor=CENTER)

    for i in range(len(self.column_lexemas)):
      tabla1.insert("", END, text=self.column_lexemas[i], values=self.column_tipos[i])
    tabla1.pack(fill=tk.BOTH, expand=True)
    self.boton.destroy()

    #Tabla de errores
    tabla2 = tk.Toplevel()
    tabla2.title('Tabla De Errores')
    tabla2.geometry('620x150')

    tabla2 = ttk.Treeview(tabla2, columns=("col1","col2","col3"))

    tabla2.column("#0", width=100, anchor=CENTER)
    tabla2.column("col1", width=150, anchor=CENTER)
    tabla2.column("col2", width=70, anchor=CENTER)
    tabla2.column("col3", width=300, anchor=CENTER)

    tabla2.heading("#0", text="Token", anchor=CENTER)
    tabla2.heading("col1", text="Lexema", anchor=CENTER)
    tabla2.heading("col2", text="Región", anchor=CENTER)
    tabla2.heading("col3", text="Descripción", anchor=CENTER)

    for token, lexema, region, descripcion in self.tabla_errores:
      tabla2.insert("", END, text=token, values=(lexema,region,descripcion))
    tabla2.pack(fill=tk.BOTH, expand=True)

    #Tabla Triplo
    tabla3 = tk.Toplevel()
    tabla3.title('Triplo')
    tabla3.geometry('620x150')

    tabla3 = ttk.Treeview(tabla3, columns=("col1","col2","col3"))

    tabla3.column("#0", width=100, anchor=CENTER)
    tabla3.column("col1", width=150, anchor=CENTER)
    tabla3.column("col2", width=70, anchor=CENTER)
    tabla3.column("col3", width=300, anchor=CENTER)

    tabla3.heading("#0", text="", anchor=CENTER)
    tabla3.heading("col1", text="Dato objetivo", anchor=CENTER)
    tabla3.heading("col2", text="Dato fuente", anchor=CENTER)
    tabla3.heading("col3", text="Operador", anchor=CENTER)

    for linea, dtoObjetivo, dtoFuente, operador in self.triplo:
      tabla3.insert("", END, text=linea, values=(dtoObjetivo,dtoFuente,operador))
    tabla3.pack(fill=tk.BOTH, expand=True)

#Clase Lectura
codigo = Lectura("Codigo2.txt")
codigo.leer_archivo()

#Clase OptimizarCodigo
optimizar = OptimizarCodigo(codigo.por_filas)
optimizar.recorrerCodigo()
if optimizar.validar == FALSE:
  codigo = Lectura("Codigo2.txt")
  codigo.leer_archivo()
else:
  codigo = Lectura("cOptimizado.txt")
  codigo.leer_archivo()

#Clase Tabla_Lexemas
T_lexemas = Tabla_Lexemas(codigo.por_cadenas)
T_lexemas.recorrer_archivo()

#Clase Tabla_Errores
T_errores = Tabla_Errores(codigo.por_filas,T_lexemas.column_lexemas, T_lexemas.column_tipos)
T_errores.recorrerCodigo()

#Clase Triplos
Triplo = Triplos(codigo.por_filas)
Triplo.recorrer_codigo()

#Clase ventana
ventana1 = tk.Tk()
tablas = Ventana(ventana1,T_lexemas.column_lexemas,T_lexemas.column_tipos, T_errores.tabla, Triplo.triplo)
ventana1.mainloop()