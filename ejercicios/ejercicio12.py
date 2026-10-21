# Ejercicio 12
#
# Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().


# Escribe tu solución aquí

def devolver_longitud_palabras(texto):
    """Devuelve una lista con la longitud de cada palabra de la frase"""

    palabras = texto.split()

    longitud_palabras = list(map(len, palabras))

    return longitud_palabras

frase = input("Inserta una frase: ")
print(devolver_longitud_palabras(frase))
