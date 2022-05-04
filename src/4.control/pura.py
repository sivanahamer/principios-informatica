n = int(input("Digite n: "))

contador = 1

while contador <= n:
    texto = f"{contador}: "
    if contador % 3 == 0:
        texto += "Pura"
    if contador % 5 == 0:
        texto += "Vida"
    print(texto)
    contador += 1