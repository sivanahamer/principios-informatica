from rellenar import imprimir_lista

def obtener_maximo(lista):
    '''
    Obtiene el numero max de una lista

        lista: La lista a analizar
    '''
    if len(lista) > 0:
        _max = lista[0]
        for valor in lista[1:]:
            if _max < valor:
                _max = valor
        return _max
    return None

lista = [70, 1000, -2]
print("El promedio de la lista")
imprimir_lista(lista)
print(f"es {obtener_maximo(lista)}")