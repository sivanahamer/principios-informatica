# 🌌 Programacion orientada a objetos

## Clase Perro

**Descripción:** La clase encarga de guardar información acerca de un perro.

**Atributos:** 

- `raza`: La raza del perro
- `edad`: La edad del perro
- `color`: El color del perro

**Métodos:**

- `constructor`: Método constructor del perro. Recibe e inicializa los atributos.
- `ladrar`: Método que imprime el resultado de un perro que ladra.
- `calcular_edad_humano`: Obtiene la edad del perro en humano. Esto es la edad del perro multiplicado por 7.

## Clase Círculo

**Descripción:** La clase encarga de guardar información acerca de un círculo.

**Atributos:** Guarda el radio del círculo.

**Métodos:**

- `constructor`: Método constructor del círculo. Recibe e inicializa el radio.
- `obtener_area`: Método que obtiene el área del círculo.
- `obtener_perimetro`: Método que obtiene el perímetro del círculo.
- `imprimir`: Método que imprime la información del círculo.

## Clase Rectángulo

**Descripción:** La clase encarga de guardar información acerca de un rectángulo.

**Atributos:** Guarda la base y altura del rectángulo.

**Métodos:**

- `constructor`: Método constructor del rectángulo. Recibe la base y la altura, y las inicializa.
- `obtener_area`: Método que obtiene el área del rectángulo.
- `obtener_perimetro`: Método que obtiene el perímetro del rectángulo.
- `imprimir`: Método que imprime la información del rectángulo.

## Clase Dado

**Descripción:** La clase encarga de guardar información acerca de un dado.

**Atributos:** Guarda la cantidad de caras del dado.

**Métodos:**

- `constructor`: Método constructor del dado. Recibe e inicializa la cantidad de caras del dado.
- `tirar`: Obtiene el resultado de tirar un dado. Para simular tirar un dado, vamos a usar `random.random()` (se ocupa importar la bibloteca `math`). Esto saca un número flotante al azar ($$a$$) cuyo rango es $$0\le a<1$$. Si uno multiplica el número al azar por la cantidad de caras ($$c$$) eso nos va a dar un número flotante que ronda entre rango es $$0\le a<c$$. Para convertir el número flotante a entero, vamos a _castear_ el número con `(int)`. _Castear_ de un flotante a un entero le quita los decimales al número. Por lo tanto, eso nos va a dar un número $$0\le a\le c-1$$. Por último, como los dados tienen números enteros entre $$1$$ y $$c$$, se le debe sumar $$1$$ al resultado.
- `imprimir`: Imprime información acerca del dado.

## Clase EcuacionesLineares

**Descripción:** La clase encarga de guardar información acerca de ecuaciones lineares.

**Atributos:** Guarda la pendiente (m) y la intersección con el eje Y (b).

**Métodos:**

- `constructor`: Método constructor de la pendiente. Recibe la pendiente e intersección con el eje Y, y las inicializa.
- `imprimir`: Método que imprime la ecuación linear. Por ejemplo, imprime $$y = 5x + 2$$
- `calcular_y`:  Recibe la coordenada X del punto a calcular. Calcula y retorna para la coordenada `y` dada la ecuación linear y la coordenada X. Se puede calcular mediante la siguiente fórmula:

$$ y = m \cdot x + b $$

## Clase Punto

**Descripción:** La clase encarga de guardar información acerca de puntos.

**Atributos:** El punto debe guardar información de sus coordenadas en el eje x, y eje y.

**Métodos:**

- `constructor`: Método constructor del punto.
- `imprimir`: Método que imprime las coordenadas del punto.
- `obtner_x`: Método que retorna la coordenada x del punto.
- `obtner_y`: Método que retorna la coordenada y del punto.
- `obtener_distancia`: Recibe otro objeto Punto. Calcula y retorna la distancia entre ambos puntos. Si el punto actual es $$p_1$$ con coordenadas $$x_1$$ y $$y_1$$, y el punto que recibe es $$p_2$$ con coordenadas $$x_2$$ y $$y_2$$, la distancia (d) entre ambos puntos es:

$$ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$

## Clase RectánguloPunto

**Descripción:** La clase encarga de guardar información acerca de un rectángulo.

**Atributos:** Guarda los puntos (Punto) de la esquina superior izquierda y esquina inferior derecha.

**Métodos:**

- `constructor`: Método constructor del rectángulo. Recibe los puntos de la esquina superior izquierda y la esquina inferior derecha y los inicializa.
- `obtener_altura`: Método que mide la altura del rectángulo.
- `obtener_ancho`: Método que obtiene el ancho del rectángulo.
- `imprimir`: Método que imprime la información del rectángulo.

**Nota:** Puede utilizar el método `obtener_distancia` de un objeto Punto para calcular la altura y el ancho.

## Clase Complejo

**Descripción:** La clase encarga de guardar información acerca de números complejos. Los números complejos son un conjunto numérico que contiene a los reales. Estos se basan en suponer que $$\sqrt{-1}$$ es un número que existe, al menos, de forma imaginaria.

**Atributos:** Cada número complejo se representa por dos partes: real e imaginaria. La real corresponde a un número real y la imaginaria (denotada por i, tal que $$i^2 = -1$$) denota el factor de $$\sqrt{-1}$$ que contiene el número. Por ejemplo:

| Complejo | Parte real | Parte imaginaria | Valor |
|---| ---| ---| ---|
| 1.00 + 1.00i | 1.00 | 1.00 | $$\sqrt{-1}$$ |
| 5.00 + 0.00i | 5.00 | 0.00 | 5.00 |
| 0.00 + 3.00i | 0.00 | 3.00 | $$ 3.00 \cdot \sqrt{-1}$$ |
|-2.00 - 4.00i |-2.00 |-4.00 | $$-2.00 -4.00 \cdot\sqrt{-1}$$ |

**Métodos:**

- `Constructor`: Método constructor de un número complejo. Recibe las partes para crear un número complejo y las inicializa.
- `sumar`: Recibe otro objeto Complejo. Realiza la suma entre ambos números complejos. Siendo $$(a + bi)$$ y $$(c + di)$$ números complejos, se suman ambos números de la siguiente manera: $$(a + bi)  +  (c + di) =  (a + c) + (b + d)i$$
    El método retorna el número complejo resultante.
- `restar`: Recibe otro objeto Complejo. Realiza la resta entre ambos números complejos. Siendo $$(a + bi)$$ y $$(c + di)$$ números complejos, se suman ambos números de la siguiente manera: $$(a + bi)  - (c + di)  =  (a - c) + (b - d)i$$
    El método retorna el número complejo resultante.
- `multiplicar`: Recibe otro objeto Complejo. Realiza la multiplicación entre ambos números complejos. Siendo $$(a + bi)$$ y $$(c + di)$$ números complejos, se suman ambos números de la siguiente manera: $$(a + bi)  * (c + di) =   (ac - bd) + (bc + ad)i$$
    El método retorna el número complejo resultante.
- `dividir`: Recibe otro objeto Complejo. Realiza la división entre ambos números complejos. Siendo $$(a + bi)$$ y $$(c + di)$$ números complejos, se suman ambos números de la siguiente manera: $$\frac{(a + bi)}{(c + di)} =   \frac{ac + bd}{c^{2} + d^{2}} + \frac{bc - ad}{c^{2} + d^{2}}i$$
    El método retorna el número complejo resultante.
- `convertir`: Convierte y retorna un número complejo a su representación en hilera `x.xx + y.yyi`.

## Clases de la Calculadora

Cree una clase calculadora que utilice los números complejos creados anteriormente. Se recomeinda crear una clase encargada de leer la entrada y otra  de mantener el estado de la memoria y hacer las operaciones.

## Clasificación de Hongos

Como parte de su práctica profesional al terminar su carrera, la sección de investigación del MINAE lo ha contratado para ayudar con la clasificación de especies de _fungi_ en los bosques del país. Su misión en particular será trabajar en los bosques cercanos a San José de la Montaña en Heredia, donde abundan diferentes especies de la familia de hongos `Agaricus`.

La familia `Agaricus` se compone de una variedad de más de 3000 especies distintas, de las cuales muchas son comestibles, pero algunas son venenosas. Un hongo particular se puede caracterizar dentro de una especie a partir de las siguientes características:

- Forma de la cabeza
- Altura del tallo
- Color del hongo
- Cantidad de anillos

La forma de la cabeza del hongo es una de las características más importantes para su clasificación. Hasta el momento, se saben que los hongos pueden tener cabezas planas, con forma de campana, convexas o redondas. La altura del tallo indica qué tan alto es el hongo en relación con su tamaño de cabeza. Por facilidad, esta altura se clasifica en bajo, mediano o alto. La variedad de colores de hongos son una de las características más llamativas de este reino. No obstante, la familia `Agaricus` tiende a tener colores más apagados. Hasta el momento los hongos dentro de la familia han sido siempre blancos, café o rojos. Por último, todo hongo puede tener cierta cantidad de anillos. Hay gran cantidad de hongos que no tienen ninguno, pero los que se han registrado hasta la fecha nunca tienen más de 2 anillos.

Las tres especies de hongos identificadas en Costa Rica son **Bisporus**, **Silvaticus**, y **Pocillator**. Los hongos **Bisporus** son una de las especies que les podrían resultar más familiares, ya que son los que se pueden comprar en el supermercado para consumir. Generalmente estos no son venenosos. Esta especie la caracteriza se exclusivamente de color blanco y de baja altura. Además, los **Bisporus** no poseen anillos. La especie **Silvaticus** es conocida como los hongos del bosque. Son una especie que crece cercana a la base de árboles o en pasto abundante. Los hongos de esta especie pueden verse muy distintos entre ellos, pero los identifica tener cabeza en forma ya sea de campana o plana, y que su tamaño nunca es bajo. Por lo mismo, un hongo de esta especie puede o puede no ser venenoso. Por último, los hongos **Pocillator** son hongos que crecen cerca de material en descomposición. Estos se caracterizan por ser altos y blancos, y de cabeza convexa o plana. Generalmente, los hongos de esta especie son venenosos.

El MINAE ha identificado (bajo mucha prueba y error) las características comunes de hongos venenosos en el resto de áreas en Costa Rica. Los hongos que se consideran venenosos tienen las siguientes características:

- Su color es blanco, y además son altos
- La forma de su cabeza es plana, y su color es café
- El hongo tiene 2 anillos

Al ministerio le interesa que usted desarrolle un programa para ayudar a los biólogos de campo a identificar la especie de los hongos que encuentran en sus expediciones, y además identificar si dicho hongo es venenoso o no. Además de identificar la especie al que pertenece dicho hongo, al final de la sesión, el programa debería imprimir estadísticas de la cantidad de hongos encontrados de las 3 especies conocidas y la cantidad de hongos de especie desconocida que se identificaron. Además, al Ministerio le interesa llevar un control de qué tantos hongos de una especie particular que se encontró eran venenosos. Por esto, para las 3 especies conocidas debería mostrarse la cantidad de hongos venenosos que se encontraron.

Implemente un programa que entonces sea capaz de recolectar información de los distintos hongos y mostrar estadísticas asociadas. Para esto, utilice un diseño de dos clases: Hongo y Biologo. La clase Hongo estaría encargada de representar la información de las características del hongo, y además poder calcular a partir de sí mismo la especie a la que pertenece, y además de verificar si es o no venenoso. Por facilidad, todo hongo además debería tener un método para poderse leer de consola con input. La clase Biólogo debería estar encargada de almacenar los hongos que son registrados, calcular la cantidad de hongos por cada una de las 3 especies, la cantidad de hongos venenosos por cada una de las 3 especies, y la cantidad de hongos de especie desconocida que se encontró. Estos datos deberían mostrarse al final del programa.

Por último, como no se sabe de antemano qué cantidad de hongos se van a encontrar, el programa pedirá hongos hasta que la persona decida terminar. Al final de ingresar la información de cada hongo, el programa preguntará si se desea ingresar un nuevo hongo. Si se decide lo contrario, el programa termina.

Entrada de ejemplo: (Entre paréntesis la clasificación y toxicidad de cada uno)

```{bash}
Forma: Campana
Altura: Medio
Color: Café
Anillos: 1
(Silvaticus, Comestible)

¿Desea seguir? Sí

Forma: Campana
Altura: Bajo
Color: Rojo
Anillos: 2
(Desconocido, Venenoso)

¿Desea seguir? Sí

Forma: Redondo
Altura: Bajo
Color: Blanco
Anillos: 0
(Bisporus, Comestible)

¿Desea seguir? Sí

Forma: Redondo
Altura: Bajo
Color: Blanco
Anillos: 0
(Bisporus, Comestible)

¿Desea seguir? Sí

Forma: Redondo
Altura: Alto
Color: Blanco
Anillos: 2
(Desconocido, Venenoso)

¿Desea seguir? Sí

Forma: Plano
Altura: Alto
Color: Café
Anillos: 0
(Silvaticus, Venenoso)

¿Desea seguir? Sí

Forma: Plano
Altura: Alto
Color: Blanco
Anillos: 0
(Pocillator, Venenoso)


¿Desea seguir? Sí

Forma: Convexo
Altura: Alto
Color: Blanco
Anillos: 0
(Pocillator, Venenoso)

¿Desea seguir? Sí

Forma: Plano
Altura: Alto
Color: Café
Anillos: 1
(Silvaticus, Venenoso)

¿Desea seguir? No
```

Salida de ejemplo:

```{bash}
Hongos Bisporus encontrados: 2
Hongos Bisporus venenosos: 0
Hongos Silvaticus encontrados: 3
Hongos Silvaticus venenosos: 2
Hongos Pocillator encontrados: 2
Hongos Pocillator venenosos: 2
Hongos de especie desconocida: 2
```

## Referencias

- Elkner, J., Downey, A. B., y Meyers, C. (2012). How to think like a computer scientist: Learning with python.
- Ramirez, J. P. (2020). Tarea 7. Material del curso CI-0202, Universidad de Costa Rica.
- Villalobos, L. (2019a). Ejercicios clase 13. Material del curso CI-0202, Universidad de Costa Rica.
- Villalobos, L. (2019b). Programación orientada a objetos. Material del curso CI-0202 Universidad de Costa Rica de Leonardo Villalobos.
