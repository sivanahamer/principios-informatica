def contar_palabras(oracion):
    palabras = oracion.split(" ")
    return len(palabras)

print(contar_palabras("hola soy una oracion"))