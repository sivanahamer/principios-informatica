def sumar_total(m):
    i = 0
    suma = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            suma += m[i][j]
            j += 1
        i+= 1
    return suma
        
# total = sumar_total([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print(total)
