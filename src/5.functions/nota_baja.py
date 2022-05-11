from math import inf

def procesar_evaluacion(cantidad_evaluaciones, mensaje, porcentaje_de_la_nota, quitar_minimo):
    minimo = inf
    total_notas = 0
    #para cada evaluacion
    for _ in range(cantidad_evaluaciones):
        #obtener las notas de las evaluaciones
        nota = float(input(mensaje))
        #obtener el minimo de las evaluaciones
        if nota < minimo:
            minimo = nota
        #sumar la nota dada al total
        total_notas+= nota
    #obtengo el porcentaje quitando el minimo
    if quitar_minimo:
        porcentaje = ((total_notas - minimo)/(cantidad_evaluaciones-1) )*porcentaje_de_la_nota
    #calcular el porcentaje con el minimo
    else:
        porcentaje = (total_notas/cantidad_evaluaciones)* porcentaje_de_la_nota
    #devolver el porcentaje
    return round(porcentaje, 2)


def procesar_estudiante():
    #obtener el id (carnet)
    carnet = input("Digite el carnet del estudiante:")

    #obtenemos los laboratorios
    porcentaje_laboratorios = procesar_evaluacion(10, "Digite la nota del laboratorio: ", 0.3, True)
    #obtener las tareas
    porcentaje_tareas = procesar_evaluacion(10, "Digite la nota de la tarea: ", 0.2, True)
    #obtener los examenes
    porcentaje_examenes = procesar_evaluacion(3, "Digite la nota del examen: ", 0.5, False)

    #obtener la nota oficial
    nota_oficial = float(input("Digite la nota indicada en el curso: "))
    #nota calculada = laboratorios+ tareas + examenes
    nota_calculada = porcentaje_laboratorios + porcentaje_tareas + porcentaje_examenes
    #si la nota oficial no es igual a la nota calculada
    if nota_oficial != nota_calculada:
        #devolvemos el carne del estudiante, nota oficial, y nota calculada
        return f"{carnet} {nota_oficial} {nota_calculada:.2f}\n"

    return ""

def procesar_grupo():
    #obtener el id
    identificador_grupo = int(input("Indique el identificador del grupo: "))
    #obtener la cantidad de estudiantes
    cantidad_estudiantes = int(input("Indique la cantidad de estudiantes: "))
    resultado_estudiante = f"Grupo {identificador_grupo}:\n"
    #para cada estudiante
    for _ in range(cantidad_estudiantes):
        resultado_estudiante += procesar_estudiante()
    return resultado_estudiante + "\n"

def procesar_notas_mas_bajas():
    ''' Procesa los grupos'''
    # recibir la cantidad de grupos
    cantidad_grupos = int(input("Cantidad de grupos: "))
    # para cada grupo
    resultado_grupo = ""
    for _ in range(cantidad_grupos):
        resultado_grupo += procesar_grupo() + "\n"

    print()
    print(resultado_grupo)

procesar_notas_mas_bajas()