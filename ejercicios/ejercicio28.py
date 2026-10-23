# Ejercicio 28
#
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.


# Escribe tu solución aquí

def buscar_primer_duplicado(lista):

    vistos = []

    for i in lista:

        if i in vistos:
            return i
        
        vistos.append(i)

    return None

print(buscar_primer_duplicado([1, 3, 5, 5, 6, 1, 9, 2]))
