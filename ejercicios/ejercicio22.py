# Ejercicio 22
#
# Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().


# Escribe tu solución aquí

from functools import reduce


lista = [2, 4, 5, 3, 6, 3, 5]

total = reduce(lambda acc, n: acc * n, lista)

print(total)