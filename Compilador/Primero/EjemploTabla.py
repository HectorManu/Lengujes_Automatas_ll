import tkinter as tk

class Tabla(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        tk.Frame.__init__(self, parent)
        self.tabla = []
        for i in range(rows):
            fila = []
            for j in range(columns):
                celda = tk.Label(self, text='', borderwidth=1, relief='solid')
                celda.grid(row=i, column=j, sticky='nsew')
                fila.append(celda)
            self.tabla.append(fila)
        for i in range(rows):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)

    def actualizar_celda(self, fila, columna, texto):
        self.tabla[fila][columna].config(text=texto)

root = tk.Tk()
tabla = Tabla(root)
tabla.pack(side="top", fill="both", expand=True)

    

tabla.actualizar_celda(0, 0, "Fila 1, Columna 1")
tabla.actualizar_celda(1, 1, "Fila 2, Columna 2")

root.mainloop()
