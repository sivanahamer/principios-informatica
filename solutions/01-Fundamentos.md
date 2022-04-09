# 💻 Fundamentos de la computación: Soluciones

## Pseudocódigo: Cocinar palomitas 🍿

### Algoritmo

1. Quitar el plástico de la bolsas.
2. Abrir el microondas.
3. Meter la bolsa en el microondas.
4. Cerrar el microondas.
5. Poner de tiempo 3 minutos en el microondas.
6. Iniciar el microondas.
7. Esperar 3 minutos.
8. Abrir el microondas.
9. Sacar las palomitas del microondas.

### Pseudocódigo

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

## Pseudocódigo: Pasear a un perro 🐕

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

### Pseudocódigo

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

## Convertir a dólares 💵

### Problema

Pasar una cantidad de colones a dolares.

### Analizar

- El tipo de cambio de dolar a colon es: 675
- dolar = colones/tipo_cambio
- Colones tiene que ser un positivo

### Diseñar (pseudocódigo)

```{bash}
colones = pedir_colones("Digite colones:")
tipo_cambio = 675 # 😔
si colones > 0:
    dolares = colones/tipo_cambio
    imprimir("Tiene $"+ dolares)
si no:
    imprimir("No se puede convertir colones que no son un numero positivo")
```

### Implementar

```{python}
colones = float(input("Digite colones: "))
tipo_cambio = 675
if colones > 0:
    dolares = colones/tipo_cambio
    print(f"Tiene ${dolares:.2f}")
else:
    print("No se puede convertir colones que no son un numero positivo")
```

### Probar

- Se prueba colones = 5000. Da resultado $7.41
- Se prueba colones = 0. No funcionaba, se agrega  manejar el caso para evitar problemas. Ahora imprime `No se puede convertir colones que no son un numero positivo`.
- Se prueba colones = -1000. Imprime `No se puede convertir colones que no son un numero positivo`.
- Se prueba colones = 70.5. Imprime `Tiene $0.10`.

<div class="alert alert-danger" role="alert">
  <i class="fa fa fa-exclamation-triangle fa-inverse fa-lg"></i> 
  Cuando probamos, es bueno probar valores "límite", que podrían dar errores o ser distintos. <br/>
  - Con números es común probar uno positivo, uno negativo, uno real y el cero.<br/>
  - Con texto es común probar texto normal y uno vacío.<br/>
  También es bueno probar que pasa si al pedir un número se le da texto o viceversa.
</div>

## Cancha de futbol ⚽

### Problema

Calcular el área de una cancha de fútbol.

### Analisis

Vamos a calcular el área de un rectángulo con la fórmula:

$$A = b ∗ a$$

### Diseño (pseudocódigo)

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

- ¿Qué pasa si se utiliza $$a=5$$ y $$b=3$$?
- ¿Qué pasa si se utiliza $$a\le 0$$? Haga las correcciones correspondientes.
- ¿Qué pasa si se utiliza $$b\le 0$$? Haga las correcciones correspondientes.