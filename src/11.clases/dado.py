from random import random

class Dado:
    def __init__(self, caras):
        self.caras = caras

    def tirar(self):
        return (int) (random() * self.caras) + 1

    def imprimir(self):
        print(f"Soy un dado de {self.caras}")

d6 = Dado(6)
print(d6.tirar())

d20 = Dado(20)
print(d20.tirar())