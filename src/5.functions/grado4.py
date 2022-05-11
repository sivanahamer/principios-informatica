def polinomioGrado4(a, b, c, d, e, x):
    '''
    Calcula realizar una sustition polinomila de grado 4 con los coeficientes.
    '''
    return a * x **4 + b * x **3 + c * x ** 2 + d * x  + e

resultado = polinomioGrado4(1,2,3,4,5,6)
print(resultado)