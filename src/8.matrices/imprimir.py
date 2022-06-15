
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f" {elemento:3}", end="")
        print()


# imprimir_matriz([[1,2,3,4], [5,6,7,8], [9,10,11,12]])