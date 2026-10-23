# Ejercicio 19
#
# Crea una función lambda que filtre los números impares de una lista dada.


# Escribe tu solución aquí

lista = [3, 4, 6, 15, 32, 68, 31]

numeros_impares = list(filter(lambda n: n % 2 != 0, lista))

print(numeros_impares)
