# 🔁 Flujos de control

## Par o impar

Un número entero es par si es divisible entre 2, o impar si no lo es. Cree un programa que pida un número, y luego muestre si es par o no.

Aquí podría ser útil el operador módulo (\%). Este muestra el residuo de la división entera de 2 números. Este tiene la propiedad de que el resultado es 0 si eran enteramente divisibles:

**Ejemplo 1:**

```{bash}
Numero: 6
 
Es par
```

**Ejemplo 2:**

```{bash}
Numero: 1023
 
Es impar
```

## Tablas

Escriba un programa que muestre, para los números entre 1 y 10, el número, su cuadrado y su cubo.

## Entrada válida

Cree un código que lea correctamente un número real. El programa deberá seguir pidiendo un número hasta que se le ingrese un real verdadero.

## Promedio

Escriba un programa al que se le ingrese un número $n$. El programa ahora deberá pedir otros $n$ nuevos números. Sobre estos, calculará su promedio (media aritmética).  

$$\frac{x_{1} + x_{2} + ... + x_{n}}{n}$$  

## Calculadora

Cree un programa que funcione como una calculadora. Pida dos números, luego una de 4 posibles operaciones: suma (+), resta (-), multiplicación (*) o división (/).

## Cuadráticas

Una ecuación cuadrática es de la forma:  
$$ax^{2} + bx + c = 0$$
Donde $a$, $b$ y $c$ son coeficientes reales y $a \neq 0$.

Escriba un programa que reciba los 3 coeficientes de una ecuación cuadrática y calcule sus raíces, o valores que la resuelven (sea igual a 0). Las raíces se pueden calcular con las fórmulas:  

$$r_{1} = \frac{-b+\sqrt{b^{2} - 4ac}}{2a}$$

$$r_{2} = \frac{-b-\sqrt{b^{2} - 4ac}}{2a}$$

Es posible que el sistema no tenga solución, que es lo que ocurre cuando el discriminante $\Delta = b^{2} - 4ac$ es negativo. En este caso, la raíz en las fórmulas no tiene solución y el programa debe mostrar un mensaje indicando que la ecuación no tiene solución.

Igualmente, es posible que se introduzca un valor de $a = 0$. Este caso no corresponde a una ecuación cuadrática, pero igualmente se mostrará la solución de la ecuación, que corresponde a:

$$r = \frac{-c}{b}$$

En el caso que $a = 0$ y $b = 0$, no se tiene una ecuación. En este caso, simplemente muestre un mensaje de error y termine con el programa. Note que es válido que $b = 0$ siempre y cuando $a \neq 0$.

**Ejemplo 1:**

```{bash}
a = 1
b = 2
c = -35
 
Las raíces de la ecuación 1.00x^2 +2.00x -35.00 = 0 son x = 5.00 y x = -7.00
```

**Ejemplo 2:**

```{bash}
a = 1
b = 1
c = 1
 
La ecuación 1.00x^2 +1.00x +1.00 = 0 no tiene solución
```

**Ejemplo 3:**

```{bash}
a = 0
b = 3
c = 9
 
La raíz de la ecuación 3.00x +9.00 = 0 es x = -3.00 
```

**Ejemplo 4:**

```{bash}
a = 0
b = 0
c = 1
 
Los valores ingresados no corresponden a una ecuación válida
```

## Conversión entre temperaturas

Cree un programa que convierta una temperatura, en Celsius o Fahrenheit, a su contraparte. Las fórmulas de conversión son:

- Fahrenheit a Celsius: $T_{C} = \frac{5}{9}(T_{F} - 32)$
- Celsius a Fahrenheit: $T_{F} = \frac{9}{5}T_{C} + 32$

## Pura vida

Escriba un programa que cada número sea divisible por 3 imprima `Pura` y cada número divisible por 5 imprima `Vida`.

## Invertir un número

Escriba un programa al que se le ingrese un número entero positivo y lo devuelva invertido. Por ejemplo, si se escribe 1234, se debería devolver 4321.

**Nota:** Debe hacerse la conversión como número. No se puede convertir a hilera.

## String al revés

Escriba un programa al que se le ingrese un número n. El programa ahora deberá pedir n letras. Sobre estos, creará un string al revés de la entrada dada. Por ejemplo, el string al revés de `pedro` es `ordep`.

**Ejemplo:**

```{bash}
Cantidad de letras: 4
Digite la letra 1: a
Digite la letra 2: b
Digite la letra 3: c
Digite la letra 4: d
 
El string al revés es: dcba
 
```

## Factores

Cree un programa que muestre los factores de un número. Los factores son los números por los cuales se es enteramente divisible. Por ejemplo, los factores de 12 son 1, 2, 3, 4, 6 y 12.

```{bash}
Introduzca un número: 12
 
1 es factor
2 es factor
3 es factor
4 es factor
6 es factor
12 es factor
```

**Nota:** El operador de módulo ()\%) puede sacar el residuo de la división. Además si la división es entera, entonces el residuo es 0. Otra cuestión es que los factores de un número siempre son menores o iguales a él. Además, se está trabajando con números enteros positivos. Dicho de otra manera, deberíamos revisar todos los números entre 1 y el número recibido.

## IMC

El índice de masa corporal es un indicador del estado del cuerpo de una persona, calculado a partir de la altura y el peso de una persona. Este valor se puede utilizar para calcular si una persona tiene un peso normal, se encuentra en sobrepeso u obesidad, o si más bien es delgado. El índice de masa corporal se puede calcular de la siguiente manera:

$$ IMC = \frac{masa}{estatura^{2}}, \textnormal{ con masa en kilogramos y estatura en metros.}$$

No obstante, esta medida en sí no nos dice nada acerca del cuerpo de una persona. Esto es porque el índice de masa corporal es una medida que se utiliza para clasificar personas, siguiente la siguiente tabla:

| Clasificación | Desde | Hasta |
| ------------- | ----- | ----- |
| Delgadez severa | - | 15.99|
| Delgadez moderada | 16.00 | 16.99 |
| Delgadez leve | 17.00 | 18.49 |
| Normal | 18.50 | 24.99 |
| Sobrepeso | 25.00 | 29.99 |
| Obesidad leve | 30.00 | 34.99 |
| Obesidad media | 35.00 | 39.00 |
| Obesidad mórbida | 40.00 | - |

Por último, vale la pena mencionar que esta clasificación sólo es verdadera para personas mayores de 18 años.

Usted tiene un registro de datos poblacionales, con nombre, edad, altura (cm) y peso (kg), estructurados de esa manera. Un ejemplo de este registro sería:

| Nombre | Edad | Altura | Peso |
| ------ | ---- | ------ | ---- |
| Miguel | 25 | 190 | 65.65 |
| Daniela | 41 | 164 | 72.54 |
| Pablo | 16 | 140 | 54.20 |
| Mario | 65 | 152 | 205.15 |

Su programa debería leer este registro de la siguiente manera: primero pediría la cantidad de personas en el registro, y pediría esa cantidad de veces estos datos. Por ejemplo:

```{bash}
Ingrese la cantidad de personas: 4
Ingrese el nombre de la persona 1: Miguel
Ingrese la edad de la persona 1: 25
Ingrese la altura de la persona 1: 190
Ingrese el peso de la persona 1: 65.65
... (Repita para las personas 2, 3 y 4)
```

Para cada una de estas personas, debería mostrar su IMC y la categoría que pertenece. Para nuestro ejemplo:

```{bash}
El IMC de Miguel es de 18.2 (Delgadez leve)
El IMC de Daniela es de 27.0 (Sobrepeso)
El IMC de Pablo es de 27.7 (No aplica)
El IMC de Mario es de 88.8 (Obesidad mórbida)
```

Por limitaciones de nuestros programas de Python, no podremos mostrar todos los resultados al final, si no que posiblemente tengamos que mostrarlos conforme los vayamos pidiendo.

## Referencias

- Villalobos, L. (2019). Clase 4. Material del curso CI-0202, Universidad de Costa Rica.