# Ejercicio 23
#
# Concatena una lista de palabras. Usa la función reduce().


# Escribe tu solución aquí

from functools import reduce


lista = ["Hola", "qué", "tal", "estás"]

frase = reduce(lambda acc, p: acc + " " + p, lista, "").strip()

print(frase)