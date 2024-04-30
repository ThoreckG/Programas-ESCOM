import math

class HexagonoRegular:
    def __init__(self, lado, color):
        self.__lado = lado
        self.__color = color

    def get_area(self):
        return self.__area()

    def get_perimetro(self):
        return self.__perimetro()

    def get_color(self):
        return self.__color

    def __area(self):
        return (3 * math.sqrt(3) / 2) * (self.__lado ** 2)

    def __perimetro(self):
        return 6 * self.__lado

# Uso de la clase HexagonoRegular
if __name__ == "__main__":
    hexagono = HexagonoRegular(5, "cyan")
    print("Área del hexágono regular: {:.2f}".format(hexagono.get_area()))
    print("Perímetro del hexágono regular: {:.2f}".format(hexagono.get_perimetro()))
    print("Color del hexágono regular: {}".format(hexagono.get_color()))
