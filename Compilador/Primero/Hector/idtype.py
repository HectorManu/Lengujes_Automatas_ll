# # # Caracteres a eliminar 
# coma = ','
# puntocoma = ';'
# parentesis1 = '('
# parentesis2 = ')'
# corchete1 = '{'
# corchete2 = '}'
# saltolinea = '\n'
# comilla = '"'
# suma = '+'
# resta = '-'
# multi = '*'
# igual = '='
# subarreglo = []

# enteros_ntr = []
# reales_van = []
# cadena_echi = []


# # Abrir archivo para imprimir en tabla
# with open('./datos.txt', 'r') as f:
#     leyendo = f.read()
#     separando_lineas = leyendo.split(' ')
#     subarreglo = leyendo.split('\n')
#     # print(leyendo)
#     arreglosinespacios = separando_lineas
#     for i in range(len(arreglosinespacios)):
#         arreglosinespacios[i] = arreglosinespacios[i].replace(coma,'').replace(parentesis1,'').replace(parentesis2,'').replace(corchete1,'').replace(corchete2,'').replace(comilla,'').replace(suma,'').replace(resta,'').replace(suma,'').replace(multi,'').replace(igual,'')

# sinvacio = [elemento for elemento in arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
# sinrepeticion = set(arreglosinespacios)

# print(sinvacio)




# cadena = [";\nHola; amigo, como estas?",'hola;']
# nueva_cadena = ""

# for i in range(len(cadena)):
#     tempo = cadena[i]
#     print(type(tempo))
#     for caracter in tempo:
#         if caracter == "\n":
#             nueva_cadena += " \n "
#         else:
#             nueva_cadena += caracter
#     cadena[i] = nueva_cadena
#     nueva_cadena = ''

# print(cadena)


cadena = ["NTR",'RACH','rasd',';','\n','NTR','R2C','asdfa','=',';','VAN','asd','ijlkjlkjñlkj',';','ECHI','hola',';']
enteros = []
reales = []
cadenas = []

for i in range(len(cadena)):
    tempo = cadena[i]
    if 'NTR' == tempo:
        for f in range(len(cadena)):
            f += i
            if cadena[f+1] == ';' or cadena[f+1] == '\n' or cadena[f+1] == '=':
                break
            else:
                enteros.append(cadena[f+1])
    if 'VAN' == tempo:
        for f in range(len(cadena)):
            f += i
            if cadena[f+1] == ';' or cadena[f+1] == '\n' or cadena[f+1] == '=':
                break
            else:
                reales.append(cadena[f+1])
    if 'ECHI' == tempo:
        for f in range(len(cadena)):
            f += i
            if cadena[f+1] == ';' or cadena[f+1] == '\n' or cadena[f+1] == '=':
                break
            else:
                cadenas.append(cadena[f+1])


print(enteros)
print(reales)
print(cadenas)