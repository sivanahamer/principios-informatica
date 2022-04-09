colones = float(input("Digite colones: "))
tipo_cambio = 675
if colones > 0:
    dolares = colones/tipo_cambio
    print(f"Tiene ${dolares:.2f}")
else:
    print("No se puede convertir colones que no son un numero positivo")