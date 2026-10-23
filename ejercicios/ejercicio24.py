# Ejercicio 24
#
# Calcula la diferencia total en los valores de una lista. Usa la función reduce().


# Escribe tu solución aquí

from functools import reduce

# ACLARACIÓN!! No sé realmente a qué se refiere el ejercicio, he interpretado que es una resta de los valores, pero no lo sé

lista = [10, 3, 2, 1]

diferencia = reduce(lambda acc, n: acc - n, lista)

print(diferencia)