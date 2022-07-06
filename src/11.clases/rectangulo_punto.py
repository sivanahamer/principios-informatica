from punto import Punto

class RectanguloPunto:
    def __init__(self, punto_superior_izquierda, punto_inferior_derecha):
        self.psi = punto_superior_izquierda
        self.pid = punto_inferior_derecha

        #Obtener las cuatro cordenadas del punto
        x_1 = self.psi.x
        x_2 = self.pid.x
        y_1 = self.psi.y
        y_2 = self.pid.y

        #Crea un punto para la esquina superior derecha
        self.psd = Punto(x_2, y_1)
        #Crea un punto para la esquina inferior izquierda
        self.pii = Punto(x_1, y_2)

    def calcular_altura(self):
        return self.psi.obtener_distancia(self.pii)

    def calcular_base(self):
        return self.pii.obtener_distancia(self.pid)

p1 = Punto(10,2)
rp = RectanguloPunto(p1, Punto(0,0))
print(rp.calcular_base())
print(rp.calcular_altura())