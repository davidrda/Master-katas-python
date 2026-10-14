# Ejercicio 6
#
# Escribe una función que calcule el factorial de un número de manera recursiva.


# Escribe tu solución aquí

def factorial(numero):

    if numero == 1:
        return 1

    return numero * factorial(numero - 1)

print(factorial(3))

    