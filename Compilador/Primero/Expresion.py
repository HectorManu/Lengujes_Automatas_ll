import re
p = re.compile(r"""\ACH([0-9]*[A-Z]*_*)RA\Z""")
palabra = 'CHA_RA'
m = p.match(palabra)

if m is None:
    print('No valida')
else:
    print('Es valida')

print(m)

