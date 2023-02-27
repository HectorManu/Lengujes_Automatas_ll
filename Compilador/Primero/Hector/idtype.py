# # Caracteres a eliminar 
coma = ','
puntocoma = ';'
parentesis1 = '('
parentesis2 = ')'
corchete1 = '{'
corchete2 = '}'
saltolinea = '\n'
comilla = '"'
suma = '+'
resta = '-'
multi = '*'
igual = '='
subarreglo = []

# Abrir archivo para imprimir en tabla
with open('./datos.txt', 'r') as f:
    leyendo = f.read()
    separando_lineas = leyendo.split(' ')
    subarreglo = leyendo.split('\n')
    # print(leyendo)
    arreglosinespacios = separando_lineas
    for i in range(len(arreglosinespacios)):
        arreglosinespacios[i] = arreglosinespacios[i].replace(coma,'').replace(parentesis1,'').replace(parentesis2,'').replace(corchete1,'').replace(corchete2,'').replace(comilla,'').replace(suma,'').replace(resta,'').replace(suma,'').replace(multi,'').replace(igual,'')

sinvacio = [elemento for elemento in arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
sinrepeticion = set(arreglosinespacios)

print(sinvacio)


for i in range(len(sinvacio)):
    if '\n' in sinvacio[i]:
        print("encontre el caracter")
        subarreglo = sinvacio[i].split(';')
        sinvacio[i:i+1] = subarreglo