continuar = True
while continuar:
    try:
        r = float(input("Digite un real: "))
        continuar = False
    except ValueError:
        print("Error! ❌❌❌❌❌")

print(r)