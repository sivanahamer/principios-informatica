# Pedir nombre
nombre = input("El nombre del animal es: ")

# Pedir caracteristicas
#TODO: usar strbool
sangre_fria = input("Tiene sangre fría: ")
glandulas = input("Tiene glándulas mamarias: ")
pelo = input("Tiene pelo: ")
vertebra = input("Tiene vertebra: ")

# Determinar si es mamifero si cumple con:
# No tienen sangre fría
# Tienen glandulas mamárias
# Tienen pelo
# Tienen vértebra
# Se asume que nos dan solo "Si" o "No"
es_mamifero = sangre_fria == "No" and glandulas == "Si" and pelo == "Si" and vertebra == "Si"

# Mostramos si es un mamifero
print(f"El animal {nombre} es mamífero: {es_mamifero}")