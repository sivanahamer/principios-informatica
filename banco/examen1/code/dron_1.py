# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI-0202 Principios de Informática
# Examen #1, Grupo 15
# II Semestre 2021
# Docente Sivana Hamer
# Licencia: CC BY-NC-SA 4.0

# Elaborado por: Sivana Hamer

#Tiempo sin probar: 17 mins, pruebas basic 19 mins

from math import sqrt

def obtener_peso_paquete():
    '''Obtiene el peso del paquete'''
    while True:
        try:
            peso = float(input("Peso paquete: "))
            if 0 < peso < 20:
                return peso
            print("Error peso!")
        except ValueError:
            pass

def obtener_tipo_dron(peso_paquete):
    '''Obtiene el tipo de dron (tamanno), dado el peso'''
    if peso_paquete < 5:
        return "pequeño"
    if peso_paquete < 10:
        return "mediano"
    return "grande"

def calcular_distancia(xa, xb, ya, yb, za, zb):
    '''Calcula la distancia entre ambos puntos'''
    return sqrt((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2)

def obtener_costo_dron(tipo_dron):
    '''Obtiene el costo por km dependiendo el tipo de dron'''
    if tipo_dron == "pequeño":
        return 0.05
    if tipo_dron == "mediano":
        return 0.08
    return 0.12

def calcular_costo_viaje(distancia, costo_km):
    '''Calcula el costo del viaje'''
    return distancia * costo_km * 2

def obtener_coordenadas_punto(nombre):
    print(f"Coordenadas de punto {nombre}: ")
    x = float(input("x: "))
    y = float(input("y: "))
    z = float(input("x: "))
    return x,y,z

def run():
    '''Run general'''
    opcion = 0
    cantidad_viajes = 0
    total_costo = 0
    total_distancia = 0
    while opcion != 4:
        print("Digite una opción:\n1) Determinar dron\n2) Realizar viaje\n3) Mostrar detalles\n4) Salir\n")
        opcion = int(input("Opción: "))
        if opcion == 1:
            peso = obtener_peso_paquete()
            tipo_dron = obtener_tipo_dron(peso)
            print(f"Un dron {tipo_dron} puede transportar un paquete de {peso:.2f}kg")
        elif opcion == 2:
            #Obtiene la distancia
            xa, ya, za = obtener_coordenadas_punto("A")
            xb, yb, zb = obtener_coordenadas_punto("B")
            distancia = calcular_distancia(xa,xb,ya,yb,za,zb)

            #Obtiene la info del dron
            peso = obtener_peso_paquete()
            tipo_dron = obtener_tipo_dron(peso)
            costo_km = obtener_costo_dron(tipo_dron)

            #Calcular viaje
            costo_viaje = calcular_costo_viaje(distancia, costo_km)
            
            #Imprimir cosas
            print()
            print(f"Distancia: {distancia:.2f}km")
            print(f"Costo del viaje: ${costo_viaje:.2f}")

            #Actualizar cosas
            cantidad_viajes+=1
            total_costo += costo_viaje
            total_distancia+= distancia

        elif opcion == 3:
            print(f"Cantidad viajes: {cantidad_viajes}")
            print(f"Total costo: ${total_costo:.2f}")
            print(f"Total distancia: {total_distancia:.2f}km")
        elif opcion > 4:
            print("ERROR! Opcion no es valida")
        print()

run()