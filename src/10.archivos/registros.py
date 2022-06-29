POSICION_LABS = 0
POSICION_TAREAS = 1
POSICION_EXAMENES = 2

def leer_archivo():
    '''Lee un archivo, que pide el nombre'''
    #Pedirle el nombre de donde se encuentra el archivo
    # RUTA ABSOLUTA EN MI COMPU: C:\Users\Sivana\source\repos\principios-ii2021\data\grupo1.csv
    # RUTA RELATIVA EN MI REPO: .\data\grupo1.csv
    nombre = input("Dar una ruta del archivo: ")
    #Abrir el archivo
    archivo = open(nombre, "r")
    #Obtener los datos
    texto = archivo.read()
    #Cerrarlo
    archivo.close()
    return texto

def procesar_linea_enteros(linea):
    '''Procesa una linea y lo cambia a enteros'''
    lista_numeros = []
    linea = linea.split(";")
    for elemento in linea:
        lista_numeros.append(int(elemento))
    return lista_numeros


def procesar_linea_flotantes(linea):
    '''Procesa una linea y lo cambia a flotantes'''
    lista_numeros = []
    linea = linea.split(";")
    for elemento in linea:
        lista_numeros.append(float(elemento))
    return lista_numeros


def obtener_promedio(notas):
    '''Calcula el promedio de notas'''
    suma_total = 0
    for nota in notas:
        suma_total+= float(nota)
    return suma_total/len(notas)

def obtener_promedio_pesos(notas, pesos):
    '''Calcula el promedio de notas con pesos'''
    total = 0
    for indice, nota in enumerate(notas):
        peso =  float(pesos[indice])
        total += float(nota) * peso
    return total

def procesar_estudiante(datos_estudiante, cantidad_evaluaciones, rubro_taras_labs, rubro_examenes):
    '''Procesa linea de la informacion de cada estudiante'''
    #Procesando la info general de estudiante
    nombre = datos_estudiante[0]
    carne = datos_estudiante[1]

    #Obtener las notas de cada tipo
    notas = datos_estudiante[2:]
    labs = notas[:cantidad_evaluaciones[POSICION_LABS]]
    tareas = notas[cantidad_evaluaciones[POSICION_LABS]:cantidad_evaluaciones[POSICION_TAREAS] + cantidad_evaluaciones[POSICION_LABS]]
    examenes = notas[cantidad_evaluaciones[POSICION_TAREAS] + cantidad_evaluaciones[POSICION_LABS]:]
    
    #Calcular la nota de promedio de estudiante
    promedio_labs = obtener_promedio(labs)
    promedio_tareas = obtener_promedio(tareas)
    #Obtiene todas las notas para cada categoria
    notas_categoria = [promedio_labs, promedio_tareas] + examenes # 90, 80, 100, 90, 80
    #Sume los resultados para cada categorias
    promedio = obtener_promedio_pesos(notas_categoria, rubro_taras_labs + rubro_examenes)

    #Creamos el texto del resultado de estudiante
    texto_estudiante = f"{nombre} ({carne}): {promedio:.2f}"
    return texto_estudiante

def procesar_evaluacion(evaluacion, notas_evaluacion):
    '''Procesa el promedio de una evaluacion'''
    promedio = obtener_promedio(notas_evaluacion)
    return f"{evaluacion}: {promedio:.2f}"

def procesar_archivo(texto):
    '''Procesa el archivo de reporte'''
    #Guarda un espacio para guardar el texto del archivo
    texto_resultado = ""
    datos_estudiantes = []

    #Obtener los datos de las asignaciones
    #Separa las lineas por \n
    lineas = texto.split("\n")

    cantidad_evaluaciones = procesar_linea_enteros(lineas[0]) #Separa una linea por ; cada elemento
    rubro_tareas_labs = procesar_linea_flotantes(lineas[1])
    rubro_examenes = procesar_linea_flotantes(lineas[2])
    header = lineas[3].split(";")
    evaluaciones = header[2:]

    #Procesar las notas por estudiante
    texto_resultado += "Promedio final por estudiante\n"
    for linea in lineas[4:]:
        #Obtenemos los datos de cada fila y los guardamos
        datos_estudiante = linea.split(";")
        datos_estudiantes.append(datos_estudiante)

        estudiante = procesar_estudiante(datos_estudiante, cantidad_evaluaciones, rubro_tareas_labs, rubro_examenes)
        #Agregar al texto resultante los valores por estudiante
        texto_resultado+= f"{estudiante}\n"

    #Procesar las notas por asignaciones
    texto_resultado += "\nPromedio por evaluacion\n"
    for indice, evaluacion in enumerate(evaluaciones):
        notas_evaluacion = []
        for fila in datos_estudiantes:
            nota_evaluacion_estudiante = fila [2 + indice]
            notas_evaluacion.append(nota_evaluacion_estudiante)
        texto_resultado+= f"{procesar_evaluacion(evaluacion, notas_evaluacion)}\n"

    return texto_resultado


def guardar_archivo(texto):
    '''Guarda el archivo de texto'''
    #Pedir el nombre/ruta de donde se guarda el archivo.
    nombre = input("Dar una ruta de donde guardar el archivo: ")
    #Abrir el archivo para escribir
    archivo = open(nombre, "w")
    #Escribimos el texto al archivo
    archivo.write(texto)
    #Cerrarlo
    archivo.close()

def correr_procesamiento():
    '''Metodo principal que invoca a los otros metodos'''
    #Leer/procesar un archivo
    texto_archivo = leer_archivo()
    #Procesamos el archivo
    texto_resultado = procesar_archivo(texto_archivo)
    #Guardar los resultados en un archivo
    guardar_archivo(texto_resultado)

correr_procesamiento()