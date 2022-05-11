from math import sin, pi

def seno_cardinal(x):
    '''
    
    Calcula el seno cardinal, y lo devuelve.

    Params:
        x: El seno a determinar 
    
    Returns:
        El seno cardinal. En caso de 0, devuelve un 1.
    
    '''

    #Calcula el seno cardinal
    if x == 0: # Caso de indefinicion
        return 1 # senc = 1
    # x!= 0
    return sin(x * pi)/(x*pi) # senc = sin(x*pi)/(x*pi)

valor = float(input("Digite el valor de x del seno cardinal: "))
senc = seno_cardinal(0)
print(f"El seno cardinal de {valor:.3f} es {senc:.3f}")
