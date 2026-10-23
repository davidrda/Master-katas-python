# Ejercicio 27

# Crea una función que calcule el promedio de una lista de números.

# Escribe tu solución aquí

from functools import reduce


def calcular_promedio(lista):

    if not lista:
        raise ValueError("La lista no puede estar vacía")

    total = reduce(lambda acc, n: acc + n, lista)

    return round(total / len(lista))

print(calcular_promedio([4, 6, 7, 2, 5, 1]))
