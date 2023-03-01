import re

cadena = ["NTR",'RACH','rasd',';','\n','NTR','R2C','asdfa','=',';','VAN','asd','ijlkjlkjñlkj',';','ECHI','hola',';','RACH','=','1111']
enteros = []
reales = []
cadenas = []
expresion_int = re.compile('1[0-9]+1')
expresion_real = re.compile('[0-9]+.1[09]+1')
expresion_tipoentero = re.compile('CH[0-9A-Z_]*RA$')

for i in range(len(cadena)):
    tempo = cadena[i]
    if 'NTR' == tempo:
        for f in range(len(cadena)):
            f += i
            if cadena[f+1] == ';' or cadena[f+1] == '\n' or cadena[f+1] == '=':
                break
            else:
                enteros.append(cadena[f+1])
    if expresion_int.match(tempo) != None:
        print(tempo)
        # enteros.append(tempo)
        # for f in range(len(cadena)):
        #     f += i
        #     if cadena[f+1] == ';' or cadena[f+1] == '\n' or cadena[f+1] == '=':
        #         break
        #     else:
        #         enteros.append(cadena[f+1])
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