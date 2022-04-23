from math import log

#Obtener x
x = float(input("Digite el x: "))

try:
    #Calcular y
    y = log(x)

    #Imprimir resultado
    print(f"El logaritmo de {x:.4f} es {y:.4f}.")

except ValueError:
    #Imprime en el caso de que se indefine
    print("El logaritmo se indefine 🤯")