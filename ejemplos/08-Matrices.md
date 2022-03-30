# 🟥 Matrices

## Imprimir

Cree una función llamada `imprimir_matriz` que recibe una matriz y la imprime con cada fila por separado y con espacaido igual entre las columnas.

**Ejemplo:**

La matriz declarada como:

```{bash}
[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
```

Se imprimiría como:

```{bash}
   1    2    3    4
   5    6    7    8
   9   10   11   12
```

## Total

Cree una función llamada `sumar_total` que recibe una matriz y retorna la suma total de la matriz.

**Ejemplo:**

La matriz declarada como:

```{bash}
[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
```

Devuelve:

```{bash}
78
```

## Total fila

Cree una función llamada `sumar_total_fila` que recibe una matriz y retorna una lista con la suma total por fila.

**Ejemplo:**

La matriz declarada como:

```{bash}
[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
```

Devuelve:

```{bash}
[10, 26, 42]
```

## Total columna

Cree una función llamada `sumar_total_columna` que recibe una matriz y retorna una lista con la suma total por columna.

**Ejemplo:**

La matriz declarada como:

```{bash}
[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
```

Devuelve:

```{bash}
[15, 18, 21, 24]
```

## Rotar

Cree un programa que, dado una matriz de números $$n \times n$$, rote en 90 grados la matriz. Además, intente realizar la rotación _in place_, es decir, en la matriz directamente sin ninguna copia.

**Ejemplo 1:**

La matriz declarada como:

|   |   |   |
| - | - | - |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Devuelve:

|   |   |   |
| - | - | - |
| 7 | 4 | 1 |
| 8 | 5 | 2 |
| 9 | 6 | 3 |

**Ejemplo 2:**

La matriz declarada como:

|    |    |    |    |    |
| -- | -- | -- | -- | -- |
|  1 |  2 |  3 |  4 |  5 |  
|  6 |  7 |  8 |  9 | 10 |
| 11 | 12 | 13 | 14 | 15 |
| 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | 24 | 25 |

Devuelve:

|    |    |    |    |    |
| -- | -- | -- | -- | -- |
| 21 | 16 | 11 |  6 |  1 |  
| 22 | 17 | 12 |  7 |  2 |
| 23 | 18 | 13 |  8 |  3 |
| 24 | 19 | 14 |  9 |  4 |
| 25 | 20 | 15 | 10 |  5 |

## Starducks

La famosa cadena internacional de cafeterías Starducks los ha contactado para llevar las finanzas de las tiendas de Costa Rica. Usted posee información financiera de ventas y costos por trimestre y por tienda. El siguiente es un ejemplo:

| Ventas | Trimestre 1 | Trimestre 2 | Trimestre 3 | Trimestre 4 |
|---| ---| ---| ---| ---|
|San Pedro | 97 | 101 | 96 | 100 |
|Heredia | 50 | 47 | 53 | 50 |
|Alajuela | 27 | 18 | 18 | 25 |

Con base en esto, debe calcular las utilidades de todas las tiendas, de toda la cadena por trimestre, y al final las utilidades anuales. Por ejemplo, para los datos anteriores, las utilidades serían:

| Ventas | Trimestre 1 | Trimestre 2 | Trimestre 3 | Trimestre 4 |
|---| ---| ---| ---| ---|
|San Pedro | 42 | 46 | 40 | 45 |
|Heredia | 28 | 25 | 31 | 25 |
|Alajuela | -11 | -25 | -18 | -17 |

**Utilidades por tienda:**

| San Pedro | Heredia | Alajuela |
|---| ---| ---|
| 173 | 109 | -71 |
|Heredia | 28 | 25 | 31 | 25 |
|Alajuela | -11 | -25 | -18 | -17 |

**Utilidades por trimestre:**

| Trimestre 1 | Trimestre 2 | Trimestre 3 | Trimestre 4 |
|---| ---| ---| ---|
| 59 | 46 | 53 | 53 |

**Utilidades anuales:**

| Utilidades anuales |
|---|
| 221 |

Cree un programa que solicite información financiera de las tiendas:

- Pida la cantidad de tiendas que hay
- Pida los nombres de las tiendas
- Pida para cada tienda las ganancias por trimestre
- Pida para cada tienda las pérdidas por trimestre

Y con base en esta, calcule:

- Utilidades de cada tienda por trimestre
- Utilidades de toda la cadena por trimestre
- Utilidades anuales

## Gomoku

Gomoku, también conocido como cinco en linea, es un juego de mesa que se jugaba en tableros de Go de $$15 \times 15$$ o $$19 \times 19$$ piezas. Cada jugador tiene un color para sus piezas (negro o blanco). Iniciando por negro, cada jugador va alternando turnos y colocando sus piezas. El juego consiste en que cada jugador, por turnos, debe intentar crear una cadena diagonal, vertical o horizontal de cinco piezas de su tipo. Gana el primero en crear la cadena de cinco en línea. Programe el juego Gomoku.

## Buscaminas

Buscaminas es un videojuego muy popular, donde se intenta despejar todo un tablero con bombas sin detonarlas. Al iniciar el juego, se generan bombas en posiciones al azar. Luego, al lado de cada posición hay un número que indica cuantas bombas están adyacentes al campo actual. Se gana al despejar todo el tablero de las bombas sin detonarlas. Programe el juego Buscaminas en un tablero $$9 \times 9$$ con $$10$$ bombas.

## Referencias

- Villalobos, L. (2019a). Ejercicios clases 10. Material del curso CI-0202, Universidad de Costa Rica.
- Villalobos, L. (2019b). Matrices. Material del curso CI-0202 Universidad de Costa Rica de Leonardo
Villalobos.
