# Ejercicio 7
#
# Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().


# Escribe tu solución aquí

def conversion(lista):

    lista_string = list(map(str, lista))

    return lista_string


print(conversion((2, 3, 5, 1)))