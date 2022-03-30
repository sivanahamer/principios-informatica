# 📂 Archivos

## Copiar

Cree un programa que copie los contenidos de un archivo a otro.

## Lista

Cree un programa que lea una lista de números enteros de input. Guárdela en un archivo, separando por comas los elementos. Luego cárguela del archivo y muestre los elementos.

## Revertir

Cree un programa que lee las lineas y cree un nuevo archivo con las lineas en orden invertido.

## CSV

Cree un programa que cargue una matriz de un archivo csv. Muestrela con print.

## Macar

Cree un programa que no imprime las líneas que contienen el substring de `Macar`. Por ejemplo, el archivo con el siguiente texto:

```{bash}
Dale a tu cuerpo alegria Macarena
Que tu cuerpo es pa' darle alegria y cosa buena
Dale a tu cuerpo alegria, Macarena
Hey Macarena
Macarena tiene un novio que se llama
Que se llama de apellido Vitorino,
Que en la jura de bandera el muchacho
Se metio con dos amigos
```

Imprimería las siguientes líneas:

```{bash}
Que tu cuerpo es pa' darle alegria y cosa buena
Que se llama de apellido Vitorino,
Que en la jura de bandera el muchacho
Se metio con dos amigos
```

## Los registros

Este semestre usted ha optado por ser el asistente de un curso. Al azar se le ha asignado al profesor LV, que es infame por entregar las notas finales del curso muy tardíamente. Pasa el tiempo y es final de semestre. El profesor necesita su ayuda para terminar de evaluar los estudiantes del curso. Además, ¡el le está pidiendo que le ayude a calificar los grupos que dio el semestre pasado y aún no ha entregado! O sea, hay mucho trabajo por delante.

Dichosamente, usted que ya llevó el curso de Principios de Informática, sabe que puede resolver mucho trabajo con el poder de la programación. Usted ha elegido crear un programa que le ayude a calcular las notas finales del curso automáticamente. Dichosamente, el profesor siempre utiliza 3 tipos de evaluación: laboratorios, tareas y exámenes. El problema es que a él le gusta experimentar con la evaluación, entonces a veces hace más o menos de un tipo de evaluación. Más aún, también le gusta cambiar el porcentaje de la nota de cada evaluación.

El profesor quiere que calcule el promedio final de cada estudiante. Además, él quiere que calcule también la nota promedio de cada evaluación.

El profesor siempre edita las notas en Excel, y las guarda en formato CSV. Este tipo de archivo (CSV) guarda una matriz de datos internamente. Las filas se encuentran separadas por cambios de línea (Enter), y las columnas por punto y coma (;). El archivo del profesor se estructura de la siguiente manera:

- La primer fila contiene 3 números (separados por ; ), que corresponden con la cantidad de laboratorios, tareas y exámenes del curso.
- La segunda fila contiene 2 números, que corresponden con el porcentaje de evaluación de laboratorios y tareas.
- La tercer fila contiene $$m$$ números, $$m$$ siendo la cantidad de exámenes, que corresponden con el porcentaje de cada examen.
- La cuarta fila contiene siempre el encabezado de la tabla: Nombre, Carné, Lab 1, ..., Lab N, Tarea1, ..., Tarea O, Examen 1, ..., Examen M. En este orden vienen los datos de los estudiantes.
- La quinta fila en adelante son los registros de notas de los alumnos. Cada nota corresponde a un estudiante y sus notas.

El siguiente archivo es uno de los registros de nota del profesor:

```{csv}
12;10;3
0.15;0.25
0.2;0.2;0.2
Nombre;Carné;Laboratorio 1;Laboratorio 2;Laboratorio 3;Laboratorio 4;Laboratorio 5;Laboratorio 6;Laboratorio 7;Laboratorio 8;Laboratorio 9;Laboratorio 10;Laboratorio 11;Laboratorio 12;Tarea 1;Tarea 2;Tarea 3;Tarea 4;Tarea 5;Tarea 6;Tarea 7;Tarea 8;Tarea 9;Tarea 10;Examen 1;Examen 2;Examen 3
Daniela Azofeifa;B00224;0;100;0;100;100;0;0;100;100;0;100;100;100.0;16.0;0.0;9.0;94.0;92.0;0.0;0.0;100.0;58.0;38.0;26.0;0.0
Flory Piedra;B91016;100;100;100;100;100;100;100;100;100;100;100;100;100.0;96.0;83.0;84.0;97.0;97.0;91.0;96.0;87.0;95.0;91.0;90.0;90.0
Johnny Ureña;B02934;0;0;0;0;0;0;0;0;0;0;0;0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0
Alejandra Sauma;B95703;100;100;100;0;100;0;0;100;100;0;100;100;0.0;17.0;10.0;86.0;0.0;76.0;33.0;31.0;0.0;26.0;0.0;49.0;57.0
Carlos Calvo;B40459;100;100;100;0;100;100;100;100;100;0;100;100;93.0;89.0;76.0;99.0;91.0;97.0;96.0;99.0;84.0;87.0;87.0;98.0;91.0
César Herrera;B75728;0;100;0;100;0;0;0;0;0;100;0;0;0.0;52.0;35.0;18.0;0.0;0.0;0.0;21.0;0.0;0.0;60.0;0.0;45.0
Carlos Rodríguez;B25941;100;100;100;100;100;100;100;100;100;100;0;100;100.0;88.0;100.0;92.0;100.0;100.0;88.0;100.0;84.0;91.0;70.0;99.0;77.0
David Ureña;B01036;0;0;0;0;0;0;0;0;0;0;0;0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0
Raquel Herrera;B81278;100;100;100;100;100;100;100;100;100;100;100;100;92.0;98.0;89.0;95.0;89.0;93.0;98.0;86.0;87.0;93.0;84.0;71.0;76.0
Alejandra Ureña;B41454;100;0;100;100;100;100;100;100;100;100;100;100;92.0;98.0;97.0;100.0;100.0;100.0;84.0;75.0;94.0;86.0;98.0;79.0;62.0
Luis Cerdas;B56255;100;100;100;100;100;100;100;100;100;100;100;100;80.0;89.0;96.0;80.0;87.0;98.0;91.0;97.0;81.0;93.0;68.0;82.0;74.0
Carolina Alvarado;B64702;100;100;0;0;0;0;100;0;0;0;100;100;18.0;59.0;65.0;27.0;35.0;33.0;12.0;0.0;73.0;33.0;40.0;72.0;69.0
Sandra Rojas;B56258;100;0;100;100;0;0;0;0;0;100;100;0;0.0;26.0;15.0;43.0;19.0;44.0;0.0;0.0;1.0;0.0;89.0;11.0;51.0
Gustavo Alvarado;B43906;0;0;0;0;0;0;0;0;0;0;0;0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0
Alejandra Mata;B03229;0;0;100;100;0;100;100;100;100;0;100;0;6.0;0.0;66.0;1.0;0.0;5.0;0.0;0.0;73.0;58.0;0.0;38.0;56.0
Michelle Piedra;B52459;100;0;100;100;100;100;100;100;100;100;100;100;100.0;77.0;77.0;94.0;100.0;83.0;79.0;80.0;96.0;74.0;100.0;52.0;82.0
Natalia Cerdas;B87659;0;0;0;0;100;100;100;0;0;0;0;0;76.0;2.0;48.0;33.0;64.0;0.0;29.0;27.0;82.0;64.0;100.0;100.0;88.0
Diego Lizano;B13837;100;0;100;0;100;100;100;100;0;0;0;0;44.0;7.0;0.0;15.0;97.0;68.0;77.0;0.0;62.0;48.0;0.0;70.0;21.0
Michelle Manzano;B62468;100;100;100;100;100;100;100;100;100;100;100;100;62.0;72.0;72.0;94.0;85.0;69.0;100.0;85.0;84.0;84.0;79.0;91.0;72.0
César Villalobos;B66661;100;100;100;100;100;100;100;100;100;100;100;100;93.0;87.0;84.0;90.0;90.0;89.0;91.0;90.0;94.0;97.0;87.0;93.0;80.0
Flory Moreno;B96110;100;100;0;0;100;100;100;100;100;100;0;100;86.0;94.0;89.0;87.0;84.0;82.0;65.0;91.0;91.0;100.0;97.0;78.0;65.0
Joel Madrigal;B04789;0;0;0;0;0;0;0;0;0;0;0;0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0
César Jimenez;B87793;100;100;100;100;100;100;100;100;100;100;100;0;39.0;20.0;0.0;0.0;74.0;13.0;0.0;46.0;82.0;29.0;97.0;60.0;17.0
Jesús Madrigal;B24193;0;0;0;0;100;0;100;100;100;0;100;100;0.0;0.0;0.0;44.0;0.0;14.0;0.0;40.0;34.0;0.0;55.0;70.0;23.0
Michelle Cerdas;B14077;100;100;100;100;100;100;100;100;100;0;100;100;91.0;92.0;84.0;89.0;78.0;90.0;74.0;95.0;89.0;91.0;72.0;79.0;85.0
Raquel Esquivel;B12064;0;0;100;100;0;100;0;100;100;0;0;0;15.0;31.0;3.0;73.0;41.0;0.0;31.0;14.0;70.0;42.0;19.0;28.0;0.0
Sebastián Ureña;B27160;0;0;0;0;0;0;0;0;0;0;0;0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0;0.0
Alejandra Rosales;B82145;100;100;100;100;100;0;100;100;0;100;100;100;76.0;90.0;81.0;81.0;80.0;89.0;83.0;75.0;87.0;74.0;74.0;76.0;76.0
Santiago Chaves;B56532;100;100;100;0;100;100;100;0;100;100;100;100;100.0;70.0;76.0;80.0;66.0;64.0;88.0;88.0;67.0;100.0;45.0;68.0;64.0
José Piedra;B80627;100;0;100;100;100;100;100;100;100;100;100;100;80.0;75.0;56.0;77.0;100.0;92.0;72.0;75.0;100.0;84.0;84.0;75.0;75.0
```

Entonces:

- La primer fila indica que hay 12 laboratorios, 10 tareas y 3 exámenes
- La segunda fila indica que los laboratorios valen 15\% de la evaluación, y las tareas valen 25\%
- La tercer fila indica que el primer examen vale 20\%, así como el segundo y el tercero
- La cuarta fila solo contiene los encabezados. Siempre vienen en el mismo orden: Nombre, Carné, Labs, Tareas, Exámenes
- Y la quinta fila en adelante son todos los datos, en el mismo orden del encabezado: Nombre, Carné, 12 labs, 10 tareas y 3 exámenes

La nota final de los laboratorios se calcula como el promedio de las notas de todos los labs. Este mismo proceso es igual para las tareas. Finalmente, el promedio final se calcula multiplicando cada nota final (labs, tareas, y cada uno de los exámenes) por su peso.

En lugar de mostrar los resultados en la pantalla, usted quiere guardarlos en un archivo. Usted quisiera que el archivo final se viera así:

```{txt}
Promedio final por estudiante
Diego Ureña (B66581): 38.05
Fernando Campos (B82997): 59.62
Carlos Sauma (B02229): 83.03
Natalia Castillo (B42971): 92.75
Natalia Bonilla (B07852): 83.80
Sandra Víquez (B01605): 53.28
Daniel Lizano (B72487): 82.65
Luis Madrigal (B25391): 83.73
Fernando Cerdas (B34416): 81.93
Flory Cerdas (B71493): 73.85
Carolina Sauma (B34026): 74.78
Alejandra Lizano (B65779): 48.63
Fernando Moreno (B42494): 73.25
Lucía Madrigal (B74510): 85.00
Jesús Ortega (B24852): 73.45
José Porras (B33835): 73.60
Fernando Cerdas (B14701): 31.53
Fernando Castillo (B07343): 59.27
Flory Madrigal (B54546): 64.40
Diego Azofeifa (B21165): 74.00
Carolina Víquez (B12781): 50.60
Christian Madrigal (B31578): 40.83
María Chaves (B26626): 22.50
Joel Sauma (B54374): 81.23
Pablo Lizano (B30530): 70.68
Christian Mata (B61297): 80.68
Carlos Alvarado (B36862): 92.93
Pablo Alvarado (B03269): 0.00
Raquel Quesada (B93677): 67.60
Christian Víquez (B70666): 80.45

Promedio por evaluación
Laboratorio 1: 70.00
Laboratorio 2: 73.33
Laboratorio 3: 76.67
Laboratorio 4: 66.67
Laboratorio 5: 76.67
Laboratorio 6: 80.00
Laboratorio 7: 60.00
Laboratorio 8: 73.33
Laboratorio 9: 86.67
Laboratorio 10: 76.67
Laboratorio 11: 80.00
Laboratorio 12: 73.33
Tarea 1: 65.07
Tarea 2: 58.97
Tarea 3: 65.73
Tarea 4: 66.97
Tarea 5: 70.73
Tarea 6: 63.57
Tarea 7: 67.53
Tarea 8: 65.03
Tarea 9: 62.63
Tarea 10: 65.83
Examen 1: 64.03
Examen 2: 63.83
Examen 3: 64.47
```

## Referencias

- Villalobos, L. (2019a). Archivos. Material del curso CI-0202 Universidad de Costa Rica de Leonardo
Villalobos.
- Villalobos, L. (2019b). Ejercicios clase 12. Material del curso CI-0202, Universidad de Costa Rica de Leonardo Villalobos.
- Downey, A. B., y Mayfield, C. (2020). Think Java: How to Think Like a Computer Scientist (Second edition ed.).
- Eck, D. J. (2020). Introduction to programming using Java (Eighth edition ed.). Geneva (NY): Hobart and William Smith Colleges, Department of mathematics and computer science.
- Elkner, J., Downey, A. B., y Meyers, C. (2012). How to think like a computer scientist: Learning with python.
