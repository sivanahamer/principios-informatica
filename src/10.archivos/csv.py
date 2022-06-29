def leer_archivo(nombre):
    '''Lee un archivo'''
    archivo = open(nombre, "r")
    texto = archivo.read()
    archivo.close()
    return texto

def pasar_lista(texto):
    '''Devuelve una lista de elementos dado un string de elementos separados por commas.'''
    lista = texto.split(",")
    return lista

def cargar_matriz(nombre):
    '''Carga una matriz desde un archivo csv'''
    texto = leer_archivo(nombre)
    matriz = []
    lineas = texto.split("\n")
    for linea in lineas:
        matriz.append(pasar_lista(linea))
    return matriz

m = cargar_matriz("./data/estudiantes.csv")
print(m[1:])