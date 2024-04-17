class Persona:
    def __init__(self, nombre, edad, sexo, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def saludar(self):
        print(f'Hola, soy {self.nombre}.')

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Altura: {self.altura}, Peso: {self.peso}'


persona1 = Persona('Juan', 30, 'Masculino', 175, 70)
persona1.saludar()
print(persona1)
