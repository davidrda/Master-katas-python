# Ejercicio 36
#
# Crea una función llamada procesar_texto
#
# - Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
# - Código a seguir:
#     a. Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
#     b. Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
#     c. Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
#     d. Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
#
# - Caso de uso:
#     - Verificar el funcionamiento completo de procesar_texto.


# Escribe tu solución aquí

def contar_palabras(texto):
    """Devuelve un diccionario con las veces que aparece cada palabra del texto"""

    signos = ".,:;!?¿¡()-"

    palabras = [p.strip(signos).lower() for p in texto.split()]

    palabras = [p for p in palabras if p]

    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def eliminar_palabra(texto, palabra):
    """Devuelve el texto sin las apariciones de la palabra indicada"""

    palabras = texto.split()

    palabras_restantes = [p for p in palabras if p != palabra]

    return " ".join(palabras_restantes)


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Devuelve el texto con cada aparición de palabra_original cambiada por palabra_nueva"""

    palabras = texto.split()

    palabras_nuevas = [palabra_nueva if p == palabra_original else p for p in palabras]

    return " ".join(palabras_nuevas)


def procesar_texto(texto, opcion, *args):
    """Procesa un texto según la opción: "contar", "reemplazar" o "eliminar"."""

    if opcion == "contar":
        if len(args) != 0:
            raise ValueError("La opción 'contar' no necesita datos extra")
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("La opción 'reemplazar' necesita 2 datos: palabra original y palabra nueva")
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("La opción 'eliminar' necesita 1 dato: la palabra a eliminar")
        return eliminar_palabra(texto, args[0])

    else:
        raise ValueError(f"Opción no válida: '{opcion}'. Usa 'contar', 'reemplazar' o 'eliminar'")


# Caso de uso
texto = "el gato y el perro"

print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "gato", "loro"))
print(procesar_texto(texto, "eliminar", "gato"))

try:
    procesar_texto(texto, "invertir")
except ValueError as e:
    print(f"Error: {e}")

try:
    procesar_texto(texto, "reemplazar", "gato")
except ValueError as e:
    print(f"Error: {e}")
