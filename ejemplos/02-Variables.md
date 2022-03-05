# 📦 Tipos de datos y variables

## Fórmula cuadrática

En un curso de matemática lo contratan a usted para crear un programa para verificar los resultados de los estudiantes al calcular las soluciones de una ecuación cuadrática. Implemente la solución.

**Ejemplo:** Si su programa se le ingresa la información:

```{bash}
La a es: 1
La b es: 4
La c es: -21
```

Debe mostrar el siguiente resultado:
  
```{bash}
x1 es: 3
x2 es: -7
```

## Menudo

Su mamá tiene mucho menudo que le ha sobrado después de ir de compras. Como no le gusta contar el menudo, ella ha dejado todas las monedas en una caja. Un día, se da cuenta que ya la caja está llena de monedas por lo que decide por fin empezar a contar el menudo. Haga un programa que lo ayuda a contar el menudo. El programa le pedira la cantidad de monedas de cada denominación y calculará el total de colónes que tiene.

**Ejemplo:** El programa le pediría los siguientes datos:

```{bash}
Ingrese la cantidad de monedas de c5: 20
Ingrese la cantidad de monedas de c10: 13
Ingrese la cantidad de monedas de c25: 2
Ingrese la cantidad de monedas de c100: 5
Ingrese la cantidad de monedas de c500: 22
```

Debe mostrar el siguiente resultado:

```{bash}
Usted tiene 11780 colones.
```

## Ángulos internos de un polígono regular

Para un curso de matemática, los profesores ocupan un programa que verifique la suma de los ángulos internos de un polígono regular, y los grados del ángulo interno del polígono regular, dado la cantidad de lados del polígono. Implemente la solución.

**Ejemplo:** Si su programa se le ingresa la información:

```{bash}
Numero de lados (n) del poligono es: 4
```

Debe mostrar el siguiente resultado:

```{bash}
La suma de los angulos interiores es: 360
Cada angulo interior del poligono es: 90
```

## Velocidad

Dado la distancia viajada (d) y el tiempo transcurrido (t) por un objeto en movimiento, uno puede calcular la velocidad (v) de un objeto. Implemente un programa que pueda calcular la velocidad dada la distancia y el tiempo.

**Ejemplo:** Si su programa se le ingresa la información:

```{bash}
Distancia viajada (d): 12
Tiempo transcurrido (t): 2
```

Significa que el objeto ha viajado 10 metros en 2 segundos (asumimos que el programa lee distancias en metros y tiempo en segundos). Debería mostrarse entonces la siguiente salida:

```{bash}
La velocidad (v) es: 6.0
```

## Monedas
 
Usted tiene un chanchito en el que guarda monedas (en dólares) de diferente denominación. Usted un día decide abrir el chanchito y contar sus contenidos. Elabore un programa que, dada la cantidad de monedas de cada denominación, calcule cuántos dólares usted tiene. Las denominaciones de monedas son las siguientes:

- **Penny:** 0.01
- **Nickel:** 0.05
- **Dime:** 0.10
- **Quarter:** 0.25
- **Half-dollar:** 0.50
- **Dollar:** 1

**Ejemplo:** El programa le pediría los siguientes datos:

```{bash}
Ingrese la cantidad de pennies: 56
Ingrese la cantidad de nickels: 17
Ingrese la cantidad de dimes: 0
Ingrese la cantidad de quarters: 6
Ingrese la cantidad de half-dollars: 3
Ingrese la cantidad de dollars: 1
```

Y debería mostrar el siguiente resultado:

```{bash}
En total son 5.41 dolares
```

## Teorema de Pitágoras

El teorema de Pitágoras indica que la longitud de la hipotenusa es igual a la suma de los cuadrados de los otros dos lados. La fórmula es la siguiente:

$$c = \sqrt{a^2 + b^2}$$

Implemente un programa que dado la longitud de los dos lados, calcule la hipotenusa (c).

**Ejemplo:** El programa le pediría los siguientes datos:

```{bash}
Longitud del lado a: 3
Longitud del lado b: 4
```

Y debería mostrar el siguiente resultado:

```{bash}
La longitud de la hipotenusa es: 5.0
```

**Nota:** La raíz cuadrada en Python se calcula con el comando sqrt(número). Este se debe importar desde math, agregando la línea ``\lstinline{from math import sqrt}''. Ejemplo:

```{python}
>>> from math import sqrt
>>> sqrt(30)
5.477225575051661
```

## Altura

Escriba un programa que convierta la altura de una persona de pies y pulgadas a metros. Un pie equivale a 0.3048 metros, y 12 pulgadas equivalen a 1 pie.

Considere que ambos (pies y pulgadas) son parte de la misma métrica. Por ejemplo, 6 pies y 2 pulgadas (6 ft 2 in) se refiere a una misma longitud. Por así decir, metros y centímetros; u horas y minutos.

**Ejemplo:** Si su programa se le ingresa la información:

```{bash}
Pies: 6
Pulgadas: 2
```

Como salida de datos, su programa mostrará lo siguiente:

```{bash}
La altura en metros es 1.8796
```

## Tiempo

Un sistema de cámaras solares registra el tiempo de funcionamiento diario antes de necesitar una recarga de energía. Usualmente este sistema genera estos datos por las noches. El sistema genera un reporte del tiempo de funcionamiento expresado en horas, minutos y segundos. Por ejemplo, una cámara reportó la semana anterior un tiempo de 14 horas, 12 minutos y 54 segundos. Estos datos son requeridos para un posterior análisis estadísticos en segundos, pero la conversión manual es lenta ya que son muchas cámaras reportando a diario.

Dada esta necesidad, usted ha sido contratado/a para crear un programa en python para automatizar la conversión de estos datos previo al análisis estadístico. Su programa espera la siguiente entrada de datos:

```{bash}
Ingrese la cantidad de horas registradas: 14
Ingrese la cantidad de minutos registrados: 12
Ingrese la cantidad de segundos registrados: 54 
```

Y como salida de datos, su programa mostrará lo siguiente:

```{bash}
La cámara registro 51174.0 segundos.
```

## Consumo automóvil

La nueva inteligencia artificial del más novedoso auto inteligente le indica al usuario al final de cada viaje cuánto combustible consume, y cuál fue el consumo por kilómetro recorrido. Entre otras cosas, usted debe programar la parte del auto que debe hacer este cálculo.

Su programa recibirá los siguientes datos en orden: combustible al inicio del viaje (L), combustible al final del viaje (L), y distancia recorrida (km). Por ejemplo:

```{bash}
Combustible al inicio (L): 20
Combustible al final (L): 15.2
Distancia recorrida (km): 2.4
```

Que significa que el auto tenía 20 litros de combustible al inicial y 15.2 al terminar, además de haber recorrido 2.4 kilómetros. Con base en esto, usted debería calcular el consumo de combustible de todo el viaje, además del consumo promedio por kilómetro.

En total, el vehículo consumió 4.8 litros. Para calcular el consumo promedio, basta con dividir el consumo total entre la cantidad de kilómetros, resultado en 2 litros consumidos por kilómetro. Debería mostrarse entonces la siguiente salida:

```{bash}
Consumo total: 4.8
Consumo promedio: 2.0
```

## Crammer

El conjunto de ecuaciones lineales:  
$$a_{1}x_{1} + b_{1}x_{2} = c_{1}$$  
$$a_{2}x_{1} + b_{2}x_{2} = c_{2}$$

Puede resolverse utilizando la regla de Crammer:  
$$x_{1} = \frac{c_{1}b_{2} - c_{2}b_{1}}{a_{1}b_{2} - b_{1}a_{2}}$$  
$$x_{2} = \frac{c_{2}a_{1} - c_{1}a_{2}}{a_{1}b_{2} - b_{1}a_{2}}$$

Implemente un programa que resuelva un par de ecuaciones lineales de esta forma utilizando la regla de Crammer.

**Ejemplo:** El sistema:  
$$3x_{1} + 4x_{2} = 40$$
$$5x_{1} + 2x_{2} = 34$$
es resuelto con $x_{1}$ = 4 y $x_{2}$ = 7.

Para este ejemplo, el programa pedirá los siguientes datos:

```{bash}
Ingrese el factor a1: 3
Ingrese el factor b1: 4
Ingrese el factor c1: 40
Ingrese el factor a2: 5
Ingrese el factor b2: 2
Ingrese el factor c2: 34
```

y aplicando resultados, mostraría los siguientes resultados:

```{bash}
x1 =  4.0
x2 =  7.0
```

## Referencias

- Méndez, J. P. R. (2020). Laboratorio 1. Material del curso CI-0202, Universidad de Costa Rica.
- Villalobos, L. (2019a). Laboratorio 2. Material del curso CI-0202, Universidad de Costa Rica.
- Villalobos, L. (2019b). Tarea 1. Material del curso CI-0202, Universidad de Costa Rica.
