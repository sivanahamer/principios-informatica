from distutils.util import strtobool

# Pedir nombre
nombre = input("El nombre del animal es: ")

# Pedir caracteristicas
# Asumimos que es complaint con strtobool
es_sangre_fria = strtobool(input("Tiene sangre fría: "))
tiene_glandulas = strtobool(input("Tiene glándulas mamarias: "))
tiene_pelo = strtobool(input("Tiene pelo: "))
tiene_vertebra = strtobool(input("Tiene vertebra: "))

# Determinar si es mamifero si cumple con:
# No tienen sangre fría
# Tienen glandulas mamárias
# Tienen pelo
# Tienen vértebra
es_mamifero = not es_sangre_fria and tiene_glandulas and tiene_pelo and tiene_vertebra

# Mostramos si es un mamifero
print(f"El animal {nombre} es mamífero: {bool(es_mamifero)}")