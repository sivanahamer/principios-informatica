from math import pi

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2

    def imprimir(self):
        print(f"Soy un rectangulo 🟥🟥 de b= {self.base} h={self.altura}")
        print(f"Perimetro: {self.calcular_perimetro():.2f}")
        area = self.calcular_area()
        print(f"Area: {area:.2f}")

r1 = Rectangulo(10, 3)
r2 = Rectangulo(5, 7)

r1.imprimir()
r2.imprimir()