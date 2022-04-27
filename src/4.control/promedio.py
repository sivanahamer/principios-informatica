# ## V1: 
# # Obtengo el n
# n = int(input("Digite n: "))

# #Reviso si el dato es valido (n > 0)
# if n > 0:

#     #Hago el setup de las variables
#     i = 0
#     suma = 0

#     # Sumar los x_i
#     while i < n:
#         xi = float(input("Digite un numero: "))
#         suma += xi
#         i += 1

#     # Calcular el promedio
#     promedio = suma /n

#     # Imprimir el promedio
#     print(promedio)

## V2:
# Obtengo el n
n = int(input("Digite n: "))

#Reviso si el dato es valido (n > 0)
if n > 0:

    #Hago el setup de las variables
    suma = 0

    # Sumar los x_i
    for _ in range(n):
        xi = float(input("Digite un numero: "))
        suma += xi

    # Calcular el promedio
    promedio = suma /n

    # Imprimir el promedio
    print(promedio)