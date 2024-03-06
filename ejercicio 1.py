import random
import time

TAM = 1000

# Generador de arreglo
def summonarray(tam):
    return [random.randint(1, 1000) for _ in range(tam)]

# Imprimir arreglo
def printarray(arreglo):
    print(', '.join(map(str, arreglo)))

# Búsqueda secuencial
def searcharray(arreglo, elemento):
    for i, num in enumerate(arreglo):
        if num == elemento:
            return i
    return -1

# Ordenar arreglo
def orderarray(arreglo):
    arreglo.sort()

# Función principal
def main():
    arreglo = []

    inicio = time.time()
    # Llamar función para generar el arreglo
    arreglo = summonarray(TAM)

    # Imprimir arreglo
    print("El arreglo generado es:")
    printarray(arreglo)

    # Búsqueda en el arreglo generado
    elemento = arreglo[0]
    posicion = searcharray(arreglo, elemento)
    if posicion != -1:
        print(f"El valor {elemento} se encuentra en la posición {posicion} del arreglo.")
    else:
        print(f"El valor {elemento} no se encuentra en el arreglo.")

    # Ordenar arreglo
    orderarray(arreglo)

    # Imprimir arreglo ordenado
    print("El arreglo ordenado es:")
    printarray(arreglo)

    # Búsqueda en el arreglo ordenado
    posicion = searcharray(arreglo, elemento)
    if posicion != -1:
        print(f"El valor {elemento} se encuentra en la posición {posicion} del arreglo ordenado.")
    else:
        print(f"El valor {elemento} no se encuentra en el arreglo ordenado.")

    fin = time.time()
    print("Tiempo de ejecución del programa:", fin - inicio, "segundos")

if __name__ == "__main__":
    main()
