from imprimir import imprimir_matriz
from total import sumar_total
from total_columna import sumar_total_columna
from total_fila import sumar_total_fila

def leer_lista(etiqueta, tamanno):
    lista = []
    for indice in range(tamanno):
        elemento = input(f"{etiqueta} {indice + 1}: ")
        lista.append(elemento)
    return lista

def obtener_lista_etiqueta(etiqueta, tamanno):
    lista = []
    for indice in range(tamanno):
        elemento =f"{etiqueta} {indice + 1}"
        lista.append(elemento)
    return lista

def leer_matriz(n, m):
    """
    Leer una matriz de n filas y m columnas
    """
    M =[]
    for i in range(n):
        fila = []
        for j in range(m):
            elemento = int(input(f"M[{i}][{j}] = "))
            fila.append(elemento)
        M.append(fila)
    return M

def restar_matrices(A, B):
    """
    Se restan las matrices
    """
    C =[]
    for i in range(len(A)):
        fila = []
        for j in range(len(A[i])):
            elemento = A[i][j] - B[i][j]
            fila.append(elemento)
        C.append(fila)
    return C

def imprimir_matriz_variable(matriz):
    #Calcular el tamanno maximo de un elemento como hilera
    max_size = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            size_actual = len(str(matriz[i][j]))
            if size_actual > max_size:
                max_size = size_actual + 1

    # Imprime la matriz
    for fila in matriz:
        for elemento in fila:
            print(f" {elemento:20}", end="")
        print()

def correr_tiendas():
    #Obtenemos las dimensiones de las matrices
    n = int(input("Cantidad de tiendas: "))
    m = int(input("Cantidad de trimestres: "))

    #Obtenemos los nombres de las tiendas y los trimestres
    tiendas = leer_lista("Tienda", n)
    trimestres = obtener_lista_etiqueta("Trimestre", m)
    print(trimestres)

    #Obtenemos las matrices de ganancias y perdidas
    print("Ganacias")
    ganacias = leer_matriz(n,m)
    print("Perdidas")
    perdidas = leer_matriz(n,m)

    #Obtenemos las utilidades
    utilidades = restar_matrices(ganacias, perdidas)
    print("Utilidades")
    imprimir_matriz(utilidades)

    #Calcular los totales
    utilidades_tiendas = sumar_total_fila(utilidades)
    print("Utilidades tiendas")
    imprimir_matriz_variable([tiendas, utilidades_tiendas])

    utilidades_trimestres = sumar_total_columna(utilidades)
    print("Utilidades trimestres")
    imprimir_matriz_variable([trimestres, utilidades_trimestres])

    utilidades_anuales = sumar_total(utilidades)
    print("Utilidades anuales")
    print(utilidades_anuales)

correr_tiendas()