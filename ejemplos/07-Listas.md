# 🗄️ Listas o arreglos

## Rellenar números

Cree una función llamada `llenar_lista` que le pide al usuario la longitud del arreglo $$l$$ y que llene los $$l$$ números en un arreglo. Por último, debe imprimir el arreglo creado.

**Ejemplo:**

```{bash}
Digite la longitud del arreglo: 3
 
Digite el número 1: 20
Digite el número 2: 30
Digite el número 3: 50
 
El arreglo que creo fue el siguiente:
{20, 30, 50}
```

### Estadística

Cree una función llamada `obtener_estadistica` que, dado un arreglo, calcule su media aritmética y la retorna. La fórmula de la media aritmética es:

$$
    \mu_{a} = \frac{x_{1} + x_{2} + ... + x_{n}}{n}
$$

**Ejemplo:**

```{bash}
La media aritmética para el arreglo
{20, 30, 50}
es 33.3334.
```

## Máximo

Cree una función llamada `obtener_maximo`, dado un arreglo de números, retorna el elemento mayor de este.

**Ejemplo:**

```{bash}
El elemento más grande del arreglo
{20, 30, 50}
es 50.
```

## Ascendente

Cree una función que llamada `verificar_ascendente` que verifica que todos revisa que para cada índice $$i, j$$ para un arreglo $$a$$ se debe cumplir que $$a[i] < a[j]$$, cuando $$i < j$$.

**Ejemplo 1:**

Para el arreglo

```{python}
a = [4, 10, 5]
```

El resultado de invocar la función da `False`.

**Ejemplo 2:**

Para el arreglo

```{python}
a = [10, 21, 22, 30]
```

El resultado de invocar la función da `True`.

## La Biblioteca de Alejandría

En su búsqueda por dominar el mundo, la famosa empresa Didney compra el país de Egipto entero; con la intención de convertirlo en un parque de atracciones. Didney decide restaurar las ruinas de la biblioteca de Alejandría, la más majestuosa biblioteca del mundo en su época. En tiempos antiguos, esta biblioteca habría sido destruida por un incendio (y posteriormente por guerra). La empresa, en un acto de «bondad» histórica y cultural, ha decidido restaurar la biblioteca en lugar de convertirla en una montaña rusa.

Por supuesto, la nueva Biblioteca de Alejandría contaría con las últimas facultades tecnológicas. En particular, el catálogo entero de la biblioteca sería completamente digital, la biblioteca en sí manejada por robots. Los visitantes simplemente seleccionarían de un catálogo el libro que deseen leer, y un robot encargado se los traería. El lugar de lectura sería más similar a una cafetería que a una biblioteca, ya que no habrían estantes de libros en medio.

El catálogo de la biblioteca deberá ser mantenido por humanos. Este catálogo contendría la información de todos los libros que existen dentro de la biblioteca. Didney lo ha contratado para programar esta funcionalidad de su sistema. Cuando un nuevo lote de libros ingresa, un funcionario de la biblioteca se encargará de ingresarlo al sistema. Como es posible que ese libro ya exista dentro del sistema, este también debería permitir buscar si existe un libro por título.

El sistema podrá calcular en cualquier momento su catálogo general. Este catálogo es una estadística general de cuántos libros existen dentro del sistema. Esta estadística debería mostrar el total de libros de toda la biblioteca, el total de libros específicos de cada género (Fantasía, Ciencia Ficción, Romance, etc), y un listado de cada autor único en la biblioteca. Esta funcionalidad se requiere porque del lado del usuario, este podrá buscar por autor y por género.

El programa además se deberá mostrar con estilo menú. Este deberá permitir las siguientes opciones:

1. Agregar un libro
2. Buscar un libro
3. Catálogo de la biblioteca
4. Quemar la biblioteca
5. Salir

Para la opción 1, se deberá pedir la información típica de un libro: título, autor, cantidad de páginas y género. Este deberá registrarse en la base de datos. La opción 2 pediría un título de un libro, y de existir un libro con este título en la base de datos, debería mostrar sus datos; y de lo contrario, un mensaje de que este no existe. La opción 3 debería desplegar el catálogo. La opción 4 consiste en borrar todos los datos de la biblioteca. Por último, el programa deberá repetirse siempre y cuando la opción 5 nunca se elija.

```{bash}
Libro:
- Titulo
- Autor
- Cantidad de Páginas
- Género

Biblioteca:
- Agregar
- Buscar por título
- Cantidad de libros
- Autores únicos
- Conteo por género

Interfaz:
- Mostrar menu
 1. Agregar Libro
 2. Buscar un libro
 3. Estadistica de biblioteca
 4. Quemar biblioteca
 5. Salir
- Input
- Output
```

## Black Jack

Programe el juego de Black Jack con una cantidad de jugadores ajustables de dos hasta cuatro.
BlackJack es un juego popular de cartas. Como la mayoría de juegos de cartas, se utiliza la baraja inglesa que contiene 52 cartas. Las cartas se dividen en trece categorías (As, 1, 2, 3 ,4 , 5, 6, 7, 8, 9, Jota, Reina\[Q\], Rey\[K\]) y cuatro palos (picas, corazones, tréboles y rombos).

Para jugar BlackJack, se inician por barajar (shuffle) las cartas del deck. Luego, se le reparten dos cartas al azar como la mano a cada jugador@. Hoy en día es común que se muestran las cartas de l@s jugador@s (face up). Cada carta tiene un valor numérico en puntos, como se puede ver en la siguiente tabla.

|  |  |  |  |  |  |  |  |  |  |  |  |
| - | - | - | - | - | - | - | - | - | - | - | - |
| As | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Jota | Reina | Rey |
1 ó 11 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 10 | 10|

Para esta versión del juego, se va a asumir que el `As` siempre es 1. Después de repartidas las dos cartas, cada jugador puede decir si pedir otra carta (hit) o decidir mantener la cantidad de cartas que tiene actualmente (stand). Gana el jugador que tiene el valor más cercano a 21 como la suma total de las cartas, pero sin sobrepasarse.

### Playlist

Es el año 200x y usted es dueñ@ de la empresa Dotify que busca crear una plataforma de streaming online de contenido multimedia. En su plataforma actualmente usted tiene canciones que tienen autor@s, nombre y una duración. Recientemente, sus usuarios han estado solicitando que les agregue un nuevo \textit{feature} (funcionalidad en el sistema), los playlists.  Un playlist puede guardar un conjunto de canciones, y este playlist también posee un nombre. Además, se pueden agregar, quitar, mostrar y obtener la cantidad de canciones en un playlists.

A usted le encargan de crear esta funcionalidad. Específicamente, quieren que programe un reproductor de música que pueda realizar lo descrito anteriormente. El programa además se deberá mostrar con estilo menú. Este deberá permitir las siguientes opciones:
 
```{bash}
1. Crear una canción
2. Buscar una canción
3. Mostrar todas las canciones
4. Mostrar todos los playlists
5. Crear un nuevo playlist
6. Agregar una canción a un playlist
7. Contar las canciones a un playlist
8. Mostrar las canciones a un playlist
9. Borrar una canción a un playlist
10. Salir
```

## Referencias

- Villalobos, L. (2019a). Colección de datos lineales (arreglos). Material del curso CI-0202 Universidad de
Costa Rica de Leonardo Villalobos.
- Villalobos, L. (2019b). Ejercicios clases 8. Material del curso CI-0202, Universidad de Costa Rica.
