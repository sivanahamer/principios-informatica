# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI-0202 Principios de Informática
# Examen parcial #1, Grupo 11
# I Semestre 2021
# Docente Sivana Hamer
# Licencia: CC BY-NC-SA 4.0

# Elaborado por: Sivana Hamer

from math import floor

def convertir_gramos_quilates(gramos):
    return gramos/200

def calcular_cantidad_anillos(rubies, quilates):
    try:
        return floor(rubies/quilates)
    except ZeroDivisionError:
        return None

def remover_rubies(quilates, cantidad_anillos):
    return cantidad_anillos * quilates

def obtener_precio_tipo_material(tipo_material):
    if tipo_material == "Plata":
        return 100
    if tipo_material == "Oro":
        return 250
    if tipo_material == "Plata":
        return 500
    return None

def calcular_precio(quilates, cantidad_anillos, material_precio):
    return ((quilates**3)*350+material_precio)*cantidad_anillos

def obtener_quilates():
    while True:
        quilates = float(input("Quilates por anillo: "))
        if 6>= quilates >= 0.5:
            return quilates
        print("ERROR! Los quilates por anillo tiene que ser mayor o igual a 0.5, o menor o igual a 6")

def correr_opcion1():
    gramos = float(input("Rubíes minados (mg): "))
    return convertir_gramos_quilates(gramos)

def correr_opcion2(rubies):
    quilates = obtener_quilates()
    cantidad_anillos = calcular_cantidad_anillos(rubies, quilates)
    print(f"Con {rubies} rubíes, se pueden producir {cantidad_anillos} anillos de {quilates} quilates")

def correr_opcion3(rubies):
    quilates = obtener_quilates()
    material_precio = obtener_precio_tipo_material(input("Tipo de material: "))
    cantidad_anillos = calcular_cantidad_anillos(rubies, quilates)
    rubies-= remover_rubies(quilates, cantidad_anillos)
    venta = calcular_precio(quilates, cantidad_anillos, material_precio)
    print(f"Se vendio ${venta:.2f}")
    return venta, rubies

def mostrar_detalles(rubies, ventas):
    print(f"Rubíes actuales: \t{rubies}")
    print(f"Ventas totales: \t${ventas:.2f}")

def correr():
    rubies = 0
    ventas = 0
    while True:
        opcion = int(input("Digite la opcion:\n1) Registrar rubíes\n2) Calcular anillos\n3) Vender anillos\n4) Mostrar detalles\n5) Salir\n\n"))
        if opcion == 1:
            rubies += correr_opcion1()
        elif opcion == 2:
            correr_opcion2(rubies)
        elif opcion == 3:
            venta, rubies = correr_opcion3(rubies)
            ventas+= venta
        elif opcion == 4:
            mostrar_detalles(rubies, ventas)
        elif opcion == 5:
            return
        else:
            print(f"ERROR! Entrada invalida")
        print()

correr()