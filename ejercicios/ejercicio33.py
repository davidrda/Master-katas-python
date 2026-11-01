# Ejercicio 33
#
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.


# Escribe tu solución aquí

lista1 = [10, 20, 30, 40]
lista2 = [2, 4, 6, 7]


calculo = list(map(lambda a, b: a + b, lista1, lista2))

print(calculo)
