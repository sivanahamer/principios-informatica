# Pedir datos 😎
a = float(input("Pedir a: "))
b = float(input("Pedir b: "))
c = float(input("Pedir c: "))

#Calcular formula: (-b +- sqrt(b^2-4ac))/(2a)
x1 = (-b + (b**2 - 4*a*c )**(0.5))/ (2*a)
x2 = (-b - (b**2 - 4*a*c )**(0.5))/ (2*a)

#Imprimir resultados
print(f"x1 = {x1:.2f}")
print("x2 = "+ str(x2))