from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

    def calcular_perimetro(self):
        return pi * 2 * self.radio

    def imprimir(self):
        print(f"Soy un circulo ⭕ de radio {self.radio}")
        print(f"Perimetro: {self.calcular_perimetro():.2f}")
        area = self.calcular_area()
        print(f"Area: {area:.2f}")

c1 = Circulo(3)
c2 = Circulo(5)

c1.imprimir()
c2.imprimir()