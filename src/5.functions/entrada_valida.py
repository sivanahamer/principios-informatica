def obtener_int(mensaje, mensaje_error):
    '''
    Obtiene un entero

    Params:
        - mensaje: El mensaje a imprimir cuando se quiere obtener el numero 
        - mensaje_error: El mensaje a imprimir cuando sucede un error.

    Returns:
        - El entero que se obtiene
    '''
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print(mensaje_error)

def obtener_flotante(mensaje, mensaje_error):
    '''
    Obtiene un flotante

    Params:
        - mensaje: El mensaje a imprimir cuando se quiere obtener el numero 
        - mensaje_error: El mensaje a imprimir cuando sucede un error.

    Returns:
        - El flotante que se obtiene
    '''
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(mensaje_error)

