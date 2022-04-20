# Pedir la cantidad de lados
n = int(input("Cantidad de lados: "))

# Calcular la suma de los angulos internos y el angulos interior de cada poligono
suma_angulos_internos = 180 * (n - 2)
angulo_interno = suma_angulos_internos / n

# Imprimir los resultados
print(f"La suma de los angulos interiores es: {suma_angulos_internos}")
print(f"La suma de los angulos interiores es: {angulo_interno}")