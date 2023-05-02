# Notas
# Unidad 1
## 07/02/2023

Operaón de las asignaciones la utilizaremos para evaluar el sintaxis y las reglas 

Sintaxis | Ejemplo
--- | ---
----|----

## 09/02/2023

El día de hoy se hizo el programa de Expresion.py en el se tenia que escribir la expresión regular de nuestras variablese para después esetablecerlas en python. 

```python
import re
# Expresión regular RA(0-9UA-ZU_)*RA
p = re.compile(r"""\ACH([0-9]*[A-Z]*_*)RA\Z""")
# En la cual para poder colocar más de una U (unión) se tuvo que poner las tres comillas y la letra r ya que daba un error de coincidencia el cual no es correcto
palabra = 'CHA_RA'
m = p.match(palabra)

if m is None:
    print('No valida')
else:
    print('Es valida')

print(m)

```

Lo que el programa debe de hacer es: 

Código: 
int hola, perro, loco;

Lexema | Tipo
--- | ---
int | 
hola |
perro |
loco |

La proxima clase se entrega esto:

int hola, perro, loco;

Lexema | Tipo
--- | ---
int | 
hola | int
perro | int
loco | int

Se realizó una versión mejorada del código anterior

```python
import re

palabra = 'CHA_RA'

expresion = re.compile('CH[0-9A-Z_]*RA$')

print(expresion.match(palabra))
```


## 14/02/2023

el día de hoy vamos a ver cómo está el manejo de errores

cada fase de n compiladore maneja diferente tipos de errores 

### Manejo de errores

* Fase de ánalisis léxco.
* Fase de análisis sintáctico
* Fase de análisis semántico: detecta constucciones que carecen de significacdo para la operación implicita.

### Tipos de errores semánticos

* incompatibilidad de tipos, es aquel eerror que revisa y se genera cuando no se cumplen con as reglas de los tipos de datos en la asgianaciones aritmeticas
  * Cómo detecta el error?
    * en latabla de tipos esta esta vacia 
    * 
* Indenid la varible, es cuando la variable no esta declarada.



### Ejemplo

### Actividad


**Nota**: las reglas para caracter 

## 16/02/2022

el dos de marzo vmaos a entregar la tabla de lexemas los errores tambien vamos a entregar la tabla de errores en la cual tendremos las 4 columnas simempre debe ser un error semantio el token el lexema vamos a tener cuál es el lexema que viola la regla . debemos de poner la descripción lel tio de imcompatiilidad de tipo y el tipo de arialb ede la varialbe de asignación. 

repasamos el siguiente ejemplo :

N = {s, Expr, Term}

T = {+,-,0,1,2,3,4,5,6,7,8,9}
I = S
p: 

S -> Expr
Expr -> Expr + Term | Expr - Term  | Term 
Term -> 0|1|2|3|4|5|6|7|8|9

Ejemplode suma de 1+2 

 por cada 

La tarea se nos ha dejado el realizar lo siguiente

### Tarea

Expresion regular

GLC

Relas semánticas

Aritmética

Árbol de derivación con atributos en los nodos internos (Simbolos no terminales)


ESPRECIÓN REGULAR ***CH[0-9UA-ZU_]*RA***


N  = {S, Expr, TERM, X}
T = {+,-,1,2,3,4,5,6,7,8,9,A,B,...,Z,_,C,H,R,A,=}
I = S
P :

S-> Term = Expr
Expr -> Exrp + Term | Expr - Term | Term
Term -> CH X RA
NOTA: E ES EPSILON
X -> E|0X|1X|...|9X|AX|BX|...|ZX|_X 

S.valor := Term.valor || "=" || Expr.valor
Expr.valor := Expr.valor || "+" || Term.valor |
             Expr.valor || "-" || Term.valor |
             Term.valor 

Term.valor := "CH" || X.valor || "RA"
X.valor := "E"||X.valor|"1"||X.valor|"2"||X.valor|...|"9"||X.valor|"A"||X.valor|"B"||X.valor|...|"Z"||X.VALOR|"_"||X.valor

Aritmetica

CH1RA = CH2RA + CH3RA

![árbol de desición](./img/2023-02-16-1.png)










## 07/03/2023

# Unidad 2

#### Generación de Codigo intermedio
tomar el código de entrrada y se empieza a transformar

**objetivo** conocer las técnicas de conversión entre notaciones, así como las técnica para rrepresenetar las intrucciones de un lenguajed e alto nivel en código intermedio.

- Aplicar los tipos de notaciones para la conversión de expresiones, infija prefija y posfija
- Representar expresiones mediane el código intemrdio
- Reconocer el manejo de tipos de expresiones y el uso de operadores
- Desarrollar las accioens que represeenten la estructura


**Estrategias**
- Exponer los 

**Cómo traducir las instrucciones a un lenguaje ensamblador**

Código intermedio realiza algunas reducciones que le permiten actuar de manerea más automatizada sin riesgos de la tradiccion no se concrete como es debido

**Notaciones**

- prefija 
  - Esun algoritmo inductiva 
  - L expresión aritmética X+10 a notción prefida es 
    - +X10
  - Ejemplo
    - 9*4/8
    - *94 /8
    - /*94
  - Ejemplo 2
    - 9*3+3-2/8
    - Anotación prefija es:
    - *96 +3 -2 /8
    - *96 +3 -/28
    - +*963-/28
    - -+*963/28
- Posfija
  - ejemplo 
    - (9-5)*2
    - 95-*2
    - 95-2*
  - ejemplo 3-8*6+7
    - 3-86*+7
    - 38 6*-+7
    - 386*-7+
  - Ejemplo (5+6)*(7+8)
    - 56+*(7+8)

#### Ejercicio
1. 2+8*2/3
   - Prefijo
     - 2+*82/3
     - 2+/*823
     - +2/*823
   - Posfijo
     - 2+82*/3
     - 2+82*3/
     -  282*3/+
2. 6+6/5+6
   -  Prefijo
      -  6+/65+6
      -  +6/65+6
      -  ++6/656
   -  Posfijo
      -  6+65/+6
      -  665/++6
      -  665/+6+
      -  665/+6+
3. 3-5+8*2
   - Prefijo
      - 3-5+*82
      - -35+*82
      - +-35*82
    - Posfijo
      - 35-82*+
4. 6+5/4+3
   - Prefijo
      - 6+/54+3
      - +6/54+3
      - ++6/543
    - Posfijo
      - 654/+3+
5. 7-9/1+0
   - Prefijo
      - 7-/91+0
      - -7/91+0
      - +-7/910
    - Posfijo
      - 791/-0+
  

### Cómo lo hace el compilador
- Definiciones direigidas por la sintaxis
  - Atributos sintetizados
    - En un nodo se calcula a partir de los valores de los atribuos de los hijos de dichos nodo en el árbol de análisis sintáctico.
    - 
  - Atributos Heredados
    - Se calcula a partir de los valores de los atribuos en los hermanos y el padre de dicho nodo.

## 16/03/2023

Representación de código intermeido

Las 3 represetaciones de código intemedio 
- códito p
  - Técnicas que usan los interpretes 
- triplos 
  - es una estructura de datos que representa la perspectiva lógica de la generación de un código intemmedio basada en operandos y operadores, para genera **operaciones temporales** qe, en conjunto, forman una operación ocmpueta. 
  - La operaciones temporales se almacenan en tabla símbolos con tres columnas.
<center>

``` python
w = x + y + 24 -z

MOV AX,X
ADD AX,Y
ADD AX,24
SUB AX,z
MOV W,AX
```

**NOTTA**: la columna de movimientos no va normalmente solo las otras 3 los movimientos solo es una explicación de lo que va en las tablas.
</center>

- Ejemplos
  - posfijo wxy+24+z-=
  
<center>

Movimientos | Datos objeto | Dato fuente | Operador
--- | --- | --- | ---
T | T1 | x | =
T | T1 | y | +
T | T1 | 24 | +
T | T1 | z | -
T | w | T1 | =

</center>

- Ejemplo 2
  - W = x+y/24
  - 

Movimientos | Datos objeto | Dato fuente | Operador
--- | --- | --- | ---
T1 = y | T1 | y | =
T1 = T1 / 24 | T1 | 24 | /
T2 | T2 | x | +
T1 | T1 | T2 | -
T | w | T1 | =


- cuadrulos
  - Otra estructura de datos que tiene 4 objetos 
  - Encabezados
    - Dato objeto
    - Dato fuente 1 
    - Dato fuente 2 
    - Operador 


### Ejercicios

1. b = j - a * 20 / k
- |. En triplo en notación prefijo y posfijo 
   - Prefijo
     - b = j - *a20 / k
     - b = j - /*a20k
     - b = -j/*a20k
     - =b-j/*a20k

      <center>

      Movimientos | Operador | Datos objeto | Dato fuente 
      --- | --- | --- | ---
      T1 = a  | = | T1 | a
      T1 * 20 | * | T1 | 20
      T1 / k | / | T1 | k
      T2 = j | = | T2 | j
      T2 - T1 | - | T2 | T1
      b = T2 | = | b | T2

      </center>

   - Posfijo
     - b = j - a20* / k
     - b = j - a20*k/
     - b = ja20*k/-
     - bja20*k/-=
- ||. En cuádruplo en notación posfijo

<center>

Datos objeto | Dato fuente 1 | Datos fuente 2 | Operador 
--- | --- | --- | ---
T1 | a | 20 | *
T2 | T1 | K | /
T3 | j | T2 | -
b | b | T3 | =

</center>

2. y = 6 + 2 / 1 + b - 5

      <center>

      Movimientos | Operador | Datos objeto | Dato fuente 
      --- | --- | --- | ---
      T1 = 2  | = | T1 | 2
      T1/1  | / | T1 | 1
      T2 = 6  | = | T1 | 6
      T2 + T1  | + | T2 | T1
      T2 + b  | + | T2 | b
      T2 - 5  | - | T2 | 5
      y = T2  | = | y | T2

      </center>


**NOTA: el compimilado evalua todoas la líneas de codigo y el interpretado solo cuando detecta el primero error se detiene.**

## cómo representar una asignación en un triplo 

**Nota**: La próxima clase hay que entregar que el tripo ya nos dé un output de un documento .csv con salida o u excel


## 30/03/2023

Contenido Representación de códogi intermedio (continuación)
- Instrucción cícica o Repetitiva 
  - While (cómo funciona si la instrucción es verdadera se repete la insrucción )
  - MIENSTRAS(condición)
    - // Instrucción
  - FINMIENTRAS

generación de código intermedio

### Ejercicios

```
b = c / 2
Do 
  a = a + 1 ;
  b = a * 2 ;
FINDO MIENTRAS (a > 10 | b < 20);
```

 -| Dato objeto | Dato Fuente | Operador
---|---|---|---
1 | T1 | c | =
2 | T1 | 2 | /
3 | b | T1 | =
4 | T1 | a | = 
5 | T1 | 1 | +
6 | a | T1 | =
7 | T1 | a | =
8 | T1 | 2 | *
9 | b | T1 | =
10 | T1 | a | =
11 | T1 | 10 | >
12 | TR1 | True | 4
13 | TR2 | False | 14
14 | T1 | b | =
15 | T1 | 20 | <
16 | TR1 | True | 4
17 | TR1 | False | 15
18 | --- | --- | ---




```
par = 0
MIENTRAS( a % 2 == 0 & a < 20 )
  par ++
  a = a + 2
FIN
```

-- | Dato objeto | Dato fuente | Operador
--- | --- | --- | ---
1 | T1 | 0 | =
2 | par | T1 | =
3 | T1 | a | =
4 | T1 | 2 | %
5 | T1 | 0 | ==
6 | TR2 | True | 8
7 | TR2 | False | 18
8 | T1 | a | =
9 | T1 | 20 | <
10 | TR1 | True | 12
11 | TR1 | False | 18
12 | T1 | par | =
13 | T1 | 1 | +
14 | par | T1 | =
15 | T1 | a | =
16 | T1 | 2 | +
17 | a | T1 | =


```Java
float Operacion (int x, float y)
{
  while(x * 6 == y + 7)
  {
    y = y +5 -x *a;

  }
  return y;
}
j = Operacion(a,w);

if (j >= 0 && j < 100 ){
  j = j % a;

}

else
{
  j = j % w
}

```
-- | Dato objeto | Dato fuente | Operador 
--- | --- | --- | ---
1 | 


```Java
x = 1;

if ( x <= 10)
{
  y = 10
  
  do
  {
    res = res + y * x;
    y--;

  } while ( y > 0 && y <= 10);

}

else 
{
  res = 0;
  x++;
}
```


# 25/04/2023


## Actividad Optimizr el código 

- Código **original**
```Java
do{
  if(x%2 == 1){
    b = x + w / 5; // puedo x + w /5
    z = a * b; // aquí puedo optimizar a * b
    w = z + b + w / 5 + y;
    c = a * b / w; // aquí puedo optimizar a * b
    w2 = x + w / 5; // puedo x + w /5
    a = w * z + w2; 
    y = a * b * 1 + a; // aquí puedo optimizar a * b
  }
  x = x + 1;
} while(x <= a + 2);

```

- Lo primero es ver qué es lo que sirve y qué es lo que no estádsiendo utilizado
- **la primera optimización es ELIMINACIÓN** 
```Java
do{
  if(x%2 == 1){
    b = x + w / 5; // puedo x + w /5
    z = a * b; // aquí puedo optimizar a * b
    w = z + b + w / 5 + y;
    // c = a * b / w; // ELIMINAMOS 
    w2 = x + w / 5; // puedo x + w /5
    a = w * z + w2; 
    y = a * b * 1 + a; // aquí puedo optimizar a * b
  }
  x = x + 1;
} while(x <= a + 2);

```

- cómo quedo 

```Java
do{
  if(x%2 == 1){
    b = x + w / 5; // puedo x + w /5
    z = a * b; // aquí puedo optimizar a * b
    w = z + b + w / 5 + y;
    w2 = x + w / 5; // puedo x + w /5
    a = w * z + w2; 
    y = a * b * 1 + a; // aquí puedo optimizar a * b
  }
  x = x + 1;
} while(x <= a + 2);

```

- **Ahora aplicamos otra para optimizar *a x b***

```Java
do{
  if(x%2 == 1){
    b = x + w / 5; // puedo x + w /5
    z = a * b; // aquí puedo optimizar a * b
    w = z + b + w / 5 + y;
    w2 = x + w / 5; // puedo x + w /5
    a = w * z + w2; 
    y = a * b * 1 + a; // aquí puedo optimizar a * b
  }
  x = x + 1;
} while(x <= a + 2);

```

**Resultado**

```Java
do{
  if(x%2 == 1){
    b = x + w / 5;
    z = a * b; 
    w = z + b + w / 5 + y;
    w2 = x + w / 5; 
    a = w * z + w2; 
    y = z * 1 + a; 
  }
  x = x + 1;
} while(x <= a + 2);

```

- cuando tienes una condición compuesta eone optimizas una variable para hacer la operación antes para solo utilizar variables 

- 
```Java
do{
  if(x%2 == 1){
    b = x + w / 5; // puedo x + w /5
    z = a * b; // aquí puedo optimizar a * b
    w = z + b + w / 5 + y;
    c = z / w; // aquí puedo optimizar a * b
    // w2 = b ; // puedo x + w /5
    a = w * z + b; 
    y = z * 1 + a; // aquí puedo optimizar a * b
  }
  x = x + 1;
} while(x <= a + 2);

```


# 02/05/2023


## Tipo de optimización de mirila

```Java
x = 8 * 7 ; // ELIMINACION POR OPTIMIZACIÓN LOCAL 


y = (a + b) * ( a - b);


while ( a + b <= c)

{

m = (j + 45)/ 3;

c = a + b / y;

a = par + 3 * 1; // Instrucciones con opereaciones algebraicas reducibles

j = a + b * m;

w = 34 + par + 3; // MÉTODO DE OPTMIZACIÓN LOCAL SE ELIMINA PAR +3

}
```

- El siguiente código quedaría de esta manera

```Java


y = (a + b) * ( a - b);

n = a + b; // Optimización a partir de bucles

while ( n <= c)

{

m = (j + 45)/ 3;

c = a + b / y;

a = par + 3 ;

j = a + b * m;


}
```

