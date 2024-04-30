class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2, color):
        self.__base_mayor = base_mayor
        self.__base_menor = base_menor
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__color = color

    def get_area(self):
        return self.__area()

    def get_perimetro(self):
        return self.__perimetro()

    def get_color(self):
        return self.__color

    def __area(self):
        return ((self.__base_mayor + self.__base_menor) * self.__altura) / 2

    def __perimetro(self):
        return self.__base_mayor + self.__base_menor + self.__lado1 + self.__lado2

# Uso de la clase Trapecio
if __name__ == "__main__":
    trapecio = Trapecio(10, 6, 5, 4, 4, "rojo")
    print("Área del trapecio: {:.2f}".format(trapecio.get_area()))
    print("Perímetro del trapecio: {:.2f}".format(trapecio.get_perimetro()))
    print("Color del trapecio: {}".format(trapecio.get_color()))
