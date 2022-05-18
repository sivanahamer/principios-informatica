from entrada_valida import obtener_flotante

def sumar(numero1, numero2):
    ''''
    Recibe dos números y retorna la suma de los números. Por ejemplo, 10 y 3 retorna 13.
    '''
    return numero1 + numero2

def restar(numero1, numero2):
    '''
    Recibe dos números y retorna la resta del primer número con el segundo número. Por ejemplo,10 y 3 retorna 7.
    '''
    return numero1 - numero2

def multiplicar(numero1, numero2):
    '''
    Recibe dos números y retorna la multiplicación de los números. Por ejemplo, 10 y 3 retorna 30.
    '''
    return numero1 * numero2

def dividir(numero1, numero2):
    '''
    Recibe dos números y retorna la división del primer número con el segundo número. Por ejemplo, 10 y 3 retorna 3.3334.
    '''
    try:
        return numero1 / numero2
    #Devuelve None cuando hay un error
    except ZeroDivisionError:
        print("No se puede dividir por cero 🤨")
        return None

def mostar_menu():
    '''
    Además, se debe implementar una función denominada mostrar_menu que muestra el menú y retorna la opción digitada del menú. 
    '''
    opcion = ""
    while opcion != "+" and opcion != "-" and opcion != "*" and opcion != "X" and opcion != "\\":
        print("Seleccione una de las siguientes opciones:\n\t+) Sumar\n\t-) Restar\n\t*) Multiplicar\n\t\) Dividir\n\tX) Detener la ejecucion")
        opcion = input("Opcion seleccionada: ")
    
    return opcion

def ejecutar_operacion(opcion, numero1, numero2):
    '''
    Ejecuta una de las operaciones
    '''
    if opcion == "+":
        return sumar(numero1, numero2)
    if opcion == "-":
        return restar(numero1, numero2)
    if opcion == "*":
        return multiplicar(numero1, numero2)
    if opcion == "\\":
        return dividir(numero1, numero2)

def correr_calculadora():
    '''
    Por último, debe implementar la función correr_calculadora que se encarga de utilizar todas las funciones declaradas anteriormente.
     El algoritmo a muy alto nivel de correr_calculadora es la siguiente:

    mientras el usuario no digite que finalice:
        opcion = mostrar_menu()
        numero1, numero2 = obtener_numeros()
        resultado = ejecutar_operacion(opcion, numero1, numero2)
        imprimir(resultado) 
    ''' 

    opcion = ""
    while opcion != "X":
        opcion = mostar_menu()
        #Caso de que queremos aplicar una operacion
        if opcion != "X":
            num1 = obtener_flotante("Digite numero1: ", "ERROR! No es un numero")
            num2 = obtener_flotante("Digite numero2: ", "ERROR! No es un numero valido")
            resultado = ejecutar_operacion(opcion, num1, num2)
            if resultado is not None:
                print(f"{num1:.4f} {opcion} {num2:.4f} = {resultado:.4f}")
    
        print()
    
correr_calculadora()