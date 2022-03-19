# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI-0202 Principios de Informática
# Examen parcial #1, Grupo 11
# I Semestre 2021
# Docente Sivana Hamer
# Licencia: CC BY-NC-SA 4.0

# Elaborado por: Sivana Hamer

def convertir_miligramos_quilates(miligramos):
    '''Convierte los miligramos a quilates'''
    return miligramos/200

def obtener_quilates():
    '''Obtiene los quilates para crear un anillo.'''
    #Ciclo para siempre obtener quilates validos
    while True:
        quilate = float(input("Quilates por anillo: "))
        #Valida la cantidad de quilates
        if 0.5 <= quilate <= 6:
            return quilate

def calcular_cantidad_anillos(rubíes_totales, quilates_por_anillo):
    '''Calcula y retorna la cantidad de anillos completos que se pueden producir'''
    return (int) (rubíes_totales/quilates_por_anillo)

def obtener_precio_tipo_material(tipo_material):
    '''Obtiene y retorna el precio del tipo de material.'''
    if tipo_material == "plata":
        return 100.0
    if tipo_material == "oro":
        return 250.0
    if tipo_material == "platino":
        return 500.0
    return None

def calcular_precio(quilates, cantidad_anillos, material_costo):
    '''Calcula el precio de los anillos'''
    return ((quilates**3) * 350 + material_costo) * cantidad_anillos

opcion = 0
rubies_ct = 0
ventas_totales = 0
while opcion != 5:
    #Mostrar el menu
    print("Digite una opción:\n1) Registrar rubíes\n2) Calcular anillos\n3) Vender anillos\n4) Mostrar detalles\n5) Salir\n")
    #Obtener las opciones
    opcion = int(input("Opción seleccionada: "))
    #Registrar rubíes
    if opcion == 1:
        rubies_mg = float(input("Rubíes minados (mg): "))
        rubies_ct +=convertir_miligramos_quilates(rubies_mg)
    #Calcular anillos
    elif opcion == 2:
        quilates_por_anillo = obtener_quilates()
        cantidad_anillos = calcular_cantidad_anillos(rubies_ct, quilates_por_anillo)
        print(f"Con {rubies_ct} rubíes, se pueden producir {cantidad_anillos} anillos de {quilates_por_anillo} quilates.")
    #Vender anillos
    elif opcion == 3:
        #Obtenemos del usuario los datos que no tenemos
        quilates_por_anillo = obtener_quilates()
        tipo_material = input("Tipo de material: ")

        #Obtener de funciones los datos requeridos
        cantidad_anillos = calcular_cantidad_anillos(rubies_ct, quilates_por_anillo)
        precio_material = obtener_precio_tipo_material(tipo_material)

        #Calcular ventas
        ventas = calcular_precio(quilates_por_anillo, cantidad_anillos, precio_material)
        print(f"Se vendio  ${ventas}")
        ventas_totales+= ventas

        #Actualizar los rubies actuales
        rubies_ct -= quilates_por_anillo * cantidad_anillos

    #Mostrar detalles
    elif opcion == 4:
        print(f"Rubíes actuales: {rubies_ct:.2f} ct")
        print(f"Ventas totales: ${ventas_totales:.2f}")
    #Salir
    elif opcion == 5:
        pass
    #Error
    else:
        print("ERROR! Opción no válida")
    print()