# Recursividad

## Fibonnaci

La sucesión de Fibonnaci donde cada número es la suma de los dos anteriores, empezando desde el 0 y 1. La secuencia es $$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...$$. Se puede definir matemáticamente de la siguiente manera:

$$
f_{n} =
\begin{cases}
    0 & n = 0\\
    1 & n = 1\\
    f_{n-2} + f_{n-1} & n > 2\\
\end{cases}
$$

Implemente la función recursiva de fibonacci.

## Número triangular n

El número triangular cuenta la cantidad de objetos que puede entrar en un triángulo equilatero. El número triangular n cuenta la cantidad de objetos en el triángulo que tiene n objetos en un lado, siendo equivalente de la suma de los números enteros de 1 a n. Por ejemplo, el númetro triangular n con $$n=5$$ es $$ 5 + 4 + 3 + 2 + 1 = 15$$. Se puede calcular de la siguiente manera:

$$
    \begin{cases}
        1 & n \leq 1\\
        n + (n - 1) & n > 1\\
    \end{cases}
$$

Implemente la función recursiva del número triangular $$n$$.

## Factorial

El factorial de un número natural es el producto de todos los números anteriores a sí y sí mismo. Por ejemplo, 5 factorial es $$5! = 5 * 4 * 3 * 2 * 1 = 120$$. Más formalmente, la definición matemática de factorial es:

$$
  n! =
  \begin{cases}
      1 & n \leq 1\\
      n * (n - 1)! & n > 1\\
  \end{cases}
$$

Implemente las funciones iterativas y recursivas de factorial.

## Triángulo pascal

El triángulo de Pascal es un arreglo de forma triangular, relacionado con los coeficientes binomiales. Se ve de la siguiente manera:

![Pascal](../imgs/pascal.png)

El resultado para cada número que no es de la primera fila es la suma del número de la izquierda y derecha de arriba. Programe las funciones que muestre el triángulo de Pascal, pero de tamaño arbitrario.

## Referencias

- Villalobos, L. (2019). Clase 9. Material del curso CI-0202, Universidad de Costa Rica.
