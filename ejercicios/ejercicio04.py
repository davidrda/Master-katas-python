# Ejercicio 4
#
# Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().


# Escribe tu solución aquí

lista1 = [10, 20, 30, 40]
lista2 = [2, 4, 6, 7]

def calculo_diferencia(lista1, lista2):

    calculo = list(map(lambda l1, l2: l1 - l2, lista1, lista2))

    return calculo

print(calculo_diferencia(lista1, lista2))