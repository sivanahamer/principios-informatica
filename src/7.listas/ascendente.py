def verificar_ascendente(lista):
    '''Verifica que todos los elementos de la lista son ascedentes'''
    for indice in range(len(lista) - 1):
        if lista[indice] > lista[indice + 1]:
            return False
    return True

print(verificar_ascendente([4, 10, 5]))
print(verificar_ascendente([10, 21, 22, 30]))
