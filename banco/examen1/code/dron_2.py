# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI-0202 Principios de Informática
# Examen #1, Grupo 15
# II Semestre 2021
# Docente Sivana Hamer
# Licencia: CC BY-NC-SA 4.0

# Elaborado por: Sivana Hamer

def obtener_peso_paquete():
    '''
    Implementa la función obtener_peso_paquete(). Obtiene el peso del paquete de la entrada estándar. Debe asegurarse que es un paquete con un peso válido.
    '''
    while True:
        peso = float(input("Digite el peso: "))
        if 0 < peso <= 20:
            break
        print("ERROR! No es un peso valido")
    return peso

def determinar_tipo_dron(peso_paquete):
    '''
    Implementa la función determinar_tipo_dron(peso_paquete). Determina y retorna el tipo de dron (pequeño, mediano o grande) que se debe utilizar, dado un peso.
    '''
    if peso_paquete < 5:
        return "Pequeño"
    if peso_paquete < 10:
        return "Mediano"
    return "Grande"

def calcular_distancia(xa, xb, ya, yb, za, zb):
    '''
    Implementa la función calcular_distancia(xa, xb, ya, yb, za, zb). Calcula y retorna la distancia entre las coordenadas del punto A y la coordenadas del punto B.
    '''
    d = ((xb-xa)**2 + (yb - ya) **2 + (zb - za)**2) ** (1/2)
    return d

def calcular_costo_km_dron(tipo_dron):
    '''Implementa la función calcular_costo_km_dron(tipo_dron). Calcula y retorna el costo por km del dron dependiendo su tipo.'''
    costo_km = 0
    if tipo_dron == "Pequeño":
        costo_km = 0.05
    elif tipo_dron == "Mediano":
        costo_km = 0.08
    else: 
        costo_km = 0.12
    return costo_km
    
def calcular_costo_viaje(distancia, costo_km):
    '''
    Implementa la función calcular_costo_viaje(distancia, costo_km). Calcula y retorna el costo del viaje.
    '''
    return distancia * costo_km * 2

def obtener_coordenadas(nombre):
    print(f"Coordenadas punto {nombre}")
    x = float(input("X: "))
    y = float(input("Y: "))
    z = float(input("Z: "))
    return x, y, z

#Pone un valor que no es 4 para que se haga el ciclo
opcion = None

#Declarar los totales y acumulados
cantidad_viajes = 0
total_costo = 0
totaL_distancia = 0

#Mientras no sea la opcion de salir
while opcion != 4:

    print("Digite la opcion\n1) Determinar dron\n2) Realizar viaje\n3) Mostrar detalles\n4) Salir\n")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        #Obtiene los datos para determinar el tipo de dron
        peso = obtener_peso_paquete()
        tipo_dron = determinar_tipo_dron(peso)

        #Imprime los resultados
        print(f"Un dron {tipo_dron} puede transportar un paquete de {peso:.2f}")
    elif opcion == 2:
        #Obtiene las coordenadas con su distancia
        xa, ya, za = obtener_coordenadas("A")
        xb, yb, zb = obtener_coordenadas("B")
        d = calcular_distancia(xa, xb, ya, yb, za, zb)

        #Obtiene el peso del paquete
        peso = obtener_peso_paquete()
        ck = calcular_costo_km_dron(determinar_tipo_dron(peso))
        c = calcular_costo_viaje(d, ck)

        #Imprime los resultados
        print(f"Distancia: {d:.2f}km")
        print(f"Costo del viaje: ${c:.2f}")

        #Actualiza los totales y las cantidades de veces
        total_costo += c
        totaL_distancia += d
        cantidad_viajes +=1

    elif opcion == 3:
        #Imprimir los datos
        print(f"\nCantidad viajes: {cantidad_viajes}")
        print(f"Total costo: ${total_costo:.2f}")
        print(f"Total distancia: {totaL_distancia:.2f}km")
    elif opcion > 4:
        print("ERROR! Opcion no es valida")
    print()