# # Caracteres a eliminar 
coma = ','
puntocoma = ';'
parentesis1 = '('
parentesis2 = ')'
corchete1 = '{'
corchete2 = '}'
saltolinea = '\n'
comilla = '"'

# Abrir archivo para imprimir en tabla
with open('./datos.txt', 'r') as f:
    leyendo = f.read()
    separando_lineas = leyendo.split(' ')
    # print(leyendo)
    arreglosinespacios = separando_lineas
    for i in range(len(arreglosinespacios)):
        arreglosinespacios[i] = arreglosinespacios[i].replace(coma,'').replace(parentesis1,'').replace(parentesis2,'').replace(corchete1,'').replace(corchete2,'').replace(comilla,'')

sinvacio = [elemento for elemento in arreglosinespacios if elemento != ""] #eliminar variables vacias después de eliminar los puntos y comas y corechetes y eso
sinrepeticion = set(sinvacio)


print(separando_lineas)