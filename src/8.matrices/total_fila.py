def sumar_total_fila(A):
    total_fila = []
    for i in range(len(A)):
        suma = 0
        for j in range (len(A[i])):
            suma += A[i][j]
        total_fila.append(suma)
    return total_fila

# total = sumar_total_fila([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(total)