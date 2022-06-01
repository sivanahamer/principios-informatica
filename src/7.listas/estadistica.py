from rellenar import imprimir_lista

def obtener_estadistica(l):
    '''Obtiene el promedio de una lista'''
    suma = 0
    for valor in l:
        suma += valor
    return suma/len(l)

lista = [90, 120]
print("El promedio de la lista")
imprimir_lista(lista)
print(f"es {obtener_estadistica(lista)}")