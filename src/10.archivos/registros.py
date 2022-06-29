def obtener_archivo(nombre):
    archivo = open(nombre, "r")
    lineas = archivo.readlines()
    archivo.close()
    datos = []
    for linea in lineas:
        datos.append(linea.replace("\n", "").split(";"))
    return datos

def obtener_notas(datos):
    #Obtener la cantidad de evaluaciones
    cantidades_evaluaciones = datos[0]
    cantidad_labs = int(cantidades_evaluaciones[0])
    cantidad_tareas = int(cantidades_evaluaciones[1])
    cantidad_examenes = int(cantidades_evaluaciones[2])

    #Obtienen los porcentajes
    tareas_labs_porcentaje = datos[1]
    examenes_porcentaje = datos[2]

    #Header (se ignora esta columna)
    header = datos[3]

    #Procesan los datos de estudiantes
    estudiantes = datos[4:]
    for estudiante in estudiantes:
        nombre_estudiante = estudiante[0]
        carne_estudiante = estudiante[1]

        print(f"{nombre_estudiante} - {carne_estudiante}")

        for indice_laboratorio in range(cantidad_labs):
            lab_n = estudiante[indice_laboratorio + 2]
            print(f"Lab: {lab_n}")
        
def escribir_resultados(nombre, resultados):
    pass

def correr_registros(archivo_lectura, archivo_resultados):
    datos = obtener_archivo(archivo_lectura)
    resultado = obtener_notas(datos)
    escribir_resultados(archivo_resultados, resultado)

correr_registros("./data/grupo1.csv", "./data/resultados_grupo1.txt")