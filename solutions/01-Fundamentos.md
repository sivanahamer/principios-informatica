# 馃捇 Fundamentos de la computaci贸n: Soluciones

## Pseudoc贸digo: Cocinar palomitas 馃嵖

### Algoritmo

1. Quitar el pl谩stico de la bolsas.
2. Abrir el microondas.
3. Meter la bolsa en el microondas.
4. Cerrar el microondas.
5. Poner de tiempo 3 minutos en el microondas.
6. Iniciar el microondas.
7. Esperar 3 minutos.
8. Abrir el microondas.
9. Sacar las palomitas del microondas.

### Pseudoc贸digo

```{bash}
// Los tiempos son en segundos
palomitas = Palomitas()
microondas = Microondas()
microondas.meter(palomitas, 180) // Abre, mete y cierra
tiempoEspera = 0
si tiempoEspera < 180:
    tiempoEspera += 1
    esperar(1)
comida = microondas.sacar() // Abre, mete y cierra
```

## Pseudoc贸digo: Pasear a un perro 馃悤

### Algoritmo

1. Revisar el clima para ver si se puede caminar (sin lluvia o mucho sol)
2. Buscar el perro
3. Buscar la correa, si no hay no se puede seguir
4. Poner la correa al perro
5. Alistar cosas que se ocupan (agua, zapatos y bolsitas)
6. Buscar las llaves, si no hay no se puede seguir.
7. Acercarnos a la puerta con el perro
8. Abrir la puerta de la casa para salir
9. Salir por la puerta de la casa
10. Cerrar la puerta para iniciar el paseo

### Pseudoc贸digo

```{bash}
clima_bonito = revisar_clima()
si clima_bonito:
    hay_perro, hay_correa, hay_llaves = buscar_lo_minimo()
    si hay_perro y hay_correa y hay_llaves:
        llaves, agua, zapatos, bolsitas, correa, perro = alistar_cosas()
        yo.poner(zapatos, agua, llaves, bolsitas)
        perro.poner(correa) #Implica que sostengamos la cinta cosa de la correo
        yo.ir_puerta()
        yo.abrir_puerta(llaves)
        yo.salir_casa()
        yo.cerrar_puerta()
```

## Convertir a d贸lares 馃挼

### Problema

Pasar una cantidad de colones a dolares.

### Analizar

- El tipo de cambio de dolar a colon es: 675
- dolar = colones/tipo_cambio
- Colones tiene que ser un positivo

### Dise帽ar (pseudoc贸digo)

```{bash}
colones = pedir_colones("Digite colones:")
tipo_cambio = 675 # 馃様
si colones > 0:
    dolares = colones/tipo_cambio
    imprimir("Tiene $"+ dolares)
si no:
    imprimir("No se puede convertir colones que no son un numero positivo")
```

### Implementar

<script src="https://gist.github.com/sivanahamer/f24efda382ab77bd127a03895e4a275b.js"></script>

### Probar

- Se prueba colones = 5000. Da resultado $7.41
- Se prueba colones = 0. No funcionaba, se agrega  manejar el caso para evitar problemas. Ahora imprime `No se puede convertir colones que no son un numero positivo`.
- Se prueba colones = -1000. Imprime `No se puede convertir colones que no son un numero positivo`.
- Se prueba colones = 70.5. Imprime `Tiene $0.10`.

<div class="alert alert-danger" role="alert">
  <i class="fa fa fa-exclamation-triangle fa-inverse fa-lg"></i> 
  Cuando probamos, es bueno probar valores "l铆mite", que podr铆an dar errores o ser distintos. <br/>
  - Con n煤meros es com煤n probar uno positivo, uno negativo, uno real y el cero.<br/>
  - Con texto es com煤n probar texto normal y uno vac铆o.<br/>
  Tambi茅n es bueno probar que pasa si al pedir un n煤mero se le da texto o viceversa.
</div>

## Cancha de futbol 鈿?

### Problema

Calcular el 谩rea de una cancha de f煤tbol.

### Analisis

Vamos a calcular el 谩rea de un rect谩ngulo con la f贸rmula:

$$A = b 鈭? a$$

### Dise帽o (pseudoc贸digo)

```{bash}
# Pedimos la base y la altura
mostrar (" Escriba la base del rectangulo : ")
b = leer ()
mostrar (" Escriba la altura del rectangulo :")
a = leer ()
# Calculamos el area
A = b * a
mostrar (" El area del rectangulo es :" , A)
```

### Pruebas

- 驴Qu茅 pasa si se utiliza $$a=5$$ y $$b=3$$?
- 驴Qu茅 pasa si se utiliza $$a\le 0$$? Haga las correcciones correspondientes.
- 驴Qu茅 pasa si se utiliza $$b\le 0$$? Haga las correcciones correspondientes.