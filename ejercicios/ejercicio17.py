# Ejercicio 17
#
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().


# Escribe tu solución aquí

from functools import reduce

def unir_digitos(lista):

    if not lista:
        raise ValueError("Debes insertar una lista con valores")

    return reduce(lambda acc, n: (acc * 10) + n, lista)

try:    
    print(unir_digitos([3, 4, 5, 6, 2]))
except ValueError as e:
    print(f"Error: {e}")
