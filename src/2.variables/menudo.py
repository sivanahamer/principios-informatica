# Pedir la cantidad de monedas de cada denominacion
c5 = int(input("Digite la cantidad de monedas de 5 colones: "))
c10 = int(input("Digite la cantidad de monedas de 10 colones: "))
c25 = int(input("Digite la cantidad de monedas de 25 colones: "))
c50 = int(input("Digite la cantidad de monedas de 50 colones: "))
c100 = int(input("Digite la cantidad de monedas de 100 colones: "))
c500 = int(input("Digite la cantidad de monedas de 500 colones: "))

# Multiplicar el valor (e.g., 5) de la moneda por la cantidad (e.g., 20)
colones = 5*c5 + 10*c10 + 25*c25 + 50*c50 + 100*c100 + 500*c500 
# colones = 5 * c5
# colones += 10*c10
# colones = colones + 25 * c25
# ...

# Imprimir la cantidad de colones
print(f"La cantidad de colones es {colones}")