def pascal(nivel, columna):
    '''Calcular el numero de pascal para un nivel y columna'''
    #Caso base del nivel 1 con columna 1 del triangulo de pascal
    if nivel == 1 and columna == 1:
        return 1
    #Caso base de la columna menor o igual a 0
    if columna <= 0:
        return 0
    #Caso base que la columna es mayor que el nivel
    if columna > nivel:
        return 0
    #Caso recursivo
    return pascal(nivel - 1, columna - 1) + pascal (nivel - 1, columna)

# print(pascal(3, 2))
# print(pascal(5, 3))
# print(pascal(7, 5))
# print(pascal(1, 1))

def nivel_pascal(nivel):
    '''Imprimir para un nivel el triangulo de pascal'''
    #Procesar todos los elementos en un nivel
    for columna in range(nivel):
        print(pascal(nivel, columna + 1), end=" ")

# nivel_pascal(8)

def triangulo_pascal(niveles):
    '''Imprime todo el triangulo de pascal'''
    #Procesa todos los nivels del triangulo de pascal
    for nivel in range(niveles):
        nivel_pascal(nivel + 1)
        print()

triangulo_pascal(8)
