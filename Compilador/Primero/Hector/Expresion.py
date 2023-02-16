import re
#p = re.compile(r"""\ACH([0-9]*[A-Z]*_*)RA\Z""")
# palabra = 'CHA12ARA'
#m = p.match(palabra)

#if m is None:
#    print('No valida')
#else:
#    print('Es valida')

#print(m)

expresion = re.compile('CH[0-9A-Z_]*RA$')
palabra = 'CHA12ARA'
print(expresion.match(palabra))

