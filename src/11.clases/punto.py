class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def obtener_x(self):
        return self.x

    def obtener_y(self):
        return self.y

    def imprimir(self):
        print(f"({self.x}, {self.y})")

    def obtener_distancia(self, p2):
        return (((self.x) - p2.obtener_x())** 2 + (self.y - p2.obtener_y())**2)**(1/2)

p1 = Punto(2, 3)
p2 = Punto(4, 4)
print(p1.obtener_distancia(p2))