class Complejo:
    '''Representa un numero complejo de la forma: a + bi'''

    def __init__(self, real, imaginaria):
        '''Constructor que inicializa los atributos'''
        self.real = real
        self.imaginaria = imaginaria

    def sumar(self, complejo):
        '''Suma dos numeros complejos'''
        suma_real = self.real + complejo.real
        suma_imaginaria = self.imaginaria + complejo.imaginaria
        return Complejo(suma_real, suma_imaginaria)

    def restar(self, complejo):
        '''Resta dos numeros complejos'''
        return Complejo(self.real-complejo.real, self.imaginaria- complejo.imaginaria)

    def multiplicar(self, complejo):
        '''Multiplica dos numeros complejos'''
        a = self.real
        b = self.imaginaria
        c = complejo.real
        d = complejo.imaginaria

        return Complejo (a*c - b*d, b* c + a*d)

    def dividir(self, complejo):
        '''Divide dos numeros complejos'''
        a = self.real
        b = self.imaginaria
        c = complejo.real
        d = complejo.imaginaria
        
        parte_real = (a * c + b * d)/(c**2 + d**2) 
        parte_imaginaria = (b* c - a * d)/(c**2 + d**2) 

        return Complejo(parte_real, parte_imaginaria)

    def convertir(self):
        '''Convierte y retorna un número complejo a su representación en hilera "x.xx + y.yyi".'''
        return f"{self.real:.2f} {self.imaginaria:+.2f}i"


class Calculo:
    '''Representa un calculo de una operacion que se le aplica a dos numeros complejos'''

    def __init__(self, complejo1, operacion, complejo2):
        self.complejo1 = complejo1
        self.operacion = operacion
        self.complejo2 = complejo2

    def aplicar(self):
        '''Aplicar la operacion respectiva. Devuelve el resultado y NA si no tiene la operacion disponible'''
        if self.operacion == "+":
            return self.complejo1.sumar(self.complejo2)
        if self.operacion == "-":
            return self.complejo1.restar(self.complejo2)
        if self.operacion == "*":
            return self.complejo1.multiplicar(self.complejo2)
        if self.operacion == "/":
            return self.complejo1.dividir(self.complejo2)
        return "NA"

    def convertir(self):
        '''Convierte a un texto la operacion a aplicar con el resultado.'''
        resultado = self.aplicar()
        if resultado != "NA":
            resultado = resultado.convertir()
        return f"({self.complejo1.convertir()}) {self.operacion} ({self.complejo2.convertir()}) = {resultado}"

class Calculadora:
    REAL1 = 0
    IMAGINARIO1 = 1
    OPERACION = 2
    REAL2 = OPERACION + 1
    IMAGINARIO2 = REAL2 + 1

    def __init__(self):
        self.calculos = []

    def cargar_operaciones(self, nombre_archivo):
        '''Carga el archivo que se le pasa a las operaciones'''
        try:
            archivo = open(nombre_archivo, "r") # .\data\calculos.csv
            #Elimina la primera linea
            header = archivo.readline() 
            #Lee todas las demas lineas
            for linea in archivo.read().split("\n"): 
                #Separa cada linea con sus partes
                partes_linea = linea.split(";")

                #Crea las partes de la operacion
                complejo1 = Complejo(float(partes_linea[Calculadora.REAL1]), float(partes_linea[Calculadora.IMAGINARIO1]))
                operacion = partes_linea[Calculadora.OPERACION]
                complejo2 = Complejo(float(partes_linea[Calculadora.REAL2]), float(partes_linea[Calculadora.IMAGINARIO2]))

                #Crea el calculo y lo agrega a todos los que se deben realizar
                calculo = Calculo(complejo1, operacion, complejo2)
                self.calculos.append(calculo)
            archivo.close()
        except:
            print("Error. No encontre el archivo 😭\n")

    def guardar_operaciones(self, nombre_archivo):
        '''Guarda las operaciones que se han aplicado en un archivo'''
        archivo = open(nombre_archivo, "w") # .\data\calculos-res.txt
        for calculo in self.calculos:
            archivo.write(calculo.convertir() + "\n")
        archivo.close()

    def leer_complejo(self, nombre):
        real = float(input(f"De la parte real del complejo {nombre}: "))
        imaginaria = float(input(f"De la parte imaginaria del complejo {nombre}: "))
        return Complejo(real, imaginaria)

    def correr(self):
        while True:
            #Obtiene la opcion
            print("1. Cargar archivo\n2. Guarde calculos\n3. Usar calculadora\n4. # operaciones\n5. Salir\n")
            opcion = int(input("Opcion: "))
            #Selecciona la opcion
            if opcion == 1:
                nombre_archivo_cargar = input("De el nombre del archivo a cargar: ")
                self.cargar_operaciones(nombre_archivo_cargar)
            if opcion == 2:
                nombre_archivo_guardar = input("De el nombre del archivo a guardar: ")
                self.guardar_operaciones(nombre_archivo_guardar)
            if opcion == 3:
                complejo1 = self.leer_complejo("uno")
                complejo2 = self.leer_complejo("dos")
                operacion = input("Digite la operacion a aplicar (+, -, *, /): ")
                calculo = Calculo(complejo1, operacion, complejo2)
                self.calculos.append(calculo)
                print(calculo.convertir())
                print()
            if opcion == 4:
                print(f"Se han aplicado {len(self.operaciones)}")
            if opcion == 5:
                break
            
calculadora = Calculadora()
calculadora.correr()