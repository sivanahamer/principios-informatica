def obtener_numeros(n):
    '''Obtiene una lista de numeros'''
    lista = []
    for _ in range(n):
        numero = int(input("Digite un numero: "))
        lista.append(numero)
    return lista

def pasar_fila(lista):
    '''Pasar una lista de numeros a un string separado por comma'''
    fila = f"{lista[0]}"
    for elemento in lista[1:]:
        fila += f",{elemento}"
    return fila

def guardar_archivo(nombre, texto):
    '''Guarda un archivo de texto'''
    archivo = open(nombre, "w")
    archivo.write(texto)
    archivo.close()

def leer_archivo(nombre):
    '''Lee un archivo'''
    archivo = open(nombre, "r")
    texto = archivo.read()
    archivo.close()
    return texto

def pasar_lista(texto):
    '''Devuelve una lista de elementos dado un string de elementos separados por commas.'''
    lista = texto.split(",")
    lista_enteros = []
    for elemento in lista:
        lista_enteros.append(int(elemento))
    return lista_enteros

ruta_archivo = "./data/lista.txt"
lista_numeros = obtener_numeros(3)
fila = pasar_fila(lista_numeros)
guardar_archivo(ruta_archivo, fila)
texto = leer_archivo(ruta_archivo)
lista_nueva = pasar_lista(texto)
print(lista_nueva)
