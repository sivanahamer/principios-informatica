# n = 5
# Imprimir esto 5, 4, 3, 2, 1

def imprimir_iterativo(n):
    ''' Imprimir los numeros iterativamente de n a 1'''

    #Iterar sobre indice de manera descendente
    indice = n
    while (indice >= 1):
        #Imprimimos
        print(indice)
        indice-=1

# imprimir_iterativo(5)


def imprimir_recursivo(n):
    ''' Imprimir los numeros recursivamente de n a 1'''
    #Imprimir n
    print(n)
    #Cuando sea n == 1, se detenga el programa
    if (n == 1):
        return
    #En otro caso, voy a seguir imprimiendo recursivamente
    else:
        return imprimir_recursivo(n - 1)

imprimir_recursivo(5)