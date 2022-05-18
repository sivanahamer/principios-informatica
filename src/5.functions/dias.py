def convertir_dia_nombre(dia):
    '''
    Recibe un entero de 0 al 6 que representa un día de la semana y retorna el nombre del día de la semana respectivo. El día 0 representa "Domingo". Por ejemplo, si recibe 3 retorna "Miercoles".
    '''
    if dia == 0:
        return "Domingo"
    if dia == 1:
        return "Lunes"
    if dia == 2:
        return "Martes"
    if dia == 3:
        return "Miercoles"
    if dia == 4:
        return "Jueves"
    if dia == 5:
        return "Viernes"
    if dia == 6:
        return "Sabado"

def convertir_nombre_dia(nombre):
    '''
    Escriba la función inversa de convertir_dia_nombre que recibe el nombre del día de la semana y retorna el numero entero. Por ejemplo, si recibe "Sabado" retorna 6.
    '''
    if nombre == "Domingo":
        return 0
    if nombre == "Lunes":
        return 1
    if nombre == "Martes":
        return 2
    if nombre == "Miercoles":
        return 3
    if nombre == "Jueves":
        return 4
    if nombre == "Viernes":
        return 5
    if nombre == "Sabado":
        return 6

def calcular_dia(nombre, delta):
    '''
    Esta función podrá responder preguntas como Si hoy es martes, y en 10 días tengo una cita, ¿qué día de la semana es?. Por lo tanto, la función recibe el día de la semana y un número de días a agregar llamado delta. Por ejemplo, si recibe "Martes" y 10 retorna "Viernes". Utilice las funciones declaradas anteriormente.
    '''

    return convertir_dia_nombre((convertir_nombre_dia(nombre) + delta) % 7)


dia = input("Digite el dia: ")
delta = int(input("Digite el delta: "))

resultado_dia = calcular_dia(dia, delta)

print(f"El dia de la semana es: {resultado_dia}")