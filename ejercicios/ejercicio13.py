# Ejercicio 13
#
# Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

# Escribe tu solución aquí

def letras_mayus_minus(texto):
    """Devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas. 
    No pueden estar repetidas"""

    texto_normalizado = texto.lower()

    # dict.fromkeys quita repetidas y mantiene el orden
    letras = dict.fromkeys(texto_normalizado)

    return list(map(lambda letra: (letra.upper(), letra.lower()), letras))



print(letras_mayus_minus("Holaaaa"))


