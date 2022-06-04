def calcular_estado(ifr):
    if 0 <= ifr < 0.5:
        return "Leve"
    if 0.5 <= ifr < 1:
        return "Semi leve"
    if 1 <= ifr < 1.5:
        return "Moderado"
    if 1.5 <= ifr < 2.0:
        return "Semi grave"
    return "Grave"

def calcular_estrellas(ifr):
    cantidad_estrellas = int(ifr /0.25)
    return "*" * cantidad_estrellas

def calcular_ifr(cm, ci):
    return (cm /ci)* 100

def imprimir_fila(nombre, cm, ci, cr):
    pm = cm/cr
    pi = ci/cr
    ifr = calcular_ifr(cm, ci)
    estado = calcular_estado(ifr)
    estrellas = calcular_estrellas(ifr)
    
    if cr > 0:
        print(f"{estado:14}{nombre:14}{estrellas:14}{cr:14}{pm:14.2f}{pi:14.2f}{ifr:14.2f}")
    else:
        na = "N/A"
        print(f"{na:14}{nombre:14}{na:14}{na:14}{na:14.2}{na:14.2}{na:14.2}")
  

def correr_hospital():
    #cm = cantidad de muertos
    #ci = cantidad de infectados
    #cr = cantidad de reportes
    #---HSJD---
    HSJD_cm = 0
    HSJD_ci = 0
    HSJD_cr = 0
    #---HCG---
    HCG_cm = 0
    HCG_ci = 0
    HCG_cr = 0
    #---HNN---
    HNN_cm = 0
    HNN_ci = 0
    HNN_cr = 0

    # Cantidad de ciclos
    cc = int(input(""))
    print()
    #Guardando los datos a insertar
    for _ in range(cc):
        h = input("")
        cm = int(input(""))
        ci = int(input(""))
        
        #Se agrega dependiendo del tipo
        if h == "HSJD":
            HSJD_cm += cm
            HSJD_ci += ci
            HSJD_cr += 1
        elif h == "HCG":
            HCG_cm += cm
            HCG_ci += ci
            HCG_cr += 1
        else:
            HNN_cm += cm
            HNN_ci += ci
            HNN_cr += 1

    print(f"{'ESTADO':14}{'HOSPITAL':14}{'GRAFICO':14}{'REPORTES':14}{'PROM. MUERTES':14.2}{'PROM. INFEC':14.2}{'IFR':14.2}")
    imprimir_fila("HSJD", HSJD_cm, HSJD_ci, HSJD_cr)
    imprimir_fila("HCG", HCG_cm, HCG_ci, HCG_cr)
    imprimir_fila("HNN", HNN_cm, HNN_ci, HNN_cr)

correr_hospital()