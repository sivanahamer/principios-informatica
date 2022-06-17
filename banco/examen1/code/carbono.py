def leer_flotante(mensaje):
    '''
    Lee un flotante del usuario
    '''
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            pass

def calcular_emisiones(dioxido_carbono, metano, oxido_nitroso, fluorocarburos, co2_retirado):
    '''Calcula las emisiones de la empresa'''
    return dioxido_carbono + metano *86 + oxido_nitroso * 298 + fluorocarburos * 22800 - co2_retirado

def calcular_multa(emisiones_netas):
    '''Calcula la multa'''
    return (emisiones_netas - 12) * 2.5

def determinar_accion(emisiones_netas, fluorocarburos):
    #Caso con CFC/fluorocarburos
    #Se asume que se prioriza esta clasificacion encima de las otras
    if fluorocarburos > 0:
        return "Clausurar" 
    #Casos con emisiones
    if emisiones_netas <= 0:
        return "Galandronar"
    elif emisiones_netas <= 12:
        return "Notificar"
    return "Multar"

def obtener_opcion():
    '''Obtiene una opcion para el menu principal'''
    while True:
        try:
            opcion = int(input("Opcion [1=Declarar 2=Histogram 3=Salir]: "))
            #Se detiene cuando la opcion es 1, 2 o 3
            if 1 <= opcion <= 3:
                return opcion
        except TypeError:
            pass

def determinar_linea_histograma(accion, comparar_accion, histograma):
    '''Determina la linea del histograma'''
    if accion == comparar_accion:
        return "*" + histograma
    return histograma + "-"

def imprimir_linea(nombre, histograma):
    '''Imprime la linea del histograma'''
    print(f'{nombre:11}: {histograma}')

def imprimir_histograma(galandronar_histograma, notificar_histograma, multar_histograma, clausurar_histograma):
    #Se revisa el caso de que no se ha hecho anteriormente
    if galandronar_histograma == "":
        print("No se han hecho declaraciones aun")
    else:
        imprimir_linea("Galandronar", galandronar_histograma)
        imprimir_linea("Notificar", notificar_histograma)
        imprimir_linea("Multar", multar_histograma)
        imprimir_linea("Clausurar", clausurar_histograma)

def correr_programa():
    #Se guarda las cantidades del histograma
    galandronar_histograma = ""
    notificar_histograma = ""
    multar_histograma = ""
    clausurar_histograma = ""

    opcion = 0

    while opcion != 3:
        opcion = obtener_opcion()
        if opcion == 1:
            #Se registran las emisiones de una empresa
            organizacion = input("Organizacion: ")
            dioxido_carbono = leer_flotante("Dioxido de carbono (Mm3): ")
            metano = leer_flotante("Metano (Mm3): ")
            oxido_nitroso = leer_flotante("Oxido nitroso (Mm3): ")
            fluorocarburos = leer_flotante("Fluorocarburos (Mm3): ")
            co2_retirado = leer_flotante("CO2 retirado (Mm3): ")

            #Se calculan los datos de emisiones
            emisiones = calcular_emisiones(dioxido_carbono, metano, oxido_nitroso, fluorocarburos, co2_retirado)
            accion = determinar_accion(emisiones, fluorocarburos)
            print(f"\n{organizacion} emitio {emisiones:.2f} Mm3 de CO2")

            #Se determina la multa
            if accion == "Multar":
                multa = calcular_multa(emisiones)
                print(f"Multa de {multa:.2f} millones de colones")
        
            #Se muestra la accion
            print(f"Accion: {accion}")
            
            #Se calculan los datos del histograma
            galandronar_histograma = determinar_linea_histograma(accion, "Galandronar", galandronar_histograma)
            notificar_histograma = determinar_linea_histograma(accion, "Notificar", notificar_histograma)
            multar_histograma = determinar_linea_histograma(accion, "Multar", multar_histograma)
            clausurar_histograma = determinar_linea_histograma(accion, "Clausurar", clausurar_histograma)

        elif opcion == 2:
            #Se muestra el historial
            imprimir_histograma(galandronar_histograma, notificar_histograma, multar_histograma, clausurar_histograma)
        else:
            print("Gracias por usar el sistema!")
        print()
correr_programa()