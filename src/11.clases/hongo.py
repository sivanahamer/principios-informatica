from distutils.util import strtobool

COLUMNA_FORMA = 0
COLUMNA_ALTURA = 1
COLUMNA_COLOR = 2
COLUMNA_ANILLOS = 3

class Hongo:
    '''
    Una clase que guarda caracteristicas de Hongos
    '''

    def __init__(self, color, cantidad_anillos, altura, forma_cabeza):
        self.color = color
        self.cantidad_anillos = cantidad_anillos
        self.altura = altura
        self.forma_cabeza = forma_cabeza

    def determinar_especie(self):
        '''
        Determina que especie de hongo es entre Bisporus, Silvaticus, Pocillator y Desconocido
        '''
        if self.color.lower() == 'blanco' and self.altura.lower() == "bajo" and self.cantidad_anillos == 0:
            return "Bisporus"
        if (self.forma_cabeza.lower() == 'campana' or self.forma_cabeza.lower() == "plano") and self.altura.lower() != "bajo":
            return "Silvaticus"
        if (self.forma_cabeza.lower() == 'convexo' or self.forma_cabeza.lower() == "plano") and self.altura.lower() == "alto" and self.color.lower() == "blanco":
            return "Pocillator"
        return "Desconocido"

    def verificar_venenoso(self):
        '''
        Verifica si un hongo es venenoso o no.
        '''
        # Su color es blanco, y además son altos
        # La forma de su cabeza es plana, y su color es café
        # El hongo tiene 2 anillos
        return (self.color.lower() == "blanco" and self.altura.lower() == "alto") or (self.forma_cabeza.lower() == "plana" and self.color.lower() == "cafe") or (self.cantidad_anillos == 2)

    def imprimir(self):
        '''
        Imprime la informacion del hongo
        '''
        es_venenoso = self.verificar_venenoso()
        if es_venenoso:
            tipo_venenoso = "Venenoso"
        else:
            tipo_venenoso = "Comestible"

        print(f"({self.determinar_especie()}, {tipo_venenoso})")

class Biologo:
    def __init__(self):
        self.hongos = []

    def leer_hongos(self, ruta_archivo):
        '''Lee de un archivo los hongos'''

        #Obtiene de un archivo el texto
        archivo = open(ruta_archivo, "r")
        texto = archivo.read()

        #Itera sobre las lineas que contienen hongos
        for linea in texto.split("\n")[1:]:
            #Separa aqui los elementos del hongo
            elementos = linea.split(",")
            #Verifica que si hay los 4 espacios que se esperan del hongo
            if len(elementos) == 4:
                #Crea un hongo y lo agrega a la lista
                hongo = Hongo(elementos[COLUMNA_COLOR], elementos[COLUMNA_ANILLOS], elementos[COLUMNA_ALTURA], elementos[COLUMNA_FORMA])
                self.hongos.append(hongo)

                #Imprime el hongoy
                hongo.imprimir()

        archivo.close()

    def obtener_hongos(self):
        '''
        Corre el codigo del Biologo
        '''
        seguir = True
        while seguir:
            #Obtiene los atributos de un hongo
            forma = input("Forma: ")
            altura = input("Altura: ")
            color = input("Color: ")
            anillos = int(input("Anillos: "))

            #Crea un hongo y lo agrega a la lista
            hongo = Hongo(color, anillos, altura, forma)
            self.hongos.append(hongo)

            #Imprime la informacion del hongo
            hongo.imprimir()
            print()

            desea_seguir = input("¿Desea seguir? ")
            if desea_seguir.lower() == "no":
                seguir = False
            print()

    def calcular_cantidad_especie(self):
        '''Calcula cuanto de cada especie hay'''
        
        #Creo estructuras de datos auxiliares
        especies = ["Bisporus", "Silvaticus", "Pocillator", "Desconocido"]
        cantidad_hongos = [0] * len(especies)
        cantidad_venenosos = [0] * len(especies)

        #Iteramos sobre todos los hongos
        for hongo in self.hongos:
            #Determinamos el indice en donde se va a guardar la informacion
            especie = hongo.determinar_especie()
            indice_especie = especies.index(especie)

            #Determinamos el arreglo para la informacion
            cantidad_hongos[indice_especie] += 1
            if hongo.verificar_venenoso():
                cantidad_venenosos[indice_especie] += 1       

        #Imprimir resultados con for
        for indice in range(len(especies)):
            print(f"Hongos {especies[indice]} encontrados: {cantidad_hongos[indice]}")
            print(f"Hongos {especies[indice]} venenosos: {cantidad_venenosos[indice]}")

        #Imprime resultados con while
        # indice = 0
        # while indice < len(especies):
        #     print(f"Hongos {especies[indice]} encontrados: {cantidad_hongos[indice]}")
        #     print(f"Hongos {especies[indice]} venenosos: {cantidad_venenosos[indice]}")  
        #     indice += 1 


biologo = Biologo()

#Determinar el metodo a invocar para obtener datos
es_archivo = strtobool(input("¿Lectura de un archivo (y/n)? "))
if es_archivo:
    # ruta = input("Digite la ruta al archivo: ")
    ruta = "./data/hongos.csv"
    biologo.leer_hongos(ruta)
else:
    biologo.obtener_hongos()

biologo.calcular_cantidad_especie()
