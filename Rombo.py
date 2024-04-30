class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado, color):
        self.__diagonal_mayor = diagonal_mayor
        self.__diagonal_menor = diagonal_menor
        self.__lado = lado
        self.__color = color

    def get_area(self):
        return self.__area()

    def get_perimetro(self):
        return self.__perimetro()

    def get_color(self):
        return self.__color

    def __area(self):
        return (self.__diagonal_mayor * self.__diagonal_menor) / 2

    def __perimetro(self):
        return 4 * self.__lado

# Uso de la clase Rombo
if __name__ == "__main__":
    rombo = Rombo(8, 6, 5, "verde")
    print("Área del rombo: {:.2f}".format(rombo.get_area()))
    print("Perímetro del rombo: {:.2f}".format(rombo.get_perimetro()))
    print("Color del rombo: {}".format(rombo.get_color()))
