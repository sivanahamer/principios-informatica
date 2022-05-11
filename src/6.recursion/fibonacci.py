#Fibonacci
#Fibonacci de 5-> Fibonacci de 3 y de 4 = 2 + 3 = 5
#Fibonacci de 3-> Fibonacci de 1, 2 = 1 + 1 = 2
#Fibonacci de 1-> 1
#Fibonacci de 2-> Fibonacci de 0 y 1 = 0 + 1 =1
#Fibonacci de 0-> 0
#Fibonacci de 1-> 1
#Fibonacci de 4 -> Fibonacci de 2 y de 3 = 1 + 2 = 3
#Fibonacci de 2-> Fibonacci de 0 y de 1 = 0 + 1 =1
#Fibonacci de 0-> 0
#Fibonacci de 1-> 1
#Fibonacci de 3-> Fibonacci de 1, 2 = 1 + 1 = 2
#Fibonacci de 1-> 1
#Fibonacci de 2-> Fibonacci de 0 y 1 = 0 + 1 =1
#Fibonacci de 0-> 0
#Fibonacci de 1-> 1

#0, 1, 1, 2, 3, 5, 8

def fibonacci(n):
    ''' Calcula el número n de la secuencia de Fibonacci recursivamente'''
    #Caso base 0
    if n == 0:
        return 0
    #Caso base 1
    if n == 1:
        return 1
    #fn = fn-2 + fn-1
    return fibonacci(n-2) + fibonacci(n-1)


#0, 1, 1, 2, 3, 5, 8
def fibonacci_iterativo(n):
    ''' Calcula el número n de la secuencia de Fibonacci iterativamente'''
    #Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
    penultimo = 0
    ultimo = 1
    #Calculamos desde el 2 hasta el n el fibonacci
    for _ in range(2, n + 1):
        #Actual es la suma del penultimo y el ultimo
        actual = penultimo + ultimo
        #Guardar en el penultimo lo ultimo
        penultimo = ultimo 
        #Guardando en ultimo el nuevo numero
        ultimo = actual 
    return actual

print(fibonacci(5))
print(fibonacci(6))