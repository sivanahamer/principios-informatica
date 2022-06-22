# se le ingrese una cadena de ADN 
def obtener_cadena():
    '''
    Obtiene una cadena de ADN en mayuscula
    '''
    adn = input("Digite la cadena de ADN: ")
    return adn.upper()

# revise que esta sea válida
def verficar_cadena(cadena_adn):
    '''
    Verifica que una cadena de adn es valida. 
    Es decir, que tenga solo bases validas.
    '''
    bases = "ACGT"
    #Iteramos sobre cada letra en la cadena de ADN
    for letra in cadena_adn:
        #Si la letra no esta dentro de las bases, sabemos que no es valida
        if letra not in bases:
            return False
    return True

# realice sobre esta los procesos de transcripción y traducción
def transcribir(adn):
    '''
    Transcribe una cadena de ADN a ARN
    '''
    return adn.replace("T", "U")

def obtener_aminoacido(triada):
    '''Obtiene un aminoacido basado en una triada de bases'''
    #Caso de A
    if triada[0] == 'A':
        #Caso de AU
        if triada[1] == "U":
            #Caso de AUG
            if triada[2] == "G":
                return "M"
            #Caso de AUU, AUC, AUA
            return "I"
        #Caso de AC
        if triada[1] == "C":
            return "T"
        #Caso de AA
        if triada[1] == "A":
            #Caso de AAA, AAG
            if triada[2] == "A" or triada[2] == "G":
                return "K"
            return "N"
        #Caso de AG
        if triada[1] == "A":
            #Caso de AGA, AGG
            if triada[2] == "A" or triada[2] == "G":
                return "R"
            return "S"       
    #Caso de G
    elif triada[0] == "G":
        #Caso de GU
        if triada[1] == "U":
            return "V"
        #Caso de GC
        if triada[1] == "C":
            return "A"
        #Caso de GG
        if triada[1] == "G":
            return "G"
        #Caso de GA
        if triada[1] == "A":
            #Caso de GAG, GAA
            if triada[2] == "A" or triada[2] == "G":
                return "E"
            return "D"  
    #Caso de U
    elif triada[0] == "U":
        #Caso de UU
        if triada[1] == "U":
            #Caso de UUU, UUC
            if triada[2] == "U" or triada[2] == "C":
                return "F"
            return "L"
        #Caso de UC
        if triada[1] == "C":
            return "S"
        #Caso de UA
        if triada[1] == "A":
            #Caso de UAU, UAC
            if triada[2] == "U" or triada[2] == "C":
                return "Y"
            return "X"
        #Caso de UG
        if triada[1] == "G":
            #Caso de UGU, UGC
            if triada[2] == "U" or triada[2] == "C":
                return "C"
            #Caso de UGA
            if triada[2] == "A":
                return "X"
            #Caso de UGG
            return "W"
    #Caso de C
    elif triada[0] == "C":
        #Caso de CU
        if triada[1] == "U":
            return "L"
        #Caso de CC
        if triada[1] == "C":
            return "P"    
        #Caso de CG
        if triada[1] == "G":
            return "R"  
        #Caso de CA
        if triada[1] == "A":
            #Caso de CAU, CAC
            if triada[2] == "U" or triada[2] == "C":
                return "H"
            #Caso de CAA, CAG
            return "Q"
    return "-"

def traducir(arn):
    '''Traduce una cadena de ARN a los amino acidos correspondientes'''
    #Iteramos en triadas de bases
    cadena_amino_acido = ""
    ha_encontrado_metionina = False
    for indice in range(0, len(arn), 3):

        #Obtener una triada de bases
        triada = arn[indice:indice + 3]

        #Obtenemos el amino acido
        amino_acido = obtener_aminoacido(triada)
        #Revisa si el amino acido es M aka el de inicio
        if amino_acido == "M":
            ha_encontrado_metionina = True
        if amino_acido == "X":
            return cadena_amino_acido
        #Agregamos el amino acido a la cadena, si ya se encontro metionina
        if ha_encontrado_metionina:
            cadena_amino_acido += amino_acido

    return cadena_amino_acido

# que muestre la proteína ensamblada.
def correr_quimera():
    adn = obtener_cadena()
    if verficar_cadena(adn):
        arn = transcribir(adn)
        print(f"ARN: {arn}")
        amino_acidos = traducir(arn)
        print(f"Amino acidos: {amino_acidos}")
    else:
        print("No es valido")

#Correr de ejemplo con: ATGGTGCATCTGACTCCTGAGGAGAAG
# ATGGTGCATCTGTAAACTCCTGAGGAGAAG
correr_quimera()