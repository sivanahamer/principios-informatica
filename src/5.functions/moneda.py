from random import random

#Definicion de la funcion
def tirar_moneda():
    '''
    Tira una moneda de dos caras. Imprime escudo o corona depenediendo el tiro.
    '''

    #Generando un numero aleatorio
    numero_aleatorio = random()
    #Determinamos si es escudo o corona, en una moneda balanceada
    if numero_aleatorio > 0.5:
        print("Escudo 🛡️")
    else:
        print("Corona 🍺")

#Invocaciones
tirar_moneda()
tirar_moneda()
tirar_moneda()
tirar_moneda()
tirar_moneda()
tirar_moneda()