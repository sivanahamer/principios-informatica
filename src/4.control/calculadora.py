continuar = True

while continuar:
    hubo_error = False

    # Pedir un numero 1
    try:
        num1 = float(input("Digite un número: "))
    except ValueError:
        hubo_error = True
        print("ERROR! No se digita un numero valido")
    #Revisamos que no sucedio un error al leer numero 1
    if not hubo_error:
        # Pedir un numero 2
        try:
            num2 = float(input("Digite un número: "))
        except ValueError:
            print("ERROR! No se digita un numero valido")
            hubo_error = True
        #Revisamos que no sucedio un error al leer numero 2
        if not hubo_error:
            # Pedir una operacion
            print("Digite una de las siguientes operaciones:\n\t+) Sumar\n\t-) Restar\n\t*) Multiplicar\n\t/) Dividir\n\tX) Salir")
            operacion = input("Operacion: ")

            resultado = 0

            # Si operacion == "+":
            if operacion == "+":
                # Sumar
                resultado = num1 + num2
            # Si operacion == "-"
            elif operacion == "-":
                # Restar
                resultado = num1 - num2
            # Si operacion == "*":
            elif operacion == "*":
                # Multiplicar
                resultado = num1 * num2
            # Si operacion == "/":
            elif operacion == "/":
                # Dividir
                try:
                    resultado = num1 / num2
                except ZeroDivisionError:
                    print("ERROR! Se intenta dividir entre 0")
                    hubo_error = True
            #Si operacion == "X":
            elif operacion == "X":
                #Se sale del ciclo
                continuar = False
            #Caso de error, que no es una operacion valida
            else:
                print("ERROR! Debe utilizar una operacion valida")
                hubo_error = True

            #Imprime el valor si no hubo error ni se dijo que quiere salir del ciclo
            if not hubo_error and operacion != "X":
                print(f"{num1:.2f} {operacion} {num2:.2f} = {resultado:.2f}")