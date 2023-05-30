## Generando triplo 

-- | Dato objeto | Dato fuente | Operador
--- | --- | --- | ---
1 | T1 | 0 | =
2 | par | T1 | = 
3 | T1 | 0 | =
4 | impar | T1 | =
5 | T1 | 1 | =
6 | x | T1 | =
7 | T1 | 6 | =
8 | T1 | X | <=
9 | TR1 | TRUE | 11
10 | TR1 | FALSE | 27
11 | T1 | X | =
12 | T1 | 2 | %
13 | T1 | 0 | ==
14 | TR1 | TRUE | 16
15 | TR1 | FALSE | 19
16 | T1 | 1 | =
17 | T1 | par | +
18 | par | T1 | =
19 | -- | 23 | JMP
20 | T1 | 1 | =
21 | T1 | impar | +
22 | impar | T1 | =
23 | T1 | 1 | =
24 | T1 | x | +
25 | x | T1 | = 
26 | -- | 7 | JR
27 | -- | -- | --




-- | Dato objeto | Dato fuente | Operador
--- | --- | --- | ---
1 | -- | JMP | 20
2 | T1 | 0 | = 
3 | i | T1 | =
4 | T1 | i | =
5 | T1 | x | %
6 | T2 | w | =
7 | T2 | T1 | +
8 | w | T2 | =
9 | T1 | i | =
10 | T1 | 1 | +
11 | i | T1 | =
12 | T1 | 10 | =
13 | T1 | i | <=
14 | TR1 | TRUE | 16
15 | TR1 | FALSE | 20
16 | T1 | 0 | =
17 | T1 | i | >=
18 | TR1 | TRUE | 4
19 | TR1 | FALSE | 20
20 | --  | JMP | 26
21 | T1 | 3.1 | =
22 | x | T1 | =
23 | T1 | 20 | =
24 | w | T1 | =
25 | -- | JMP | 2
26 | T1 | w | = 
27 | j | T1 | =
28 | -- | -- | --
