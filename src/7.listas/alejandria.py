LIBRO_TITULO = 0
LIBRO_AUTOR = 1
LIBRO_PAGS = LIBRO_AUTOR + 1
LIBRO_GENERO = LIBRO_PAGS + 1

def pedir_libro():
    # Pedir datos
    titulo = input("Titulo: ")
    autor = input("Autor@: ")
    pags = int(input("# paginas: "))
    genero = input("Genero: ")

    #Creamos un libro como una lista y lo devolvemos
    libro = [titulo, autor, pags, genero]
    return libro

def imprimir_libro(libro):
    print("-" * 30)
    print(f"Titulo: {libro[LIBRO_TITULO]}\tAutor@: {libro[LIBRO_AUTOR]}")
    print(f"# pags: {libro[LIBRO_PAGS]}\tGenero: {libro[LIBRO_GENERO]}")
    print("-" * 30)

def encontrar_libro(libros, titulo):
    '''Encontrar el primer libro con el titulo'''
    for libro in libros:
        if libro[LIBRO_TITULO] == titulo:
            return libro
    return None


def obtener_todos(lista, indice):
    lista_todos = []
    for elemento in lista:
        lista_todos.append(elemento[indice])
    return lista_todos

def obtener_unicos(lista_todos):
    lista_unicos = []
    for elemento in lista_todos:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    
    return lista_unicos

def imprimir_catalogo(libros):
    print(f"# libros = {len(libros)}")

    print("Autores unicos")
    autores_todos = obtener_todos(libros, LIBRO_AUTOR)
    print(obtener_unicos(autores_todos))

    print("Cantidad libros por genero")
    genero_todos = obtener_todos(libros, LIBRO_GENERO)
    genero_unico = obtener_unicos(genero_todos)
    for genero in genero_unico:
        print(f"{genero} : {genero_todos.count(genero)}")

def perdir_opcion():
    opcion = int(input("Digite una opcion...\n\t1) Agregar un libro\n\t2) Buscar un libro\n\t3) Borrar un libro\n\t4) Catálogo de la biblioteca\n\t5) Quemar la biblioteca\n\t6) Imprimir bibloteca\n\t7) Salir\n Opcion: "))
    return opcion

def correr_bibloteca():
    libros = []
    continuar = True
    while continuar:
        opcion = perdir_opcion()
        if opcion == 1:
            print("boop beep 🤖")
            print("digite un libro beep")
            libro = pedir_libro()
            libros.append(libro)
        elif opcion == 2:
            print("beep boop 🤖")
            titulo = input("digite el libro a buscar: ")
            libro = encontrar_libro(libros, titulo)
            if libro is not None:
                imprimir_libro(libro)
            else:
                print("NO HAY LIBRO BEEP")
        elif opcion == 3:
            print("Borrar titulo")
            print("beep boop 🤖")
            titulo = input("digite el libro a borrar: ")
            libro = encontrar_libro(libros, titulo)
            if libro is not None:
                libros.remove(libro)
            else:
                print("NO HAY LIBRO BEEP")
        elif opcion == 4:
            imprimir_catalogo(libros)
        elif opcion == 5:
            print("BORRRARRR 🔥🔥🔥🔥🔥")
            libros.clear()
        elif opcion == 6:
            print()
            for indice, libro in enumerate(libros):
                print(f'Libro {indice + 1}')
                imprimir_libro(libro)
        elif opcion == 7:
            continuar = False
        else:
            print("Opcion no valida. Vuelvalo a intentar.")
        print()
            
correr_bibloteca()