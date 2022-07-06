class Perro:
    def __init__(self, nombre, raza, edad, color):
        # Constructor
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color

    def __str__(self):
        return f"{self.raza}-{self.edad}-{self.color}"

    def ladrar(self):
        print(f"{self.nombre}: Woof 🐕")

    def calcular_edad_humano(self):
        '''Calcula la edad de un perro en humano'''
        return self.edad * 7


poker = Perro("Poker", "fox terrier", 15, "negro, cafe y blanco") #Invoca el constructor al inicializar
print(poker)

cherry = Perro("Cherry", "NA", 1, "negro, cafe y blanco")

poker.ladrar()
cherry.ladrar()
poker.ladrar()
print(cherry.calcular_edad_humano())
print(poker.calcular_edad_humano())