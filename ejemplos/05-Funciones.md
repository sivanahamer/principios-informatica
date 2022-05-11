# ↪ Funciones

## Moneda

Escriba una función que simule el tirar una moneda. La función deberá imprimir escudo o corona.

## Dado

Escriba una función que simule el tirar un dado. La función deberá imprimir la cantidad de caras resultantes.

## Seno cardinal

Las funciones pueden utilizarse como funciones matemáticas. Recordemos nuestro famoso seno cardinal. Se puede definir de la siguiente forma:

$$sinc(x) =
\begin{cases}
    \frac{sin(x \pi)}{x \pi} & x != 0\\
    1 & x = 0\\
\end{cases}
$$

Escriba un programa que implemente la función seno_cardinal que recibe x.

## Sustitución polinomial

Escriba una función que represente un polinomio de segundo grado $$a x^{2} + b x + c$$. A esta se le pasarán los valores de $$a != 0$$, $$b$$, $$c$$ y $$x$$, y la función deberá retornar el resultado de sustituir estos valores en la expresión de arriba.

Al invocar la función con $$a=1$$, $$b=2$$, $$c=3$$, y $$x=4$$:

```{bash}
polinomioGrado2(1, 2, 3, 4)
```

Devuelve lo siguiente:

```{bash}
27
```

Escriba una función que represente un polinomio de cuarto grado $$a x^{4} + b x^{3} + c x^{2} + d x + e$$. A esta se le pasarán los valores de $$a != 0$$, $$b$$, $$c$$, $$d$$, $$e$$, y $$x$$, y la función deberá retornar el resultado de sustituir estos valores en la expresión de arriba.

Al invocar la función con $$a=1$$, $$b=2$$, $$c=3$$, $$d=4$$, $$e=5$$, y $$x=6$$:

```{bash}
polinomioGrado4(1, 2, 3, 4, 5, 6)
```

Devuelve lo siguiente:

```{bash}
1865
```

**Nota:** Puede asumir que $$a$$, $$b$$, $$c$$, y $$d$$ son distintos a 0. Por lo tanto, no requiere validar los números.

## Brújula

Las brújulas son instrumentos de navegación que nos indican una dirección relativa hacia los puntos cardinales. Los puntos cardinales son norte (N), oeste (O), sur (S), y este (E). Cree un programa que simule la rotación de una brújula. Debera constar de las siguientes funciones. Cree las siguientes funciones:

- **rotar_agujas_del_reloj:** Recibe uno de los cuatro puntos cardinales como parámetro y retorna el siguiente punto cardinal en la dirección de las agujas del reloj. Por ejemplo, si se le digita `"N"` retorna `"E"`.
- **rotar_contra_agujas_del_reloj:** Recibe uno de los cuatro puntos cardinales como parámetro y retorna el siguiente punto cardinal en la dirección contra las agujas del reloj. Por ejemplo, si se le digita `"N"` retorna `"O"`.
- **imprimir_menu:** No recibe ningún parámetro y retorna la opción seleccionada del usuario en el menú entre rotar con la dirección del reloj o en contra del reloj.
- **rotar_brujula:** No recibe ni retorna nada. Esta función se encarga de llamar a las funciones previamente definidas.

En caso de una entrada no valida en las funciones, retorna `None`. Por ejemplo si en `rotar_agujas_del_reloj` se le da `pedro` retorna `None`.

**Ejemplo:**

```{bash}
Seleccione la opcion para la brujula:
    1) Rotar con las agujas del reloj
    2) Rotar contra las agujas del reloj
Cualquier otra opcion termina el programa.
Seleccion: 1

Digite el punto cardinal: S
El punto cardinal con las agujas del reloj es: O

Seleccione la opcion para la brujula:
    1) Rotar con las agujas del reloj
    2) Rotar contra las agujas del reloj
Cualquier otra opcion termina el programa.
Seleccion: 2

Digite el punto cardinal: E
El punto cardinal contra las agujas del reloj es: N

Seleccione la opcion para la brujula:
    1) Rotar con las agujas del reloj
    2) Rotar contra las agujas del reloj
Cualquier otra opcion termina el programa.
Seleccion: adios
```

## Calculadora de días

Cree las siguientes funciones:

- **convertir_dia_nombre:** Recibe un entero de 0 al 6 que representa un día de la semana y retorna el nombre del día de la semana respectivo. El día 0 representa `"Domingo"`. Por ejemplo, si recibe `3` retorna `"Miercoles"`.
- **convertir_nombre_dia:** Escriba la función inversa de `convertir_dia_nombre` que recibe el nombre del día de la semana y retorna el numero entero. Por ejemplo, si recibe `"Sabado"` retorna `6`.
- **calcular_dia:** Esta función podrá responder preguntas como Si hoy es martes, y en 10 días tengo una cita, ¿qué día de la semana es?. Por lo tanto, la función recibe el día de la semana y un número de días a agregar llamado delta. Por ejemplo, si recibe `"Martes"` y `10` retorna `"Viernes"`. Utilice las funciones declaradas anteriormente.

En caso de una entrada no valida en las funciones, retorna `None`. Por ejemplo si en `convertir_dia_nombre` se le da `halloween` retorna `None`.

**Ejemplo 1:**

```{bash}
Digite el dia: Martes
Digite el delta: 10

El dia de la semana es: Viernes
```

**Ejemplo 2:**

```{bash}
Digite el dia: Martes
Digite el delta: -2

El dia de la semana es: Domingo
```

**Ejemplo 3:**

```{bash}
Digite el dia: Lunes
Digite el delta: 0

El dia de la semana es: Lunes
```

## Calculadora

Las calculadoras son dispositivos eléctronicos que nos automatizan algunas operaciones aritméticas. Implemente las siguientes operaciones en funciones:

- **sumar:**  Recibe dos números y retorna la suma de los números. Por ejemplo, `10` y `3` retorna `13`.
- **restar:** Recibe dos números y retorna la resta del primer número con el segundo número. Por ejemplo,`10` y `3` retorna `7`.
- **multiplicar:** Recibe dos números y retorna la multiplicación de los números. Por ejemplo, `10` y `3` retorna `30`.
- **dividir:** Recibe dos números y retorna la división del primer número con el segundo número. Por ejemplo, `10` y `3` retorna `3.3334`.

Además, se debe implementar una función denominada `mostrar_menu` que muestra el menú y retorna la opción digitada del menú. Por último, debe implementar la función `correr_calculadora` que se encarga de utilizar todas las funciones declaradas anteriormente. El algoritmo a muy alto nivel de `correr_calculadora` es la siguiente:

```{python}
mientras el usuario no digite que finalice:
    opcion = mostrar_menu()
    numero1, numero2 = obtener_numeros()
    resultado = ejecutar_operacion(opcion, numero1, numero2)
    imprimir(resultado) 
```

**Ejemplo:**

```{bash}
Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 1
Digite el primer numero: 10
Digite el segundo numero: 3
10.0 + 3.0 = 13.0


Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 2
Digite el primer numero: 10
Digite el segundo numero: 3
10.0 - 3.0 = 7.0


Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 3
Digite el primer numero: 10
Digite el segundo numero: 3
10.0 * 3.0 = 30.0


Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 4
Digite el primer numero: 10
Digite el segundo numero: 3
10.0 / 3.0 = 3.3333333333333335


Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 2bornot2b
ERROR: El codigo no es valido


Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 1
Digite el primer numero: nosoynumero
ERROR: No es un numero real
Digite el primer numero: 9
Digite el segundo numero: 4
9.0 + 4.0 = 13.0


Seleccione una de las siguientes opciones:
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Detener la ejecucion
Opcion seleccionada: 5


----Fin de programa----
```

## Referencias

- Elkner, J., Downey, A. B., y Meyers, C. (2012). How to think like a computer scientist: Learning with python.
- Villalobos, L. (2019a). Ejercicios clases 6. Material del curso CI-0202, Universidad de Costa Rica.
- Villalobos, L. (2019b). Subrutinas. Material del curso CI-0202 Universidad de Costa Rica de Leonardo Villalobos.
- Villalobos, L. (2019c). Tarea 4. Material del curso CI-0202, Universidad de Costa Rica.
