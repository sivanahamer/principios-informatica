def calcular_superficie(lat_ne, long_ne, lat_so, long_so):
    return ((long_ne - long_so) * 59.38) * ((lat_ne -lat_so) * 58.95)

def mostrar_informacion_region(lat_ne, long_ne, lat_so, long_so, tipo, superficie):
    print("+ Información de la región:\n")
    print(f"- Latitud: {long_ne:.2f} - {long_so:.2f}")
    print(f"- Longitud: {lat_ne:.2f} - {lat_so:.2f}")
    print(f"- Superficie aproximada: {superficie:.4f} km^2")
    print(f"- Tipo de terreno: {tipo}")

def obtener_punto(nombre):
    '''Obtiene los datos de un punto con un nombre'''
    print(f"Datos punto {nombre}:")
    lat = float(input("Latitud: "))
    long = float(input("Latitud: "))
    return lat, long

def correr():
    continuar = True

    #Totales por terreno
    total_montanna = 0
    total_llano = 0
    total_desierto = 0
    total_crater = 0
    total_volcan = 0

    while continuar:
        #Pide la información del menú y lo procesa
        print("Menú:\n1) Procesar una medición\n2) Mostrar totales geográficos\n3) Salir")
        opcion = int(input("Ingrese una opción: "))
        print()

        if opcion == 1:
            #Proces los datos de la medicion del terreno
            lat_ne, long_ne = obtener_punto("NE")
            print()
            lat_so, long_so = obtener_punto("SO")
            print()
            superficie = calcular_superficie(lat_ne, long_ne, lat_so, long_so)

            #Obtiene los datos del tipo de terreno y los guarda dependiendo el tipo
            print("1) montaña\n2) llano\n3) desierto\n4) cráter\n5) volcán")
            opcion_terreno = int(input("Ingrese una opción de terreno: "))

            if opcion_terreno == 1:
                total_montanna += superficie
                tipo = "montaña"
            elif opcion_terreno == 2:
                total_llano += superficie
                tipo = "llano"
            elif opcion_terreno == 3:
                total_desierto += superficie
                tipo = "desierto"
            elif opcion_terreno == 4:
                total_crater += superficie
                tipo = "cráter"
            elif opcion_terreno == 5:
                total_volcan += superficie
                tipo = "volcán"

            mostrar_informacion_region(lat_ne, long_ne, lat_so, long_so, tipo, superficie)

        elif opcion == 2:
            print("+ Totales geográficos:\n")
            print(f"montaña: {total_montanna:.4f} km^2")
            print(f"llano: {total_llano:.4f} km^2")
            print(f"desierto: {total_desierto:.4f} km^2")
            print(f"cráter: {total_crater:.4f} km^2")
            print(f"volcán: {total_volcan:.4f} km^2")
        elif opcion == 3:
            continuar = False
        else:
            print("Error: Opción no disponible")
        print()

correr()