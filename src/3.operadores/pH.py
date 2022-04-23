from math import log10

# Se pide la concentración de iones
concentracion = float(input("Ingrese la concentración de iones de hidrógeno (mol/L): "))

try:
    # Calculamos el pH
    pH = -log10(concentracion)
except ValueError:
    pH = 14.0

# Imprimir el pH
print(f"pH = {pH}")

# Determinar la clasifacion el Ph
print(f"Es alcalino: {pH > 7}")
print(f"Es neutral: {pH == 7}")
print(f"Es acido: {pH < 7}")

#Tambien se puede hacer con ifs/else ...
# if (pH > 7):
#     print("Es alcalino")
# ...