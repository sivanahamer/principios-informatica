from random import random

#Definicion de la funcion
def tirar_dado(n):
    '''
    Tira una dado de n caras. Imprime el numero dependiendo el dado
    '''
    caras = int((random() * n) + 1)
    print(caras)


#Invocaciones
tirar_dado(6)
tirar_dado(8)
tirar_dado(20)
tirar_dado(8)