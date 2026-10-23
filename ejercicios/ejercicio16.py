# Ejercicio 16
#
# Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().


# Escribe tu solución aquí

def lista_filtro_n(texto, n):
    """Devuelve una lista de palabras que vienen de un texto y que sean mayores que n"""

    lista_palabras = list(filter(lambda p: len(p) > n, texto.split()))

    return lista_palabras


print(lista_filtro_n("Hola que tal como va todo", 3))


