import math

class Punto3D:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y, point.z)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2 + (self.z - otro_punto.z)**2)


# Parte 2
import random

# Crear arreglo de 10 objetos de tipo Punto3D
puntos = [Punto3D(random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)) for _ in range(10)]

# Calcular todas las distancias y determinar la menor
min_distancia = float('inf')
for i in range(len(puntos)):
    for j in range(i + 1, len(puntos)):
        dist = puntos[i].distancia(puntos[j])
        if dist < min_distancia:
            min_distancia = dist

print(f"La menor distancia entre los puntos es: {min_distancia}")
