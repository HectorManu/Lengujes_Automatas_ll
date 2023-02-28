import re
from tkinter import *
from tkinter import ttk



def Lexemas(palabra):

    ident = re.compile('^CH[0-9A-Z_]*RA$')
    separadores = re.compile('[(){,};]')
    #oparit = re.compile('^[+-*/%]$')
    opasig = re.compile('=')
    retorno = re.compile('return')
    #datos = re.compile('')



    cadena = 'nt]'
    print(ident.search(cadena))

def Tipo():
    print()


def Panel():
    ventana = Tk()
    ventana.title('Lexemas')
    ventana.geometry('400x300')
    ventana['bg'] = '#fb0'

    tv = ttk.Treeview(ventana, columns=("col1"))

    tv.column("#0", width=150)
    tv.column("col1", width=150, anchor=CENTER)

    tv.heading("#0", text="Lexema", anchor=CENTER)
    tv.heading("col1", text="Tipo", anchor=CENTER)

    tv.insert("", END, text="INT", values=("INT"))

    tv.pack()
    ventana.mainloop()

palabras=[]
try:
    archivo = open("Codigo.txt","r")
    for linea in archivo:
        palabras.extend(linea.split())
        for palabra in palabras:
            print(palabras)
except FileNotFoundError:
    print("no encontrado")
except PermissionError:
    print("No permisos")
except:
    print("Ocurrio un error")