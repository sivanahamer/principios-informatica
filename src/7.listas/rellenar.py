def llenar_lista(l):
    """
    Cree una función llamada llenar_lista que le pide al usuario la longitud del arreglo  y que llene los  números en un arreglo.

        l: La longitud del arreglo
    """
    
    lista = []

    for indice in range(l):
        numero =float(input(f"Digite el número {indice + 1}: "))
        lista.append(numero)

    return lista

def imprimir_lista(l):
    '''
    Imprime una lista

        l: La lista a imprimir+
    '''


    print(f"{{{l[0]}", end="")
    for valor in l[1:]:
        print(f", {valor}", end="")    
    print(f"}}")


def imprimir_lista2(l):
    '''
    Imprime una lista usando un while

        l: La lista a imprimir
    '''

    indice = 0
    print(f"[", end="")
    while indice < len(l):
        print(f"{l[indice]} ", end="")
        indice += 1
    print(f"]")


def imprimir_reves(l):
    '''
    Imprime una lista al reves

        l: La lista a imprimir
    '''

    indice = len(l) - 1
    print(f"[", end="")
    while indice >= 0:
        print(f"{l[indice]} ", end="")
        indice -= 1
    print(f"]")


def imprimir_reves2(l):
    '''
    Imprime una lista al reves

        l: La lista a imprimir
    '''

    print(f"[", end="")
    for indice in range(len(l) - 1, -1, -1):
        print(f"{l[indice]} ", end="")
    print(f"]")


def imprimir_reves3(l):
    '''
    Imprime una lista al reves

        l: La lista a imprimir
    '''

    indice = -1
    print(f"[", end="")
    while indice >= - len(l):
        print(f"{l[indice]} ", end="")
        indice -= 1
    print(f"]")


def imprimir_reves4(l):
    '''
    Imprime una lista al reves

        l: La lista a imprimir
    '''

    resultado = ""
    for indice in range(len(l)):
        resultado = f"{l[indice]} {resultado}" 
    return f"[{resultado}]"

longitud = int(input("Digite la longitud del arreglo: "))

a = llenar_lista(longitud)

imprimir_lista(a)
imprimir_lista2(a)
imprimir_reves(a)
imprimir_reves2(a)
imprimir_reves3(a)