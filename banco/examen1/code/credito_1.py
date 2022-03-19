# Universidad de Costa Rica
# Escuela de Ciencias de la Computación e Informática
# CI-0202 Principios de Informática
# Examen parcial #1, Grupo 12
# II Semestre 2020
# Docente Sivana Hamer
# Licencia: CC BY-NC-SA 4.0

# Elaborado por: Sivana Hamer

def calcular_puntaje_creditos(annos_historial, salario_mensual, utilidades_mensuales, deuda):
    return (annos_historial / 4) * ((salario_mensual - utilidades_mensuales)/deuda) * 75

def obtener_categoria_credito(puntaje_credito):
    if puntaje_credito <= 580:
        return "Malo", 6.0
    if 580 < puntaje_credito <= 670:
        return "Razonable", 5.25
    if 670 < puntaje_credito <= 740:
        return "Bueno", 4.5
    if 740 < puntaje_credito <= 800:
        return "Muy bueno", 3.75
    if 800 < puntaje_credito:
        return "Excelente", 3

def calcular_prestamo_compuesto(prestamo, tasa_interes, meses):
    return prestamo * (1+ (tasa_interes/100))**meses

def obtiene_datos_prestamo():
    annos_historial = float(input("Años de historial de crédito: "))
    salario_mensual = float(input("Salario mensual actual ($): "))
    utilidades_mensuales = float(input("Utilidades mensuales actuales ($): "))
    deuda = float(input("Total en deuda actual ($): "))
    prestamo = float(input("Préstamo ($): "))
    meses = int(input("Meses que han pasado: "))
    return annos_historial, salario_mensual, utilidades_mensuales, deuda, prestamo, meses

def obtener_opcion():
    # print("Seleccione una de las siguientes opciones:")
    print("1) Procesar")
    print("2) Mostrar")
    print("3) Salir")
    return int(input("Ingrese una opción: "))

def calcular_prestamo():
    #Totales de prestamos
    total_malo = 0
    total_razonable = 0
    total_bueno = 0
    total_muy_bueno = 0
    total_excelente = 0

    #Ciclo
    seguir = True
    while seguir:
        opcion = obtener_opcion()
        print()
        if opcion == 1:
            #Obtener datos
            annos_historial, salario_mensual, utilidades_mensuales, deuda, prestamo, meses = obtiene_datos_prestamo()

            #Obtiene el puntaje de credito
            puntaje_credito = calcular_puntaje_creditos(annos_historial, salario_mensual, utilidades_mensuales, deuda)

            #Obtiene las categorias
            categoria, tasa_interes = obtener_categoria_credito(puntaje_credito)

            #Calcula los intereses compuestos
            prestamo_compuestos = calcular_prestamo_compuesto(prestamo, tasa_interes, meses)

            #Suma el total a la categoria
            if categoria == "Malo":
                total_malo += prestamo_compuestos
            elif categoria == "Razonable":
                total_razonable += prestamo_compuestos
            elif categoria == "Bueno":
                total_bueno += prestamo_compuestos
            elif categoria == "Muy bueno":
                total_muy_bueno += prestamo_compuestos
            elif categoria == "Excelente":
                total_excelente += prestamo_compuestos

            #Muestra los mensajes
            print()
            print(f"Puntaje crédito: {puntaje_credito}")
            print(f"Categoría: {categoria}")
            print(f"Préstamo a cobrar: ${prestamo_compuestos:.4f}")

        elif opcion == 2:
            #Mostar totales
            print(f"Total de préstamos:")
            print(f"Malo: ${total_malo:.4f}")
            print(f"Razonable: ${total_razonable:.4f}")
            print(f"Bueno: ${total_bueno:.4f}")
            print(f"Muy bueno: ${total_muy_bueno:.4f}")
            print(f"Excelente: ${total_excelente:.4f}")

        elif opcion == 3:
            seguir = False

        else:
            print("ERROR: Opción no valida")
        print()

calcular_prestamo()