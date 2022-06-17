def ajustar_termometro(temp, porcentaje, ajuste):
    '''
    
    Realiza el ajuste de temperaturas basado en un porcentaje
    
    ajuste: Si es + es que reporta valores mayores, si es - reporta valores menores. En otro caso, no hay ajuste
    '''
    if ajuste == "+":
        return temp - (temp * porcentaje)
    elif ajuste == "-":
        return temp + (temp * porcentaje)
    return temp

def histograma_linea(cantidad_fuera_ideal, cantidad_registros, num_zona):
    cantidad_asteriscos =  cantidad_fuera_ideal
    cantidad_guiones = cantidad_registros - cantidad_fuera_ideal
    print(f'Zona {num_zona}: {"*" * cantidad_asteriscos}{"-" * cantidad_guiones}')

def verificar_temperatura_idonea(temp):
    return 16 < temp < 25

def imprimir_histograma(cantidad_fuera_zona1, cantidad_fuera_zona2, cantidad_registros):
    if cantidad_registros == 0:
        print("No se han registrado lecturas aun")
    else:
        histograma_linea(cantidad_fuera_zona1, cantidad_registros, "1")
        histograma_linea(cantidad_fuera_zona2, cantidad_registros, "2")

def calcular_promedio(temp1, temp2):
    return (temp1 + temp2) / 2

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Opcion [1=Registro 2=Histograma 3=Salir]: "))
            #Se detiene cuando la opcion es 1, 2 o 3
            if 1 <= opcion <= 3:
                return opcion
        except TypeError:
            pass

def procesar_temperaturas():
    temp_e = "NA"
    temp_o = "NA"
    temp_c = "NA"
    cont_temperaturas = 1
    while temp_e == "NA" or temp_o == "NA" or temp_c == "NA":
        term = input(f"Termometro {cont_temperaturas}: ")
        if term == "O":
            temp_o = float(input(f"Temperatura {cont_temperaturas}: "))
            cont_temperaturas += 1
        elif term == "C":
            temp_c = float(input(f"Temperatura {cont_temperaturas}: "))
            temp_c = ajustar_termometro(temp_c, 0.15, "+")
            cont_temperaturas += 1
        elif term == "E":
            temp_e = float(input(f"Temperatura {cont_temperaturas}: "))
            temp_e = ajustar_termometro(temp_e, 0.025, "-")
            cont_temperaturas += 1
        else:
            print("Error: Termometro invalido")

    promedio_zona_1 = calcular_promedio(temp_o, temp_c)
    promedio_zona_2 = calcular_promedio(temp_c, temp_e)
    print()
    print("Promedio de temperaturas tras ajuste:")
    print(f"Zona 1: {promedio_zona_1:.2f}")
    print(f"Zona 2: {promedio_zona_2:.2f}")
    print()

    #Obtner cantidad fuera de la zona
    cantidad_fuera_zona1 = 0
    cantidad_fuera_zona2 = 0
    if not verificar_temperatura_idonea(promedio_zona_1):
        cantidad_fuera_zona1 +=1
    if not verificar_temperatura_idonea(promedio_zona_2):
        cantidad_fuera_zona2 +=1
    return cantidad_fuera_zona1,cantidad_fuera_zona2 

def correr_invernadero():
    opcion = ""
    cantidad_fuera_zona1 = 0
    cantidad_fuera_zona2 = 0
    cantidad_registros = 0
    while opcion != 3:
        opcion = obtener_opcion()
        if opcion != 3:
            #Opcion 1
            if opcion == 1:
                fuera_zona1, fuera_zona2 = procesar_temperaturas()
                cantidad_fuera_zona1 += fuera_zona1
                cantidad_fuera_zona2 += fuera_zona2
                cantidad_registros += 1
            #Opcion 2
            else:
                imprimir_histograma(cantidad_fuera_zona1, cantidad_fuera_zona2, cantidad_registros)
        else:
            print("Gracias por usar el sistema!")

correr_invernadero()