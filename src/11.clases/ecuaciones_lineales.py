class EcuacionLineal:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def imprimir(self):
        print(f"{self.m:.2f}x {self.b:+.2f}")

    def calcular_y(self, y):
        return y * self.m + self.b

el1 = EcuacionLineal(5, 2)
el1.imprimir()
print(el1.calcular_y(20))