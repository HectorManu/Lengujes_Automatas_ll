import re
import tkinter as tk

identificadores = re.compile('CH[0-9A-Z_]*RA')
separadores = re.compile('[(){,};]')
cadena = '(CH_RA,)'
print (identificadores.match(cadena))



# Crear la ventana principal
root = tk.Tk()

# Crear la tabla
table = tk.Frame(root)
table.pack()

# Crear las dos columnas
col1 = tk.Label(table, text="Columna 1")
col1.grid(row=0, column=0)

col2 = tk.Label(table, text="Columna 2")
col2.grid(row=0, column=1)

# Agregar datos a la tabla
dato1 = tk.Label(table, text="Dato 1")
dato1.grid(row=1, column=0)

dato2 = tk.Label(table, text="Dato 2")
dato2.grid(row=1, column=1)

dato3 = tk.Label(table, text="Dato 3")
dato3.grid(row=2, column=0)

dato4 = tk.Label(table, text="Dato 4")
dato4.grid(row=2, column=1)

# Iniciar el loop principal de la ventana
root.mainloop()
#if (len(separadores.findall(cadena))) > 1: