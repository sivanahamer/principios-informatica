def quitar_vocales(texto):
    '''
    Quita vocales creando una nueva hilera sin las vocales
    '''
    # #Pasamos a minuscula
    # texto = texto.lower()

    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    resultado = ""
    #Revisamos que cada letra del texto no este en vocales
    for letra in texto:
        if letra not in vocales:
            resultado += letra
    return resultado

def quitar_vocales2(texto):
    '''
    Quita vocales replazando una vocal por un caracter vacio
    '''
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    #Se replaza cualquier vocal que se encuentra dentro de vocales
    for vocal in vocales:
       texto = texto.replace(vocal, "")
    return texto

print(quitar_vocales2("Pájaro"))