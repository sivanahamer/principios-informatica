def rotar_agujas_reloj(punto_cardinal):
    '''
    Recibe uno de los cuatro puntos cardinales como parámetro y retorna el siguiente punto cardinal en la dirección de las agujas del reloj. Por ejemplo, si se le digita "N" retorna "E".
    '''
    # N -> E
    if punto_cardinal == "N":
        return "E"

    # E -> S
    if punto_cardinal == "E":
        return "S"

    # S -> O
    if punto_cardinal == "S":
        return "O"

    # O -> N
    if punto_cardinal == "O":
        return "N"


def rotar_contra_agujas_del_reloj (punto_cardinal):
    '''
    Recibe uno de los cuatro puntos cardinales como parámetro y retorna el siguiente punto cardinal en la dirección contra las agujas del reloj. Por ejemplo, si se le digita "N" retorna "O".
    '''
    # N -> O
    if punto_cardinal == "N":
        return "O"

    # O -> S
    elif punto_cardinal == "O":
        return "S"

    # S -> E
    elif punto_cardinal == "S":
        return "E"

    # E -> N
    elif punto_cardinal == "E":
        return "N"


def imprimir_menu():
    '''
    No recibe ningún parámetro y retorna la opción seleccionada del usuario en el menú entre rotar con la dirección del reloj o en contra del reloj.
    '''
    pass

def rotar_brujula():
    '''
    No recibe ni retorna nada. Esta función se encarga de llamar a las funciones previamente definidas.
    '''
    pass

# Pruebas ~~~~
print("ROTAR CON AGUJA:")
print(f"N -> {rotar_agujas_reloj('N')}")
print(f"E -> {rotar_agujas_reloj('E')}")
print(f"S -> {rotar_agujas_reloj('S')}")
print(f"O -> {rotar_agujas_reloj('O')}")


print("ROTAR CONTRA AGUJA:")
print(f"N -> {rotar_contra_agujas_del_reloj('N')}")
print(f"O -> {rotar_contra_agujas_del_reloj('O')}")
print(f"S -> {rotar_contra_agujas_del_reloj('S')}")
print(f"E -> {rotar_contra_agujas_del_reloj('E')}")
