def sumar_total_columna(A):
    total_columna = []
    for j in range (len(A[0])):
        suma = 0
        for i in range(len(A)):
            suma += A[i][j]
        total_columna.append(suma)
    return total_columna

# total = sumar_total_columna([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(total)