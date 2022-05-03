n = int(input("Digite n: "))

contador = 1

while contador <= n:
    print(f"{contador}: ", end="")
    if contador % 3 == 0:
        print("Pura", end="")
    if contador % 5 == 0:
        print("Vida", end="")
    print()
    contador += 1